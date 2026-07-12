# MEMORIA TÉCNICA “DESARROLLO EVOLUTIVO Y CORRECTIVO DEL PORTAL EDUCATIVO, EL LDAP, EL CLOUD, MAX Y OTROS SISTEMAS DE EDUCAMADRID (BAC06_2026)

Sobre 1: Documentación relativa a los criterios de adjudicación cuya ponderación está sujeta a un juicio de valor

Este documento es propiedad de empresa_s y su contenido es confidencial. Este documento no puede ser reproducido, en su totalidad o parcialmente, ni mostrado a terceros, ni utilizado para otros propósitos que los que han originado su entrega, sin el previo permiso escrito de empresa_s . En el caso de ser entregado en virtud de un contrato, su utilización y difusión estarán limitadas a lo expresamente autorizado en dicho contrato. empresa_s no podrá ser considerada responsable de eventuales errores u omisiones en la edición del presente documento.

Rev A




Contenido

1 IDENTIFICACIÓN DE LA EMPRESA...........................................3
2 RESUMEN EJECUTIVO ............................................................5
3 MEMORIA TÉCNICA ................................................................9
3.1 SOLUCIÓN TÉCNICA OFERTADA .............................................9
3.1.1 ARQUITECTURA PLANTEADA EN LOS DISTINTOS SUBPROYECTOS .............. 9
3.1.2 GRADO DE COMPRENSIÓN DE LOS REQUISITOS PLANTEADOS ................... 18
3.1.3 VIABILIDAD DEL PROYECTO EN GENERAL.......................24
3.1.4 METODOLOGÍA DE TRABAJO APLICADA .........................27
3.1.5 RENDIMIENTO PREVISIBLE DE LAS DISTINTAS SOLUCIONES ..................... 30
3.1.6 SATISFACCIÓN DE LOS REQUISITOS ..............................35
3.1.6.1 DEFINICIÓN Y ALCANCE DE LOS TRABAJOS ................35
3.1.6.2 SERVICIO DE MANTENIMIENTO 24/7 Y CAU ...............202
3.2 PLANIFICACIÓN DEL SERVICIO ...........................................207
3.2.1 CALENDARIO DE LOS TRABAJOS A DESARROLLAR ......207
3.2.2 ANÁLISIS DE RIESGOS DEL PROYECTO .........................210
3.2.3 PLAN DE GESTIÓN DE CONTINGENCIAS .......................217
3.2.4 PLAN DE GESTIÓN DE LA CALIDAD DEL SERVICIO ........225
3.2.5 TRAZABILIDAD DEL SERVICIO ......................................234


1 Identificación de la empresa empresa_s es una compañía sólida, líder en servicio y soluciones TIC y comunicaciones, con una trayectoria de crecimiento sostenido y con la experiencia y capacitación para emprender proyectos de cualquier envergadura, según la necesidad del cliente. Desde nuestros comienzos en 1983 como distribuidores de informática, hemos evolucionado hasta convertirnos en uno de los integradores más relevantes a nivel nacional, con un equipo de más de 70 personas. Con un gran capital humano que concibe el negocio con creatividad, iniciativa y pasión, continuamos innovando y adaptándonos a las tendencias buscando la calidad y la satisfacción de nuestros clientes, que es nuestro mayor objetivo. Nos mantenemos en continua mejora, en la búsqueda de la eficiencia, lo que nos ha permitido alcanzar una facturación de más de 30 millones de euros.

Abarcamos una propuesta de valor que alcanza todos los sectores, tipos de compañía y necesidades a nivel nacional. Cubriendo cada proyecto con una propuesta flexible y adaptada en estrecha colaboración con el cliente.

Sector Privado:
- Grandes Cuentas. Contamos con clientes en todos los sectores Finanzas, Industria,
Sanidad, Educación, Telecomunicaciones, Banca y Seguros. Sector Público:
- Consolidada experiencia y presencia en la Administración Central, Autonómica y Local.
Alianzas y Certificaciones:
- empresa_s tiene alianzas y acuerdos de colaboración con los principales fabricantes del
sector informático, tanto en hardware como en software:



Por todo ello, empresa_s declara, bajo su responsabilidad, que toda la información incluida en la presente propuesta técnica es veraz, completa y ha sido elaborada con arreglo a los principios de buena fe y rigor profesional. Asimismo, manifiesta que los datos, descripciones y soluciones aportadas reflejan fielmente la capacidad real de la organización para llevar a cabo los servicios o suministros ofertados, comprometiéndose a acreditar documentalmente cualquier aspecto que le sea requerido por la entidad contratante.



2 Resumen Ejecutivo Visión estratégica de la propuesta La presente oferta configura un modelo de servicio integral, industrializado y orientado a la excelencia operativa, diseñado específicamente para garantizar la continuidad, evolución y modernización de la plataforma EducaMadrid, uno de los ecosistemas educativos digitales más críticos y complejos del ámbito público. No se plantea como un servicio tradicional de mantenimiento, sino como una plataforma de operación tecnológica avanzada, capaz de:
- Garantizar la continuidad de servicio sin interrupciones.
- Anticipar riesgos y evitar incidencias.
- Evolucionar de forma controlada y sostenible.
- Mejorar de forma continua la experiencia de los usuarios.
Todo ello sobre un entorno de alta criticidad, con miles de usuarios concurrentes, miles de bases de datos y servicios educativos esenciales.

Nuestro enfoque diferencial: de mantenimiento a operación inteligente El valor de nuestr a propuesta reside en la transformación del modelo tradicional en un modelo de operación inteligente, proactiva y basada en datos:
- De reactivo a predictivo:
o Detección de incidencias en \<1 minuto. o Sistemas de alerta anticipada. o Modelos predictivos de capacidad y rendimiento.
- De manual a automatizado:
o Automatización de más del 80% de tareas. o Reducción drástica del error humano. o Despliegues seguros, reversibles y sin impacto.
- De silo a plataforma integrada:
o Visión unificada de todos los sistemas. o Integración real entre portal, LDAP, cloud, aulas, correo e IA. o Trazabilidad end- to-end de todas las actuaciones. Este cambio de paradigma permite garantizar no solo el cumplimiento del pliego, sino superar sus expectativas operativas y de calidad.

Solución técnica: robusta, escalable y sin incertidumbre La solución se fundamenta en una arquitectura diseñada desde el principio para la continuidad real del servicio educativo: Disponibilidad y resiliencia:
- Alta disponibilidad estructural (≥ 99,95%– 99,99%).
- Recuperación automática ante fallos (\<5 minutos).
- Balanceo dinámico y replicación en tiempo real.
Escalabilidad total:


- Capacidad para soportar crecimiento continuo (\>2M usuarios).
- Escalado horizontal en todos los componentes críticos.
- Adaptación dinámica a picos educativos (inicio curso, evaluaciones).
Rendimiento garantizado:
- Latencia en bases de datos ≤50 ms.
- Tiempo de respuesta en aulas virtuales ≤2 s.
- Autenticación ≤500 ms.
Resultado: Una plataforma preparada para crecer, evolucionar y operar sin degradación del servicio.

Metodología: rigor + agilidad + resultados Se adopta un enfoque híbrido y perfectamente alineado con Administración Pública, que combina: Base sólida:
- Métrica v3 (estándar en sector público).
- ISO/IEC 12207.
Capacidad de adaptación:
- Metodologías ágiles.
- DevOps / GitOps.
- Integración continua.
Garantía de calidad:
- Validación previa en preproducción.
- Pruebas automáticas de regresión y rendimiento.
- Trazabilidad completa desde requisito hasta producción.
Resultado: máximo control sin perder velocidad de ejecución.

Planificación: coherente, realista y optimizada para el entorno educativo La planificación se ha diseñado específicamente para el contexto EducaMadrid: Optimización del calendario:
- Actuaciones críticas en periodos no lectivos.
- Minimización del impacto en centros educativos.
- Coordinación total con el calendario escolar.
Estructuración del servicio:
- 13 áreas funcionales completamente cubiertas.
- ~89 entregables definidos.
- Servicio continuo de principio a fin del contrato .
Alta capacidad operativa:
- Más de 10.000 horas anuales de servicio.
- Cobertura 24x7 para incidencias críticas.
- Servicios bajo ANS exigentes.


Gestión del servicio: control total y trazabilidad absoluta Uno de los elementos más valorables de la propuesta es su capacidad de gobierno y control real del servicio: Modelo de gobierno multinivel:
- Estratégico: alineación y dirección.
- Táctico: planificación y control.
- Operativo: ejecución diaria.
Trazabilidad completa:
- Registro de todas las actividades, incidencias y decisiones.
- Control de versiones.
- Auditoría completa del servicio.
Monitorización 360º:
- 100% de servicios monitorizados.
- Observabilidad (logs, métricas, trazas).
- Dashboards ejecutivos.
Resultado: control absoluto, transparencia total y capacidad de auditoría.

Seguridad y cumplimiento: integrada, no añadida La seguridad se integra desde el diseño:
- Cumplimiento completo del ENS.
- Monitorización continua de amenazas.
- Resolución de vulnerabilidades críticas ≤24h.
- Hardening, auditorías y control de accesos.
Además, se incorporan capacidades avanzadas:
- Detección temprana de incidentes (\<1 minuto).
- Protección sin degradación del rendimiento.
- Seguridad alineada con entornos educativos.

Innovación real: automatización e inteligencia artificial La propuesta introduce innovación práctica y aplicable: Automatización:
- Infraestructura como Código.
- Autoescalado de servicios.
- Procesos self-healing.
Inteligencia Artificial:
- Integración transversal en servicios.
- Modelos predictivos de capacidad.
- Optimización de operaciones.
No se trata de innovación teórica, sino de capacidades operativas integradas en el servicio.


Equipo: excelencia técnica alineada con el pliego El equipo que realizará el servicio cubre el 100% de perfiles requeridos:
- Arquitectura, sistemas, bases de datos, cloud.
- Ciberseguridad, automatización e IA.
- Gobierno y gestión.
Se caracteriza por:
- Alta especialización.
- Experiencia en entornos complejos.
- Capacidad de ejecución inmediata.

Valor para la Comunidad de Madrid La propuesta aporta beneficios directos y medibles: Para el servicio educativo:
- Continuidad garantizada.
- Mejora de la experiencia de usuario.
- Eliminación de interrupciones no controladas.
Para la organización:
- Reducción de riesgos operativos.
- Optimización de costes (automatización + open source).
- Control completo del ecosistema tecnológico.
Para el futuro:
- Plataforma preparada para crecimiento.
- Base sólida para evolución digital.
- Integración progresiva de IA.


Fecha: 21/05/2026

3 Memoria Técnica 3.1 Solución técnica ofertada 3.1.1 Arquitectura planteada en los distintos subproyectos Arquitectura de los distintos subproyectos de la plataforma EducaMadrid según criterios de arquitectura, viabilidad, rendimiento, seguridad, escalabilidad y coherencia técnica. Se propone una arquitectura híbrida, modular, segura, observable y multinivel, adaptada a la criticidad y naturaleza de cada servicio. Arquitectura transversal La arquitectura transversal incluye SSO centralizado mediante Keycloak, integración LDAP, monitorización centralizada, Fuente única de verdad CMDB, balanceadores, backups, trazabilidad y automatización CI/CD (GIT y Ansible) Web principal y Portal Educativo Arquitectura multinivel basada en Liferay y desarrollos propios, con balanceadores de cargas, APIs desacopladas, caché distribuida y bases de datos HA. Uso de entornos virtuales para frontales, middleware y Bases de datos. Componentes

Capa Elementos Frontal Liferay, desarrollos propios, caché HTTP Middleware APIs REST, integración con servicios EducaMadrid Backend Base de datos, repositorios documentales, buscador Seguridad LDAP, control de sesiones, protección CSRF/XSS Operación Despliegues, pruebas de regresión

Decisión técnica Aspecto Decisión Contenedores Se estudiará para frontales y APIs Virtualización Para componentes legacy y BBDD IA No, por el momento Nivel Multinivel Criticidad Muy alta

Aulas Virtuales Moodle Arquitectura altamente escalable mediante nodos Moodle balanceados, posibilidad de cache redis, almacenamiento compartido y diferentes instancias de bases de datos organizadas por tipos de centro. Separación de entornos por tipología de uso. Componentes Capa Elementos


Fecha: 21/05/2026

Frontal Nodos Moodle balanceados Datos PostgreSQL en diferentes Instancias Ficheros NFS HA Monitorización Métricas por curso, actividad y concurrencia

Decisión técnica Aspecto Decisión Contenedores Se estudiará para frontales y APIs Virtualización Para componentes legacy y BBDD IA Si, para generación de preguntas. Nivel Multinivel Criticidad Muy alta

Mediateca Arquitectura orientada a contenidos multimedia con procesamiento asíncrono, workers de transcodificación, almacenamiento object storage y etiquetado inteligente. Componentes Capa Elementos Frontal Portal de gestión multimedia Procesamiento Workers de transcodificación Almacenamiento NFS y bloque Datos Metadatos, Base de datos cluster Gallera y Max Scale Seguridad Control de visibilidad, permisos por centro/docente/alumno Integración EMPieza, SSO, Moodle, Portal, Videoconferencias

Decisión técnica Aspecto Decisión Contenedores En estudio frontales y APIs Virtualización Para componentes legacy y BBDD IA Si, subtitulado automático y transcripción Nivel Multinivel Criticidad Muy alta

Retransmisión en vivo Arquitectura especializada para streaming basada en Wowza y servicios de transcodificación escalables con distribución CDN y control de acceso. Componentes Capa Elementos Frontal App Wonza, caché HTTP


Fecha: 21/05/2026

Middleware APIs REST, integración con servicios EducaMadrid Seguridad LDAP, control de sesiones, protección CSRF/XSS Operación Despliegues actualizaciones, pruebas de regresión

Decisión técnica Aspecto Decisión Contenedores En estudio para aplicación. Virtualización Posible para componentes legacy IA No, por el momento Nivel Multinivel Criticidad Media

WordPress y WordPress Multisite Arquitectura web escalable con nodos balanceados, WAF, catálogo homologado de plugins y actualizaciones controladas. Componentes Capa Elementos Frontal WordPress Multisite Datos APIs REST, integración con servicios EducaMadrid Backend Base de datos MySql optimizada Ficheros Almacenamiento NFS compartido Seguridad WAF, control de plugins, hardening Operación Actualizaciones controladas

Decisión técnica Aspecto Decisión Contenedores En estudio para nodos web Virtualización Componentes legacy y BBDD IA No, por el momento Nivel Multinivel Criticidad Alta

Correo electrónico Arquitectura crítica distribuida basada en RoundCube, QMail, antispam y almacenamiento de buzones en alta disponibilidad. Componentes Capa Elementos Webmail RoundCube adaptado Transporte SMTP TLS Antispam, antimalware SPF/DKIM/DMARC


Fecha: 21/05/2026

Backend Base de datos, repositorios documentales, buscador Seguridad Filtrado por geolocalización y resto de componentes de transporte. Almacenamiento Buzones distribuidos MailBox Observabilidad Colas, rechazos, latencia, volumen Continuidad Backups, réplica, plan de recuperación

Decisión técnica Aspecto Decisión Contenedores En estudio para frontales Roundcube Virtualización Sí para MTA y almacenamiento crítico IA Si, generación y resumen de correos Nivel Multinivel Criticidad Muy alta

NextCloud y edición colaborativa Arquitectura cloud colaborativa con NextCloud y Collabora desacoplados, almacenamiento escalable y control de sesiones mediante Redis. Componentes Capa Elementos Frontal Nextcloud balanceado Edición Collabora Balanceado en nodos separados Caché Redis Datos Base de datos cluster Gallera y Max Scale Ficheros Almacenamiento NFS, pruebas futuras con object storage Seguridad Antivirus, cuotas, compartición controlada

Decisión técnica Aspecto Decisión Contenedores En estudio para nodos web Virtualización Para Nodos actuales y Bases de datos IA Si a futuro para análisis de contenido tipo RAG Nivel Multinivel Criticidad Alta

Comparti2 Servicio temporal de compartición de archivos basado en Jirafeau, con control de expiración y trazabilidad gestionado desde EMPieza. Componentes Capa Elementos


Fecha: 21/05/2026

Frontal Web de subida/descarga Backend Gestión de enlaces temporales Datos Metadatos de fichero Almacenamiento Temporal con caducidad en NFS Seguridad Límites, trazabilidad Integración EMPieza y SSO

Decisión técnica Aspecto Decisión Contenedores No, por el momento Virtualización Si, para los diversos componentes IA No necesaria Nivel Dos o tres niveles Criticidad Media

eXeLearning Online Arquitectura web integrada con Moodle y Mediateca para la generación de recursos educativos abiertos con ayuda IA. Componentes Capa Elementos Frontal Web + app Backend Base de datos, repositorios documental Seguridad SSO, control de sesiones Operación Despliegues CI/CD, pruebas de regresión

Decisión técnica Aspecto Decisión Contenedores Sí para frontales, Base de Datos y APIs Virtualización Para los hosts IA No, por el momento Nivel Multinivel Criticidad Media

EMPieza Microservicio central de automatización e integración entre plataformas EducaMadrid mediante APIs y motor de reglas. Componentes Capa Elementos Frontal Frontal Web y aplicación Core balanceadas


Fecha: 21/05/2026

Backend Datos de grupos, permisos y acciones Datos Base de datos cluster Gallera y Max Scale Seguridad LDAP, control de sesiones, protección CSRF/XSS Integración APIs internas Seguridad Trazabilidad de acciones

Decisión técnica Aspecto Decisión Contenedores En estudio para frontales webs. Virtualización Para todos los componentes actuales IA No, por el momento Nivel Multinivel Criticidad Muy alta

Avisos centralizados Arquitectura basada en eventos y colas de mensajería para distribución de avisos segmentados a usuarios y centros. Componentes Capa Elementos Frontal Aplicación, Motor web NGINX y caché HTTP Backend Base de datos principal de la aplicación. Seguridad Control de sesiones, protección CSRF/XSS Operación Despliegues de actualizaciones.

Decisión técnica Aspecto Decisión Contenedores No, por el momento. Virtualización Sí, para todos los componentes IA No, por el momento Nivel Multinivel Criticidad Alta

Formularios LimeSurvey Arquitectura web multinivel con separación de aplicación, base de datos y exportación segura de información. Componentes Capa Elementos Frontal Aplicación y motor web http


Fecha: 21/05/2026

Backend Base de datos MySql optimizada Datos Almacenamiento NFS compartido Seguridad Control de sesiones Operación Refresco de BBDD y actualización Aplicación

Decisión técnica Aspecto Decisión Contenedores No, por el momento. Virtualización Sí, para todos los componentes IA No, por el momento Nivel Dos o tres niveles Criticidad Alta

Videoconferencias Jitsi y BigBlueButton Arquitectura especializada con Jitsi y BigBlueButton, nodos media dedicados, grabaciones separadas y monitorización QoS. Componentes Capa Elementos Señalización Jitsi Meet / BBB Media Videobridges / SFU Grabación Solo BBB en nodos separados Integración Moodle, LDAP Operación Latencia, pérdida, jitter, participantes

Decisión técnica Aspecto Decisión Contenedores Parcial BBB Virtualización Sí para nodos media dedicados IA No, por el momento Nivel Multinivel especializado Criticidad Alta

Aplicación EMLab Sistema de analítica y certificación de uso de servicios EducaMadrid basado en indicadores y cuadros de mando. Componentes Capa Elementos Frontal Aplicación, Motor web apache Backend Base de datos principal de la aplicación.


Fecha: 21/05/2026

Seguridad Control de sesiones. Operación Actualizaciones y versionado

Decisión técnica Aspecto Decisión Contenedores No, por el momento, en estudio Virtualización Sí, para todos los componentes IA No, por el momento Nivel Dos o tres niveles Criticidad Alta

Recursos educativos y herramientas Arquitectura modular para Animalandia, Wiris, EducaSAAC y otros recursos educativos con búsqueda semántica y reutilización de contenidos. Arquitectura mixta según servicio Capa Elementos Animalandia Web + repositorio multimedia + buscador + BBDD Wiris Integración externa/controlada + monitorización Albor Aplicación especializada con datos estructurados EducaSAAC Repositorio visual + buscador + permisos Recursos educativos Portal + metadatos + almacenamiento

Decisión técnica Aspecto Decisión Contenedores No, por el momento, en estudio Virtualización Sí, para todos los componentes IA En proyecto, Albor Nivel Variable, preferentemente multinivel Criticidad Media

Aplicaciones internas y de gestión Segmentación segura para GitLab, Redmine, Mattermost, Keycloak y herramientas internas de operación y soporte.

Decisión técnica Aspecto Decisión Contenedores Sí para GitLab, ELK, Mattermost, Redmine si procede Virtualización Sí para servicios críticos o legacy IA Para uso de contenido interno con LLM propio autoalojado. Nivel Multinivel


Fecha: 21/05/2026

Criticidad Alta interna Uso de Inteligencia Artificial Uso controlado y gobernado de IA para búsqueda semántica, analítica, clasificación de contenidos, automatización y soporte docente.

La IA debe implantarse con: Control Descripción Gobierno de prompts Versionado, aprobación y trazabilidad Auditoría Registro de consultas y resultados Seguridad No exposición de datos sensibles Supervisión humana Validación en usos críticos Evaluación continua Medición de precisión, sesgos y errores

Seguridad transversal Integración de WAF, MFA, RBAC, auditoría, cifrado, protección perimetral, segmentación de red y cumplimiento normativo.

DevOps y CI/CD Pipeline de integración y despliegue continuo mediante GitLab CI/CD, análisis automático, pruebas de seguridad y despliegues.


![Imagen de la página 17](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0017-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0017-imagen-003.png -->
- Infografía de gobernanza de inteligencia artificial.
- Incluye gobierno y versionado de prompts, auditoría de consultas y resultados, protección de datos sensibles, supervisión humana en usos críticos y evaluación continua de precisión, sesgos y errores.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0017-imagen-003.png -->

Riesgos y mitigación Definición de riesgos operativos, de capacidad, seguridad y disponibilidad junto con medidas preventivas y planes de contingencia. Conclusiones La propuesta adapta la arquitectura más adecuada a cada subproyecto, garantizando escalabilidad, rendimiento, seguridad, trazabilidad y mantenibilidad a largo plazo.

3.1.2 Grado de comprensión de los requisitos planteados
1. Declaración de comprensión
Consideramos que nuestra solución propuesta detallada un grado de comprensión exhaustivo, profundo y operativo de los requisitos del pliego, no limitándose a su interpretación, sino demostrando:
- Lo presentamos desglos ado completo por áreas funcionales y técnicas, alineado con cada
uno de los requisitos solicitados en el Anexo II del pliego.
- Hemos traducido directamente a soluciones concretas, medibles y ejecutables en el
apartado 3.1.6 de la presente oferta-
- Su contextualización dentro del ecosistema real de EducaMadrid, incluyendo sus
dependencias, criticidad y volumen. Esta comprensión se materializa en una correspondencia explícita y verificable requisito → solución → mejora → valor , eliminando ambigüedades y garantizando una implementación y mantenimiento sin incertidumbres. Hemos realizado un mapeo integral de todos los requisitos del pliego, organizándolos por áreas funcionales (BD, MON, UPD, CLO, COR, MAX, AV, POR, SEG, CON, MIG, IA) y reflejando su interdependencia operativa dentro de la plataforma, lo que permite comprender no solo cada requisito aislado, sino su papel dentro del conjunto del sistema. Esta estructuración se ha traducido en el apartado 3.1.6 en una definición directa de soluciones técnicas, medibles y ejecutables, alineadas con los entregables exigidos (hasta 89 entregables identificados en el pliego) y con los esfuerzos estimados, incluyendo tanto trabajos ordinarios como extraordinarios. Se ha considerado explícitamente el modelo de prestación del servicio (Tipo A, B y C), integrando en nuestra solución tanto el desarrollo evolutivo como el mantenimiento correctivo bajo ANS, con sus correspondientes exigencias de tiempos de respuesta, resolución e indicadores de servicio.


![Imagen de la página 18](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0018-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0018-imagen-003.png -->
- Lista visual de prácticas de operación y DevOps.
- Reúne GitLab CI/CD, despliegues Blue/Green y Canary, pruebas automatizadas, entornos de desarrollo, preproducción y producción, gestión de configuración con Ansible o Terraform y gestión de incidencias con Redmine o Mattermost.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0018-imagen-003.png -->

Adicionalmente, nuestra comprensión no se limita al plano técnico, sino que incorpora una visión sistémica del ecosistema EducaMadrid, caracterizado por:
- Un entorno altamente distribuido, con más de 25 aplicaciones interrelacionadas (portal,
Moodle, mediateca, cloud, correo, IA, etc.).
- Altos volúmenes de uso (millones de usuarios, cientos de millones de interacciones), que
implican requisitos estrictos de escalabilidad, rendimiento y disponibilidad.
- Una criticidad elevada del servicio, que exige continuidad operativa, soporte 24x7 en
incidencias críticas y cumplimiento de ANS exigentes.
- Un marco normativo exigente (ENS nivel medio, protección de datos, seguridad desde el
diseño), que condiciona todas las decisiones técnicas y operativas. Sobre esta base, nuestra propuesta incorpora una comprensión contextualizada , integrando:
- Las dependencias técnicas (por ejemplo, interacciones entre LDAP, portal, SSO, cloud o
servicios de correo).
- Las particularidades tecnológicas (Liferay, Moodle, NextCloud, MariaDB, contenedores,
etc.).
- Las líneas de evolución estratégica del pliego (migración de CPDs, contenerización,
adopción de IA on- premise, automatización avanzada). Como resultado, esta comprensión se materializa en un modelo explícito de correspondencia estructurada requisito → solución → mejora → valor , que constituye uno de los elementos diferenciales de la propuesta:
- Requisito: identificado y clasificado según Anexo II.
- Solución: definida técnicamente con detalle suficiente para su ejecución.
- Mejora: incorporación de optimizaciones o extensiones coherentes con el entorno.
- Valor: impacto medible en rendimiento, calidad de servicio, seguridad o sostenibilidad
operativa. Este enfoque elimina ambigüedades interpretativas, reduce riesgos de ejecución y garantiza una implantación completamente trazable, verificable y alineada con los objetivos del contrato, asegurando además la coherencia entre el diseño de la solución, su operación y su mejora continua. En definitiva, la propuesta no sólo pretende demostrar comprensión, sino capacidad de ejecución basada en conocimiento profundo del entorno, del pliego y de las dinámicas reales de explotación de EducaMadrid.
2. Comprensión estructural del alcance del pliego
Interpretación completa del objeto del contrato El proyecto ha sido entendido en su totalidad como:
- Un servicio integral y continuo de:
o mantenimiento (correctivo, evolutivo, adaptativo, perfectivo). o evolución tecnológica. o aseguramiento de la continuidad del servicio.
- Sobre un ecosistema crítico, distribuido y altamente concurrente, que incluye:
o Portal, LDAP, Cloud, MAX, Aulas Virtuales, Correo, IA, etc. Esto implica que la solución no se plantea como un desarrollo puntual, sino como una operación compleja y sostenida en el tiempo, tal y como exige el pliego.


Comprensión del modelo de prestación Se ha interpretado la naturaleza híbrida del contrato como:
- Tipo A: desarrollos definidos.
- Tipo B: servicio bajo ANS (soporte continuo).
- Tipo C: evolución por unidades de actividad.
La propuesta de empresa_s integra estos tres modelos en un único marco operativo coherente, con el fin de demostrar una comprensión real del modelo de ejecución contractual.
3. Comprensión operativa del servicio
Para empresa_s es fundamental, más allá de los requisitos técnicos, evidenciar comprensión de: Condiciones reales de ejecución
- Necesidad de actuar en:
o ventanas no lectivas. o entornos productivos críticos. o sistemas con impacto directo en centros educativos. Importancia de los ANS
- tiempos de respuesta y resolución.
- soporte continuo 24x7.
- clasificación y priorización de incidencias.
Necesidad de trazabilidad y control empresa_s entiende que el pliego exige:
- seguimiento completo de actividades.
- trazabilidad de cambios.
- control de entregables.
La solución incluye:
- trazabilidad end- to-end.
- control de versiones.
- registro estructurado de tareas, incidencias y decisiones.
4. Comprensión orientada a valor
El objetivo de empresa_s mediante esta propuesta no se limita a cumplir requisitos, sino entender su finalidad:
- Garantizar continuidad del servicio educativo.
- Mejorar rendimiento y experiencia de usuario.
- Permitir evolución tecnológica sostenible.
- Reducir riesgos operativos.
Por ello incorpora mejoras coherentes:
- Automatización.
- Modelos predictivos.
- Observabilidad avanzada.
- Integración de IA.


Nuestra propuesta parte de una premisa fundamental: en un entorno como EducaMadrid, caracterizado por su criticidad, volumen de uso y heterogeneidad tecnológica, la mera satisfacción de requisitos no es suficiente. Es necesario comprender el propósito último de cada requisito y su contribución al valor global del servicio. En este sentido, la propuesta de empresa_s se fundamenta en una interpretación finalista del pliego, alineada con los objetivos reales de la Plataforma EducaMadrid, que incluyen la garantía de la continuidad del servicio, la mejora de la experiencia de la comunidad educativa y la evolución tecnológica sostenida del sistema. Así, cada línea de trabajo recogida en el Anexo II ha sido reinterpretada no solo como una obligación técnica, sino como un vector de generación de valor en un sistema crítico, con millones de usuarios y altos requisitos de disponibilidad, rendimiento y seguridad. Objetivos de valor identificados Bajo este enfoque, la comprensión del pliego se traduce en la identificación de cuatro objetivos estratégicos que guían toda la propuesta:
- Garantía de la continuidad del servicio educativo: La plataforma soporta servicios
esenciales como aulas virtuales, portal educativo, correo o cloud, con uso intensivo y continuo. Por ello, cada requisito se ha alineado con la necesidad de asegurar alta disponibilidad, tiempos de respuesta ajustados a ANS y resiliencia operativa, incluyendo soporte 24x7 en incidencias críticas .
- Mejora del rendimiento y la experiencia de usuario: Dado el elevado número de
usuarios concurrentes y el volumen de operaciones, se ha interpretado cada requisito como una oportunidad para optimizar tiempos de carga, escalabilidad, eficiencia en procesos y usabilidad de los servicios, impactando directamente en la calidad percibida por docentes, alumnos y personal administrativo.
- Evolución tecnológica sostenible y alineada con el roadmap: El pliego incorpora
explícitamente líneas de evolución como la contenerización, la migración de CPD o la integración de IA en modelos on- premise. Nuestra comprensión integra estos elementos como parte de una estrategia de modernización progresiva, gobernada y compatible con el ecosistema existente .
- Reducción de riesgos operativos y técnicos: En un entorno con más de 3.500 bases de
datos, múltiples aplicaciones interdependientes y cumplimiento ENS, cada intervención implica riesgos que deben ser gestionados. Por ello, cada requisito se ha contextualizado en términos de seguridad, trazabilidad, control del cambio y prevención de incidencias. Materialización en mejoras coherentes A partir de esta comprensión orientada a valor, la propuesta no se limita a reproducir lo solicitado, sino que incorpora un conjunto de mejoras alineadas con los objetivos del contrato y perfectamente coherentes con el entorno de EducaMadrid:
- Automatización avanzada de operaciones: Se propone la automatización de tareas
recurrentes (despliegues, mantenimiento, gestión de incidencias, operaciones sobre infraestructura), en línea con los sistemas de automatización y contenedores descritos en el pliego, reduciendo la dependencia manual, minimizando errores y mejorando los tiempos de respuesta.
- Incorporación de modelos predictivos de operación: A partir de los sistemas de
monitorización y análisis existentes, se introducen capacidades de análisis predictivo orientadas a anticipar incidencias, saturaciones o degradaciones del servicio, evolucionando desde un modelo reactivo a uno proactivo y preventivo.


- Implantación de un modelo de observabilidad avanzada: Más allá de la monitorización
tradicional, se plantea un modelo integral de observabilidad (logs, métricas, trazas) que permita una visión completa del estado del sistema, facilitando el diagnóstico, la optimización continua y el cumplimiento de ANS.
- Integración efectiva y gobernada de Inteligencia Artificial: En línea con el propio pliego,
que ya contempla la evaluación e integración de modelos IA en entorno local, se propone su incorporación controlada para casos de uso concretos (asistencia, análisis, automatización), garantizando privacidad, soberanía tecnológica y eficiencia operativa.
5. Evidencias objetivas de comprensión
La propuesta de empresa_s no se limita a declarar un alto grado de comprensión, sino que l o demuestra mediante evidencias objetivas, verificables y directamente contrastables con el pliego, permitiendo al evaluador validar de forma inequívoca la correspondencia entre necesidades, soluciones y resultados esperados. Esta acreditación se articula a través de los siguientes mecanismos: Cobertura exhaustiva y sistemática de los requisitos El apartado 3.1.6 de la presente oferta constituye la principal evidencia de dicha comprensión, al incorporar una cobertura completa, estructurada y trazable de todos y cada uno de los requisitos definidos por EducaMadrid en el Anexo II, incluyendo la totalidad de áreas funcionales y técnicas (bases de datos, monitorización, cloud, correo, seguridad, automatización, IA, etc.) . Esta cobertura no es meramente declarativa, sino que:
- Descompone cada requisito en unidades operativas ejecutables, alineadas con los
entregables exigidos.
- Integra tanto las prestaciones de desarrollo (Tipo A) como las de mantenimiento bajo ANS
(Tipo B), alineándose con el modelo de servicio del contrato .
- Considera la complejidad real del entorno, incluyendo volúmenes, criticidad y
dependencias entre sistemas del ecosistema EducaMadrid. Correspondencia estructurada requisito → solución → mejora → valor Como segundo elemento de evidencia objetiva, la propuesta establece un modelo explícito de trazabilidad que conecta de forma directa:
- El requisito del pliego, identificado y clasificado.
- La solución técnica propuesta, descrita con nivel suficiente de detalle para su
implementación.
- La mejora incorporada, cuando procede, en coherencia con el entorno tecnológico y
operativo.
- El valor obtenido, expresado en términos de rendimiento, calidad del servicio, mitigación
de riesgos o eficiencia operativa. Esta correspondencia estructurada permite:
- Validar de forma inmediata el grado de alineación con el pliego.
- Identificar claramente los diferenciales de la propuesta frente a un cumplimiento básico.
- Garantizar la coherencia entre diseño, ejecución y resultados.
Se configura así un modelo de lectura que facilita la evaluación, reduce la incertidumbre y posiciona la propuesta en un nivel de excelencia en satisfacción de requisitos Definición de KPIs medibles, verificables y alineados con ANS Página 22 de 239


Como tercer pilar de evidencia, empresa_s incorpora un sistema de indicadores (KPIs) que traduce la comprensión del servicio en parámetros objetivos de control, seguimiento y mejora continua, alineados con los niveles de servicio exigidos en el pliego. Estos KPIs:
- Están directamente vinculados a los ANS definidos (tiempos de respuesta, resolución de
incidencias, disponibilidad, etc.) .
- Permiten medir el desempeño real del servicio en términos cuantitativos.
- Facilitan la trazabilidad y auditoría del cumplimiento contractual.
- Habilitan la mejora continua mediante la identificación de desviaciones y oportunidades de
optimización. Además, se definen bajo criterios de realismo y alcanzabilidad , considerando tanto los recursos adscritos como la complejidad técnica del entorno, lo que refuerza la viabilidad global de la propuesta.
6. Elementos diferenciales
Nuestra propuesta incorpora una serie de elementos diferenciales que evidencian no solo una adecuada comprensión del pliego, sino una capacidad superior de interpretación, aterrizaje operativo y generación de valor, alineada con la complejidad y criticidad del ecosistema EducaMadrid. Estos elementos se concretan en los siguientes aspectos clave: Enfoque práctico y orientado a ejecución Frente a aproximaciones meramente descriptivas o declarativas, la propuesta adopta un enfoque eminentemente práctico, en el que cada requerimiento del pliego ha sido traducido en acciones concretas, procedimientos operativos y soluciones técnicamente implementables. Este enfoque se apoya en:
- La descomposición de los requisitos en unidades de trabajo ejecutables.
- La definición de tareas, flujos y responsabilidades claras.
- La alineación con el modelo real de prestación del servicio (desarrollo evolutivo +
mantenimiento bajo ANS) . De este modo, se elimina cualquier ambigüedad y se facilita una ejecución directa, sin necesidad de reinterpretaciones posteriores, lo que incrementa la confianza en la viabilidad de la propuesta. Traducción directa a operación real del servicio La propuesta no se queda en el plano conceptual, sino que realiza una transposición completa al contexto operativo de EducaMadrid, caracterizado por:
- Altos volúmenes de carga y concurrencia.
- Requisitos estrictos de disponibilidad y tiempos de resolución.
- Operación continua con soporte 24x7 para incidencias críticas .
Cada solución planteada ha sido diseñada teniendo en cuenta estas condiciones reales de explotación, asegurando su aplicabilidad inmediata en producción y su coherencia con los procedimientos de gestión de incidencias, ANS y operación definidos en el pliego. Integración completa y no fragmentada de los sistemas Uno de los principales diferenciales radica en la visión integral y sistémica de la plataforma:
- No se aborda cada área (BD, cloud, correo, portal, IA, seguridad, etc.) de forma aislada.


- Se consideran explícitamente sus interrelaciones, dependencias y puntos de integración.
- Se alinean las soluciones con la arquitectura real del ecosistema, compuesto por múltiples
servicios interconectados (portal, Moodle, NextCloud, LDAP, correo, etc.). Este enfoque evita soluciones parciales o inconexas y garantiza una coherencia global de la plataforma, clave en un entorno con más de 25 aplicaciones y múltiples tecnologías coexistiendo. Identificación de problemáticas implícitas del pliego Más allá de los requisitos explícitos, la propuesta aporta valor mediante la identificación de retos y riesgos no expresamente detallados en el pliego, pero inherentes a la naturaleza del servicio, tales como:
- Riesgos derivados de la alta interdependencia entre sistemas.
- Complejidad en la gestión de entornos híbridos (legacy + contenerización progresiva).
- Necesidad de control del cambio en entornos críticos con millones de usuarios.
- Impacto operativo de la evolución tecnológica (migraciones, IA, automatización).
Esta capacidad de anticipación demuestra un nivel de comprensión avanzado y permite incorporar medidas preventivas desde el diseño, reduciendo la probabilidad de incidencias y mejorando la resiliencia del servicio. Propuesta de mejoras alineadas con las necesidades reales de EducaMadrid Todas las mejoras propuestas (automatización, observabilidad, modelos predictivos, integración de IA, entre otras) no se presentan como elementos genéricos, sino como respuestas concretas a necesidades detectadas en el pliego y en el entorno real de la plataforma, tales como:
- Optimización de la operación (automatización y reducción de tareas manuales).
- Mejora de la calidad del servicio (monitorización y observabilidad avanzada).
- Anticipación de incidencias (modelos predictivos).
- Evolución tecnológica alineada con el roadmap del pliego (IA on- premise, contenerización)
. Esto garantiza que las mejoras sean:
- Coherentes con el contexto.
- Viables técnicamente.
- Relevantes desde el punto de vista del servicio.
- Valorables positivamente por el evaluador como aportación sustancial.
3.1.3 Viabilidad del proyecto en general Declaración de viabilidad La solución propuesta presenta una viabilidad plena, contrastada y sin incertidumbres, quedando acreditada en los planos:
- Técnico, mediante una arquitectura probada, alineada con el entorno real de
EducaMadrid y basada en tecnologías consolidadas.
- Operativo, mediante un modelo industrializado que garantiza continuidad, eficiencia y
cumplimiento de ANS.
- Organizativo, mediante un modelo de gobierno estructurado y roles claramente definidos.
- De riesgo, mediante un sistema preventivo y proactivo de control continuo.


Esta viabilidad está basada en los requisitos del pliego y su implementación detallada en el apartado 3.1.6 de la presenta oferta, donde empresa_s considera cubrir de forma exhaustiva cada uno de los ámbitos funcionales y técnicos exigidos. Viabilidad técnica sin incertidumbre Adaptación completa al ecosistema EducaMadrid La propuesta se apoya en un conocimiento real y profundo del entorno:
- Gestión de plataformas distribuidas con alta criticidad: Portal educativo, LDAP, cloud, MAX,
correo, IA, aulas virtuales.
- Volumen y complejidad: +3.500 bases de datos y miles de usuarios concurrentes.
No se introducen tecnologías disruptivas no probadas, sino que se optimiza y evoluciona el ecosistema existente, eliminando riesgos de adopción. Arquitectura diseñada para continuidad real del servicio La arquitectura garantiza:
- Alta disponibilidad estructural (\>99,95% – 99,99%).
- Escalabilidad horizontal en todos los niveles (BBDD, cloud, LDAP, LMS).
- Tolerancia a fallos con recuperación automática (\<5 min).
Además:
- Balanceo de carga dinámico.
- Replicación near real-time.
- Redistribución automática de servicios.
Modelo de ingeniería moderno (DevOps + automatización + IA) El proyecto se implementa bajo un modelo integrado:
- DevOps / GitOps / IaC.
- Automatización \>80% de tareas operativas.
- Integración continua + validación en preproducción.
- Observabilidad completa (métricas, logs, trazas).
Resultado:
- Eliminación de errores manuales.
- Despliegues seguros y reversibles.
- Reducción drástica del riesgo técnico.
Viabilidad operativa: ejecución garantizada Cobertura íntegra del servicio exigido Se cubren todos los bloques del pliego:
- Bases de datos, cloud, correo, seguridad, IA.
- Monitorización y pruebas de rendimiento.
- Evolución de servicios y mantenimiento correctivo/evolutivo.
- Servicios bajo ANS y soporte continuo.
Resultado: No hay lagunas funcionales → viabilidad completa del alcance. Operación industrializada y medible


El servicio se basa en:
- Monitorización 100% de servicios.
- Detección de incidencias \<1 minuto.
- Tiempo de reacción \<5 minutos.
- Pruebas de estrés superiores al 120% de carga real.
Resultado: Esto transforma la operación de reactiva a proactiva y predictiva . Continuidad de servicio garantizada Se establecen mecanismos específicos:
- Despliegues blue- green / rolling / canary.
- Ventanas controladas y periodos no lectivos.
- Rollback automático en caso de incidencia.
Impacto: Cero interrupciones no controladas en servicios educativos críticos. Viabilidad organizativa y de gobierno Modelo de gobierno multinivel (factor diferenciador) Estructura consolidada en:
- Nivel estratégico → dirección y alineación.
- Nivel táctico → planificación, calidad, control .
- Nivel operativo → ejecución diaria.
Con:
- Comités periódicos.
- Seguimiento continuo.
- Trazabilidad total.
Garantiza control completo del proyecto en todo momento. Alineación con perfiles del pliego El equipo cubre todas las especialidades requeridas:
- Sistemas, BBDD, cloud, ciberseguridad, IA, automatización
No hay dependencia externa no controlada → mayor viabilidad. Viabilidad basada en control de riesgos Gestión preventiva real (no declarativa) Se parte de:
- Catálogo de riesgos críticos (servicios core EducaMadrid) .
- Matriz probabilidad- impacto.
- Priorización continua.
Mecanismos de mitigación efectivos
- Alta disponibilidad y redundancia.
- Backups automatizados y validados.
- Hardening y seguridad continua.
- Failover automático.


Viabilidad económica y sostenibilidad El modelo es sostenible gracias a:
- Uso intensivo de automatización → reducción de costes operativos .
- Tecnologías Open Source → optimización económica.
- Arquitectura escalable → crecimiento sin sobrecostes .
Alineamiento total con la satisfacción de requisitos (Punto 3.1.6 de la presente oferta técnica) La viabilidad queda reforzada por:
- Correspondencia 1:1 entre requisitos y solución técnica.
- Cobertura integral de todos los apartados del Anexo II.
- Incorporación de mejoras reales:
o Automatización. o Observabilidad. o IA. o Modelos predictivos. Elementos diferenciales que
- Enfoque proactivo y predictivo (no reactivo).
- Automatización avanzada (reducción de riesgo operativo).
- Integración real de IA (no teórica).
- Observabilidad completa (control total del sistema).
- Trazabilidad end- to-end (auditable y verificable).
- Adaptación al calendario educativo (clave sector público).
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


Este enfoque garantiza la trazabilidad completa desde los requisitos hasta la puesta en producción, combinando prácticas de desarrollo estructurado y orientado a objetos, e incorporando técnicas de modelado estándar como UML. Estudio de Viabilidad del Sistema (EVS) En esta fase se analizan las necesidades planteadas y se definen posibles soluciones desde un punto de vista técnico, económico, operativo y legal. Se evaluarán distintas alternativas (desarrollo a medida, soluciones comerciales o mixtas), seleccionando la más adecuada en base a su impacto, coste y riesgos asociados. El resultado de este análisis servirá como base para la toma de decisiones y la definición del alcance del proyecto. Análisis del Sistema de Información (ASI) Esta fase tiene como finalidad definir en detalle los requisitos del sistema, tanto funcionales como no funcionales, garantizando su correcta comprensión y trazabilidad. Se elaborarán modelos de análisis (casos de uso, modelo de datos, procesos, etc.) y se definirán las interfaces de usuario, asegurando que el sistema responde a las necesidades reales de los usuarios. El resultado principal será la Especificación de Requisitos de Software (ERS) , que actuará como referencia contractual y técnica para el desarrollo posterior. Diseño del Sistema de Información (DSI) En esta fase se define la arquitectura técnica del sistema y el diseño detallado de sus componentes, incluyendo:
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
Se establecerá un sistema de gestión de incidencias y evolución que permita el seguimiento, control y análisis de todas las actuaciones realizadas. 3.1.5 Rendimiento previsible de las distintas soluciones
1. Bases de Datos (BD)
Rendimiento previsible:
- Alta disponibilidad mediante clustering MariaDB/PostgreSQL + ProxySQL.
- Balanceo dinámico de carga entre nodos.
- Reducción de latencia de consultas mediante tuning continuo.
KPIs:
- Latencia de consultas críticas: ≤ 50 ms.
- Replicación: near real-time (≤ 1s).
- Disponibilidad BD: ≥ 99,99 %.
- Tiempo de recuperación ante fallo: \< 5 min.
Escalabilidad:
- Horizontal mediante incremento de nodos.
- Redistribución automática de carga.
Valor diferencial:
- Modelos predictivos de crecimiento y autooptimización continua.

2. Monitorización, testeo y rendimiento (MON)
Rendimiento previsible:
- Detección proactiva de incidencias (antes del impacto).
- Validación continua mediante pruebas de carga.
KPIs:
- Detección de incidencias: \< 1 min.
- Tiempo de reacción ante alertas: \< 5 min.
- Cobertura monitorizada: 100% servicios.


Capacidad:
- Simulación de picos \>120% carga real.
Valor diferencial:
- Integración con DevOps → pruebas automáticas en cada despliegue.

3. Actualización de servicios (UPD)
Rendimiento previsible:
- Actualizaciones sin impacto mediante estrategia rolling / blue- green.
- Reducción de degradaciones post-upgrade.
KPIs:
- Disponibilidad durante actualización: ≥ 99,9 %.
- Fallos post-despliegue: \< 2 %.
- Tiempo rollback: \< 10 min.
Valor diferencial:
- Validación completa en preproducción + rollback automatizado.

4. Cloud (CLO)
Rendimiento previsible:
- Plataforma capaz de soportar \> 2 millones de usuarios.
- Reducción de latencia mediante segmentación y balanceo NFS.
KPIs:
- Tiempo de acceso a ficheros: ≤ 1 segundo.
- Latencia de sincronización: ≤ 2 segundos.
- Disponibilidad cloud: ≥ 99,95 %.
Escalabilidad:
- Crecimiento dinámico de almacenamiento sin impacto.
- Redistribución automática de usuarios.
Valor diferencial:
- Arquitectura distribuida sin cuellos de botella.

5. Otros desarrollos (OTR)
Autenticación y SSO:
- Tiempo de login: ≤ 500 ms.
- Disponibilidad: 99,99 %.
- Autenticación multifactor sin impacto perceptible.
Automatización:
- Reducción de intervención manual: \> 80 %.
- Tiempo de ejecución tareas: reducción \> 50 %.
ELK / Analítica:
- Indexación en tiempo real


- Consulta de logs: \< 2 segundos.
IA:
- Latencia de inferencia: ≤ 1- 2 segundos.
- Escalado GPU dinámico.
- Alta concurrencia sin degradación.

6. Correo electrónico (COR)
Rendimiento previsible:
- Gestión inteligente de colas de envío.
- Adaptación automática a límites de proveedores.
KPIs:
- Entrega efectiva: ≥ 98 %.
- Latencia envío masivo: optimizada sin bloqueo.
- Disponibilidad: ≥ 99,95 %.
Valor diferencial:
- Control dinámico anti-spam y reputación.

7. Sistema Operativo MAX (MAX)
Rendimiento previsible:
- Optimización del sistema operativo para entornos educativos con recursos heterogéneos.
- Reducción de tiempos de arranque y login mediante tuning de servicios y procesos.
- Integración eficiente con LDAP, cloud y aulas virtuales.
- Actualización controlada sin impacto en el usuario.
KPIs:
- Tiempo de arranque: ≤ 60 s.
- Tiempo de login: ≤ 5 s.
- Consumo medio RAM: ≤ 2 GB.
- Disponibilidad: ≥ 99,5 %.
- Incidencias post-update: \< 1 %.
Escalabilidad:
- Despliegue masivo en miles de dispositivos.
- Gestión centralizada de configuraciones.
- Adaptación a hardware heterogéneo.
Valor diferencial:
- Optimización real para entornos educativos con hardware limitado.
- Automatización completa de despliegues y actualizaciones.

8. Aulas Virtuales (AV)
Rendimiento previsible:
- Alta disponibilidad de plataforma LMS bajo alta concurrencia.


- Balanceo de carga entre islas y nodos Moodle.
- Optimización de bases de datos y consultas.
- Pruebas periódicas de carga y estrés.
KPIs:
- Tiempo de respuesta usuario: ≤ 2 s.
- Disponibilidad: ≥ 99,95 %.
- Concurrencia: miles de usuarios simultáneos.
- Latencia acceso BD: ≤ 50 ms.
Escalabilidad:
- Escalado horizontal de frontales y nodos.
- Redistribución de usuarios entre islas.
- Ampliación dinámica de capacidad.
Valor diferencial:
- Optimización específica para picos educativos (inicio curso, evaluaciones).
- Modelo predictivo de carga y redistribución inteligente.

9. LDAP y Portal Educativo (POR)
Rendimiento previsible:
- Autenticación rápida y transparente.
- Replicación eficiente y consistente entre nodos.
- Balanceo de carga y alta disponibilidad.
- Integración con servicios externos (cloud, SSO, aulas).
KPIs:
- Tiempo autenticación: ≤ 500 ms.
- Latencia replicación: ≤ 1 s.
- Disponibilidad: ≥ 99,99 %.
- Errores autenticación: \< 0,1 %.
Escalabilidad:
- Ampliación de nodos LDAP sin impacto.
- Distribución geográfica del servicio.
- Balanceo mediante DNS o proxy.
Valor diferencial:
- Arquitectura redundante orientada a identidad masiva.
- Acceso unificado y transparente a todos los servicios.

10. Seguridad (SEG)
Rendimiento previsible:
- Protección continua sin degradación del servicio.
- Monitorización y correlación de eventos en tiempo real.
- Detección temprana de vulnerabilidades.


- Aplicación de medidas de hardening.
KPIs:
- Disponibilidad: ≥ 99,95 %.
- Tiempo detección incidente: \< 1 min.
- Resolución vulnerabilidades críticas: ≤ 24 h.
- Cumplimiento ENS: 100 %.
Escalabilidad:
- Adaptación a crecimiento de servicios y usuarios.
- Integración con sistemas distribuidos.
- Centralización de seguridad.
Valor diferencial:
- Seguridad proactiva integrada en operación.
- Equilibrio óptimo entre protección, rendimiento y experiencia.

11. Automatización y Contenedores (CON)
Rendimiento previsible:
- Despliegues rápidos y sin interrupción.
- Autoescalado de servicios según demanda.
- Optimización de recursos mediante orquestación.
- Reducción de errores manuales.
KPIs:
- Tiempo despliegue: ≤ 5 min.
- Disponibilidad: ≥ 99,95 %.
- Automatización tareas: \> 80 %.
- Tiempo recuperación fallo: ≤ 2 min.
Escalabilidad:
- Escalado automático horizontal (Kubernetes).
- Distribución dinámica de carga.
- Elasticidad en consumo de recursos.
Valor diferencial:
- Modelo DevOps + GitOps completamente automatizado.
- Infraestructura como Código (IaC).

12. Migración de servidores entre CPDs (MIG)
Rendimiento previsible:
- Migraciones sin impacto perceptible en usuario.
- Continuidad del servicio durante transición.
- Validación completa antes y después de migración.
- Supervisión intensiva post-migración.
KPIs: Página 34 de 239


- Disponibilidad durante migración: ≥ 99,9 %.
- Tiempo parada servicio: mínimo / controlado.
- Integridad datos: 100 %.
- Incidencias post-migración: \< 2 %.
Escalabilidad:
- Migración masiva de servicios.
- Adaptación a distintas arquitecturas CPD.
- Optimización de recursos destino.
Valor diferencial:
- Procedimientos industrializados y automatizados.
- Hiper-supervisión y control total del proceso.

13. Inteligencia Artificial (IA)
Rendimiento previsible:
- Baja latencia en inferencia de modelos.
- Alta capacidad de procesamiento concurrente.
- Optimización dinámica de uso de CPU/GPU.
- Integración transversal en servicios.
KPIs:
- Latencia inferencia: ≤ 1– 2 s.
- Throughput: miles de peticiones simultáneas.
- Disponibilidad: ≥ 99,9 %.
- Uso eficiente GPU: optimizado dinámicamente.
Escalabilidad:
- Escalado horizontal de nodos de inferencia.
- Adaptación automática a carga.
- Balanceo de peticiones.
Valor diferencial:
- Modelo LLMOps para operación eficiente.
- Integración real de IA en ecosistema educativo.
## Memoria Técnica

### Solución técnica ofertada

#### Satisfacción de los requisitos

3.1.6 Satisfacción de los requisitos 3.1.6.1 Definición y Alcance de los trabajos II.1. Descripción del servicio de mantenimiento y actualización para aseguramiento de la continuidad del servicio de los sistemas en entornos productivos. APARTADO: II.1.1. Mantenimiento y mejora de entornos de Bases de Datos (BD) Requisito: II.1.1.1. Mantenimiento y mejora de entornos de Bases de Datos MariaDB y ProxySQL avanzado Requerimiento EducaMadrid


Algunos servicios, necesitan entornos de base de datos MariaDB Cluster, así como en configuración de Proxy Avanzado (BD1). Para ello se solicita:
- Optimizar, mantener y, en definitiva, adecuar los diferentes nodos de bases de datos del
clúster MySQL / MariaDB, y también realizar las tareas de optimización y el mantenimiento del proxy SQL avanzado tanto en los entornos de preproducción como en producción.
- Optimizar los procesos de Monitorización y Mantenimiento del clúster de Base de Datos
mediante una herramienta específica, así como el mantenimiento de la misma. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el mantenimiento y evolución de los entornos MariaDB Cluster y ProxySQL como un servicio continúo orientado a garantizar la alta disponibilidad, el rendimiento y la escalabilidad de la plataforma EducaMadrid. Se implantará un modelo de operación basado en monitorización avanzada, automatización operativa y optimización continua, permitiendo detectar de forma proactiva posibles degradaciones del servicio y anticipar necesidades de crecimiento. empresa_s realizará un análisis periódico y automatizado del estado de los clústeres MariaDB y de la capa ProxySQL, supervisando métricas críticas como consumo de recursos, latencia de consultas, concurrencia, estado de replicación y balanceo de carga. Asimismo, se identificarán consultas ineficientes, bloqueos, cuellos de botella y nodos degradados que puedan afectar al rendimiento de la plataforma. La optimización del entorno incluirá el ajuste avanzado de parámetros del motor MariaDB (InnoDB, buffers, cachés y conexiones), la revisión de consultas SQL y planes de ejecución, así como la mejora de los modelos de replicación y balanceo entre nodos para garantizar resiliencia y alta disponibilidad. ProxySQL será tratado como un componente estratégico de la arquitectura, optimizando reglas de routing, pools de conexiones, mecanismos de failover y tiempos de respuesta, asegurando un comportamiento estable incluso en escenarios de alta concurrencia o fallo. La operación del servicio se apoyará en herramientas de observabilidad y monitorización centralizada, definiendo KPIs técnicos, alertas automáticas y automatización de tareas recurrentes de mantenimiento, validación y optimización. Para garantizar la estabilidad del servicio, todos los cambios relevantes serán previamente validados en entornos clonados o de preproducción, realizando pruebas funcionales y de rendimiento antes de su paso a producción. Las actuaciones críticas se ejecutarán en ventanas controladas y coordinadas con los responsables técnicos de EducaMadrid. Asimismo, empresa_s garantizará la documentación actualizada de configuraciones y arquitectura, así como la trazabilidad completa de todas las actuaciones realizadas sobre el entorno. Propuesta de mejora y evolución del servicio Con el objetivo de evolucionar el servicio hacia un modelo más resiliente, automatizado y escalable, empresa_s propone:
- Implantación de entornos clonados para validación avanzada y pruebas de tuning antes de
aplicar cambios en producción.
- Ejecución periódica de pruebas de carga y estrés para identificar límites operativos y
optimizar el comportamiento del clúster y ProxySQL.
- Integración de plataformas avanzadas de gestión y monitorización tipo ClusterControl para
centralizar la supervisión, automatizar failovers y mejorar la operación del clúster.


- Implementación de modelos predictivos de capacidad y automatización de respuestas ante
incidencias mediante mecanismos self-healing.
- Evolución hacia un modelo de operación proactiva basado en métricas, tendencias
históricas y observabilidad avanzada.

Valor aportado Estas mejoras permiten garantizar la continuidad del servicio, mejorar el rendimiento y reducir el impacto de incidencias. Además, permiten incrementar la disponibilidad de la plataforma, optimizar el reparto de carga entre nodos y proxies, reducir tiempos de intervención mediante automatización operativa y anticipar necesidades de crecimiento futuras, garantizando una gestión más eficiente, segura y escalable de los entornos de bases de datos críticos de EducaMadrid.

Requisito: II.1.1.2. Mantenimiento y optimización proactiva de las bases de datos de la plataforma Requerimiento EducaMadrid Actualmente la plataforma de EducaMadrid utiliza en torno a 3.500 bases de datos entre el portal, las aulas virtuales, la aplicación de cloud y el resto de los servicios. Se necesita la realización de las tareas oportunas para el mantenimiento, mejora y optimización proactiva de las bases de datos de EducaMadrid (BD2). Se solicita:
- Optimizar de forma continua las diferentes bases de datos, haciendo labores de
mantenimiento, mejora y optimización orientadas a mejorar las consultas y de backup para asegurar la información.

- Asegurar una correcta seguridad en las conexiones a las BBDD.


![Imagen de la página 37](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0037-imagen-003.jpg>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0037-imagen-003.jpg -->
- Arquitectura de base de datos en tres capas con cliente, balanceador y clúster.
- Las aplicaciones se conectan por MySQL a un proxy inverso MaxScale, ProxySQL o HAProxy, que distribuye lecturas y escrituras entre tres nodos Galera.
- ClusterControl aparece conectado a los tres nodos para administrar o supervisar el clúster.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0037-imagen-003.jpg -->

![Imagen de la página 37](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0037-imagen-004.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0037-imagen-004.png -->
- Esquema de replicación Galera con tres nodos MariaDB.
- Todos los nodos usan wsrep, comparten la capa de replicación y admiten comunicación bidireccional con el cliente.
- La disposición representa un clúster multimaestro en el que cualquier nodo puede recibir operaciones.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0037-imagen-004.png -->

- Realizar tareas de mantenimiento preventivo y proactivo en fechas de una menor carga,
planificando dichas tareas con antelación. Se deben de aprovechar los períodos no lectivos vacaciones de verano, semana santa y/o Navidad. Estas tareas se realizarán periódicamente dos veces al año. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el mantenimiento y optimización de las más de 3.500 bases de datos de la plataforma EducaMadrid mediante un modelo de operación continuo, basado en monitorización avanzada, automatización y optimización proactiva, garantizando el rendimiento, la disponibilidad y la seguridad de los diferentes servicios de la plataforma. Se realizará una supervisión centralizada y automatizada del estado de las bases de datos, controlando métricas críticas como tiempos de respuesta, carga de consultas, consumo de recursos, concurrencia y crecimiento de las instancias. Este análisis permitirá identificar de forma temprana degradaciones de rendimiento, consultas ineficientes, bloqueos y posibles cuellos de botella. empresa_s implantará una estrategia de optimización continúa adaptada a cada motor de base de datos y tipología de servicio, incluyendo optimización de consultas SQL, mantenimiento de índices, ajuste de parámetros de configuración, reorganización de datos y redistribución de carga entre instancias cuando sea necesario. La gestión de copias de seguridad se realizará de forma automatizada y planificada en ventanas de baja carga, garantizando la integridad y disponibilidad de la información mediante validaciones periódicas de restauración, políticas de retención y control de versionado. Asimismo, se reforzará la seguridad de las bases de datos mediante revisión de accesos, control de usuarios y privilegios, auditoría de conexiones y aplicación de mecanismos de cifrado y endurecimiento de configuraciones. Las tareas de mantenimiento preventivo y correctivo se ejecutarán de forma planificada, priorizando periodos de baja actividad o ventanas no lectivas para minimizar el impacto sobre la plataforma. La operación del servicio estará apoyada en automatización avanzada:
- scripts de control de carga y rendimiento,

- automatización de tareas de mantenimiento y backup,

- inventariado automático de instancias y configuraciones,

- integración con sistemas globales de monitorización.

empresa_s garantizará además la trazabilidad completa de actuaciones, el control de cambios y la actualización continua de la documentación técnica e inventario de bases de datos. Propuesta de mejora y evolución del servicio Con el objetivo de evolucionar hacia un modelo más eficiente, automatizado y predictivo, empresa_s propone:
- Implantación de sistemas de análisis diario de carga y rendimiento para redistribución
dinámica entre instancias.

- Monitorización avanzada individualizada por base de datos, permitiendo detectar
desviaciones y anticipar degradaciones.

- Automatización de tareas recurrentes de optimización:


o Indexación,

o Limpieza,

o Reorganización, o Tuning continuo.

- Generación de métricas históricas y cuadros de mando para análisis evolutivo de
rendimiento y capacidad.

- Implantación de inventariado automatizado de versiones, configuraciones y dependencias.

- Evolución hacia modelos predictivos basados en tendencias reales de uso y crecimiento
de la plataforma. Valor aportado Estas mejoras permiten garantizar la continuidad del servicio, mejorar el rendimiento y reducir el impacto de incidencias. Además, permiten optimizar el uso de recursos, mejorar la capacidad de anticipación ante crecimientos futuros, automatizar tareas operativas críticas y garantizar una gestión más eficiente, segura y escalable de los entornos de bases de datos de EducaMadrid .

Requisito: II.1.1.3. Mantenimiento y evolución de las bases de datos de gestión de la configuración (CMDB) Requerimiento EducaMadrid La plataforma de EducaMadrid dispone de Bases de Datos relacionadas con la gestión de la configuración (CMDBuild, …), las cuales necesitan de la realización de las tareas oportunas para el mantenimiento, mejora y optimización proactiva (BD3). Se solicita:
- Adecuar la Base de Datos para incorporar y comprender todos los elementos actuales a
nivel físico y lógico (BBDD, firewalls, hosts, DNS, redes, tamaño de almacenamiento, backups, balanceadores, contenedores), así como las diferentes aplicaciones y las relaciones entre todos estos elementos. Así como tener una relación de los diferentes contenedores y los hosts de los mismos.
- Alimentar de la propia Base de Datos de los datos extraídos de los entornos
preferiblemente de manera automatizada o manual en caso de ser necesario.
- Para ello se usarán las herramientas De Software Libre necesarias.
Estas tareas se realizarán periódicamente. Propuesta técnica de empresa_s


![Imagen de la página 39](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0039-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0039-imagen-003.png -->
- Franja infográfica con una propuesta de mejora y evolución continua del servicio de bases de datos.
- Enumera análisis diario de carga, monitorización avanzada, mantenimiento y ajuste automatizados, uso de históricos, inventario de bases y versiones, modelos predictivos y optimización basada en datos reales.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0039-imagen-003.png -->

Los especialistas de empresa_s abordarán la evolución y mantenimiento de la CMDB de EducaMadrid mediante un modelo orientado a la automatización, normalización del dato y sincronización continua con la infraestructura real de la plataforma. Se realizará un análisis del modelo actual de gestión de configuración, revisando la estructura de datos, relaciones entre activos y calidad de la información almacenada, con el objetivo de garantizar una CMDB coherente, actualizada y alineada con la realidad operativa de EducaMadrid. empresa_s definirá un modelo de datos optimizado y escalable que permita integrar de forma estructurada:
- Hosts y servidores,
- Bases de datos y aplicaciones,
- Redes, DNS y balanceadores,
- Firewalls y reglas de seguridad,
- Almacenamiento y NFS,
- Contenedores y relaciones entre servicios.
La actualización de la información se realizará mediante procesos automatizados de extracción, transformación y carga (ETL), integrando datos procedentes de inventarios, sistemas, redes, plataformas de virtualización y entornos contenerizados. Para ello se desarrollarán scripts y playbooks de automatización mediante Ansible, permitiendo la sincronización periódica y centralizada de la información, reduciendo la intervención manual y garantizando la trazabilidad completa de los cambios realizados. Asimismo, empresa_s realizará tareas continuas de mantenimiento y optimización de la CMDB:
- Revisión de integridad y consistencia de datos,
- Actualización de inventarios y relaciones,
- Optimización de rendimiento de la base de datos,
- Adaptación a nuevos servicios e infraestructuras.
Toda la operación estará coordinada con los equipos técnicos y de seguridad de EducaMadrid, garantizando la coherencia funcional y operativa del entorno. Propuesta de mejora y evolución del servicio Con el objetivo de evolucionar la CMDB hacia un modelo más automatizado, fiable y alineado con la operación real de la plataforma, empresa_s propone:
- Automatización completa del ciclo de vida del dato: descubrimiento, ingesta, validación y
actualización.
- Evolución hacia una CMDB sincronizada en tiempo casi real con los sistemas de
infraestructura y servicios.
- Implantación de controles automáticos de calidad del dato para detectar inconsistencias,
duplicidades o elementos obsoletos.
- Integración con herramientas de monitorización y operación para enriquecer la CMDB con
información de estado y dependencias.
- Optimización del modelo relacional para facilitar análisis de impacto, auditoría y gestión de
incidencias.


Valor aportado Estas mejoras permiten garantizar la continuidad del servicio, mejorar la calidad y trazabilidad de la información y reducir el impacto de incidencias derivadas de configuraciones desactualizadas o inconsistentes. Además, permiten disponer de una CMDB más automatizada, coherente y alineada con la infraestructura real de EducaMadrid, facilitando la gestión operativa, el análisis de impacto y la evolución futura de la plataforma. Requisito: II.1.1.4. Mantenimiento y optimización de las bases de datos de las Aulas Virtuales Requerimiento EducaMadrid Actualmente EducaMadrid tiene más de 2500 bases de datos de PostgreSQL distribuidas en 20 servidores tanto físicos clusterizados como virtuales (BD4). Se solicita:
- Realizar un análisis del uso y carga soportada por dichos servidores, con herramientas
propias de la BBDD.

- Adaptar la arquitectura actual, actualizando, ampliando, configurando o eliminando
servidores de bases de datos PostgreSQL acorde a los datos obtenidos.

- Redistribuir las bases de datos entre todos los servidores, en base a la carga, uso y
tamaño.

- Modificar la planificación de los backups de las bases de datos involucradas.
Estas tareas se realizarán periódicamente, en períodos no lectivos. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el mantenimiento de las bases de datos de las Aulas Virtuales como un proceso continuo orientado a garantizar el rendimiento, la estabilidad y la escalabilidad de los más de 2.500 entornos PostgreSQL distribuidos entre servidores físicos clusterizados y plataformas virtualizadas. Se realizará un análisis periódico y automatizado del comportamiento de los servidores y bases de datos mediante herramientas nativas de PostgreSQL y sistemas de monitorización avanzados, evaluando carga, consumo de recursos, concurrencia, tiempos de respuesta y crecimiento de las bases de datos.


![Imagen de la página 41](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0041-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0041-imagen-003.png -->
- Arquitectura de una CMDB centralizada alimentada automáticamente desde inventarios, redes, virtualización, bases de datos, seguridad, almacenamiento y monitorización.
- La ingesta realiza recolección, validación, normalización, transformación ETL y carga periódica en CMDBuild.
- El modelo central relaciona infraestructura, servicios, aplicaciones, redes, seguridad y almacenamiento.
- La CMDB sirve para soporte, análisis de impacto y cambios, auditoría, capacidad, reporting y cuadros de mando.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0041-imagen-003.png -->

A partir de los resultados obtenidos, empresa_s ejecutará tareas de optimización y redistribución dinámica de bases de datos entre servidores, equilibrando la carga y adecuando la arquitectura a las necesidades reales de uso de las Aulas Virtuales. Se llevarán a cabo:
- Ajustes de configuración y tuning específico de PostgreSQL.

- Redistribución controlada de bases de datos según carga, tamaño y criticidad.

- Instalación y adaptación de nuevos servidores cuando sea necesario.

- Optimización de entornos clusterizados y virtualizados.

- Validación de compatibilidad con las versiones del LMS y servicios asociados.
En paralelo, se revisará y optimizará la estrategia de backups:
- Automatización y planificación de copias de seguridad.

- Verificación periódica de restauración.

- Optimización de ventanas de backup para minimizar impacto.

- Ajuste de políticas de retención y almacenamiento.
Las actuaciones de mayor impacto se realizarán en periodos no lectivos, garantizando la continuidad del servicio y minimizando afectaciones sobre usuarios y centros educativos. Asimismo, se mantendrá una trazabilidad completa de las actuaciones realizadas:
- Documentación actualizada de arquitectura y configuraciones.
- Registro de redistribuciones y cambios ejecutados.
- Coordinación continua con los equipos técnicos de EducaMadrid.
Propuesta de mejora y evolución del servicio empresa_s propone evolucionar el entorno PostgreSQL de las Aulas Virtuales hacia un modelo más automatizado, equilibrado y escalable mediante:
1. Creación de plantillas estandarizadas de servidores PostgreSQL para despliegues rápidos
y homogéneos.
2. Actualización controlada de versiones PostgreSQL alineadas con la matriz de
compatibilidad del LMS.
3. Automatización del análisis periódico de carga, tamaño y utilización de bases de datos.
4. Implementación de métricas históricas y modelos predictivos para anticipar saturaciones y
necesidades de ampliación.
5. Automatización de redistribuciones de carga y optimización continua del rendimiento de los
entornos. Valor aportado Estas mejoras permiten garantizar la continuidad del servicio, optimizar el rendimiento de las Aulas Virtuales y evolucionar la plataforma hacia un modelo más resiliente, escalable y adaptado al crecimiento continuo de EducaMadrid. Requisito: II.1.1.5. Mantenimiento y optimización de disparadores y Foreign Data Wrappers en los entornos “Portal” y “LDAP Plano”


Requerimiento EducaMadrid Tareas adicionales necesarias en la optimización, actualización y mantenimiento de las Bases de Datos del Portal y el LDAP Plano (BD5). Se solicita:
- Realizar un análisis pormenorizado de los datos actuales de raíces, así como los diferentes
campos, fechas de cambios y modificaciones.

- Adecuar y mantener las diferentes funciones y disparadores en las BBDD, así como la
creación de los campos, índices y Foreign Data Wrappers necesarios.

- Adecuar y mantener los scripts necesarios para que de manera recurrente todos los datos
de raíces estén sincronizados con la BBDD del Portal y estos a su vez con el LDAP plano.

Estas tareas se realizarán periódicamente, en períodos no lectivos. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el mantenimiento y optimización de los entornos “Portal” y “LDAP Plano” mediante un modelo orientado a garantizar la coherencia, integridad y sincronización continua de la información entre plataformas. Se realizará un análisis detallado de las estructuras de datos, relaciones, campos y mecanismos actuales de sincronización, evaluando el comportamiento de triggers, funciones y procesos batch asociados a la integración entre el Portal y el LDAP plano. empresa_s llevará a cabo la optimización de:
- Disparadores (triggers) y funciones de sincronización.

- Índices y estructuras de tablas.

- Foreign Data Wrappers (FDW) para acceso eficiente entre entornos.

- Procesos de carga y actualización automática de datos.
Asimismo, se desarrollarán y mantendrán scripts de sincronización recurrentes que permitan garantizar la actualización automática y controlada de la información entre sistemas, minimizando latencias y evitando inconsistencias o duplicidades. La operación estará apoyada en mecanismos de monitorización y control:
- validación automática de integridad de datos

- generación de logs y trazabilidad

- alertas ante errores o desincronizaciones

- seguimiento continuo del rendimiento de los procesos
Las tareas de mayor impacto se ejecutarán en periodos no lectivos o ventanas controladas, reduciendo la afectación sobre los servicios productivos de EducaMadrid . Propuesta de mejora y evolución del servicio empresa_s propone evolucionar el modelo actual hacia un sistema de sincronización más eficiente, automatizado y resiliente mediante:


1. Implantación de un entorno de preproducción para validación de triggers, FDW y scripts
antes de producción.
2. Optimización avanzada de procesos batch y sincronización para reducir tiempos de
ejecución y consumo de recursos.
3. Automatización de informes diarios del estado de sincronización y replicación.
4. Mejora de políticas de backup y recuperación del entorno LDAP plano y bases de datos
asociadas.
5. Evolución hacia un modelo de sincronización con menor latencia y mayor capacidad de
trazabilidad y control. Valor aportado Estas mejoras permiten garantizar la continuidad del servicio, mejorar la coherencia de la información y reducir el impacto de incidencias derivadas de errores de sincronización o inconsistencias de datos. Además, permiten disponer de un entorno más estable, automatizado y preparado para la evolución continua de los servicios integrados de EducaMadrid. Requisito: II.1.1.6. Implementación y mantenimiento de bases de datos en entornos de microservicios Requerimiento EducaMadrid Actualmente EducaMadrid está adaptando algunos de sus aplicativos y servicios a la arquitectura de contenedores y microservicios (BD6). Se solicita:
- Adecuar las Bases de Datos a una versión actualizada en el entorno correspondiente.
- Realizar las adaptaciones necesarias de BBDD Virtuales a BBDD DevOps de cada nueva
versión para asegurar un rendimiento óptimo.
- Realizar mantenimiento correctivo de cada nueva versión instalada.

Estas tareas se realizarán periódicamente, en períodos no lectivos. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la implantación y mantenimiento de bases de datos en entornos de microservicios mediante un modelo orientado a la automatización, escalabilidad y alta disponibilidad, alineado con la evolución tecnológica de EducaMadrid hacia arquitecturas DevOps y contenerizadas. Se realizará una gestión continua del ciclo de vida de los sistemas gestores de bases de datos, garantizando la actualización controlada de versiones MySQL/MariaDB y PostgreSQL, así como su adaptación a entornos basados en imágenes Docker y servicios desacoplados. empresa_s ejecutará las tareas necesarias para:
- Migración de bases de datos desde entornos virtualizados tradicionales a plataformas
contenerizadas.

- Diseño de arquitecturas optimizadas para persistencia y alta disponibilidad.

- Automatización de despliegues mediante Dockerfiles, YAML y plantillas reutilizables.

- Integración de backups automatizados y políticas de recuperación.


- Optimización de rendimiento y tuning continuo de las bases de datos.

- Monitorización proactiva de recursos, consumo y latencias.
Todas las actuaciones se validarán previamente en entornos de preproducción, garantizando compatibilidad con los aplicativos y minimizando el impacto sobre producción. Asimismo, empresa_s realizará mantenimiento correctivo y evolutivo continuo:
- aplicación de parches y actualizaciones
- resolución de incidencias
- optimización de configuraciones
- adaptación a nuevas necesidades funcionales
Propuesta de mejora y evolución del servicio Con el objetivo de evolucionar hacia un modelo más moderno, resiliente y automatizado, empresa_s propone:
1. Implantación de entornos completos de preproducción para validación de nuevas versiones
y despliegues.
2. Creación de imágenes Docker optimizadas y homologadas para los distintos motores de
bases de datos.
3. Automatización del ciclo de despliegue y actualización mediante pipelines DevOps.
4. Ejecución periódica de pruebas de carga, estrés y validación funcional.
5. Evolución hacia arquitecturas desacopladas, escalables y orientadas a alta disponibilidad.

Valor aportado Estas mejoras permiten garantizar la continuidad del servicio, acelerar los despliegues y reducir el impacto de incidencias y cambios de versión. Además, permiten evolucionar los entornos de bases de datos hacia arquitecturas más flexibles, automatizadas y preparadas para el crecimiento futuro de la plataforma EducaMadrid.
##### APARTADO: MONITORIZACIÓN, TESTEO Y PRUEBAS DE RENDIMIENTO (MON)
Requisito: II.1.2.1. Mantenimiento periódico del almacenamiento de los centros Requerimiento EducaMadrid EducaMadrid cuenta con un gran número de aplicativos que utilizan NFS para su funcionamiento. De ellos algunos NFS tienen un tamaño que dificulta su control (MON1).


![Imagen de la página 45](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0045-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0045-imagen-003.png -->
- Diagrama de migración de entornos de bases de datos hacia producción y preproducción modernizadas.
- Cada mitad muestra un entorno de producción que debe validarse antes de alimentar una preproducción contenerizada con Docker, Dockerfile y docker-compose.
- Si la validación falla se repite la migración; si es correcta se avanza al nuevo entorno.
- Los beneficios indicados son seguridad, despliegues automatizados, rendimiento, escalabilidad nativa de nube y continuidad.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0045-imagen-003.png -->

Se solicita:
- Realizar de forma periódica una redistribución de los espacios ocupados por los centros
por los distintos NFS atendiendo a la ocupación de estos.

- Para las tareas más pesadas o que requieran de parada del servicio, se deben aprovechar
los períodos no lectivos de vacaciones de verano, semana santa y/o Navidad.

Estas tareas se realizarán periódicamente. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el mantenimiento del almacenamiento NFS de EducaMadrid mediante un modelo basado en monitorización continua, redistribución inteligente y automatización operativa, orientado a garantizar la disponibilidad, escalabilidad y rendimiento de los entornos de almacenamiento utilizados por los centros educativos y servicios de la plataforma. Se realizará un análisis periódico y centralizado del estado de las cabinas y volúmenes NFS, evaluando métricas de ocupación, latencia, throughput y concurrencia, permitiendo identificar de forma temprana situaciones de saturación o degradación del servicio. empresa_s implantará una estrategia de redistribución dinámica de datos:
- Balanceo de carga entre cabinas y nodos de almacenamiento.

- Reorganización lógica de espacios NFS según tipología de uso.

- Optimización de accesos para servicios docentes, contenidos multimedia y plataformas
colaborativas.

- Definición de umbrales preventivos para redistribuciones automáticas.

Las migraciones de datos se realizarán mediante procedimientos controlados y sincronización incremental, utilizando herramientas optimizadas de copia y validación para minimizar el impacto sobre los servicios productivos. La operación estará apoyada en:
- Monitorización continua del rendimiento y capacidad.

- Generación de alertas automáticas.

- Validación de integridad de datos.

- Trazabilidad completa de actuaciones y redistribuciones.

Las intervenciones críticas se planificarán en periodos no lectivos o ventanas controladas, garantizando la continuidad operativa de la plataforma.


![Imagen de la página 46](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0046-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0046-imagen-003.png -->
- Arquitectura de almacenamiento con dos cabinas Infinidat conectadas de forma bidireccional a un núcleo central de servicios y carpetas.
- Un panel superior representa monitorización, métricas y alertas; a la derecha aparecen nube, base de datos y protección.
- El flujo verde sugiere replicación, alta disponibilidad y acceso compartido a documentos, imágenes, vídeo y otros contenidos.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0046-imagen-003.png -->

Propuesta de mejora y evolución del servicio empresa_s propone evolucionar el modelo actual de almacenamiento hacia una arquitectura más eficiente, resiliente y automatizada mediante:
1. Implantación de modelos predictivos de crecimiento y ocupación por centro y servicio.
2. Automatización de redistribuciones preventivas entre cabinas y volúmenes NFS.
3. Integración del almacenamiento con plataformas centralizadas de monitorización y
alertado.
4. Optimización de acceso a contenidos de alta demanda mediante estrategias de caching
distribuido.
5. Generación automática de informes de capacidad, rendimiento y evolución del
almacenamiento. Valor aportado Estas mejoras permiten garantizar la continuidad del servicio, optimizar el rendimiento del almacenamiento y reducir riesgos derivados de saturaciones o degradaciones de capacidad. Además, permiten evolucionar el entorno NFS de EducaMadrid hacia un modelo más automatizado, escalable y preparado para el crecimiento continuo de la plataforma.

Requisito: II.1.2.2. Realización periódica de pruebas de estrés en diferentes entornos de la plataforma Requerimiento EducaMadrid Es necesario determinar de forma continua el comportamiento de las diferentes aplicaciones y entornos funcionales (MON2). Para ello se solicita:
- Medir el rendimiento de las diferentes aplicaciones y entornos funcionales y analizar todos
los datos generados evaluando el desempeño general de la aplicación.

- En caso de encontrar anomalías se debe comenzar un trabajo de investigación para
detectar los problemas del sistema y así poder buscar las posibles soluciones.

Estas tareas se realizarán periódicamente. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la validación del rendimiento de la plataforma EducaMadrid mediante un modelo continuo de pruebas de carga y estrés, orientado a garantizar la estabilidad, escalabilidad y capacidad de respuesta de los diferentes servicios y aplicativos. Se realizará la definición y ejecución periódica de pruebas sobre los entornos críticos de la plataforma, simulando escenarios reales y picos de concurrencia superiores a la carga habitual, permitiendo identificar de forma anticipada posibles degradaciones o cuellos de botella. Las pruebas se realizarán utilizando herramientas Open Source especializadas como Apache JMeter, Gatling o Apache Benchmark, seleccionando en cada caso la más adecuada según el tipo de servicio y arquitectura evaluada. Las tareas contemplarán:


![Imagen de la página 47](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0047-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0047-imagen-003.png -->
- Banda de beneficios operativos del almacenamiento.
- Destaca rendimiento optimizado, servicio continuo, escalabilidad garantizada, uso eficiente de la capacidad, mantenimiento proactivo y mejor experiencia para centros y usuarios.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0047-imagen-003.png -->

- Diseño de escenarios de carga adaptados al uso real de la plataforma.

- Simulación de concurrencia intensiva y pruebas de estrés controladas.

- Monitorización en tiempo real de métricas de sistema, aplicaciones y bases de datos.

- Análisis de tiempos de respuesta, consumo de CPU, memoria, I/O y concurrencia.

- Identificación de cuellos de botella y degradaciones de servicio.

- Validación del comportamiento de la plataforma bajo cargas extremas.

- Elaboración de informes técnicos con propuestas de optimización y mejora.

empresa_s realizará pruebas periódicas tanto en entornos de preproducción como en producción controlada, coordinando las actuaciones con los responsables técnicos de EducaMadrid para minimizar el impacto sobre los servicios. Propuesta de mejora y evolución del servicio empresa_s propone evolucionar el modelo actual hacia un sistema continuo de validación y optimización del rendimiento mediante:
1. Integración de pruebas automáticas de carga dentro de procesos DevOps y despliegues
controlados.
2. Implantación de cuadros de mando de observabilidad y rendimientos integrados con
Grafana, Prometheus y Zabbix.
3. Automatización de alertas proactivas ante degradaciones de servicio o saturaciones.
4. Ejecución periódica de pruebas comparativas antes/después para validar mejoras.
5. Generación de métricas históricas y tendencias para anticipar necesidades de crecimiento.
6. Evolución hacia un modelo proactivo de capacity planning y optimización continua.
Valor aportado Estas mejoras permiten garantizar la estabilidad y disponibilidad de los servicios de EducaMadrid incluso en escenarios de alta concurrencia, reduciendo riesgos de saturación y mejorando la capacidad de anticipación ante incidencias. Además, permiten disponer de una plataforma más resiliente, monitorizada y preparada para absorber el crecimiento continuo de usuarios y servicios digitales.


Requisito: II.1.2.3. Mantenimiento y actualización del sistema de monitorización y estadísticas Requerimiento EducaMadrid EducaMadrid cuenta con multitud de servicios, que necesitan conocer su nivel de uso tanto por el rendimiento como por las mismas estadísticas de uso (MON3). Para ello se solicita:
- Incorporar de forma continua al sistema de monitorización y estadísticas de todos los
servidores y servicios incluidos los de nueva creación o migrados.

- Usar herramientas de código abierto para dicho objetivo.

- Realizar una actualización de la herramienta actual a su última versión.

- Asegurar el correcto funcionamiento de la monitorización adecuando las alertas reactivas
a las necesidades de EducaMadrid y adaptando las alertas proactivas a las nuevas necesidades de los servicios. Estas tareas se realizarán de forma continuada y sincronizada con las modificaciones de servicios. Propuesta técnica de empresa_s Los especialistas de empresa_s plantean una estrategia de monitorización integral, continua y plenamente integrada en el ciclo de vida de los servicios de EducaMadrid, garantizando visibilidad completa, capacidad de anticipación y adaptación a la evolución constante de la plataforma.
1. Integración continua de servicios en el sistema de monitorización
Se establecerá un modelo de incorporación automática y sincronizada de todos los activos tecnológicos:
- Inclusión sistemática de servidores, servicios y aplicaciones (existentes, migrados o de
nueva creación) en el sistema de monitorización.

- Integración específica de servicios críticos del ecosistema como Moodle, NextCloud o
sistemas de autenticación basados en Keycloak.


![Imagen de la página 49](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0049-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0049-imagen-003.png -->
- Flujo completo de pruebas de carga y optimización de los entornos EducaMadrid.
- JMeter genera carga y estrés, mientras Grafana, Prometheus, Zabbix y Metabase proporcionan observabilidad sobre preproducción, producción controlada, otros entornos y servicios críticos.
- El ciclo pasa por monitorización, análisis, optimización y validación, con retorno para repetir las pruebas.
- Los resultados buscados son rendimiento, disponibilidad, escalabilidad, experiencia de usuario y detección temprana de problemas.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0049-imagen-003.png -->

- Sincronización con los entornos (desarrollo, preproducción y producción) asegurando
coherencia en todos ellos.
2. Uso de herramientas Open Source y arquitectura escalable
empresa_s empleará un stack de monitorización basado en tecnologías abiertas y ampliamente consolidadas:
- Recolección de métricas mediante Prometheus y exporters específicos.

- Visualización avanzada mediante Grafana.

- Monitorización híbrida (infraestructura + servicios) con Zabbix, MetaBase o soluciones
equivalentes.

- Separación de capas:
o captura de métricas, o almacenamiento, o visualización, o gestión de alertas. Esto permite escalabilidad horizontal y adaptación al crecimiento previsto del entorno (más de 700 servidores y crecimiento anual). Propuesta de mejora y evolución del servicio
1. Actualización del sistema de monitorización
- Migración controlada a la última versión estable (LTS) de las herramientas existentes.

- Validación previa en entornos de preproducción.

- Garantía de compatibilidad con plugins, APIs y sistemas actuales.

- Eliminación de componentes obsoletos o no soportados.
2. Optimización de alertas reactivas
- Revisión completa de umbrales en función de:
o carga real del sistema, o comportamiento histórico.
- Clasificación por niveles (informativo, aviso, crítico).

- Integración con sistemas de notificación y gestión de incidencias.

- Reducción de falsos positivos mediante ajuste fino de métricas.

3. Operación continua y sincronización con cambios
- Integración del sistema de monitorización dentro del ciclo de despliegue (DevOps).

- Actualización automática ante cambios en la infraestructura.

- Revisión periódica del sistema de métricas y dashboards.

empresa_s propone evolucionar el sistema actual hacia un modelo avanzado de observabilidad:
- Centralización de logs para correlación con métricas.
- Dashboards específicos por servicio educativo, facilitando la toma de decisiones.


- Modelo de capacity planning, anticipando necesidades de infraestructura.
Valor aportado Estas mejoras permiten no solo monitorizar, sino anticipar, analizar y optimizar el comportamiento global de la plataforma. Requisito: II.1.2.4. Mantenimiento y evolución del sistema de monitorización y estadísticas de servicios basados en IA Requerimiento EducaMadrid EducaMadrid dispone de servicios basados en modelos de lenguaje de gran tamaño (LLM) desplegados sobre infraestructura propia y OpenSource, cuyo uso debe ser monitorizado tanto desde el punto de vista del rendimiento como desde la perspectiva de estadísticas de consumo y calidad del servicio (MON4). Para ello se solicita:
- Incorporar de forma continua al sistema de monitorización y estadísticas todos los servicios
basados en LLM, incluyendo nuevos modelos, endpoints de inferencia.

- Utilizar las herramientas necesarias de código abierto para dicho objetivo.

- Asegurar el correcto funcionamiento del sistema de monitorización, adecuando las alertas
reactivas a incidencias en los servicios LLM y definiendo alertas proactivas orientadas a nuevas necesidades. Estas tareas se realizarán de forma continuada y coordinada con las modificaciones, ampliaciones o migraciones de los servicios basados en modelos de lenguaje. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la monitorización de los servicios de Inteligencia Artificial de EducaMadrid mediante un modelo avanzado de observabilidad orientado a garantizar el rendimiento, disponibilidad y escalabilidad de los entornos LLM desplegados sobre infraestructura propia. La solución permitirá integrar de forma continua los servicios basados en vLLM y LiteLLM dentro del ecosistema corporativo de monitorización, centralizando la supervisión de modelos, endpoints y consumo de recursos asociados a aulas virtuales, correo web, cloud y aplicaciones internas. Se implantará una arquitectura basada en tecnologías Open Source:
- Prometheus para recolección de métricas.
- Grafana para dashboards técnicos y ejecutivos.
- Metabase para explotación estadística y análisis de uso.
- Integración de métricas avanzadas de GPU, inferencia y consumo de tokens.
La plataforma permitirá supervisar de forma centralizada:
- tiempos de inferencia y latencias,
- throughput y tokens procesados,
- uso de GPU, CPU y memoria,
- peticiones concurrentes,
- errores, timeouts y degradaciones,
- consumo por servicio o aplicación,


Asimismo, empresa_s implantará un sistema de alertado proactivo y reactivo capaz de detectar degradaciones de servicio, saturación de recursos, anomalías de consumo o necesidades de escalado automático. El servicio incluirá mantenimiento evolutivo continuo, adaptación de métricas y validación tras nuevas versiones de modelos o ampliaciones de infraestructura IA. Propuesta de mejora y evolución del servicio empresa_s propone evolucionar la plataforma hacia un modelo avanzado de operación LLMOps mediante:
1. Dashboards específicos para IA orientados tanto a operación técnica como a análisis
funcional.
2. Integración de métricas avanzadas de calidad de servicio y experiencia de usuario.
3. Sistemas de autoscaling basados en métricas de Prometheus y carga GPU.
4. Observabilidad completa mediante correlación de métricas, logs y trazabilidad.
5. Análisis predictivo de consumo y capacidad mediante históricos de uso.
6. Optimización continua del rendimiento de inferencia sobre vLLM y LiteLLM.
7. Integración de monitorización IA dentro de pipelines DevOps y LLMOps.

Valor aportado Estas mejoras permiten garantizar una operación estable, eficiente y escalable de los servicios de Inteligencia Artificial de EducaMadrid, mejorando la capacidad de supervisión, detección temprana de incidencias y optimización continua del rendimiento. Además, permiten evolucionar hacia un modelo moderno de observabilidad LLMOps, preparado para soportar el crecimiento futuro de nuevos servicios IA dentro del ecosistema educativo.
##### APARTADO: ACTUALIZACIÓN DE SERVICIOS EXISTENTES (UPD)
Requisito: II.1.3.1. Mantenimiento y mejora de los sistemas de videoconferencias Requerimiento EducaMadrid EducaMadrid cuenta con una solución De Software Libre para videoconferencias: Jitsi . Se necesitan tener esta herramienta actualizada en los tres sistemas, con una periodicidad mínima trimestral manteniendo la compatibilidad con las últimas versiones de los navegadores principales (UPD1).


![Imagen de la página 52](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0052-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0052-imagen-003.png -->
- Captura de un panel de Grafana para supervisar solicitudes de un servicio.
- Muestra 3.852 solicitudes totales, 3.831 correctas, 21 erróneas y una tasa de error del 0,545 por ciento.
- Para el rango seleccionado aparecen 164 solicitudes correctas y ningún error, además de contadores de tokens de entrada y salida.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0052-imagen-003.png -->

Se solicita:
- Mantener una versión actualizada abordando sus correspondientes migraciones.

- Realizar las adaptaciones necesarias de cada nueva versión para asegurar un rendimiento
óptimo.

- Realizar mantenimiento correctivo de cada nueva versión instalada.

Estas tareas se realizarán periódicamente cuatro veces al año. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la evolución de la plataforma de videoconferencia como un proceso continuo de actualización, optimización y adaptación tecnológica, garantizando la estabilidad del servicio y su compatibilidad con los entornos de usuario. Se establecerá un proceso estructurado de cuatro ciclos anuales de actualización, alineado con lo requerido en el pliego:
- Migración controlada a las versiones estables más recientes de los componentes
principales: o Jitsi Meet o Jicofo o Jitsi Videobridge (JVB)
- Adaptación del ecosistema asociado:
o Prosody (señalización XMPP) o Nginx (proxy inverso) o Coturn (TURN/STUN)
- Validación previa en entorno de preproducción antes de paso a producción.
- Procedimientos de rollback automatizado ante incidencias.
Tras cada actualización, se realizarán ajustes específicos orientados al rendimiento:
- Configuración de codecs y bitrate adaptativo en función del ancho de banda disponible.
- Ajuste de parámetros WebRTC:
o control de jitter o estimación de ancho de banda o gestión de pérdida de paquetes
- Optimización del comportamiento de salas:
o número máximo de participantes o gestión de vídeo activo (LastN, simulcast)
- Revisión del uso de servidores TURN para garantizar conectividad en entornos restrictivos
(centros educativos).
- Validación continua con navegadores principales:
o Google Chrome o Mozilla Firefox o Microsoft Edge o Safari
- Pruebas en versiones estables y actualizadas de cada navegador.
- Verificación en dispositivos móviles y redes con limitaciones (entornos escolares).
Se garantizará el correcto funcionamiento de los distintos entornos desplegados, asegurando la continuidad del servicio y la resolución de incidencias derivadas de actualizaciones.
- Resolución de incidencias derivadas de nuevas versiones o cambios en navegadores.


- Ajustes en caliente de configuración para evitar degradaciones del servicio.

- Monitorización continua del estado de las sesiones y del backend de videobridge.

- Coordinación con plataformas integradas como Moodle para garantizar compatibilidad en
entornos educativos. Adaptación específica a los tres entornos definidos:
- Entorno privado (usuarios autenticados mediante SSO).

- Entorno semiprivado (control por anfitriones).

- Integración con Moodle (uso embebido en aula virtual).

Cada entorno contará con validaciones independientes para asegurar su correcto funcionamiento. Propuesta de mejora y evolución del servicio empresa_s propone evolucionar la plataforma hacia un modelo más robusto y escalable:
1. Entorno de preproducción: Validación previa de actualizaciones en entornos controlados.
2. Monitorización avanzada: Métricas en tiempo real de calidad de sesión.
3. Optimización del escalado: Mejora del reparto de carga entre nodos.
4. Funcionalidades avanzadas: Integración de grabación, accesibilidad y mejora en
dispositivos móviles. Valor aportado Estas actuaciones permiten garantizar la estabilidad del servicio, mejorar la calidad de las comunicaciones y adaptar la plataforma al crecimiento del uso. Requisito: II.1.3.2. Mantenimiento y mejora del sistema secundario de videoconferencia con opción de grabación Requerimiento EducaMadrid EducaMadrid cuenta con un servicio secundario de videoconferencias basado en la solución de Software Libre BigBlueButton para videoconferencias con opción de grabación (UPD2). Se solicita:
- Adaptar, mantener y actualizar el entorno a la versión más actualizada con su
correspondiente migración.

- Realizar las adaptaciones necesarias de cada nueva versión para asegurar la funcionalidad
de grabación y un rendimiento óptimo de la aplicación.

- Realizar mantenimiento correctivo de cada nueva versión instalada.
Estas tareas se realizarán periódicamente cuatro veces al año. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el mantenimiento y evolución de la plataforma de videoconferencia BigBlueButton mediante un modelo orientado a garantizar disponibilidad, estabilidad, rendimiento y calidad de grabación en los entornos educativos de EducaMadrid. Se realizará un análisis técnico de la infraestructura actual, homogeneizando configuraciones, versiones y personalizaciones existentes entre los distintos servidores de videoconferencia.


empresa_s gestionará el ciclo completo de actualización de la plataforma:
- Migración a versiones estables y soportadas de BigBlueButton.

- Adaptación de configuraciones y personalizaciones corporativas.

- Validación funcional tras cada actualización.

- Mantenimiento correctivo y preventivo continuo.
La solución incluirá:
- Optimización del sistema de grabación y almacenamiento centralizado.

- Integración mediante almacenamiento compartido NFS.

- Supervisión de sesiones concurrentes y consumo de recursos.

- Monitorización continua del servicio y capacidad.

Asimismo, se realizarán pruebas periódicas de carga y estrés para validar:
- Concurrencia de usuarios.

- Estabilidad de sesiones.

- Rendimiento de grabaciones.

- Comportamiento de la plataforma ante escenarios de alta demanda.

Todas las actuaciones críticas se ejecutarán en periodos no lectivos o ventanas controladas para minimizar el impacto sobre los usuarios. Propuesta de mejora y evolución del servicio empresa_s propone evolucionar la plataforma de videoconferencia hacia un modelo más robusto, escalable y resiliente mediante:
1. Implantación de entornos diferenciados de desarrollo y preproducción.
2. Homogeneización completa de versiones y configuraciones de BigBlueButton.
3. Centralización de grabaciones sobre almacenamiento compartido NFS.
4. Integración avanzada con Aulas Virtuales y servicios educativos.
5. Automatización de monitorización y estadísticas de uso.
6. Ejecución periódica de pruebas de carga y estrés.
7. Evolución progresiva hacia arquitecturas más escalables y balanceadas.
Valor aportado Estas mejoras permiten garantizar la continuidad y estabilidad del servicio de videoconferencia de EducaMadrid, mejorando la experiencia de usuario, la calidad de las grabaciones y la capacidad de crecimiento ante incrementos de demanda. Además, permiten disponer de una plataforma más homogénea, monitorizada y preparada para la evolución continua de los entornos educativos digitales.


Requisito: II.1.3.3. Mantenimiento y mejora de la herramienta Mattermost Requerimiento EducaMadrid EducaMadrid tiene integrada como plataforma interna de comunicación y colaboración la herramienta Mattermost. Se necesita tener esta herramienta actualizada y funcionando en condiciones óptimas (UPD3). Se solicita:
- Mantener una versión actualizada con su correspondiente migración.

- Realizar las adaptaciones necesarias de cada nueva versión para asegurar un rendimiento
óptimo.

- Realizar mantenimiento correctivo de cada nueva versión instalada.
Esta tarea se realizará periódicamente. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el mantenimiento de la plataforma de colaboración como un proceso continuo orientado a garantizar su disponibilidad, rendimiento y adaptación al ecosistema tecnológico de EducaMadrid. Se realizará la actualización periódica de la herramienta, incluyendo procesos de migración controlada, validación previa y despliegue en producción con verificación completa. Se establecerá un modelo de actualización continua basado en versiones estables:
- Migración periódica a versiones soportadas de Mattermost (canal estable/LTS).

- Gestión coordinada de dependencias:
o Base de datos (PostgreSQL) o Backend de almacenamiento o Integraciones externas
- Validación previa en entorno de preproducción.

- Procedimientos de rollback automatizado.
Cada nueva versión será adaptada específicamente al entorno:


![Imagen de la página 56](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0056-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0056-imagen-003.png -->
- Arquitectura de BigBlueButton en alta disponibilidad integrada con aulas virtuales Moodle.
- El plugin permite crear o unir sesiones distribuidas entre tres servidores con conferencia web, audio, vídeo, pantalla y chat.
- Las grabaciones se guardan en almacenamiento NFS compartido, centralizado, cifrado y escalable, y pueden consultarse desde Moodle.
- Grafana, Prometheus y alertas supervisan tanto el clúster como el almacenamiento.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0056-imagen-003.png -->

- Ajuste de parámetros de rendimiento:

o concurrencia de usuarios o tamaño de mensajes y adjuntos o indexación de búsquedas
- Optimización de integraciones:

o autenticación mediante Keycloak (SSO) o integración con servicios internos (notificaciones, workflows)
- Validación de compatibilidad con navegadores y clientes móviles.

Mantenimiento correctivo:
- Resolución de incidencias derivadas de:

o cambios de versión o incompatibilidades de plugins o integraciones
- Corrección de errores funcionales detectados en producción.

- Ajustes en caliente para evitar degradación del servicio.

Operación y continuidad del servicio:
- Planificación de ventanas de mantenimiento fuera de horario crítico.

- Monitorización continua del estado del sistema:
o tiempos de respuesta o carga de backend o número de sesiones activas
- Coordinación con otros servicios de EducaMadrid para garantizar coherencia operativa.

Se garantizará:
- Compatibilidad con navegadores y sistemas actuales
- Integración con sistemas de autenticación
- Estabilidad en entornos de uso intensivo
Se llevará a cabo mantenimiento correctivo para resolver incidencias derivadas de nuevas versiones o cambios en el entorno. Propuesta de mejora y evolución del servicio empresa_s propone reforzar la plataforma mediante:
1. Entorno de preproducción replicado, con validación funcional y de carga.
2. Monitorización avanzada integrada, alineada con el sistema global
(Prometheus/Grafana).
3. Optimización de almacenamiento de archivos compartidos, integrando con servicios
como NextCloud.
4. Políticas de retención y archivado de mensajes, mejorando rendimiento y cumplimiento.
Valor aportado Estas mejoras permiten garantizar la continuidad del servicio, mejorar el rendimiento y reducir el impacto de incidencias. Requisito: II.1.3.4. Mantenimiento de la solución Kanban


Requerimiento EducaMadrid EducaMadrid dispone de una solución de gestión de tareas/proyectos con integración de Kanban. Se necesita tener esta herramienta actualizada y funcionando en condiciones óptimas (UPD4). Se solicita:
- Mantener una versión actualizada con su correspondiente migración.

- Realizar mantenimiento correctivo de cada nueva versión instalada.

Esta tarea se realizará periódicamente. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el mantenimiento de la solución Kanban (basada en Wekan) como un componente operativo dentro del ecosistema de gestión interna de EducaMadrid, garantizando su evolución controlada, estabilidad y alineación con los flujos de trabajo existentes. Se definirá un proceso periódico de actualización basado en versiones estables:
- Evaluación previa de nuevas versiones de Wekan.

- Ejecución de migraciones controladas:

o datos (tableros, tarjetas, usuarios) o configuraciones o reglas de acceso
- Validación en entorno de preproducción antes de despliegue.

- Procedimientos de reversión en caso de incidencia.

Tras cada actualización, se realizarán ajustes orientados a garantizar la continuidad del servicio:
- Validación de flujos Kanban:

o creación y movimiento de tareas o automatizaciones internas
- Optimización del rendimiento en función de:
o número de usuarios concurrentes o volumen de proyectos activos
- Revisión de compatibilidad con navegadores y entorno de ejecución.
Mantenimiento correctivo continuo.
- Análisis de logs de aplicación y backend.

- Resolución de incidencias derivadas de cambios de versión.

- Ajuste de dependencias (Node.js, MongoDB u otras).

- Corrección de errores funcionales detectados en uso real.
Se realizarán actualizaciones periódicas de la herramienta, incluyendo:
- Migración a versiones estables.


- Validación de funcionalidad.

- Adaptación a nuevas dependencias.
empresa_s tratará la solución Kanban como una pieza conectada al entorno global:
- Integración con sistemas de autenticación centralizada mediante Keycloak.

- Coordinación con herramientas colaborativas como Mattermost para notificaciones y
seguimiento de tareas.

- Posibilidad de integración con sistemas de monitorización para trazabilidad del uso.

Propuesta de mejora, optimización y mejora operativa empresa_s propone evolucionar la solución Kanban hacia un modelo más integrado y eficiente:
- Despliegue contenerizado, facilitando actualizaciones sin impacto.

- Entorno de preproducción dedicado, para validación funcional antes de cambios.

- Integración de notificaciones automáticas con sistemas de mensajería interna.

- Definición de plantillas de flujo Kanban, adaptadas a procesos habituales de
EducaMadrid.

- Análisis de uso y optimización de tableros, evitando sobrecarga y mejorando la
productividad.


![Imagen de la página 59](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0059-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0059-imagen-003.png -->
- Captura de un tablero kanban en Wekan para gestionar funcionalidades de una aplicación de viajes.
- Las columnas recorren backlog, selección, especificación, desarrollo, pruebas y despliegue.
- Las tarjetas incluyen funciones como mensajería, SSO, filtros, vuelos, alquiler de coches, hoteles y pagos.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0059-imagen-003.png -->

Valor aportado Estas actuaciones permiten mantener una herramienta estable, actualizada como un sistema real de gestión operativa, no solo como un repositorio de tareas y adaptada al uso real de los usuarios. Requisito: II.1.3.5. Mantenimiento, actualización y evolución de la solución GitLab Requerimiento EducaMadrid Actualmente, EducaMadrid utiliza GitLab como herramienta de control de versiones de código abierto para la gestión de proyectos y colaboración en el desarrollo de software. Se necesita tener esta herramienta actualizada y funcionando en condiciones óptimas (UPD5). Se solicita:
- Mantener GitLab actualizado a la última versión estable, incluyendo migraciones
necesarias entre versiones.

- Realizar mantenimiento correctivo y preventivo de la herramienta, incluyendo parches de
seguridad y ajustes de configuración

Esta tarea se realizará periódicamente, al menos dos veces al año. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la gestión de la plataforma GitLab de EducaMadrid mediante un modelo orientado a garantizar la disponibilidad, seguridad y evolución continua del ecosistema DevOps corporativo. Se realizará el mantenimiento integral de la plataforma GitLab, incluyendo actualizaciones periódicas sobre versiones estables, validación previa en entornos controlados y despliegues planificados minimizando el impacto sobre los equipos de desarrollo y sistemas. La solución incluirá:
- Administración y optimización de la plataforma GitLab Omnibus.

- Gestión de repositorios, grupos, permisos y políticas de acceso.

- Integración con LDAP corporativo para autenticación centralizada y sincronización de
usuarios.

- Soporte a flujos de trabajo DevOps y metodologías CI/CD.

- Gestión de GitLab Runners dedicados para automatización de despliegues y tareas de
integración continua.


![Imagen de la página 60](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0060-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0060-imagen-003.png -->
- Esquema del funcionamiento de un sistema kanban con límites de trabajo en curso.
- Las ideas del cliente entran en una cola priorizada y son arrastradas por análisis, diseño, desarrollo, pruebas, aceptación y despliegue.
- Las tarjetas verdes, naranjas y amarillas representan solicitudes de cambio, defectos y mantenimiento hasta llegar a terminado y archivo.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0060-imagen-003.png -->

- Aplicación de parches de seguridad y mantenimiento preventivo.

- Automatización de backups y validación periódica de restauración.

- Monitorización continua del rendimiento, uso de recursos y crecimiento del
almacenamiento. Asimismo, empresa_s garantizará la trazabilidad de cambios, la continuidad operativa y la correcta integración de GitLab con el resto de los servicios tecnológicos de EducaMadrid. Propuesta de mejora y evolución del servicio empresa_s propone evolucionar la plataforma GitLab hacia un modelo DevOps más automatizado, escalable y seguro mediante:
1. Implantación de entornos de preproducción para validación de actualizaciones y pipelines.
2. Integración avanzada de pipelines CI/CD para automatización de despliegues y
validaciones.
3. Implementación de GitLab Runners escalables y segmentados por tipología de servicio.
4. Refuerzo de la seguridad mediante auditoría, protección de ramas y control avanzado de
accesos.
5. Integración con sistemas de monitorización corporativos (Grafana, Prometheus y logs
centralizados).
6. Generación de métricas de actividad, uso y rendimiento para capacity planning y
optimización continua. Valor aportado Estas mejoras permiten garantizar la continuidad del servicio, reforzar la seguridad de los desarrollos y optimizar la operación de los equipos técnicos de EducaMadrid. Además, permiten consolidar una plataforma DevOps centralizada, automatizada y preparada para la evolución continua de los servicios y aplicaciones corporativas. Requisito: II.1.3.6. Mantenimiento y mejora de la solución LimeSurvey Requerimiento EducaMadrid EducaMadrid dispone de una solución de formularios mediante la herramienta de Software Libre LimeSurvey. Se necesita mantener esta herramienta actualizada, con rendimiento adecuado y con usabilidad adecuada (UPD6). Se solicita:
- Mantener una versión actualizada con su correspondiente migración si fuera necesaria.

- Mejorar el diseño de las nuevas arquitecturas para el correcto rendimiento de la aplicación.

- Realizar las adaptaciones necesarias de aspecto y usabilidad en la nueva versión
actualizada.

- Asegurar el rendimiento haciendo los ajustes necesarios para que la experiencia de usuario
sea la esperada por EducaMadrid.

Esta tarea se realizará periódicamente. Propuesta técnica de empresa_s


Los especialistas de empresa_s abordarán el mantenimiento de la plataforma LimeSurvey de EducaMadrid mediante un modelo orientado a garantizar la disponibilidad, escalabilidad y fiabilidad del servicio, especialmente en escenarios de recogida masiva de información y alta concurrencia. Se realizará la actualización periódica de la plataforma sobre versiones estables y soportadas, incluyendo validaciones previas en entornos de preproducción, pruebas funcionales y procedimientos controlados de migración y rollback. La solución incluirá:
- Optimización de la arquitectura web y base de datos para soportar campañas masivas.

- Ajuste de rendimiento sobre PHP, MariaDB/MySQL y servidor web.

- Revisión y optimización de formularios, consultas e índices.

- Integración con sistemas corporativos de autenticación y monitorización.

- Personalización visual alineada con la imagen corporativa de EducaMadrid.

- Adaptación responsive y mejora de la experiencia de usuario.

- Automatización de backups y validación periódica de restauración.

- Resolución de incidencias y mantenimiento preventivo y correctivo.

Asimismo, empresa_s implantará mecanismos de monitorización continua sobre tiempos de respuesta, concurrencia y estado de la plataforma, permitiendo anticipar degradaciones del servicio y optimizar el comportamiento de las encuestas críticas. Propuesta de mejora y evolución del servicio empresa_s propone evolucionar LimeSurvey hacia una plataforma más eficiente, resiliente y orientada a la explotación de datos mediante:
1. Segmentación de servicios frontend/backend para mejorar escalabilidad y rendimiento.
2. Integración con sistemas de analítica y reporting corporativo.
3. Optimización avanzada de bases de datos y mantenimiento automatizado.
4. Monitorización específica de formularios críticos y campañas masivas.
5. Implantación de entornos de preproducción para validación de cambios y nuevas
versiones.
6. Mejora continua de usabilidad y accesibilidad en formularios y encuestas.
Valor aportado Estas mejoras permiten garantizar la continuidad del servicio, mejorar la experiencia de usuario y asegurar la estabilidad de la plataforma en escenarios de alta demanda. Además, permiten evolucionar LimeSurvey hacia una solución más robusta, escalable y preparada para integrarse de forma eficiente en el ecosistema tecnológico de EducaMadrid.


Requisito: II.1.3.7. Mantenimiento y mejora de sonarqube Requerimiento EducaMadrid Actualmente EducaMadrid utiliza la herramienta de Software Libre SonarQube para la gestión de la calidad del código (UPD7). Se solicita:
- Actualizar la herramienta a la última versión estable.

- Realizar todas las tareas necesarias de gestión de usuarios y proyectos, así como las
modificaciones necesarias en los proyectos existentes para su integración en SonarQube.

- Implementar las reglas y perfiles de calidad marcados por la Consejería .
Estas tareas se realizarán periódicamente dos veces al año. Propuesta, enfoque técnico de empresa_s Los especialistas de empresa_s abordarán el mantenimiento de SonarQube como un elemento clave dentro del ciclo de vida del software de EducaMadrid, orientado a garantizar la calidad, seguridad y mantenibilidad del código en todos los servicios de la plataforma. Se establecerá un proceso de actualización semestral alineado con versiones estables:
- Evaluación previa de compatibilidad:
o versión de Java o base de datos (PostgreSQL u otras) o plugins instalados
- Despliegue en entorno de preproducción:
o validación de análisis existentes o comprobación de reglas activas
- Migración controlada a producción con:
o backup completo o validación de integridad histórica
- Procedimientos de rollback definidos.


![Imagen de la página 63](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0063-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0063-imagen-003.png -->
- Mapa funcional de la plataforma LimeSurvey dividido en toma de encuestas, administración e integraciones.
- El frontal cubre cuestionarios, estadísticas, autenticación, impresión, sesiones, respuestas, importación y exportación.
- El backoffice incorpora edición de encuestas, usuarios, permisos, tokens, plantillas, base de datos y utilidades.
- Las integraciones incluyen LDAP, SSO, API, servicios web, exportación, copias, monitorización, rendimiento y seguridad.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0063-imagen-003.png -->

Gestión avanzada de usuarios y proyectos:
- Organización de accesos mediante:
o roles y permisos (RBAC) o grupos de usuarios por equipo/proyecto
- Gestión centralizada de proyectos:
o trazabilidad de análisis o control de versiones analizadas
- Integración con sistemas de autenticación como Keycloak.
empresa_s garantizará la integración real con el ciclo DevOps:
- Configuración de análisis automático en pipelines:
o GitLab CI o Jenkins o otros sistemas equivalentes
- Uso de configuraciones estandarizadas (sonar-project.properties, API REST).
- Análisis continuo en cada commit/push.
Implementación de reglas y perfiles de calidad
- Configuración de perfiles específicos por lenguaje:
o Java, PHP, JavaScript, Python, etc.
- Aplicación de criterios definidos por la Consejería :
o cobertura mínima o deuda técnica o vulnerabilidades
- Ajuste de severidad y priorización de incidencias críticas.
Supervisión y mantenimiento correctivo:
- Monitorización de resultados de análisis:
o bugs críticos o vulnerabilidades de seguridad
- Resolución de incidencias derivadas de:
o cambios de versión o incompatibilidades de plugins
- Revisión periódica de rendimiento del sistema.
Flujo de integración del ciclo de desarrollo

Propuesta de mejora y evolución del servicio


![Imagen de la página 64](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0064-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0064-imagen-003.png -->
- Flujo de integración continua entre Git, Jenkins, Maven, JaCoCo y SonarQube.
- Un envío de código activa la construcción y las pruebas; JaCoCo genera cobertura y SonarQube analiza código y métricas.
- Jenkins espera el resultado de la puerta de calidad: si se supera permite el despliegue y si falla detiene el proceso.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0064-imagen-003.png -->

empresa_s propone evolucionar SonarQube hacia un modelo de calidad continua:
- Automatización del alta de proyectos, mediante plantillas y scripts.

- Definición de Quality Gates estrictos, bloqueando despliegues con errores críticos.

- Análisis de tendencias de calidad, detectando degradaciones progresivas.

- Formación a equipos técnicos, mejorando interpretación de métricas.

- Integración con herramientas colaborativas, como Mattermost para notificación de
incidencias. Valor aportado Estas mejoras permiten convertir SonarQube en una herramienta activa de mejora continua del software, no solo en un sistema de control. Requisito: II.1.3.8. Mantenimiento, actualización y evolución de la herramienta Redmine Requerimiento EducaMadrid El equipo de EducaMadrid usa Redmine como herramienta de Software Libre para la gestión de las incidencias y para las solicitudes y seguimiento de las tareas de los técnicos. También se usa esta herramienta para gestionar las incidencias comunicadas por usuarios y centros educativos a través del CAU (UPD8). Se pide como parte del mantenimiento de Redmine:
- Actualizar la versión de Redmine a la versión estable más reciente, y mantenerlo
actualizado según se vayan publicando nuevas versiones.

- Implementación de los scripts necesarios para realizar automatización de carga y
actualización de tareas mediante plugins o scripting (vía REST API).

- Implementación mediante plugins o scripts de un sistema de autentificación 2FA.
Estas tareas se realizarán periódicamente. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la gestión de Redmine como una plataforma centralizada de seguimiento de incidencias, tareas y coordinación técnica, orientada a garantizar estabilidad, automatización y trazabilidad dentro del ecosistema de EducaMadrid . Se realizará el mantenimiento integral de la plataforma, incluyendo actualizaciones periódicas sobre versiones estables, validación de plugins y migraciones controladas minimizando el impacto sobre los usuarios. La solución incluirá:
- Administración y optimización del entorno Redmine.

- Gestión de proyectos, roles, permisos y flujos de trabajo.

- Integración con LDAP corporativo y sistemas de autenticación reforzada (2FA).

- Automatización de incidencias mediante API REST y scripting.

- Integración con sistemas CAU, correo corporativo y herramientas DevOps.


- Mantenimiento de plugins corporativos, tableros Kanban y documentación técnica.

- Automatización de backups y validación de restauración.

- Monitorización continua del rendimiento y uso de la plataforma.
Asimismo, empresa_s garantizará la trazabilidad completa de incidencias y cambios, mejorando la coordinación entre los equipos de sistemas, desarrollo y soporte técnico. Propuesta de mejora y evolución del servicio empresa_s propone evolucionar Redmine hacia una plataforma más automatizada, colaborativa y alineada con prácticas DevOps mediante:
1. Implantación de entornos de preproducción para validación de cambios y plugins.
2. Automatización avanzada de tickets desde CAU, correo y sistemas externos mediante API
###### REST.
3. Integración con GitLab para trazabilidad entre incidencias, commits y despliegues.
4. Implantación de métricas de actividad, tiempos de resolución y carga de trabajo.
5. Refuerzo de seguridad mediante 2FA, auditoría de accesos y segmentación de permisos.
6. Optimización de base de datos y rendimiento para escenarios de alta concurrencia.
7. Evolución de tableros Kanban y documentación técnica integrada mediante Markdown y
diagramación avanzada.

Valor aportado Estas mejoras permiten garantizar la continuidad del servicio, optimizar la gestión de incidencias y mejorar la coordinación entre los distintos equipos técnicos de EducaMadrid. Además, permiten evolucionar Redmine hacia una plataforma más segura, automatizada y preparada para integrarse de forma eficiente dentro del ecosistema DevOps corporativo. Requisito: II.1.3.9. Mantenimiento, configuración y evolución del sistema Wowza Streaming Engine Requerimiento EducaMadrid EducaMadrid usa la herramienta Wowza Streaming Engine para retransmisiones en vivo (UPD9). Página 66 de 239


![Imagen de la página 66](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0066-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0066-imagen-003.png -->
- Arquitectura de Redmine en producción para centralizar incidencias procedentes de CAU, correo, sistemas externos y API.
- Incluye proyectos, incidencias, tareas, calendarios, documentos, wiki, flujos automatizados, reglas, alertas, plugins e integración con LDAP, 2FA, correo y SSO.
- Un entorno de preproducción valida actualizaciones, plugins, flujos y rendimiento antes de desplegar.
- GitLab, webhooks, API y lanzamientos completan las integraciones DevOps, apoyadas por base de datos optimizada y monitorización.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0066-imagen-003.png -->

Se solicita:
- Mantener actualizados los servidores y servicios involucrados en la arquitectura de Wowza
Streaming Engine.

- Configurar el entorno para su funcionamiento óptimo.

- Parametrizar los diferentes codificadores RTMP o RTSP/RTP y la salida HLS si fuera
necesario, así como cualquier elemento necesario para su adecuación con el resto de los entornos de la plataforma.

Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la gestión de la plataforma Wowza Streaming Engine mediante un modelo orientado a garantizar retransmisiones seguras, estables y escalables para los servicios audiovisuales de EducaMadrid. Se realizará el mantenimiento integral de la plataforma, incluyendo actualización de versiones, optimización del motor de streaming y modernización de la infraestructura sobre sistemas operativos soportados y securizados. La solución incluirá:
- Actualización controlada de Wowza Streaming Engine y del sistema operativo.

- Optimización de parámetros JVM, buffers y conexiones concurrentes.

- Configuración de flujos RTMP, RTSP/RTP y HLS.

- Integración y validación de codificadores externos.

- Implementación de certificados SSL y mecanismos de protección de streaming.

- Automatización de backups y validación de recuperación.

- Monitorización continua de rendimiento, ancho de banda y concurrencia.

- Resolución de incidencias y mantenimiento preventivo y correctivo.
Asimismo, empresa_s garantizará la validación funcional de los entornos antes de cada migración o actualización, minimizando el impacto sobre las retransmisiones activas y los usuarios finales. Propuesta de mejora y evolución del servicio empresa_s propone evolucionar la plataforma Wowza hacia un modelo más robusto, seguro y preparado para escenarios de alta concurrencia mediante:
1. Implantación de entornos de preproducción para validación de actualizaciones y pruebas
de emisión.
2. Optimización avanzada de JVM y del motor de streaming para mejorar estabilidad y
latencia.
3. Ejecución de pruebas de carga y estrés para validar capacidad de usuarios concurrentes.
4. Refuerzo de seguridad mediante certificados corporativos y control de accesos a streams.
5. Implantación de métricas avanzadas de uso y calidad de servicio.
6. Evolución hacia arquitecturas distribuidas origen/edge y posible integración futura con
CDN.
7. Integración con sistemas corporativos de monitorización y observabilidad.


Valor aportado Estas mejoras permiten garantizar la continuidad del servicio, optimizar la calidad de las retransmisiones y mejorar la capacidad de respuesta ante eventos de alta demanda. Además, permiten evolucionar Wowza hacia una plataforma de streaming más eficiente, segura y preparada para el crecimiento continuo de los servicios audiovisuales de EducaMadrid. Requisito: II.1.3.10. Mantenimiento de la solución de bibliotecas AbiesWeb Requerimiento EducaMadrid EducaMadrid proporciona soporte a AbiesWeb, la aplicación de bibliotecas escolares (UPD10). Mientras esta aplicación se siga usando, se solicita:
- Realizar las actualizaciones y parcheado necesarios y gestiones de contenidos del sistema
de bibliotecas escolares AbiesWeb.

- Mantener y aplicar las actualizaciones evolutivas y parches que son suministradas por el
Ministerio de Educación y Formación Profesional.

- Asistir a las incidencias producidas en el aplicativo y gestionado de la carga de volúmenes
de las nuevas bibliotecas mientras sea requerido. Propuesta técnica de empresa_s para la continuidad operativa Los especialistas de empresa_s abordarán el mantenimiento de AbiesWeb como un servicio crítico orientado a la gestión distribuida de bibliotecas escolares , garantizando su estabilidad operativa, correcta evolución y coherencia con las directrices del Ministerio de Educación. Se establecerá un procedimiento controlado para la aplicación de evolutivos y parches oficiales:
- Análisis previo de cada actualización publicada por el Ministerio:
o impacto funcional o compatibilidad con el entorno EducaMadrid
- Despliegue en entorno de preproducción:
o validación de catálogo o pruebas de acceso y consultas
- Aplicación en producción con:
o backup completo previo o validación posterior del sistema
- Registro documental de cambios aplicados.
empresa_s proporcionará soporte continuo tanto a nivel técnico como funcional:
- Resolución de incidencias:
o errores de acceso o problemas en catálogo bibliográfico o degradaciones de rendimiento
- Coordinación con centros educativos para la gestión de incidencias.
- Uso de herramientas de ticketing para trazabilidad completa.
Gestión de contenidos y carga de bibliotecas:
- Alta estructurada de nuevas bibliotecas escolares.
- Carga masiva de fondos bibliográficos:
o validación de formatos o control de duplicidades


- Migración de catálogos existentes si fuera necesario.
- Control de coherencia de datos entre centros.
Gestión de datos y copias de seguridad:
- Definición de política de backups:
o copias segmentadas por centro o recuperación granular
- Auditorías periódicas de integridad de datos.
- Aplicación de medidas de seguridad:
o control de accesos o protección de información sensible Flujo operativo del sistema de bibliotecas

Propuesta de mejora y evolución del servicio empresa_s propone reforzar la solución AbiesWeb mediante un enfoque operativo y preventivo:
- Entorno de preproducción sincronizado, validando cada actualización antes de
producción.

- Monitorización específica del servicio, detectando degradaciones de rendimiento.

- Automatización de cargas masivas, reduciendo errores manuales.

- Sistema de auditoría y trazabilidad, registrando accesos y cambios.


![Imagen de la página 69](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0069-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0069-imagen-003.png -->
- Diagrama de flujo de datos de nivel uno para un sistema de biblioteca.
- Los procesos gestionan existencias, reservas y préstamos, conectados con depósitos de libros, reservas y préstamos.
- Los prestatarios solicitan, reservan, devuelven y renuevan libros, mientras el responsable de biblioteca recibe estadísticas y actualiza el inventario.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0069-imagen-003.png -->

- Generación de informes periódicos, con métricas de uso y estado del sistema.

Valor aportado Estas mejoras permiten evolucionar AbiesWeb hacia un sistema más robusto, controlado y escalable, adaptado al crecimiento del número de centros y fondos. Requisito: II.1.3.11. Mantenimiento de la solución Abies+ Requerimiento EducaMadrid EducaMadrid proporciona soporte a Abies+, la nueva aplicación de bibliotecas escolares que sustituirá en breve a AbiesWeb (UPD11). Se solicita:
- Realizar las pruebas, mejoras y actualizaciones y parcheados necesarios en la aplicación
y los servidores que la soportan.

- Realizar la gestión de contenidos del sistema de las bibliotecas escolares Abies+.

- Mantener y aplicar las actualizaciones evolutivas y parches que son suministrados por el
Ministerio de Educación y Formación Profesional.

- Asistir a las incidencias producidas en el aplicativo y en los procesos de carga de
volúmenes de las nuevas bibliotecas. Propuesta técnica de empresa_s, implantación y evolución Los especialistas de empresa_s abordarán Abies+ como un proyecto estratégico dentro de EducaMadrid, enfocado no solo al mantenimiento, sino a su implantación robusta, evolución controlada y transición desde AbiesWeb, garantizando continuidad del servicio y escalabilidad futura. empresa_s definirá una arquitectura preparada para soportar crecimiento y alta concurrencia:
- Dimensionamiento de recursos:
o CPU, memoria y almacenamiento adaptados a uso real por centros
- Configuración de entornos:
o desarrollo, preproducción y producción
- Integración con sistemas de almacenamiento existentes (SAN/NAS).
- Aplicación de políticas de hardening en sistemas operativos.
Gestión de base de datos y alta disponibilidad:
- Configuración optimizada de base de datos:
o índices, buffers, consultas críticas
- Implementación de mecanismos de alta disponibilidad:
o replicación o backups consistentes
- Integración con sistemas de identidad mediante Keycloak o LDAP.
Publicación segura del servicio:
- Configuración de acceso seguro:
o certificados SSL/TLS o control de acceso
- Balanceo de carga en caso de alta concurrencia.
- Segmentación de red y control de tráfico.


Pruebas, validación y transición desde AbiesWeb: Este es un punto clave donde empresa_s aporta valor diferencial:
- Creación de entorno de preproducción espejo.
- Ejecución de pruebas:
o funcionales o de carga (simulación de múltiples centros)
- Validación de migración de datos desde el sistema anterior.
- Planificación de transición progresiva:
o coexistencia temporal de sistemas o migración controlada por fases
- Definición de plan de rollback.
Gestión de contenidos y operación del sistema:
- Alta de nuevas bibliotecas escolares.
- Carga masiva de fondos bibliográficos:
o validación previa de datos o control de consistencia
- Resolución de incidencias funcionales y técnicas.
- Coordinación con centros educativos.
Arquitectura de despliegue y transición

Propuesta de mejora orientada a escalabilidad empresa_s propone evolucionar Abies+ hacia un sistema plenamente gobernado y escalable:
- Automatización del ciclo de actualizaciones, reduciendo tiempos de despliegue.

- Panel de control de uso y rendimiento, con métricas por centro.

- Optimización de cargas masivas, mediante validación automática de datos.


![Imagen de la página 71](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0071-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0071-imagen-003.png -->
- Arquitectura de una aplicación en una VPC distribuida entre dos zonas de disponibilidad.
- El usuario resuelve DNS y accede por una IP elástica a un balanceador que distribuye HTTP entre dos instancias ECS.
- Las aplicaciones usan una base MySQL RDS con balanceador interno, nodo maestro en una zona y esclavo en la otra.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0071-imagen-003.png -->

- Sistema de auditoría avanzada, con trazabilidad completa de operaciones.

- Definición de estrategia de transición progresiva desde AbiesWeb, minimizando
impacto en usuarios.

Valor aportado Estas mejoras permiten posicionar Abies+ como una plataforma moderna, robusta y preparada para el crecimiento del sistema educativo. Requisito: II.1.3.12. Implementación, mantenimiento y mejora de empieza Requerimiento EducaMadrid Se necesita realizar el mantenimiento, las actualizaciones y mejoras del sistema Empieza (servicio de desarrollo propio que proporciona a los profesores la capacidad de organizar y automatizar tareas) incluyendo la configuración para su escalado con alta disponibilidad tanto en la parte Frontend como Backend (UPD12). Se solicita:
- Mantener, actualizar y mejorar los servidores y aplicaciones que soportan Empieza,
asegurando su correcto funcionamiento.

- Configurar y parametrizar la herramienta para permitir escalado horizontal y vertical,
garantizando alta disponibilidad y redundancia de los servicios.

- Adaptar la arquitectura de frontend y backend para soportar la distribución de carga,
balanceo de peticiones y tolerancia a fallos.

- Supervisar las pruebas de rendimiento y optimización de los componentes para asegurar
la estabilidad del sistema ante incrementos de usuarios o cargas de trabajo. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la evolución de Empieza como una plataforma crítica dentro del ecosistema EducaMadrid, garantizando su disponibilidad, rendimiento y capacidad de crecimiento ante el incremento continuo de usuarios y servicios integrados. Se realizará el mantenimiento correctivo y preventivo del aplicativo PHP, así como la actualización continua de dependencias, librerías y sistemas operativos asociados, incorporando controles de seguridad y validación funcional tras cada cambio. empresa_s evolucionará la arquitectura actual hacia un modelo distribuido y altamente disponible mediante:
- Despliegue de frontales web redundados en configuración activo- activo.

- Balanceo de carga y eliminación de puntos únicos de fallo.

- Optimización de base de datos MySQL con replicación y tuning avanzado.

- Separación del servicio de chat en tiempo real mediante Node.js dedicado.

- Mejora de integración con Moodle, correo, calendario, videoconferencia y servicios
corporativos.

- Optimización del backend PHP, sesiones y consultas SQL.


- Monitorización continua de rendimiento, concurrencia y disponibilidad.

Asimismo, se ejecutarán pruebas de carga y estrés para validar el comportamiento del sistema en escenarios de alta concurrencia educativa. Propuesta de mejora y evolución del servicio empresa_s propone evolucionar Empieza hacia una arquitectura moderna, escalable y desacoplada mediante:
1. Transformación progresiva desde un modelo monolítico hacia servicios distribuidos.
2. Implantación de balanceadores y mecanismos de alta disponibilidad.
3. Desacoplamiento del chat en Node.js para mejorar el rendimiento en tiempo real.
4. Optimización avanzada de MySQL y políticas automatizadas de backup y recuperación.
5. Escalabilidad horizontal de frontales web según demanda.
6. Implantación de métricas avanzadas y observabilidad centralizada.
7. Evolución futura hacia arquitecturas orientadas a microservicios y APIs internas.

Valor aportado Estas mejoras permiten garantizar la continuidad del servicio, reducir tiempos de respuesta y mejorar la estabilidad global de la plataforma Empieza. Además, permiten disponer de una arquitectura más resiliente, preparada para escenarios de alta concurrencia y alineada con la evolución tecnológica de EducaMadrid .

Requisito: II.1.3.13. Mantenimiento y mejora del sistema de gestión de la configuración Requerimiento EducaMadrid Actualmente EducaMadrid dispone un sistema de gestión de la configuración IT basada en diferentes aplicaciones de Software Libre: CMDBuild, Ansible, etc. Se necesita la gestión,


![Imagen de la página 73](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0073-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0073-imagen-003.png -->
- Arquitectura de la plataforma unificada Empieza de EducaMadrid.
- Los usuarios acceden por internet y balanceo a un servicio de identidad con portal, servidores de autenticación, directorio central, SSO y alta disponibilidad.
- La aplicación dispone de dos frontales Linux activos, chat en tiempo real y una capa de datos balanceada con clúster replicado.
- Producción, preproducción y desarrollo comparten almacenamiento, y la propuesta enfatiza disponibilidad, escalabilidad, rendimiento, seguridad, modularidad y observabilidad.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0073-imagen-003.png -->

![Imagen de la página 73](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0073-imagen-004.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0073-imagen-004.png -->
- Banda de observabilidad y seguridad con cuatro capacidades.
- Incluye monitorización de rendimiento y disponibilidad, registros centralizados y trazables, alertas proactivas, copias y recuperación, y control de accesos con auditoría y permisos.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0073-imagen-004.png -->

mantenimiento, actualización y adaptación de los sistemas y aplicaciones que prestan este servicio de gestión de la configuración IT (UPD13). Para ello se solicita:
- Mantener, actualizar y mejorar tanto el servidor como las aplicaciones necesarias para la
gestión de las configuraciones IT.

- Configurar y parametrizar todo el servicio para su correcto funcionamiento.

- Automatizar el entorno para la ingesta de los datos tanto de entrada como de salida.
Correlar los datos para asegurar su coherencia y homogeneidad, así como su adecuación e interoperabilidad con el resto de los entornos. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la evolución del sistema de gestión de configuración de EducaMadrid como un elemento estratégico para el control, automatización y gobierno de la infraestructura IT. Se realizará el mantenimiento correctivo y evolutivo de la plataforma CMDB basada en herramientas Open Source como CMDBuild, Ansible y sistemas auxiliares, garantizando su disponibilidad, seguridad y adaptación continua a la evolución tecnológica de la plataforma. empresa_s implantará un modelo centralizado y automatizado para la gestión de activos y relaciones de infraestructura:
- Modelado y actualización continua de elementos de configuración (servidores, redes,
BBDD, almacenamiento, contenedores y servicios).

- Automatización de inventariado e ingesta de información mediante playbooks Ansible y
scripts de sincronización.

- Correlación automática de datos procedentes de monitorización, sistemas, DNS,
balanceadores y plataformas externas.

- Validación continua de consistencia, integridad y trazabilidad del dato.

- Integración con sistemas de monitorización, ticketing y herramientas de explotación
analítica.

Asimismo, se garantizará la actualización permanente de la CMDB como “Single Source of Truth” de la infraestructura tecnológica de EducaMadrid . Propuesta de mejora y evolución del servicio empresa_s propone evolucionar la plataforma hacia un modelo avanzado de automatización y observabilidad de configuración mediante:
1. Automatización completa de procesos de descubrimiento, actualización y sincronización
de activos.
2. Integración avanzada entre CMDB, monitorización, ticketing y automatización mediante
Ansible.
3. Implantación de pipelines de correlación y normalización de datos procedentes de múltiples
fuentes.
4. Generación automática de incidencias y alertas ante desviaciones detectadas en
infraestructura.


5. Apertura controlada de información mediante APIs y accesos de solo lectura.
6. Evolución hacia una CMDB orientada a servicios y análisis de impacto.
7. Mejora continua de calidad del dato, trazabilidad y gobierno de configuración.
Valor aportado Estas mejoras permiten disponer de una CMDB centralizada, fiable y permanentemente actualizada, mejorando el control operativo y la capacidad de análisis sobre la infraestructura de EducaMadrid. Además, facilitan la automatización de procesos, reducen errores manuales y permiten evolucionar hacia un modelo de operación más eficiente, trazable y orientado al dato.

Requisito: II.1.3.14. Mantenimiento, evolución y optimización de la plataforma de contenedores y microservicios Requerimiento EducaMadrid EducaMadrid se encuentra inmerso en un proceso de transición de algunas de sus aplicaciones y servicios a entornos contenerizados y de microservicios. Se necesita tanto la gestión, mantenimiento, actualización y mejora de las aplicaciones de infraestructura que dan soporte a estas tecnologías (Docker, Kubernetes, Podman, …), como la adaptación de las aplicaciones para funcionar en una infraestructura contenerizada. También se necesita mantener, adaptar y mejorar los sistemas de automatización de tareas que facilitan tanto los despliegues como el redimensionamiento de los servicios ofrecidos desde esta plataforma. (UPD14) Para ello se solicita:
- Gestionar, mantener, mejorar y adaptar los servidores, aplicaciones y servicios necesario
para la adecuación del entorno y su usabilidad a las características de los aplicativos y servicios de EducaMadrid.

- Configurar y parametrizar tanto los servidores como las aplicaciones y servicios para su
correcto funcionamiento.


![Imagen de la página 75](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0075-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0075-imagen-003.png -->
- Arquitectura de una CMDBuild central como fuente única de verdad para infraestructura y servicios.
- Recibe datos de infraestructura, nube, bases de datos, ficheros, informes y monitorización, y los procesa con modelo de datos, correlación, calidad, gobierno, API y cuadros de mando.
- Ansible automatiza descubrimiento, ingesta, correlación y actualización continua.
- La CMDB se integra con ticketing, monitorización, automatización, analítica y accesos externos, y genera acciones automáticas ante cambios o desviaciones.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0075-imagen-003.png -->

- Desarrollar scripts y estrategias de automatización de tareas que permitan aumentar la
productividad minimizando los riesgos y el tiempo de despliegue tanto de las aplicaciones existentes como de las futuras que se vayan incorporando al ecosistema de contenedores de EducaMadrid.

Propuesta técnica de empresa_s empresa_s propone un modelo integral de evolución y operación de la plataforma de contenedores de EducaMadrid, orientado a consolidar un ecosistema cloud- native seguro, automatizado y altamente escalable. Se realizará el mantenimiento continuo de entornos basados en Docker, Kubernetes y tecnologías asociadas, garantizando estabilidad operativa, optimización de recursos y alta disponibilidad de los servicios desplegados. La propuesta incluye:
- Administración y actualización de clústeres Kubernetes y nodos de contenedores.

- Configuración avanzada de namespaces, networking, almacenamiento persistente y
políticas de despliegue.

- Adaptación progresiva de aplicaciones a arquitecturas contenerizadas y microservicios.

- Automatización de despliegues mediante pipelines CI/CD integrados con GitLab, Jenkins
y Ansible.

- Implementación de mecanismos de autoescalado, balanceo y tolerancia a fallos.

- Integración de sistemas centralizados de monitorización, logging y observabilidad.

- Refuerzo de seguridad mediante control de accesos, gestión de secretos y análisis de
vulnerabilidades en imágenes. Asimismo, empresa_s realizará pruebas periódicas de rendimiento y validación técnica para garantizar la resiliencia y continuidad del servicio ante escenarios de alta concurrencia. Propuesta de mejora y evolución del servicio Con el objetivo de evolucionar hacia una plataforma moderna y alineada con estándares cloudnative, empresa_s propone:
1. Implantación de modelos GitOps e Infraestructura como Código (IaC) para automatizar el
ciclo completo de despliegue y operación.
2. Estandarización de arquitecturas Kubernetes y plantillas reutilizables para todos los
entornos.
3. Implementación de estrategias avanzadas de despliegue: rolling update, blue/green y
canary deployment.
4. Optimización continua del consumo de recursos y autoescalado dinámico de aplicaciones.
5. Integración avanzada con Prometheus, Grafana y sistemas centralizados de logging y
trazabilidad.
6. Escaneo automático de vulnerabilidades y políticas de seguridad integradas en pipelines
###### CI/CD.
7. Evolución progresiva hacia arquitecturas desacopladas basadas en microservicios
distribuidos.


Valor aportado Estas mejoras permiten disponer de una plataforma más resiliente, automatizada y preparada para la evolución tecnológica de EducaMadrid, reduciendo tiempos de despliegue, minimizando incidencias y mejorando la capacidad de escalado y continuidad de los servicios. Además, la incorporación de prácticas DevOps, observabilidad avanzada y automatización operativa favorece una gestión más eficiente, segura y alineada con entornos cloud- native de alta disponibilidad. Requisito: II.1.3.15. Mantenimiento, gestión y decomisionado de servidores Requerimiento EducaMadrid Se necesita la gestión y mejora en los procesos de decomisionado de cualquier elemento que haya llegado a su fin de vida útil (End Of Life, EOL). Se necesita especial atención a la mejora de los procesos que afectan a elementos críticos como los servidores de forma que tras su desmantelación no queden elementos o configuraciones sin gestionar, tales como IPs, espacios de almacenamiento, hostnames, redireccionamientos DNS, etc. (UPD15) Para ello se solicita:
- Gestionar la información actual de dichos entornos.

- Actualizar, adaptar y mantener los servicios que se están prestando en servidores
modernos, compatibles y seguros.

- Decomisionar los servidores que han llegado al final de su vida útil.

Propuesta técnica de empresa_s empresa_s propone un modelo integral de gestión del ciclo de vida de servidores, orientado a garantizar la trazabilidad, seguridad y eliminación controlada de sistemas que alcancen su fin de vida útil (EOL). Se realizará un mantenimiento continuo del inventario de activos, identificando servidores obsoletos, dependencias asociadas y servicios críticos vinculados a cada infraestructura. La propuesta contempla:
- Gestión centralizada del inventario y estado de servidores físicos y virtuales.

- Análisis de dependencias técnicas: DNS, IPs, almacenamiento, balanceadores, accesos y
reglas de seguridad.

- Migración controlada de servicios hacia plataformas modernas y soportadas.

- Validación funcional tras cada migración o retirada de sistemas.

- Ejecución de procedimientos estructurados de decomisionado:

o parada controlada de servicios o salvaguarda de información o limpieza de configuraciones residuales o retirada segura del activo
- Coordinación continua con equipos de sistemas, comunicaciones y ciberseguridad.


Asimismo, empresa_s garantizará la verificación completa de eliminación de elementos huérfanos, evitando riesgos operativos o de seguridad derivados de configuraciones no gestionadas. Propuesta de mejora y evolución del servicio Con el objetivo de evolucionar hacia un modelo más automatizado y eficiente, empresa_s propone:
1. Estandarización completa del proceso de decomisionado mediante procedimientos
auditables y homogéneos.
2. Automatización de inventariado, validaciones y seguimiento de servidores mediante
scripting y Ansible.
3. Generación automática de reportes históricos y trazabilidad completa de activos retirados.
4. Integración con CMDB y sistemas de monitorización para detección automática de
elementos obsoletos.
5. Implementación de controles preventivos para evitar configuraciones residuales, accesos
activos o dependencias no documentadas.
6. Evolución hacia un modelo centralizado de gobierno del ciclo de vida de infraestructuras
IT. Valor aportado Estas mejoras permiten garantizar una gestión controlada, segura y trazable del ciclo de vida de los servidores de EducaMadrid, reduciendo riesgos operativos y eliminando configuraciones residuales que puedan afectar a la estabilidad o seguridad de la plataforma. Además, la automatización y centralización de procesos favorecen una operación más eficiente, homogénea y alineada con las mejores prácticas de gobierno IT.

##### APARTADO: CLOUD (CLO)
Requisito: II.1.4.1. Mantenimiento del servicio de la nube de EducaMadrid Requerimiento EducaMadrid EducaMadrid cuenta con una infraestructura de código abierto para el servicio de nube. Esta infraestructura debe optimizarse, evolucionar y mantenerse para ofrecer mejor servicio (CLO1). Se solicita:
- Mantener y mejorar la infraestructura de código abierto para el servicio de la nube de
EducaMadrid. Página 78 de 239


![Imagen de la página 78](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0078-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0078-imagen-003.png -->
- Flujo gobernado para retirar sistemas y servicios obsoletos desde la CMDB.
- Tras identificar elementos al final de vida se analizan dependencias e impacto, se migran los servicios, se realiza una retirada segura y se registra toda la trazabilidad.
- Redmine gestiona ticket, asignación, planificación, ejecución, validación y cierre.
- Políticas, seguridad, automatización y monitorización acompañan todo el proceso.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0078-imagen-003.png -->

- La estructura debe permitir una distribución balanceada de los distintos centros a los que
se da servicio, compuestos por un total de 2 millones de usuario aprox.

- Se tendrá que realizar una redistribución de los NFS para su correcta funcionalidad a nivel
multicentro y planificar y gestionar su crecimiento a medio y largo plazo.

- Mantener la solución con su debida gestión y corrección de incidencias.

- Mejorar la gestión de cuota del cloud actual que se realiza desde el desarrollo propio de
Gestor de Usuarios del portal.

- Realizar las actualizaciones necesarias de versionado del aplicativo de manera recurrente.
Propuesta técnica de empresa_s empresa_s propone un modelo integral de mantenimiento y evolución de la plataforma cloud de EducaMadrid, basada en NextCloud y orientada a garantizar disponibilidad, rendimiento y escalabilidad para un entorno de aproximadamente 2 millones de usuarios. Se realizará un mantenimiento continuo del ecosistema cloud mediante actualización coordinada de servidores web, PHP, bases de datos y sistemas de cacheo, asegurando compatibilidad y estabilidad operativa mediante validaciones previas en entornos de preproducción. La propuesta contempla:
- Evolución continua de la plataforma NextCloud y sus componentes asociados.

- Arquitectura distribuida y balanceada por centros educativos para optimizar concurrencia
y rendimiento.

- Gestión avanzada de almacenamiento NFS, evitando saturaciones y mejorando la
distribución de carga.

- Optimización y sincronización del sistema de cuotas integrado con el portal corporativo.

- Monitorización continua del rendimiento, almacenamiento y operaciones concurrentes.

- Resolución proactiva de incidencias relacionadas con sincronización, accesos y
degradación del servicio.

Asimismo, las actuaciones críticas se realizarán en ventanas controladas para minimizar el impacto sobre los usuarios y garantizar la continuidad operativa del servicio. Propuesta de mejora y evolución del servicio Con el objetivo de evolucionar la nube de EducaMadrid hacia un entorno más eficiente y resiliente, empresa_s propone:
1. Segmentación inteligente de usuarios y almacenamiento por centros educativos.
2. Automatización de redistribución de carga y crecimiento dinámico del almacenamiento
NFS.
3. Implantación de pruebas avanzadas de carga y concurrencia para validar escenarios
masivos de uso.
4. Integración de monitorización proactiva con métricas específicas de sincronización,
latencia y consumo.
5. Optimización de experiencia de usuario mediante reducción de tiempos de acceso y
sincronización.


6. Definición de un modelo de crecimiento progresivo y planificación predictiva de capacidad.
7. Evolución hacia una arquitectura cloud más distribuida, escalable y preparada para futuras
ampliaciones.

Valor aportado Estas mejoras permiten consolidar una plataforma cloud robusta, escalable y preparada para soportar grandes volúmenes de usuarios y datos, garantizando continuidad de servicio y optimización del rendimiento. Además, la automatización operativa, la monitorización avanzada y la segmentación inteligente de carga reducen incidencias, mejoran la experiencia de usuario y facilitan la evolución continua de la infraestructura cloud de EducaMadrid.

Requisito: II.1.4.2. Mantenimiento y adaptación del sistema de almacenamiento temporal de datos de la nube Requerimiento EducaMadrid EducaMadrid dispone de un sistema de almacenamiento temporal de información integrado en su entorno de nube, cuyo objetivo es optimizar el acceso a datos y mejorar el rendimiento global de los servicios prestados. Dicho sistema requiere labores de mantenimiento, adaptación y evolución para garantizar su continuidad operativa, su adecuación a los cambios de carga y su correcta interacción con el conjunto de servicios de la plataforma (CLO2). Se solicita:
- Mantener el sistema de almacenamiento temporal de datos, asegurando su disponibilidad,
estabilidad y correcto funcionamiento, incluyendo las tareas necesarias de gestión, actualización y resolución de incidencias.

- Garantizar que dicho sistema continúe siendo compatible e interoperable con la nube de
EducaMadrid y con los servicios que hacen uso de mecanismos de acceso optimizado a información temporal, sin alterar la arquitectura funcional existente.

- El sistema tiene que adecuarse a la carga y se realizarán las tareas necesarias para el
escalado del mismo

Propuesta técnica de empresa_s


![Imagen de la página 80](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0080-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0080-imagen-003.png -->
- Arquitectura escalable de Nextcloud con varios nodos de aplicación y balanceo interno.
- Una base de datos replicada en alta disponibilidad sirve a la capa de aplicaciones.
- Los servicios compartidos incluyen caché distribuida, colaboración en tiempo real, colas, búsqueda y notificaciones.
- El almacenamiento se reparte entre varios nodos con redundancia, escalabilidad y distribución inteligente de datos.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0080-imagen-003.png -->

Los especialistas de empresa_s abordarán el mantenimiento y evolución del sistema de almacenamiento temporal de datos de la nube como un componente crítico de alto rendimiento dentro del ecosistema de EducaMadrid, garantizando su escalabilidad, estabilidad y eficiencia operativa para un volumen superior a los 2 millones de usuarios y decenas de terabytes de información. El sistema actual, basado en una arquitectura distribuida sobre múltiples NFS, será mantenido y evolucionado como modelo de almacenamiento escalable horizontalmente, evitando la concentración de carga en un único sistema. Se mantendrá el modelo de almacenamiento basado en:
- Un NFS principal (“data principal”) donde se ubican los nuevos usuarios.

- Múltiples NFS secundarios (“datas secundarias”) donde se distribuyen los usuarios.

- Uso de enlaces simbólicos a nivel de sistema operativo para redirigir cada usuario desde
la data principal a su ubicación real.

empresa_s realizará el mantenimiento operativo del sistema, incluyendo:
- Supervisión continua del estado de los NFS:
o Disponibilidad. o Rendimiento. o Latencia de acceso.
- Control de ocupación de almacenamiento por volumen.

- Gestión de incidencias relacionadas con acceso a datos.

- Verificación de integridad de enlaces simbólicos.

Se garantizará la compatibilidad total con la arquitectura de Nextcloud, asegurando que:
- No se modifica la lógica funcional de acceso a datos.

- El sistema sigue siendo transparente para la aplicación.

- Se mantiene la interoperabilidad con todos los servicios de la nube.
El sistema será adaptado dinámicamente a la carga mediante:
- Scripts automatizados de redistribución de usuarios:
o Movimiento controlado de carpetas de usuario entre NFS. o Actualización automática de enlaces simbólicos.
- Control de crecimiento:
o Definición de umbrales de ocupación por NFS. o Creación de nuevas datas secundarias al alcanzar límites definidos.
- Balanceo progresivo del almacenamiento.
Este modelo permite:
- Evitar saturación de la data principal.

- Distribuir la carga de I/O.

- Mantener tiempos de acceso óptimos.

Se realizará mantenimiento de los mecanismos de backup, aprovechando la arquitectura distribuida: Página 81 de 239


- Ejecución de copias en paralelo sobre múltiples NFS.

- Reducción del tiempo total de backup.

- Mejora de ventanas operativas.

Propuesta de mejora, escalabilidad y optimización del almacenamiento empresa_s propone evolucionar el sistema hacia un modelo avanzado de gestión automatizada del almacenamiento:
1. Motor inteligente de distribución de usuarios. Automatización basada en:
- Porcentaje de ocupación.

- Rendimiento del NFS.

- Número de usuarios por volumen.

2. Monitorización avanzada de almacenamiento. Métricas clave:
- Uso por NFS.

- IOPS.

- Latencia.

- Crecimiento por volumen.


![Imagen de la página 82](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0082-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0082-imagen-003.png -->
- Infografía del almacenamiento temporal distribuido de Nextcloud para más de dos millones de usuarios.
- Los nuevos usuarios parten de una data principal NFS y se redistribuyen a datas secundarias enlazadas simbólicamente cuando se alcanza un umbral de ocupación.
- La operación incluye monitorización, compatibilidad, balanceo, automatización, trazabilidad y copias paralelas.
- Se destacan más de 70 TB, millones de ficheros, escalabilidad horizontal, alta disponibilidad y continuidad operativa.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0082-imagen-003.png -->

3. Automatización del crecimiento del sistema:
- Creación automática de nuevos NFS.

- Integración transparente en el sistema.

- Redistribución progresiva de usuarios.
4. Optimización de backups distribuidos:
- Paralelización total de copias.

- Reducción de ventanas de backup.

- Mayor resiliencia ante fallos.

5. Trazabilidad y control del sistema:
- Registro de movimientos de usuarios.

- Logs de automatización.

- Auditoría de estado del almacenamiento.

Valor aportado Estas actuaciones permiten disponer de un sistema de almacenamiento altamente escalable, distribuido y eficiente, capaz de soportar millones de usuarios y grandes volúmenes de datos sin degradación de rendimiento, eliminando cuellos de botella y mejorando significativamente la gestión de backups y la operativa global de la nube. Requisito: II.1.4.3. Mantenimiento del sistema de edición en línea Requerimiento EducaMadrid EducaMadrid cuenta con un servicio de edición en línea de documentos. Este servicio necesita evolucionar y mantenerse para ofrecer mejor servicio (CLO3). Se solicita:
- Mejorar la infraestructura necesaria para soportar la edición en línea a los usuarios de la
plataforma EducaMadrid.

- El sistema debe permitir la integración con la nube de EducaMadrid.

- Mantener y mejorar la solución con su debida gestión y corrección de incidencias.

- El sistema tiene que adecuarse a la carga y se realizarán las tareas necesarias para el
escalado del mismo Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la solución de edición en línea como un servicio crítico de colaboración en tiempo real, estrechamente integrado con la plataforma cloud de EducaMadrid, garantizando rendimiento bajo alta concurrencia y escalabilidad progresiva. empresa_s implantará un modelo de actualización continua:
- Migración a versiones estables del entorno de edición basado en Collabora Online.
- Validación de compatibilidad con:
o formatos estándar (ODF, DOCX, XLSX, etc.)


o navegadores modernos
- Despliegue controlado en entorno de preproducción.
- Procedimientos de rollback ante incidencias.
Arquitectura optimizada para edición colaborativa:
- Despliegue del servicio en entorno distribuido:
o contenedores o nodos virtualizados
- Integración nativa con la nube basada en NextCloud mediante WOPI/WebSocket.
- Optimización de recursos:
o CPU y memoria por sesión o gestión de procesos concurrentes
- Configuración orientada a sesiones simultáneas de edición.
Escalabilidad y adaptación de carga:
- Definición de arquitectura en clúster:
o múltiples nodos de edición o balanceo de carga mediante HAProxy u equivalente
- Ajuste dinámico en función de:
o número de usuarios activos o volumen de documentos abiertos
- Planificación de crecimiento progresivo del sistema.
Validación y pruebas de rendimiento:
- Pruebas funcionales:
o edición simultánea o guardado automático o historial de versiones
- Pruebas de carga:
o simulación de múltiples usuarios concurrentes o medición de latencia y consumo de recursos
- Identificación de cuellos de botella.
Operación y mantenimiento correctivo:
- Resolución de incidencias:
o errores de edición o problemas de sincronización
- Ajustes en caliente ante degradación del servicio.
- Monitorización continua de sesiones activas y estado del sistema.
Arquitectura:


Propuesta de mejora, escalabilidad, integración y experiencia de usuario empresa_s propone evolucionar el sistema hacia un modelo de alta concurrencia y resiliencia:
- Ampliación del clúster de edición, incrementando nodos según demanda.

- Monitorización específica de sesiones, con métricas en tiempo real.

- Definición de umbrales de escalado, anticipando picos de uso.

- Optimización de experiencia de usuario, reduciendo latencia en edición.

- Segmentación de carga por perfiles de usuario, mejorando eficiencia del sistema.
Valor aportado Estas mejoras permiten consolidar la edición en línea como un servicio estable, escalable y plenamente integrado en el ecosistema cloud.
##### APARTADO: OTROS DESARROLLOS (OTR)
Requisito: II.1.5.1. Mantenimiento y mejora del sistema de autenticación centralizada Requerimiento EducaMadrid Es necesaria el mantenimiento y la mejora del sistema basado en de Software Libre KeyCloak de inicio de sesión único (OTR1). Se solicita:
- Mantener y mejorar la solución de código abierto de inicio de sesión único (SSO).

- Dicha solución SSO debe sincronizarse con el servicio de autentificación de la plataforma
(actualmente LDAP).


![Imagen de la página 85](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0085-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0085-imagen-003.png -->
- Arquitectura de nube para editores de documentos en línea como Collabora u ONLYOFFICE.
- Internet y SSO con Keycloak, LDAP o Active Directory dan acceso a nodos de aplicación escalables, balanceadores externos e internos y varias instancias de edición.
- Una red trasera de alta velocidad conecta almacenamiento NFS o Ceph redundante.
- Las características indicadas son disponibilidad, rendimiento, escalabilidad, monitorización, cifrado y copias automáticas.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0085-imagen-003.png -->

- La solución debe incluir los controles necesarios para proporcionar el login automático en
los aplicativos donde se implemente y permitir los accesos a estas con un inicio de sesión única, accediendo directamente a las aplicaciones si un usuario se encuentra logado y presentar la página de login cuando no sea así.

- Mantener la solución con su debida gestión.

- Mejorar la solución implementando redundancia a la Solución a través de una configuración
en HA.

- Implementar 2FA en los servicios de Administración de la plataforma.
Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el mantenimiento del sistema de autenticación centralizada de EducaMadrid como un servicio crítico orientado a garantizar seguridad, disponibilidad y acceso unificado a todas las plataformas corporativas mediante tecnología SSO basada en Keycloak. Se realizará un mantenimiento continuo del entorno:
- Actualización periódica de Keycloak y componentes asociados.

- Supervisión de rendimiento, logs, sesiones y base de datos.

- Resolución proactiva de incidencias y aplicación de parches de seguridad.

- Gestión de copias de seguridad y validación de recuperación.

empresa_s garantizará la integración e interoperabilidad con el ecosistema corporativo:
- Integración con LDAP y directorio corporativo.

- Compatibilidad con aplicaciones educativas y servicios integrados.

- Gestión centralizada de autenticación y control de sesiones.

- Adaptación continua a nuevos servicios y necesidades funcionales.

La seguridad y resiliencia del servicio se reforzarán mediante:
- Implantación de autenticación multifactor (2FA) para accesos críticos.

- Políticas avanzadas de control de accesos y gestión de credenciales.

- Arquitectura redundante basada en múltiples instancias Keycloak.

- Base de datos PostgreSQL en alta disponibilidad.

Propuesta de mejora y evolución del servicio


![Imagen de la página 86](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0086-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0086-imagen-003.png -->
- Lista breve de características de autenticación.
- Señala SSO transparente, alta disponibilidad, autenticación multifactor para administradores, integración con LDAP y auditoría completa.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0086-imagen-003.png -->

empresa_s propone evolucionar la plataforma SSO hacia un modelo más robusto, automatizado y resiliente mediante:
1. Implantación de entornos de preproducción para validación segura de cambios y nuevas
versiones.
2. Arquitectura HA con balanceo y redundancia completa del servicio Keycloak.
3. Automatización de backups, recuperación y despliegues del sistema.
4. Integración avanzada con métricas, monitorización y alertas proactivas.
5. Refuerzo de seguridad mediante MFA, auditoría de accesos y trazabilidad completa.
6. Optimización de experiencia de usuario con autenticación transparente entre servicios
EducaMadrid. Valor aportado Estas mejoras permiten disponer de un sistema SSO altamente disponible, seguro y preparado para el crecimiento continuo de la plataforma EducaMadrid. Asimismo, se mejora la experiencia de usuario mediante autenticación unificada, se refuerza la seguridad de acceso a servicios críticos y se reduce el impacto operativo ante incidencias o cambios evolutivos. Requisito: II.1.5.2. Mantenimiento, configuración y gestión de autenticación multifactor (2FA) en el sistema SSO Requerimiento EducaMadrid Es necesaria la implementación y el mantenimiento de un sistema 2FA en los servicios que utilicen inicio de sesión único (OTR2). Se solicita:
- Realizar la implementación y el mantenimiento necesaria de la autentificación de dos
factores (2FA).

- Dicha solución 2FA debe implementarse en los servicios que utilicen un inicio de sesión
única en la plataforma.

- El flujo de autentificación debe permitir el acceso libre en los entornos educativos
conectados a la red de Madrid Digital, así como permitir la autentificación mediante OTP, como por correo electrónico alternativo.

- Será obligatorio definir y mapear los correspondientes mapeos LDAP para mantener el
correo electrónico EducaMadrid como principal en los diferentes servicios que se autentifiquen mediante SSO.

- La solución debe ser capaz de sincronizar y correlacionar el Token OTP del SSO con el
Token OTP del correo electrónico web de la plataforma.

- Mantenimiento de la solución con su debida gestión.
Propuesta técnica de empresa_s Los especialistas de empresa_s implantarán y mantendrán un sistema de autenticación multifactor (2FA) integrado con la plataforma SSO de EducaMadrid, garantizando un acceso seguro, centralizado y adaptado al contexto educativo.


La solución estará basada en Keycloak y mecanismos OTP sincronizados con los sistemas corporativos:
- Integración con LDAP y correo corporativo.

- Gestión centralizada de tokens OTP y cuentas de recuperación.

- Sincronización automática mediante APIs entre SSO y servicios de correo.

- Monitorización continua del estado del sistema y resolución proactiva de incidencias.
empresa_s configurará flujos de autenticación adaptativos:
- Aplicación obligatoria de 2FA en accesos externos o administrativos.

- Exclusión de MFA en redes de confianza definidas.

- Gestión avanzada de sesiones, accesos y políticas de seguridad.

- Auditoría y trazabilidad completa de eventos de autenticación.
La arquitectura garantizará alta disponibilidad, seguridad y coherencia entre plataformas de identidad y autenticación. Propuesta de mejora y evolución del servicio empresa_s propone evolucionar el sistema hacia un modelo de autenticación inteligente, automatizado y resiliente mediante:
1. Implantación de autenticación adaptativa basada en IP, ubicación y contexto de acceso.
2. Sincronización avanzada y continua de tokens OTP entre SSO, correo y directorio
corporativo.
3. Refuerzo de seguridad en accesos críticos mediante MFA obligatorio y control avanzado
de sesiones.
4. Integración con sistemas de monitorización y alertas de comportamiento anómalo.
5. Centralización de auditoría y trazabilidad de accesos y eventos de autenticación.
6. Automatización de backups y recuperación de configuraciones MFA.

Valor aportado Estas mejoras permiten disponer de un sistema de autenticación multifactor robusto, seguro y alineado con las necesidades de escalabilidad y protección de EducaMadrid. Página 88 de 239


![Imagen de la página 88](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0088-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0088-imagen-003.png -->
- Conjunto de diagramas de flujo para configurar y utilizar autenticación de doble factor en servicios EducaMadrid.
- El flujo principal permite activar 2FA, confirmar el correo, elegir método secundario y resolver errores de configuración.
- Otros paneles muestran el inicio de sesión en Correo Web y Empieza con 2FA, mediante acceso directo, correo o aplicación TOTP.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0088-imagen-003.png -->

Asimismo, se mejora la experiencia de usuario mediante autenticación contextual, se refuerza la protección frente a accesos no autorizados y se garantiza una gestión centralizada y trazable del ciclo completo de autenticación. Requisito: II.1.5.3. Mantenimiento y mejora de herramientas de automatización de tareas Requerimiento EducaMadrid EducaMadrid necesita actualizar los sistemas de automatización de tareas de los diferentes aplicativos y BBDD (OTR3). Para ello se solicita:
- Mejorar los sistemas de automatización de tareas de los diferentes aplicativos y BBDD.

- Mantener la solución con su debida gestión y corregir las incidencias.
Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la automatización de tareas como un elemento estratégico para garantizar la operación continua, la reducción de errores manuales y la eficiencia operativa de la plataforma EducaMadrid. Se realizará un mantenimiento continuo de los sistemas actuales de automatización:
- Revisión y optimización de scripts y tareas programadas.

- Resolución proactiva de incidencias y validación de ejecuciones.

- Gestión de logs, backups y control de errores.

- Supervisión del correcto funcionamiento de procesos automatizados.

empresa_s implantará un modelo estandarizado y gobernado:
- Normalización de scripts, nomenclaturas y documentación.

- Integración con sistemas de versionado y pipelines CI/CD.

- Centralización de tareas mediante herramientas open source como Ansible.

- Automatización basada en playbooks reutilizables y mantenibles.
La solución incorporará mecanismos avanzados de observabilidad:
- Monitorización de ejecuciones y tiempos de respuesta.

- Alertas automáticas ante fallos o anomalías.

- Auditoría y trazabilidad completa de cambios y tareas.

- Control centralizado del ciclo de vida de automatizaciones.
Propuesta de mejora y evolución del servicio empresa_s propone evolucionar el modelo actual hacia una plataforma de automatización moderna, escalable y orientada a Infraestructura como Código (IaC):
1. Implantación de automatización centralizada basada en Ansible y playbooks reutilizables.
2. Integración completa con GitLab y pipelines CI/CD para control y despliegue automatizado.


3. Automatización avanzada de validaciones, reintentos y recuperación ante errores.
4. Incorporación de métricas, monitorización y reporting de ejecuciones.
5. Evolución hacia un modelo Automation as Code totalmente versionado y auditable.
6. Extensión progresiva de automatizaciones a nuevos servicios cloud, contenedores y
microservicios. Valor aportado Estas mejoras permiten disponer de una plataforma de automatización más robusta, homogénea y preparada para la evolución tecnológica de EducaMadrid. Asimismo, se reducen errores operativos, se mejora la trazabilidad de cambios y se incrementa la capacidad de despliegue y operación continua mediante procesos automatizados y controlados. Requisito: II.1.5.4. Mantenimiento y mejora del sistema de gestión y análisis de datos basado en ELK Requerimiento EducaMadrid EducaMadrid dispone de un sistema de gestión de datos centralizado y escalable adecuado para arquitecturas Big Data basado en el Software Libre Elastik (ELK), el cual se usa para analizar datos, generar informes y auditar las diferentes aplicaciones (OTR4). Se solicita:
- Actualizar los diferentes servicios asociados al ELK-Stack incluyendo el sistema de
almacenamiento distribuido, el motor de búsqueda y de procesamiento y el sistema de visualización.

- Mantener la solución con su debida gestión y corregir las incidencias.
Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el mantenimiento del stack ELK como una plataforma estratégica de observabilidad, auditoría y explotación de datos para el ecosistema EducaMadrid . Se realizará un mantenimiento continuo de Elasticsearch, Logstash y Kibana:
- Actualización controlada de versiones y revisión de compatibilidades.

- Optimización de rendimiento, indexación y almacenamiento.

- Supervisión de nodos, capacidad y estado de la plataforma.

- Resolución proactiva de incidencias y gestión del ciclo de vida del dato.

empresa_s garantizará una gestión eficiente de la ingesta y explotación de información:
- Automatización de procesos ETL y cargas programadas.

- Integración con CMDB, monitorización y servicios corporativos.

- Normalización y transformación avanzada de datos.

- Evolución y mantenimiento de dashboards, auditoría y trazabilidad.

La solución se apoyará en un modelo escalable y seguro:
- Arquitectura desacoplada y preparada para contenerización.


- Control centralizado de accesos y políticas de seguridad.

- Integración con sistemas de observabilidad y alertado.

- Adaptación continua a nuevos requisitos funcionales y operativos.
Propuesta de mejora y evolución del servicio empresa_s propone evolucionar el stack ELK hacia una plataforma moderna, resiliente y orientada a analítica avanzada mediante:
1. Evolución hacia arquitecturas basadas en contenedores y despliegues cloud- native.
2. Implantación de entornos de preproducción para validación segura de versiones y
pipelines.
3. Optimización avanzada de ingesta, procesamiento y correlación de eventos.
4. Integración con CMDB, monitorización y sistemas corporativos de auditoría.
5. Refuerzo de seguridad y cumplimiento alineado con ENS y buenas prácticas CCN-CERT.
6. Centralización de métricas, logs y trazabilidad operativa en tiempo real.
7. Mejora del gobierno del dato y automatización del ciclo de vida de índices y
almacenamiento.

Valor aportado Estas mejoras permiten disponer de una plataforma ELK más eficiente, escalable y preparada para el crecimiento continuo de los servicios de EducaMadrid. Asimismo, se mejora la capacidad de análisis y observabilidad, se incrementa la trazabilidad de eventos y se refuerza la seguridad y gobierno del dato mediante una arquitectura moderna y automatizada. Requisito: II.1.5.5. Mantenimiento y mejora de la herramienta de flujos de trabajo Requerimiento EducaMadrid Se necesita facilitar las tareas del equipo interno de EducaMadrid, así como el registro de las peticiones y progresos del trabajo realizado por cualquier técnico en la infraestructura de EducaMadrid, de forma que redunde en un menor tiempo de respuesta a los usuarios (OTR5). Para ello se solicita:
- Mejorar la herramienta que permite la gestión de flujos de trabajo, de forma que se puedan
recoger los datos de salida de distintas aplicaciones, bases de datos, documentos, etc. y ser procesados como entrada de otras partes de la plataforma.

- Mantener la solución con su debida gestión y corregir las incidencias.

- Actualizar la versión del aplicativo y paso a una base de datos externa dedicada.


![Imagen de la página 91](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0091-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0091-imagen-003.png -->
- Cuatro tarjetas que resumen capacidades de la pila Elastic.
- Elasticsearch se presenta como motor de búsqueda y API; Observability agrupa registros, métricas y trazas; Security previene y responde a amenazas; Analytics permite explorar y visualizar datos.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0091-imagen-003.png -->

Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la herramienta de flujos de trabajo como un componente estratégico para la coordinación operativa, trazabilidad y automatización de procesos técnicos dentro del ecosistema EducaMadrid. Se realizará un mantenimiento continuo de la plataforma:
- Actualización controlada de versiones y componentes.
- Resolución proactiva de incidencias y optimización del rendimiento.

- Migración a bases de datos dedicadas para mejorar disponibilidad y desacoplamiento.

- Supervisión continua de la operación y estabilidad del servicio.
empresa_s implantará un modelo orientado a automatización y gobierno operativo:
- Optimización de flujos de trabajo y procedimientos técnicos.

- Automatización de tareas e integraciones con sistemas corporativos.

- Estandarización de procesos, estados y trazabilidad.

- Integración con plataformas como GitLab, CMDB, monitorización y SSO.

La solución permitirá disponer de una plataforma centralizada y escalable para la gestión de incidencias, cambios y operaciones técnicas. Propuesta de mejora y evolución del servicio empresa_s propone evolucionar la herramienta hacia un entorno avanzado de orquestación y automatización de procesos mediante:
1. Integración completa con sistemas corporativos: SSO, CMDB, monitorización y bases de
datos.
2. Automatización end- to-end de flujos operativos y generación automática de tareas.
3. Integración con GitLab y pipelines DevOps para trazabilidad completa de cambios.
4. Implantación de métricas, reporting y cuadros de mando operativos.
5. Evolución hacia arquitecturas basadas en contenedores y despliegues escalables.
6. Refuerzo de auditoría, control de accesos y trazabilidad de operaciones.
Valor aportado Estas mejoras permiten disponer de una plataforma de gestión más integrada, automatizada y alineada con la operación continua de EducaMadrid. Asimismo, se mejora la coordinación entre equipos, se reducen tiempos de gestión y se incrementa la trazabilidad y control operativo mediante flujos centralizados y automatizados. Requisito: II.1.5.6. Mantenimiento y mejora del Portal CAU Requerimiento EducaMadrid La plataforma de EducaMadrid pone a disposición de sus usuarios la herramienta “Portal CAU” (portalcau.educa.madrid.org), basada en la solución de Software Libre Redmine, para que cualquiera pueda crear incidencias y seguir el estado de avance en la resolución de las mismas. Se necesita una mejora y mantenimiento (OTR6): Se solicita: Página 92 de 239


- Mantener, actualizar y mejorar el proyecto, de forma que se optimice el procedimiento de
respuesta de las incidencias de nivel uno y el escalado de aquellas incidencias que deban ser tratadas por el nivel dos de soporte.

- Adaptar, mejorar y mantener un sistema que realice de forma automática la asignación de
las nuevas incidencias a los distintos trabajadores del CAU de forma consecutiva, para una mayor agilidad de incidencias

- Mejorar, Optimizar y mantener los procesos que permiten detectar si el autor de una
incidencia ya ha sido atendido por algún operario en los últimos días para que las nuevas incidencias abiertas por ese mismo autor sean asignadas al mismo operario, por si estuvieran relacionadas.

- Mantener la solución con su debida gestión y corregir las incidencias.
Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el mantenimiento y evolución del Portal CAU como un sistema central de gestión de incidencias integrado dentro del ecosistema de EducaMadrid, orientado a optimizar los tiempos de respuesta, automatizar la gestión operativa y mejorar la experiencia tanto de usuarios como de técnicos de soporte. empresa_s mantendrá y evolucionará la plataforma basada en Redmine, garantizando su estabilidad, actualización tecnológica y correcta operación, incluyendo:
- Actualización periódica de la plataforma:
o Evaluación de nuevas versiones de Redmine. o Migraciones controladas de datos y configuraciones. o Validación en entorno de preproducción.
- Mantenimiento correctivo:
o Análisis de logs. o Resolución de incidencias funcionales. o Ajuste de dependencias (Ruby, base de datos, plugins). Uno de los pilares del sistema será la automatización de la creación de incidencias mediante integración con correo electrónico:
- Recepción de incidencias vía email:
o Procesamiento automático de correos entrantes. o Extracción de:
- Asunto → título de la incidencia.
- Cuerpo → descripción.
- Enriquecimiento automático mediante LDAP:
o Consulta del usuario remitente. o Obtención de atributos:
- Tipo de usuario (alumno, docente, institucional).
- Centro educativo.
- Información organizativa.
- Clasificación automática de incidencias:
o Asignación a categorías. o Enrutamiento a departamentos específicos según tipología. empresa_s implementará y mantendrá un sistema automatizado de asignación de incidencias:
- Asignación consecutiva (round- robin):
o Reparto equitativo entre técnicos de nivel 1. o Balanceo de carga de trabajo. Página 93 de 239


- Reglas dinámicas de asignación:
o Por tipo de incidencia. o Por perfil de usuario. o Por área funcional. Se desarrollará un sistema de continuidad de atención por usuario:
- Identificación de incidencias previas del mismo usuario:
o Consulta histórica en Redmine.
- Reasignación automática:
o Si el usuario ha sido atendido recientemente, la incidencia se asigna al mismo técnico.
- Mejora de la resolución:
o Continuidad en el tratamiento. o Reducción de tiempos de diagnóstico. En relación con el escalado de incidencias:
- Definición de flujos de trabajo:
o Nivel 1 → Nivel 2.
- Automatización de escalado:
o Basado en:
- Tipo de incidencia.
- Tiempo sin resolución.
- Complejidad detectada.
- Seguimiento del estado de incidencias:
o Control de SLA. o Tiempos de respuesta. Propuesta de mejora, automatización y optimización del CAU empresa_s propone evolucionar el Portal CAU hacia un modelo inteligente y altamente automatizado:
1. Motor avanzado de clasificación de incidencias. Clasificación automática basada en:
- Contenido del correo.

- Perfil del usuario.

- Históricos previos.
2. Sistema inteligente de asignación:
- Balanceo dinámico de carga.

- Reasignación automática según disponibilidad.

- Priorización de incidencias.
3. Trazabilidad completa del ciclo de incidencias:
- Registro de asignaciones.

- Seguimiento de tiempos de resolución.

- Auditoría de cambios.
4. Optimización del escalado:
- Reglas automáticas de derivación a nivel 2.

- Reducción de intervención manual.


- Mejora en tiempos de resolución.

5. Monitorización del servicio CAU. Métricas clave:
- Tiempo medio de resolución.

- Número de incidencias por técnico.

- Carga por departamento.
Valor aportado Estas actuaciones transforman el Portal CAU en un sistema inteligente de gestión de incidencias, automatizando la entrada, clasificación y asignación, mejorando la eficiencia operativa del soporte y reduciendo significativamente los tiempos de respuesta y resolución. Requisito: II.1.5.7. Mantenimiento y evolución de servicios de Inteligencia Artificial para la plataforma EducaMadrid Requerimiento EducaMadrid EducaMadrid dispone de servicios que incorporan capacidades de Inteligencia Artificial para apoyar y mejorar la prestación de distintos servicios de la plataforma, incluyendo, correo web, aulas virtuales y entornos cloud. Estos servicios requieren labores continuas de supervisión, mantenimiento, mejora y adaptación para garantizar su disponibilidad, eficiencia operativa, interoperabilidad con otros sistemas y adecuación a las necesidades funcionales de la plataforma (OTR7). Se solicita:
- Mantener, supervisar y mejorar los servicios de Inteligencia Artificial existentes,
asegurando su correcto funcionamiento, disponibilidad y continuidad, incluyendo la gestión de incidencias y ajustes operativos que se consideren necesarios.

- Garantizar la integración de los servicios de Inteligencia Artificial con los distintos
componentes de la plataforma, de manera que puedan prestar funcionalidades de forma coherente y centralizada a los diferentes servicios que los requieran.

- Realizar las adaptaciones, ajustes y optimizaciones que se consideren oportunas para
adecuar los servicios a la carga, al uso previsto y a las necesidades funcionales y operativas, sin que ello implique la definición de un método técnico concreto.

- Llevar a cabo todas las tareas necesarias para la mejora continua, escalabilidad y
resiliencia de los servicios, de forma que se asegure su estabilidad, eficiencia y capacidad de respuesta ante cambios en la demanda o en los requisitos funcionales.

- Documentar, reportar y gestionar de manera adecuada los trabajos realizados,
manteniendo la trazabilidad de las acciones y asegurando la continuidad del servicio, sin que ello implique un procedimiento técnico único ni limitativo.

Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la plataforma de Inteligencia Artificial de EducaMadrid como un entorno estratégico y transversal, orientado a proporcionar servicios LLM altamente disponibles, escalables y seguros para los distintos aplicativos educativos y corporativos. empresa_s realizará una gestión integral de la plataforma:
- Supervisión continua de servicios de IA y entornos contenerizados.


- Optimización del uso de infraestructura GPU (T4, A40, H100).

- Gestión de incidencias, capacidad y rendimiento de inferencia.

- Control de versiones y ciclo de vida de modelos.
La arquitectura propuesta estará basada en tecnologías modernas y desacopladas:
- Uso de vLLM para inferencia optimizada de modelos LLM.

- Implantación de LiteLLM como gateway unificado de acceso a modelos.

- Balanceo de carga y alta disponibilidad entre nodos de inferencia.

- Integración de modelos open source adaptados a los distintos casos de uso.

La plataforma permitirá la integración transversal de IA en servicios como:
- Correo web.

- Aulas Virtuales.

- Herramientas cloud y colaborativas.

- Aplicativos corporativos y automatización operativa.

Asimismo, se implantará un modelo avanzado de observabilidad:
- Monitorización mediante Prometheus y Grafana.

- Métricas de consumo, latencia y uso GPU.

- Control de sesiones y trazabilidad de peticiones.

- Supervisión proactiva del rendimiento del servicio.
Propuesta de mejora y evolución del servicio empresa_s propone evolucionar la plataforma hacia un modelo corporativo de AI Platform plenamente gobernado y automatizado mediante:
1. Centralización del acceso a modelos mediante LiteLLM como punto único de entrada.
2. Automatización del despliegue y ciclo de vida de modelos mediante pipelines
DevOps/LLMOps.
3. Optimización dinámica del uso de GPU y selección inteligente de modelos.
4. Integración de nuevos modelos open source europeos y especializados.
5. Implantación de entornos de preproducción para validación funcional y de rendimiento.
6. Refuerzo de seguridad, auditoría y control de consumo de servicios IA.
7. Evolución hacia arquitecturas distribuidas y altamente resilientes basadas en
microservicios. Valor aportado Estas mejoras permiten consolidar una plataforma de Inteligencia Artificial moderna, eficiente y preparada para el crecimiento continuo de EducaMadrid.


Asimismo, se mejora la disponibilidad, la capacidad de integración y el rendimiento de los servicios basados en IA, garantizando un entorno gobernado, escalable y alineado con estrategias cloudnative y LLMOps.

##### APARTADO: CORREO ELECTRÓNICO (COR)
Requisito: II.1.6.1. Mantenimiento y mejora de los sistemas de control de envíos de correo Requerimiento EducaMadrid Determinados proveedores de correo, por ejemplo, sólo admiten un envío máximo de correos por hora, otros establecen otros parámetros que implican límites al envío de correos desde la plataforma de EducaMadrid. Para garantizar que se puedan realizar los envíos de los correos necesarios desde nuestra plataforma (tanto puntuales como masivos, p. ej. Boletines) se hace necesario implementar adaptaciones que aseguren que dichos correos lleguen a las direcciones que se desea, impidiendo, al mismo tiempo, el envío de correos no deseados o fraudulentos (COR1). Se solicita:
- Mejorar el servicio que permite configurar un número máximo de correos/hora que se
envíen a determinados proveedores, permitiendo una configuración distinta por cada proveedor.

- Mejorar cualquier otro servicio relacionado con la gestión y control de envíos de correo que
disponga EducaMadrid y que sean necesarios para dar un servicio de correo correcto y de calidad a sus usuarios.


![Imagen de la página 97](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0097-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0097-imagen-003.png -->
- Arquitectura de una plataforma de inteligencia artificial de EducaMadrid en producción.
- Los servicios internos acceden por API a una pasarela con tokens, balanceo y límites de consumo; esta conecta con modelos abiertos, especializados y externos y con un clúster de inferencia Docker con GPU.
- La plataforma contempla test, acceso seguro de usuarios, monitorización, Prometheus, Grafana, trazabilidad, auditoría, seguridad y gobierno del dato.
- Los beneficios destacados son rendimiento, escalabilidad, disponibilidad, integración e innovación.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0097-imagen-003.png -->

- Mantener las soluciones implementadas con su debida gestión y corregir las incidencias.

Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el sistema de correo de EducaMadrid como una infraestructura crítica, enfocada a garantizar entregabilidad, control de volumen, seguridad y cumplimiento normativo, especialmente en un entorno con millones de usuarios y uso intensivo de comunicaciones masivas. Se implementará un sistema flexible de limitación adaptado a políticas externas:
- Configuración dinámica de límites de envío:
o por proveedor (Gmail, Outlook, Yahoo, etc.) o por dominio destino
- Control de velocidad de envío (rate limiting):
o por hora / ventana temporal
- Ajuste automático en función de:
o rebotes o respuestas de servidores externos (4xx / 5xx)
- Priorización de envíos:
o mensajes críticos vs campañas masivas Optimización de colas de correo:
- Segmentación de colas:
o por tipo de mensaje (notificaciones, boletines, sistema) o por prioridad
- Configuración de reintentos escalados.
- Monitorización de colas:
o detección de bloqueos o tiempos de espera
- Optimización de MTA (Postfix o equivalente).
Mejora de entregabilidad y reputación:
- Implementación y mantenimiento de:
o SPF o DKIM o DMARC
- Monitorización de reputación de IPs:
o listas negras (RBL) o scoring de entregabilidad
- Análisis de rebotes:
o hard / soft bounce
- Coordinación con DNS para ajustes necesarios.
Gestión de incidencias y soporte: Resolución de incidencias: o colas bloqueadas o errores de entrega
- Análisis de logs de correo.
Diagnóstico de problemas de entregabilidad. Control de comunicaciones en entorno educativo de menores. empresa_s implementará un sistema específico de control adaptado al contexto educativo:


- Restricción de envío/recepción externa para cuentas de alumnos:
o según políticas de autorización parental
- Control de destinatarios externos:
o validación por dominio
- Aplicación de reglas diferenciadas:
o alumnos vs docentes
- Supervisión de comportamiento anómalo.
Propuesta de mejora, control de flujo y seguridad Motor de reglas dinámicas por proveedor:
- Configuración avanzada por:
o proveedor o tipo de correo o carga del sistema
- Adaptación automática a cambios de políticas externas.
Monitorización avanzada de entregabilidad:
- Métricas clave:
o tasa de entrega o rebotes o volumen por dominio
- Alertas proactivas ante degradación.
Gestión inteligente de campañas masivas:
- Distribución temporal de envíos (throttling inteligente).
- Separación de tráfico:
o boletines vs correo operativo
- Prevención de saturación del sistema.
Valor aportado Estas mejoras permiten disponer de un sistema de envío de correo inteligente, adaptable y altamente fiable, capaz de ajustarse dinámicamente a las restricciones de los proveedores externos, optimizar la entregabilidad en escenarios de alta carga y prevenir bloqueos o degradaciones del servicio, garantizando así una comunicación eficiente, segura y continua para todos los usuarios de EducaMadrid. Requisito: II.1.6.2. Mantenimiento automatizado de listas de distribución Requerimiento EducaMadrid EducaMadrid tiene una herramienta de Software Libre que da soporte a un servicio de listas de distribución. En esta herramienta hay definidas muchas listas de distribución, las cuales se necesita tener actualizadas, mantenidas y actualizadas (COR2). Se solicita:
- Gestionar, mantener y mejorar el sistema de distribución de listas de correo.

- Mantener con especial atención la adaptación que permite a la herramienta realizar una
actualización automatizada de las listas de profesores, según nuevas incorporaciones y bajas a lo largo del curso.


Se deben realizar actualizaciones de estas listas de manera periódica (eliminación y carga completa) dos veces por curso coincidiendo con el período previo al comienzo de curso y el período no lectivo de navidad. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el sistema de listas de distribución como un servicio crítico de comunicación interna, garantizando su automatización, consistencia de datos y adaptación dinámica a los cambios organizativos del sistema educativo. empresa_s realizará la modernización del sistema actual basado en Sympa:
- Migración a la última versión estable disponible:
o mejora de rendimiento o refuerzo de seguridad o compatibilidad con sistemas actuales
- Validación en entorno de preproducción:
o integridad de listas existentes o compatibilidad de configuraciones
- Ejecución de migración controlada con:
o backup previo o plan de rollback Automatización del ciclo de vida de listas:
- Gestión automática de:
o altas, bajas y modificaciones de usuarios
- Sincronización continua con:
o sistema de usuarios o LDAP / directorio corporativo
- Generación dinámica de listas:
o por centro educativo o por rol (docente, administrativo, etc.)
- Validación automática:
o duplicados o errores de formato o inconsistencias Procesos periódicos de regeneración completa:
- Ejecución de cargas completas:
o inicio de curso o periodo navideño
- Eliminación controlada de listas obsoletas.
- Regeneración estructurada del sistema completo de listas.
- Validación post-proceso:
o consistencia de datos o correcta asignación de usuarios Monitorización y gestión de incidencias:
- Supervisión de procesos automáticos:
o errores de sincronización o fallos en generación de listas
- Análisis de logs del sistema.
- Resolución de incidencias en tiempo real.
- Integración con sistemas de monitorización global.
Propuesta de mejora centrada en automatización, trazable y escalable


empresa_s propone evolucionar el sistema hacia un modelo completamente automatizado y trazable:
1. Optimización de cargas masivas: Procesos paralelos y asincrónicos para grandes
volúmenes, reduciendo los tiempos de regeneración.
2. Sistema de auditoría avanzada. Registro completo de usuarios añadidos, eliminados y
modificaciones, con generación automática de informes.
3. Panel de control operativo. Visualización en tiempo real del estado de sincronización y
detección de errores.
4. Adaptabilidad tecnológica. Evaluación continua del sistema actual (Sympa) y evolución en
caso de limitaciones.

Valor aportado Estas mejoras permiten disponer de un sistema de listas de distribución altamente automatizado, eficiente y completamente trazable, reduciendo la intervención manual, minimizando errores en los procesos de sincronización y garantizando que la información distribuida esté siempre actualizada y alineada con la realidad organizativa de EducaMadrid, incluso en escenarios de cambios masivos como los inicios de curso. Requisito: II.1.6.3. Gestión del sistema de cuotas de correo Requerimiento EducaMadrid EducaMadrid, para la gestión del sistema de correo electrónico, necesita mantener los espacios limitados y por lo tanto se necesita un sistema de cuotas para usuarios (COR3). Se solicita:
- Monitorizar que se aplican las cuotas de correo correctas y actualizadas a todos los
usuarios de EducaMadrid.

- Actualizar el sistema actual para permitir la gestión de las mismas, aplicando las cuotas
correctas dependiendo del tipo de cuenta.

- Mantener y actualizar el desarrollo propio de gestor de usuarios para que en el alta de
usuarios se especifique la cuota por defecto.

- Mantener las soluciones implementadas con su debida gestión y corregir las incidencias.
Propuesta técnica de empresa_s


![Imagen de la página 101](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0101-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0101-imagen-003.png -->
- Captura de la página de bienvenida del servicio Listas EducaMadrid.
- La interfaz ofrece acceso, búsqueda de listas y texto introductorio sobre suscripción, baja, archivos y gestión de listas.
- Predominan una cabecera azul, un área central oscura y un gran botón de búsqueda.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0101-imagen-003.png -->

Los especialistas de empresa_s abordarán el sistema de cuotas de correo como un componente clave de gobernanza del almacenamiento y control de recursos, garantizando su correcta aplicación, trazabilidad y adaptación dinámica a la tipología de usuarios de EducaMadrid. empresa_s implantará un sistema de supervisión continua:
- Monitorización del uso de almacenamiento por usuario.
- Verificación automática de cumplimiento de cuotas:
o docentes o alumnos o personal administrativo
- Detección de desviaciones:
o cuotas incorrectas o ampliaciones no controladas
- Generación de alertas:
o superación de límites o crecimiento anómalo Evolución del sistema de gestión de cuotas:
- Refactorización del sistema actual para permitir:
o configuración dinámica o reglas parametrizables
- Definición de políticas de cuotas:
o por tipo de usuario o por centro o por rol funcional
- Gestión granular:
o asignación individual o por grupos Integración con el sistema de usuarios:
- Automatización de asignación de cuotas en el alta:
o integración con gestor de usuarios
- Validación en tiempo real:
o coherencia entre perfil y cuota
- Actualización automática ante cambios:
o cambio de rol o cambio de centro Mantenimiento correctivo y continuidad:
- Resolución de incidencias:
o errores de asignación o inconsistencias de almacenamiento
- Revisión periódica del sistema.
- Adaptación a cambios en infraestructura de correo.
Propuesta de mejora y evolución hacia la automatización empresa_s propone evolucionar el sistema hacia un modelo automatizado y gobernado:
1. Auditoría proactiva de cuotas. Identificación de cuentas fuera de política y recuperación
controlada de espacio.
2. Sistema autogestionable. Interfaz para técnicos con definición de políticas y trazabilidad
completa.
3. Asignación dinámica basada en eventos. Ajuste automático ante cambios de rol o
movimientos de usuarios.
4. Escalabilidad y planificación. Evaluación periódica del uso y preparación para ampliaciones
futuras. Página 102 de 239


Valor aportado Estas mejoras permiten disponer de un sistema de gestión de cuotas automatizado, flexible y plenamente gobernado, capaz de adaptarse en tiempo real a los cambios organizativos, optimizar el uso del almacenamiento disponible y garantizar el cumplimiento de las políticas definidas, evitando desviaciones y mejorando la eficiencia global del sistema de correo de EducaMadrid. Requisito: II.1.6.4. Control del spam y simulación de ataques Requerimiento EducaMadrid EducaMadrid necesita tener la seguridad de que son adecuados los controles de spam en el sistema de correo electrónico. (COR4). Para ello, se solicita:
- Mantener, actualizar y mejorar cualquier solución desarrollada desde el departamento de
Sistemas relacionada con el control del SPAM las cuales sirven de complemento a las soluciones implementadas desde el departamento de Ciberseguridad.

- Realizar y soportar las simulaciones controladas de ataques mediante phishing, o de
cualquier otro tipo, incluyendo cualquier otra tarea relacionada con dichas pruebas. Esta tarea se realizará periódicamente, como mínimo una vez al año. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el control del SPAM como un sistema integral de seguridad, análisis de comportamiento y protección proactiva, complementando las soluciones del área de Ciberseguridad y adaptándose al contexto específico del entorno educativo. empresa_s garantizará la operatividad y mejora continua de las soluciones existentes:
- Actualización de sistemas de filtrado:
o listas negras/blancas o reglas personalizadas
- Ajuste continuo basado en:
o tasa de falsos positivos/negativos o volumen de spam detectado
- Optimización del rendimiento en entornos de alta carga.
- Integración con sistemas de correo existentes.
implantación y evolución de los sistema propios de EducaMadrid, orientado a detección basada en comportamiento:
- Análisis inteligente de envíos:
o detección de envíos masivos anómalos (especialmente en alumnos)
- Identificación de patrones sospechosos:
o repetición de destinatarios o comportamiento automatizado
- Detección de intentos de suplantación:
o manipulación del campo FROM
- Bloqueo preventivo de envíos a destinos de riesgo:
o listas dinámicas de dominios maliciosos
- Clasificación por perfil de usuario:
o docente / alumno / sistema


Este enfoque permite pasar de un modelo reactivo a uno proactivo basado en comportamiento real. empresa_s realizará campañas periódicas de concienciación:
- Uso de herramientas como GoPhish.
- Diseño de campañas:
o phishing básico o spear phishing o adjuntos maliciosos
- Segmentación por perfiles:
o docentes o personal administrativo o usuarios técnicos
- Simulación de escenarios realistas.
Analisis y reporting:
- Generación de informes detallados:
o tasa de apertura o clics en enlaces o introducción de credenciales
- Evaluación por perfil de usuario.
- Identificación de riesgos y vulnerabilidades.
- Propuesta de medidas correctivas:
o formación o ajustes técnicos Propuesta de mejora hacia un modelo de seguridad y concienciación empresa_s propone evolucionar el sistema hacia un modelo de seguridad adaptativa:
1. Concienciación progresiva. Seguimiento histórico del comportamiento y personalización de
campañas.
2. Mejora de simulaciones. Uso de plantillas avanzadas y métricas de interacción.
3. Coordinación con ciberseguridad. Alineación con políticas y adaptación a amenazas
emergentes.
4. Automatización del sistema. Integración con sistemas de usuarios y ejecución
automatizada de campañas. Valor aportado Estas mejoras permiten evolucionar hacia un sistema de protección frente al spam y amenazas asociadas dinámico, adaptativo y orientado al comportamiento del usuario, reforzando la capacidad de detección ante nuevas técnicas de ataque, mejorando la concienciación de la comunidad educativa y garantizando una mayor seguridad y fiabilidad en el uso del correo electrónico dentro de EducaMadrid. Requisito: II.1.6.5. Mantenimiento de buzones de correo Requerimiento EducaMadrid Actualmente EducaMadrid cuenta con cerca de 2 millones de buzones de correo. Se necesita mantener optimizada la gestión de buzones de correo para la mejora continua del servicio (COR5). Se solicita:
- Mantener los buzones de correo de EducaMadrid.


- Mejorar los procesos de mantenimiento al eliminar la creación del buzón con el alta, y que
esta creación se realice en el primer acceso o cuando reciba el primer correo. La asignación de la ubicación de dichos buzones deberá ser realizada por el portal como hasta ahora.

- Modificar periódicamente dicha asignación para que ésta tenga en cuenta los nuevos
mailboxes y maildirs disponibles para los usuarios, repartiendo la carga entre los diferentes espacios asignados al servicio.

- Gestionar, mejorar y mantener los procesos de creación, recuperación y eliminación de
buzones de correo, así como de los relacionados con el reparto de carga.

- Mejorar y mantener los procesos de alta masiva de buzones de correo.

- Análisis y gestionar las cuentas sin uso o de usuarios borrados, prestando especial
atención a la liberación del espacio ocupado por los mailboxes y al reparto de carga tras el borrado.

Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la gestión de buzones como un sistema distribuido de alto volumen, optimizado para eficiencia operativa, equilibrio de carga y uso racional del almacenamiento. Se implantará un modelo de provisión diferida, eliminando la creación automática de buzones en el alta de usuario y generándolos únicamente en el primer acceso o recepción de correo. Este enfoque reduce significativamente el número de buzones inactivos y optimiza el uso de recursos. empresa_s implantará un modelo de provisión diferida:
- Eliminación de creación de buzones en el alta inicial.
- Generación del buzón únicamente:
o en el primer acceso o o al recibir el primer correo
- Reducción de:
o buzones inactivos o consumo innecesario de almacenamiento Se mejorará el sistema de asignación de buzones mediante:
- Evolución del sistema de asignación gestionado por el portal:
o incorporación de métricas en tiempo real:
- uso de espacio
- carga de I/O
- número de buzones por servidor
- Distribución inteligente de nuevos buzones:
o por capacidad disponible o por nivel de saturación
- Redistribución periódica de carga:
o adaptación a nuevos mailboxes y maildirs Se mantendrán y optimizarán los procesos de:
- Automatización de procesos:
o creación o recuperación o eliminación
- Soporte a altas masivas:
o validación previa


o asignación automática
- Análisis de cuentas sin uso:
o detección de buzones inactivos o liberación controlada de espacio
- Reorganización del almacenamiento tras eliminaciones.
Evolución de la infraestructura:
- Despliegue de nuevos buzones en entornos actualizados (RHEL 10).

- Convivencia controlada con sistemas existentes.

- Evaluación continua de rendimiento y estabilidad.

- Planificación de migración progresiva.

Propuesta de mejora, gestión inteligente y escalable empresa_s propone evolucionar el sistema hacia un modelo inteligente y automatizado:
1. Motor dinámico de asignación. Decisión automática basada en carga real, uso de
almacenamiento y capacidad disponible.
2. Monitorización avanzada. Métricas de ocupación, rendimiento de acceso y alertas ante
desequilibrios.
3. Depuración automatizada. Identificación y eliminación segura de buzones inactivos.
4. Evolución tecnológica. Evaluación continua de sistemas de archivos y planificación de
migraciones. Valor aportado


![Imagen de la página 106](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0106-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0106-imagen-003.png -->
- Arquitectura de correo con agentes de usuario, transferencia y entrega.
- El correo saliente entra autenticado por SMTP en el MTA y el entrante llega por el puerto 25; OpenLDAP aporta usuarios, contraseñas, dominios y alias.
- Rspamd filtra spam, el MDA entrega por LMTP a los buzones y los clientes acceden por IMAPS.
- Solr proporciona indexación y búsqueda de texto completo.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0106-imagen-003.png -->

Estas mejoras permiten disponer de un sistema de gestión de buzones optimizado, automatizado y adaptativo, capaz de distribuir la carga de forma eficiente, maximizar el aprovechamiento del almacenamiento disponible y eliminar de forma controlada los recursos innecesarios, garantizando así la sostenibilidad, el rendimiento y la escalabilidad del servicio de correo de EducaMadrid a gran escala. Requisito: II.1.6.6. Seguridad del sistema de correo Requerimiento EducaMadrid Actualmente EducaMadrid da servicio de correo electrónico a cerca de 2 millones de usuarios sobre una infraestructura compuesta por más de 30 servidores entre servidores de mailbox y aplicativos (COR6). Se solicita:
- Actualizar los servicios manteniendo actualizados los certificados, implementando los
accesos mediante la última versión disponible del protocolo seguro TLS.

- Gestionar, mantener, actualizar y mejorar cualquier elemento del sistema de correo de
forma que se cumplan los requisitos de seguridad impuestos desde el departamento de Ciberseguridad. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la seguridad del sistema de correo de EducaMadrid como un servicio crítico, garantizando la protección de las comunicaciones, el cumplimiento normativo y la resiliencia ante amenazas, en una infraestructura distribuida de más de 30 servidores y cerca de 2 millones de usuarios. Gestión automatizada de certificados digitales :
- Inventario completo de certificados:
o SMTP, IMAP, POP, Webmail
- Renovación automatizada mediante:
o ACME / Certbot u otras soluciones equivalentes
- Validación continua:
o cadena de confianza o expiración o configuración correcta
- Pruebas periódicas de seguridad:
o robustez criptográfica o headers de seguridad Se reforzará el uso de protocolos seguros: o Implementación de TLS 1.2 y 1.3 o Eliminación de versiones y cifrados obsoletos o Configuración de suites criptográficas seguras Se mantendrá el sistema mediante: o Aplicación de parches de seguridad o Hardening de servidores o Control de accesos y autenticación segura Todas las actuaciones se alinearán con los requisitos establecidos por Ciberseguridad:
- Aplicación de directrices del área de Ciberseguridad:
o autenticación o trazabilidad


o cifrado
- Refuerzo de autenticación:
o SASL / LDAP
- Registro de eventos:
o accesos o errores o intentos fallidos

Propuesta de mejora y evolución del servicio empresa_s propone evolucionar el sistema hacia un modelo de seguridad proactiva y automatizada:
1. Gestión centralizada de certificados. Automatización completa del ciclo de vida de
certificados y validación continua.
2. Auditoría periódica de seguridad. Evaluación semestral mediante herramientas
especializadas y generación de informes. Uso de herramientas:
- OpenVAS

- Lynis

3. Sistema de detección de configuraciones inseguras. Alertas automáticas ante desviaciones
en configuración o riesgos potenciales.
4. Refuerzo de autenticación. Evolución hacia modelos de autenticación más robustos en
accesos críticos. Valor aportado Estas mejoras permiten evolucionar el sistema de correo hacia un modelo de seguridad preventiva y automatizada, reduciendo riesgos operativos, evitando incidencias por configuraciones inseguras y garantizando el cumplimiento continuo de los estándares de ciberseguridad exigidos en el entorno EducaMadrid. Requisito: II.1.6.7. Actualización de la infraestructura de correo Requerimiento EducaMadrid


![Imagen de la página 108](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0108-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0108-imagen-003.png -->
- Diagrama de intercambio seguro de correo entre dos dominios y un servidor intermedio propio.
- Los servidores se comunican mediante SMTP cifrado con SSL.
- Un cliente como Thunderbird accede al servidor propio mediante IMAP también cifrado con SSL.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0108-imagen-003.png -->

Actualmente EducaMadrid da servicio de correo electrónico a cerca de 2 millones de usuarios sobre una infraestructura compuesta por más de 30 servidores entre servidores de mailbox y aplicativos (COR7). Se solicita:
- Actualizar y mantener los servidores MX Gateway para que se ejecuten en la última versión
disponible de RHEL. Esta labor requerirá la migración del entorno a versiones más actuales y soportadas del aplicativo.

- Actualizar, migrar y mantener los servidores Client Access Server (CAS) para que se
ejecuten en la última versión disponible de RHEL.

- Actualizar, migrar y mantener todos los servidores Mailbox server para que se ejecuten en
la última versión disponible de RHEL.

- Aplicar los parches y correcciones requeridas desde el departamento de Ciberseguridad
para resolver las vulnerabilidades críticas detectadas. Las vulnerabilidades no críticas se acumularán para gestionarlas junto con las actualizaciones de versión de los aplicativos relacionados con el servicio.

Las labores de actualización de versiones y corrección de vulnerabilidades no críticas relacionadas con este servicio se realizarán al menos una vez al año aprovechando periodos no lectivos. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la actualización de la infraestructura como un proceso planificado de modernización tecnológica, garantizando la continuidad del servicio y la compatibilidad con los sistemas existentes. Se realizará la migración progresiva:
- Migración progresiva a la última versión soportada de RHEL:
o planificación por nodos o minimización de impacto
- Validación de servicios críticos:
o SMTP relay o autenticación
###### o SPF/DKIM/DMARC
- Aplicación prioritaria de parches de seguridad.
- Pruebas de rendimiento y estabilidad tras migración.
Actualización de servidores CAS y Mailbox.
- Migración controlada de:
o Client Access Servers (CAS) o Mailbox Servers
- Optimización post-migración:
o rendimiento de I/O o acceso concurrente
- Revisión de servicios asociados:
o monitorización o backups o logging Gestión estructurada de vulnerabilidades:
- Aplicación inmediata de vulnerabilidades críticas.


- Consolidación de vulnerabilidades no críticas:
o despliegue en ventanas planificadas
- Uso de herramientas de análisis:
o OpenVAS o Nessus
- Auditoría de configuración tras cada intervención.
Planificación de actualizaciones:
- Definición de ciclos de actualización:
o al menos una vez al año
- Ejecución en periodos no lectivos:
o Verano o Navidad o Semana Santa
- Coordinación con el equipo de EducaMadrid.
Propuesta de mejora orientada a la seguridad, estabilidad y escalabilidad empresa_s propone evolucionar la infraestructura hacia un modelo automatizado y resiliente:
1. Automatización de operaciones. Uso de herramientas de configuración para despliegue y
mantenimiento.
2. Gestión continua de vulnerabilidades. Integración con sistemas de análisis y seguimiento
de incidencias.
3. Planificación estructurada. Calendario anual de mantenimiento y actualización.
4. Validación continua. Pruebas automatizadas tras cada intervención.
Valor aportado Estas mejoras permiten transformar la infraestructura de correo en un entorno moderno, automatizado y resiliente, reduciendo riesgos asociados a obsolescencia tecnológica, mejorando la capacidad de respuesta ante vulnerabilidades y garantizando la continuidad del servicio en escenarios de alta demanda. Requisito: II.1.6.8. Escalado de servidores Mailbox Requerimiento EducaMadrid Actualmente EducaMadrid da servicio de correo electrónico a cerca de 2 millones de usuarios sobre una infraestructura compuesta por más de 30 servidores entre servidores de mailbox y aplicativos (COR8). Se solicita:

- Adecuar el número de servidores Mailbox server, ampliando, manteniendo o reduciendo el
número actual, en unidades suficientes para que la carga de los servidores en producción esté situada en torno a un 25%. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el dimensionamiento de la infraestructura de Mailbox como un proceso continuo de capacity planning, balanceo de carga y escalabilidad controlada, con el objetivo de mantener la carga operativa de los nodos en torno al 25%. Se realizará un análisis continuo de:
- Auditoría completa de los servidores Mailbox:
o CPU, RAM, I/O, sesiones concurrentes


- Análisis de patrones de uso:
o picos lectivos o actividad diaria
- Modelado predictivo de crecimiento:
o evolución de usuarios o incremento de uso por servicio
- Definición de baseline de carga objetivo (≤25%).
Ampliación controlada de infraestructura:
- Incorporación de nuevos nodos Mailbox:
o despliegue homogéneo o configuración estandarizada
- Integración en la arquitectura existente:
o autenticación o backup o monitorización
- Minimización del impacto en producción.
Redistribución inteligente de buzones:
- Balanceo basado en:
o capacidad real de cada nodo o carga actual
- Uso de algoritmos de distribución:
o round- robin ponderado o hash por usuario
- Migración controlada de buzones:
o sin impacto en usuario final
- Ajuste continuo tras redistribución.
Validación y control de rendimiento:
- Pruebas de carga post-ampliación.
- Monitorización intensiva:
o detección de nodos saturados
- Ajuste fino del reparto de carga.
- Verificación del cumplimiento del objetivo del 25%.
Propuesta de mejora , rendimiento y balanceo dinámico empresa_s propone evolucionar el sistema hacia un modelo de escalado inteligente:
1. Monitorización en tiempo real. Métricas por nodo:
- CPU, memoria, I/O
- número de buzones activos
2. Alertas ante desviaciones del 25%.
3. Balanceo automatizado. Redistribución dinámica de buzones en función de carga.
4. Escalabilidad planificada. Definición de umbrales que activen ampliaciones automáticas.
5. Optimización continua. Ajuste periódico del reparto de carga.


Valor aportado Estas mejoras permiten garantizar una infraestructura de correo equilibrada, eficiente y preparada para el crecimiento, evitando situaciones de saturación, optimizando el uso de recursos y asegurando un rendimiento homogéneo para todos los usuarios de EducaMadrid. Requisito: II.1.6.9. Módulo de inyección directa de correo Requerimiento EducaMadrid EducaMadrid solicita disponer de un módulo receptor de inyección directa orientado a la deposición de entidades de mensaje completas en la infraestructura de spool del transporte de correo existente, coexistiendo con los endpoints tradicionales de sesión SMTP, sin sustituirlos ni alterar su comportamiento operativo (COR9). Se solicita:
- Integrar el Módulo de forma transparente con la arquitectura de transporte y recepción de
correo actualmente operativa, coexistiendo con los componentes desplegados sin interferir en su lógica transaccional ni requerir su sustitución.

- Garantizar que el Módulo actúe como complemento de inyección dentro del dominio de
transporte, compartiendo la infraestructura de cola y los mecanismos de persistencia existentes, sin modificar las rutas tradicionales de sesión ni los procesos activos de recepción.

- Mantener la definición funcional del Módulo como tubería de ingestión postransaccional
para la materialización persistente de entidades de mensaje completas en la capa de spool, preservando la integridad sintáctica y semántica del encabezado SMTP de origen.

- Garantizar la generación de objetos persistentes de spool con los metadatos obligatorios
definidos, sin realizar entrega directa a buzones. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la implementación del módulo de inyección directa como una extensión nativa del dominio de transporte, respetando estrictamente el modelo solicitado: inyección postransaccional en spool sin alterar el flujo SMTP existente. Enfoque técnico de la solución: La solución propuesta se basa en la incorporación de un módulo de ingestión directa compatible con el protocolo Quick Mail Queueing (QMQP), mediante el componente qmqpd. Página 112 de 239


![Imagen de la página 112](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0112-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0112-imagen-003.png -->
- Esquema de escalado horizontal de servidores.
- Un cliente distribuye sus solicitudes entre cinco servidores equivalentes dentro de un grupo.
- La flecha de escalado indica que la capacidad aumenta añadiendo más nodos.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0112-imagen-003.png -->

Este módulo permite la transferencia de mensajes completos como entidades atómicas , evitando la sobrecarga del protocolo SMTP en entornos de alto volumen. Funcionamiento operativo:
- Recepción de mensajes completos:
o cabeceras o cuerpo o destinatarios
- Transacción única:
o sin secuencia SMTP (EHLO, MAIL FROM, RCPT TO…)
- Conversión directa a objeto de spool:
o escritura atómica en cola
- Consumo por procesos existentes:
o sin modificación de lógica de entrega Funcionamiento operativo:
- Recepción de mensajes completos:
o cabeceras o cuerpo o destinatarios
- Transacción única:
o sin secuencia SMTP (EHLO, MAIL FROM, RCPT TO…)
- Conversión directa a objeto de spool:
o escritura atómica en cola
- Consumo por procesos existentes:
o sin modificación de lógica de entrega Integración con la arquitectura existente: La solución cumple estrictamente los requisitos del pliego:
- Coexistencia con listeners SMTP:
o sin interferencias
- Integración directa con el sistema de spool:
o sin alterar rutas de transporte
- No sustitución de componentes existentes:
o modelo no intrusivo
- Despliegue reversible:
o activación/desactivación sin impacto Cumplimiento funcional del módulo:
- Ingestión postransaccional:
o deposición directa en spool
- Persistencia completa del mensaje:
o integridad sintáctica y semántica
- Generación de metadatos obligatorios:
o conforme al sistema existente
- No entrega directa a buzones:
o uso exclusivo de la cola de transporte Arquitectura de inyección directa en spool:


Propuesta de mejora y evolución del servicio Ventajas técnicas de la solución:
- Reducción de latencia: eliminación de negociación SMTP.

- Alta eficiencia: menor consumo de CPU y sockets.

- Escalabilidad: múltiples instancias en paralelo.

- Fiabilidad: persistencia síncrona en spool.

- Compatibilidad total: formato de cola inalterado.


![Imagen de la página 114](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0114-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0114-imagen-003.png -->
- Arquitectura de un webmail escalable con balanceador, servidores web, colas y almacenamiento especializado.
- Los mensajes salientes pasan a una cola, luego a SMTP con reintentos y comprobaciones de virus y spam antes de internet; los fallos se separan en una cola de error.
- La capa de almacenamiento distingue metadatos, índice de búsqueda, adjuntos en objetos y caché para el correo reciente.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0114-imagen-003.png -->

Mantenimiento y supervisión:
- Integración con sistemas existentes de monitorización.
- Supervisión basada en:
o estado de cola o uso de disco
- Sin dependencias externas adicionales.
- Mantenimiento mínimo.
Requisito: II.1.6.10. Mantenimiento y soporte del módulo de inyección directa Requerimiento EducaMadrid EducaMadrid necesita que se realice un mantenimiento y soporte especializado del módulo receptor de inyección directa que garantice el cumplimiento de los requisitos técnicos, de rendimiento y de aceptación establecidos, así como su coexistencia estable con los sistemas de correo existentes (COR10). Se solicita:
- Cumplir y mantener los requisitos técnicos mínimos del sistema, incluyendo la interfaz de
recepción TCP con opción de cifrado, la escritura atómica y durable del spool, los mecanismos configurables de back-pressure, la escalabilidad en múltiples instancias y la integración con los sistemas de observabilidad existentes.

- Garantizar que el Módulo actúe como complemento de inyección dentro del dominio de
transporte, compartiendo la infraestructura de cola y los mecanismos de persistencia existentes, sin modificar las rutas tradicionales de sesión ni los procesos activos de recepción.

- Realizar las pruebas de validación y aceptación necesarias, incluyendo pruebas de
generación correcta del spool, compatibilidad con los procesos existentes de entrega, pruebas de carga, resiliencia y coexistencia con los listeners SMTP activos.


![Imagen de la página 115](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0115-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0115-imagen-003.png -->
- Flujo básico de entrega de correo mediante SMTP.
- El remitente usa un agente de usuario que deposita el mensaje en una cola y lo entrega a un agente de transferencia cliente.
- Una conexión TCP por el puerto 25 intercambia órdenes, respuestas y mensajes con el agente de transferencia servidor, que los coloca en buzones para el destinatario.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0115-imagen-003.png -->

- Garantizar que el despliegue, actualización, parada o retirada del módulo sea reversible y
no tenga impacto en los servicios de recepción de correo existentes.

- Gestionar las herramientas de administración del módulo, incluyendo inspección, reintento
y gestión de cola, así como la atención y resolución de incidencias relacionadas con el software y los servicios implicados.

- Mantener actualizada la documentación técnica, los procedimientos de operación, los
scripts asociados y realizar la transferencia de conocimiento necesaria para la correcta explotación del sistema.

Propuesta técnica de empresa_s Los especialistas de empresa_s proporcionarán un servicio integral de mantenimiento y soporte del módulo de inyección directa implantado, garantizando su estabilidad operativa, rendimiento sostenido y plena integración con la infraestructura de transporte existente, en continuidad con la solución basada en QMQP. Mantenimiento técnico del módulo:
- Supervisión del servicio qmqpd:
o disponibilidad del socket TCP o estado de procesos
- Validación continua de:
o escritura atómica en spool o integridad de mensajes
- Revisión de configuración:
o parámetros de back-pressure o concurrencia de conexiones
- Actualización controlada del componente:
o sin impacto en producción Garantía de integración y coexistencia:
- Verificación continua de:
o coexistencia con SMTP o no interferencia en rutas de transporte
- Validación de compatibilidad con:
o sistema de spool o procesos de entrega existentes
- Control de integridad del flujo de mensajes:
o desde ingestión hasta entrega Pruebas de validación y aceptación: empresa_s ejecutará un conjunto estructurado de pruebas:
- Validación funcional:
o correcta generación de objetos de spool
- Pruebas de carga:
o volumen de mensajes concurrentes
- Pruebas de resiliencia:
o comportamiento ante fallos
- Pruebas de coexistencia:
o operación paralela con SMTP Flujo operativo del módulo:


Operación, administración y soporte:
- Gestión de cola:
o inspección de mensajes o reintentos
- Análisis de incidencias:
o fallos de ingestión o errores de spool
- Monitorización integrada:
o métricas de ingestión o latencia
- Integración con herramientas existentes de observabilidad.
Propuesta de mejora y evolución del servicio Reversibilidad y despliegue controlado:
- Garantía de despliegue no intrusivo: activación progresiva

- Capacidad de parada inmediata: sin impacto en SMTP

- Procedimientos de rollback definidos.

- Validación post-cambios.
Documentación y transferencia de conocimientos:
- Documentación técnica:
o arquitectura o configuración
- Procedimientos operativos:
o despliegue o mantenimiento
- Scripts asociados:
o automatización
- Formación al equipo técnico de EducaMadrid .
##### APARTADO: SISTEMA OPERATIVO MAX (MAX)
Requisito: II.1.7.1. Mantenimiento y actualización de MAX de forma presencial en centros de forma regular Requerimiento EducaMadrid


![Imagen de la página 117](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0117-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0117-imagen-003.png -->
- Flujo de envío de correo mediante MailerQ y colas de mensajes.
- Una aplicación envía correo normal por SMTP; MailerQ lo transforma en JSON y lo coloca en una cola de entrada.
- Un script consume, procesa y publica mensajes en una cola de salida, que MailerQ vuelve a consumir para enviarlos a internet por SMTP.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0117-imagen-003.png -->

Se necesita llevar la distribución MAX a los distintos centros educativos (MAX1). Con este fin se solicita:
- Realizar tareas presenciales en los centros Educativos para el mantenimiento y
actualización de las distribuciones Oficiales Soportadas del Sistema Operativo MAX de la Comunidad de Madrid.

- Configurar los diferentes tipos de periféricos adquiridos por el centro siempre y cuando
cuenten con soporte para la distribución Linux en la que se basa MAX. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el mantenimiento y actualización presencial de las distribuciones MAX como un servicio estructurado, orientado a garantizar la homogeneidad de los entornos, la compatibilidad hardware y la sostenibilidad operativa del parque tecnológico de los centros educativos. empresa_s definirá un modelo de intervención presencial planificado, basado en:
- Priorización de centros:
o Por criticidad. o Por estado de versiones. o Por antigüedad del hardware.
- Planificación de visitas:
o Calendario coordinado con los centros. o Agrupación por zonas geográficas. o Optimización de desplazamientos. Durante las actuaciones presenciales, empresa_s realizará el mantenimiento completo de las distribuciones MAX soportadas:
- Actualización del sistema operativo:
o Migraciones entre versiones soportadas. o Aplicación de parches de seguridad. o Validación de compatibilidad tras actualización.
- Adaptación a hardware existente:
o Ajuste de configuraciones según recursos del equipo. o Optimización de rendimiento en equipos antiguos. o Selección de perfiles adecuados (full/lite). En relación con los periféricos, empresa_s aplicará un enfoque de compatibilidad controlada:
- Identificación de dispositivos:
o Impresoras. o Pizarras digitales. o Tablets. o Dispositivos USB educativos.
- Validación de compatibilidad con MAX:
o Uso de drivers oficiales o comunitarios. o Evaluación de soporte en kernel/Linux.
- Configuración y puesta en marcha:
o Instalación de controladores. o Integración con aplicaciones educativas. o Validación funcional en entorno real. Además, se realizará una validación completa del entorno tras cada intervención:
- Verificación de arranque del sistema.
- Validación de acceso de usuario.


- Comprobación de conectividad.
- Pruebas básicas de uso en aula.
empresa_s documentará cada intervención realizada:
- Estado inicial del equipo.
- Acciones ejecutadas.
- Versiones instaladas.
- Problemas detectados.
- Recomendaciones futuras.
Propuesta de mejora , estandarización y evolución del servicio empresa_s propone evolucionar el servicio hacia un modelo industrializado y escalable:
1. Modelo de imagen base estandarizada MAX
- Definición de imágenes certificadas por tipo de hardware.
- Reducción de tiempos de intervención en centros.
2. Sistema de diagnóstico previo remoto
- Análisis antes de la visita presencial.
- Identificación de necesidades reales.
- Preparación anticipada de soluciones.
3. Catálogo de compatibilidad de dispositivos
- Base de conocimiento de periféricos validados.
- Reducción de incidencias en instalación.
4. Automatización de configuraciones
- Scripts de despliegue de drivers y configuraciones.
- Homogeneización de entornos.
5. Informe técnico por centro
- Estado global del parque.
- Recomendaciones de renovación o mejora.
- Plan de evolución tecnológica.
Valor aportado Estas actuaciones permiten transformar el mantenimiento presencial en un servicio estructurado, predecible y eficiente, reduciendo tiempos de intervención, mejorando la compatibilidad de dispositivos y asegurando una experiencia homogénea para los usuarios en todos los centros educativos. Requisito: II.1.7.2. Mantenimiento y actualización del servidor MAX para el desarrollo de distribuciones Requerimiento EducaMadrid
A) Pr Actualmente MAX cuenta con un servidor de creación de distribuciones MAX basado en
Debian. En él se realiza la compilación de las aplicaciones nuevas y actualizadas (MAX2). Se solicita:
- Realizar el mantenimiento del servidor legacy MAX usado para versiones anteriores. Este
servidor es un servidor Debian.

- Resolver las dependencias necesarias para el mantenimiento de las aplicaciones legadas.


- Realizar el mantenimiento del servidor MAX usado para desarrollar la versión actual, así
como las posteriores. Este servidor es un servidor Debian. También, se mantendrán las dependencias experimentales para las aplicaciones más recientes y para aquellas que se encuentran en desarrollo.

- Adaptar y optimizar los servidores sobre los que se desarrollan las nuevas distribuciones
de MAX para que dejen de depender de Ubuntu (debido a la nueva política de licenciamiento de Canonical a través de Ubuntu Pro), de forma que las nuevas versiones de MAX dependan de otras distribuciones de Software Libre.

Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el mantenimiento y evolución de la infraestructura de generación de distribuciones MAX como un sistema crítico de construcción, orientado a garantizar la estabilidad de versiones actuales, la compatibilidad de aplicaciones y la sostenibilidad tecnológica futura del ecosistema MAX. empresa_s gestionará de forma diferenciada los entornos existentes:
- Entorno legacy:
o Mantenimiento del servidor Debian utilizado para versiones anteriores. o Resolución de dependencias obsoletas. o Adaptación de paquetes legacy para mantener compatibilidad.
- Entorno de desarrollo actual:
o Mantenimiento del servidor principal de construcción. o Gestión de dependencias estables y experimentales. o Preparación para nuevas versiones de MAX. Se realizará una gestión avanzada de dependencias:
- Control de versiones de paquetes:
o Identificación de dependencias críticas. o Fijación de versiones estables.
- Resolución de conflictos:
o Adaptación de librerías incompatibles. o Recopilación de paquetes si es necesario.
- Separación de entornos:
o Stable. o Testing. o Experimental. empresa_s implantará un modelo estructurado de construcción de distribuciones:
- Automatización del proceso de build:
o Scripts reproducibles. o Generación de imágenes ISO. o Validación automática de builds.
- Gestión de repositorios internos:
o Repositorios Debian propios para MAX. o Control de paquetes adaptados. o Versionado de builds. En relación con la transición tecnológica, empresa_s realizará la evolución progresiva hacia un modelo independiente de Ubuntu:
- Análisis de dependencias actuales con Canonical.
- Migración progresiva a base Debian pura:
o Sustitución de repositorios Ubuntu. o Validación de paquetes equivalentes.


- Adaptación del sistema de construcción:
o Eliminación de dependencias de Ubuntu Pro. o Garantía de continuidad funcional. Se garantizará la estabilidad del entorno mediante:
- Aplicación de parches de seguridad.
- Actualización controlada de paquetes esenciales.
- Monitorización del sistema de build.
- Control de errores en compilaciones.
Propuesta de mejora , automatización y evolución del sistema de construcción empresa_s propone evolucionar la plataforma hacia un modelo industrializado de generación de distribuciones:
1. Pipeline automatizado de construcción (CI/CD)
- Generación automática de builds.
- Validación continua de paquetes.
- Reducción de errores manuales.
2. Entornos aislados de construcción
- Uso de contenedores para builds reproducibles.
- Aislamiento de dependencias.
- Mejora de estabilidad.
3. Sistema de versionado y trazabilidad
- Control completo de versiones de distribuciones.
- Histórico de builds.
- Identificación de cambios.
4. Repositorios propios optimizados
- Gestión centralizada de paquetes MAX.
- Reducción de dependencias externas.
- Mayor control sobre el ciclo de vida del software.
5. Plataforma preparada para evolución futura
- Adaptación a nuevas distribuciones base.
- Flexibilidad ante cambios tecnológicos.
- Reducción de dependencia de terceros.
Valor aportado Estas actuaciones permiten transformar el entorno de generación de MAX en una plataforma robusta, automatizada y sostenible, reduciendo riesgos derivados de dependencias externas, mejorando la calidad de las distribuciones y facilitando su evolución futura. Requisito: II.1.7.3. Mantenimiento de aplicaciones basadas en MAX Requerimiento EducaMadrid La Consejería de Digitalización lanza una versión de MAX aproximadamente una vez al año (MAX3). Por ello se solicita:
- Mantener la configuración específica y el parcheado de aplicaciones.

- Para el mantenimiento de las aplicaciones instaladas en las distribuciones MAX es
necesario que se descargue el código fuente y se compile sobre la distribución deseada con el propósito de satisfacer el funcionamiento de las aplicaciones.


Esta tarea se realizará periódicamente. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el mantenimiento de aplicaciones en MAX como un proceso continuo de aseguramiento de compatibilidad, seguridad y estabilidad, garantizando que todas las aplicaciones integradas en la distribución funcionen correctamente sobre cada versión publicada. empresa_s establecerá un modelo estructurado de mantenimiento de aplicaciones basado en el control completo del ciclo de vida del software:
- Gestión del código fuente:
o Descarga y control de versiones de aplicaciones. o Identificación de cambios relevantes en nuevas versiones. o Evaluación de compatibilidad con la distribución MAX.
- Proceso de compilación adaptado:
o Compilación de aplicaciones sobre la distribución objetivo. o Ajuste de dependencias específicas de MAX. o Adaptación de configuraciones necesarias para su correcto funcionamiento.
- Gestión de parcheado:
o Aplicación de parches de seguridad. o Corrección de incompatibilidades. o Adaptación de aplicaciones no mantenidas por sus desarrolladores originales. empresa_s realizará auditorías periódicas del repositorio de aplicaciones:
- Identificación de:
o Aplicaciones obsoletas. o Software sin mantenimiento activo. o Componentes con vulnerabilidades conocidas.
- Evaluación de alternativas:
o Sustitución por soluciones activas. o Validación de compatibilidad funcional. Se garantizará la estabilidad del ecosistema mediante:
- Validación funcional de aplicaciones:
o Pruebas de ejecución. o Verificación de integración con el sistema.
- Control de dependencias:
o Resolución de conflictos entre paquetes. o Aseguramiento de coherencia en el sistema. Propuesta de mejora, calidad y control del software empresa_s propone evolucionar el mantenimiento de aplicaciones hacia un modelo de control de calidad avanzado:
1. Entorno de validación previo (preproducción)
- Testeo de aplicaciones antes de su incorporación.
- Reducción de errores en producción.
2. Sistema de certificación de aplicaciones MAX
- Validación de compatibilidad.
- Verificación de seguridad.
- Control de calidad del software incluido.
3. Monitorización del estado del software
- Seguimiento de vulnerabilidades.
- Control de versiones obsoletas.


- Alertas ante riesgos de seguridad.
4. Catálogo controlado de aplicaciones
- Listado oficial de software validado.
- Eliminación de aplicaciones no mantenidas.
- Mejora de la coherencia del sistema.
5. Automatización del proceso de compilación
- Reducción de errores manuales.
- Mejora de tiempos de generación de paquetes.
- Homogeneidad en builds.
Valor aportado Estas actuaciones permiten garantizar un ecosistema de aplicaciones estable, seguro y actualizado, reduciendo riesgos derivados de software obsoleto, mejorando la calidad de las distribuciones MAX y asegurando su correcto funcionamiento en los entornos educativos. Requisito: II.1.7.4. Lanzamiento de distribuciones de MAX “Full Equip” anualmente Requerimiento EducaMadrid La Consejería de Digitalización lanza anualmente una nueva versión de MAX o hasta dos actualizaciones de versión (MAX4). Para cada nuevo lanzamiento, se pide:
- La actualización y adaptación de la nueva versión de MAX.

- Para cada versión lanzada, hay que realizar el mantenimiento periódico, con configuración,
actualización de las aplicaciones externas, y mantenimiento y supervisión del parcheado de la distribución. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el lanzamiento de las distribuciones MAX “Full Equip” como un proceso controlado de ingeniería de software, orientado a garantizar la calidad, estabilidad y coherencia funcional de cada nueva versión distribuida en los centros educativos. empresa_s estructurará el ciclo de vida de cada versión en fases claramente definidas:
- Fase de definición:
o Identificación de requisitos funcionales. o Selección de aplicaciones incluidas. o Definición de configuraciones base del sistema.
- Fase de construcción:
o Generación de la distribución sobre la base tecnológica definida. o Integración de paquetes propios y externos. o Configuración del entorno educativo.
- Fase de validación:
o Pruebas funcionales completas:
- Arranque del sistema.
- Instalación en distintos entornos.
- Ejecución de aplicaciones clave.
o Validación de compatibilidad:
- Hardware.
- Periféricos habituales en centros.
empresa_s implantará un modelo de versiones progresivas:


- Versiones internas: Builds técnicos para validación interna.
- Versiones alfa: Pruebas iniciales de funcionalidad.
- Versiones beta: Validación ampliada en entornos controlados.
- Versión final: Distribución oficial.
Tras el lanzamiento, se realizará mantenimiento evolutivo continuo:
- Actualización de paquetes:
o Aplicación de parches de seguridad. o Actualización de aplicaciones incluidas.
- Corrección de incidencias detectadas:
o Análisis de errores reportados. o Publicación de actualizaciones correctivas.
- Supervisión del comportamiento en producción.
Se garantizará la compatibilidad entre versiones:
- Control de migraciones:
o Actualización desde versiones anteriores. o Validación de configuraciones existentes.
- Mantenimiento de coherencia en el entorno:
o Evitar incompatibilidades entre versiones. Propuesta de mejora, calidad y evolución del ciclo de versiones empresa_s propone evolucionar el modelo de lanzamiento hacia un sistema industrializado y controlado:
1. Pipeline automatizado de generación de distribuciones
- Construcción automática de versiones.
- Validación continua.
- Reducción de errores manuales.
2. Sistema de testing estructurado
- Pruebas automatizadas.
- Validación funcional completa.
- Mejora de la calidad final.
3. Versionado controlado y trazabilidad
- Registro de cambios por versión.
- Histórico de builds.
- Identificación de incidencias por versión.
4. Modelo de actualizaciones incremental
- Publicación periódica de mejoras.
- Reducción de necesidad de reinstalaciones completas.
5. Mejora continua del entorno educativo
- Adaptación a nuevas necesidades docentes.
- Incorporación progresiva de nuevas herramientas.


![Imagen de la página 124](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0124-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0124-imagen-003.png -->
- Esquema de ramas y versiones de software entre master y develop.
- La rama master crea etiquetas 12.0.0 y 12.1.1 que regeneran entornos asociados.
- Develop contiene una línea MAX 12.1, una rama release para 12.1.1 y una rama de funcionalidad para MAX 12.2.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0124-imagen-003.png -->

Valor aportado Estas actuaciones permiten transformar el lanzamiento de MAX en un proceso controlado, repetible y de alta calidad, asegurando distribuciones estables, compatibles y adaptadas a las necesidades reales de los centros educativos, reduciendo incidencias tras su despliegue. Requisito: II.1.7.5. Lanzamiento de distribuciones de “MAX lite” y/o “MAX gestión” Requerimiento EducaMadrid Históricamente, EducaMadrid ha distribuido una distribución ligera de MAX destinada a equipos antiguos y de bajo consumo. También se dispone de opciones para incluir aplicaciones específicas dirigidas a los equipos directivos y de gestión TIC de los centros (MAX5). Para ello se solicita:
- Mantener, actualizar y mejorar las distribuciones alternativas que EducaMadrid desea
poner a disposición de sus usuarios, ya sea para facilitar su ejecución en equipos menos potentes y sin conexión a Internet, o ya sea para incorporar aplicaciones específicas de gestión que ayuden a los coordinadores TIC o a los miembros de los equipos directivos de los centros educativos de la Comunidad de Madrid, o para cualquier otro cometido que se defina.

- Dado que actualmente el foco está sobre la opción de gestión, habrá que realizar las tareas
necesarias para mantener, actualizar, mejorar y parchear la distribución de “MAX Gestión” de forma que se genera una nueva versión y hasta dos actualizaciones de la misma anualmente.

Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el mantenimiento y evolución de las distribuciones alternativas de MAX como soluciones especializadas dentro del ecosistema educativo, orientadas a cubrir escenarios específicos como entornos con hardware limitado o necesidades de gestión avanzada en centros. empresa_s diferenciará claramente las dos líneas de distribución:
- MAX Lite:
o Orientada a equipos con recursos limitados. o Optimizada para bajo consumo de CPU y memoria. o Selección de aplicaciones ligeras.
- MAX Gestión:
o Orientada a equipos directivos y personal TIC. o Integración de herramientas de gestión, administración y seguridad. o Enfoque en control y operación del entorno. Para MAX Lite, empresa_s realizará:
- Optimización del sistema:
o Reducción de servicios en segundo plano. o Selección de entornos gráficos ligeros. o Minimización del consumo de recursos.
- Adaptación a hardware antiguo:
o Ajustes de kernel y drivers. o Configuración específica para equipos legacy.
- Validación de funcionamiento:
o Pruebas en entornos reales con hardware limitado. Para MAX Gestión, empresa_s realizará:


- Integración de herramientas específicas:
o Administración de sistemas. o Gestión de usuarios. o Herramientas de diagnóstico.
- Refuerzo de seguridad:
o Configuración de políticas de acceso. o Endurecimiento del sistema.
- Adaptación a necesidades del cliente:
o Incorporación de herramientas solicitadas. o Configuración personalizada. empresa_s garantizará el mantenimiento continuo de ambas distribuciones:
- Actualización de paquetes:
o Aplicación de parches de seguridad. o Actualización de aplicaciones.
- Corrección de incidencias:
o Análisis de problemas detectados. o Publicación de mejoras.
- Validación de estabilidad:
o Pruebas periódicas de funcionamiento. Se gestionará el ciclo de versiones:
- Generación de nuevas versiones anuales.
- Publicación de actualizaciones intermedias.
- Control de compatibilidad entre versiones.
Propuesta de mejora, especialización y optimización de distribuciones empresa_s propone evolucionar estas distribuciones hacia un modelo más adaptado y eficiente:
1. Perfiles de uso definidos
- Distribuciones adaptadas a distintos escenarios:
o Aula. o Gestión. o Equipos antiguos.
2. Modularidad del sistema
- Instalación por componentes.
- Flexibilidad en despliegue.
- Adaptación a necesidades concretas.
3. Optimización avanzada de rendimiento
- Ajustes específicos por tipo de hardware.
- Mejora de tiempos de arranque.
- Reducción de consumo de recursos.
4. Integración de herramientas de gestión
- Mejora del control de equipos.
- Facilidades para equipos TIC.
- Centralización de operaciones.
5. Evolución controlada del catálogo de software
- Selección de aplicaciones adecuadas a cada perfil.
- Eliminación de software innecesario.
- Mejora de la experiencia de usuario.


Valor aportado Estas actuaciones permiten disponer de distribuciones MAX adaptadas a distintos escenarios reales, mejorando el rendimiento en equipos antiguos, facilitando la gestión de los centros y asegurando un uso más eficiente y controlado del sistema operativo. Requisito: II.1.7.6. Integración de aplicaciones externas a los repositorios oficiales Requerimiento EducaMadrid EducaMadrid cuenta con una serie de servicios y aplicaciones en la nube. Se necesita una integración de estos servicios con las aplicaciones de escritorio de MAX (MAX6). Para ello se solicita:
- Mantener, actualizar y mejorar la integración de aplicaciones externas que cumplan con
las necesidades de los profesores en los centros educativos.

- Realizar la integración de las aplicaciones requeridas por la distribución para cumplir con
las demandas del servicio ofrecido por EducaMadrid y asegurarse de que puedan ser distribuidas por los repositorios oficiales de MAX.

Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la integración de aplicaciones externas en el ecosistema MAX como un proceso controlado de adaptación, validación y distribución, garantizando su compatibilidad con la distribución, su seguridad y su correcta integración con los servicios de EducaMadrid. empresa_s implantará un modelo estructurado para la incorporación de software externo:
- Análisis previo de aplicaciones:
o Evaluación funcional de la herramienta. o Validación de compatibilidad con la distribución MAX. o Identificación de dependencias necesarias.
- Revisión de seguridad:
o Análisis de vulnerabilidades conocidas. o Validación del origen del software. o Cumplimiento de estándares de seguridad (ENS). Se realizará la adaptación técnica de las aplicaciones:
- Reconstrucción de paquetes:
o Compilación desde código fuente cuando sea necesario. o Adaptación a la versión de la distribución.
- Resolución de dependencias:


![Imagen de la página 127](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0127-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0127-imagen-003.png -->
- Imagen de presentación de la distribución MAX versión 12.5 de EducaMadrid.
- El logotipo MAX aparece sobre un paisaje rocoso oscuro y encima de la marca institucional EducaMadrid.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0127-imagen-003.png -->

o Inclusión de librerías necesarias. o Ajuste de versiones para evitar conflictos.
- Integración con el sistema:
o Configuración de instalación. o Integración con menús, accesos y entorno de usuario. empresa_s gestionará la distribución a través de los repositorios MAX:
- Empaquetado en formato Debian (.deb):
o Adaptado a estándares de la distribución.
- Publicación en repositorios:
o Control de versiones. o Validación previa a despliegue.
- Mantenimiento de paquetes:
o Actualizaciones periódicas. o Corrección de incidencias. Se garantizará la compatibilidad con los servicios de EducaMadrid:
- Integración con aplicaciones en la nube.
- Validación de autenticación y acceso.
- Aseguramiento de funcionamiento conjunto con el resto del sistema.
Propuesta de mejora , control y seguridad del software integrado empresa_s propone evolucionar la integración de aplicaciones hacia un modelo gobernado y seguro:
1. Catálogo controlado de aplicaciones externas
- Listado oficial de aplicaciones autorizadas.
- Clasificación por tipo de uso.
- Control de versiones.
2. Sistema de validación previa
- Entorno de pruebas para nuevas aplicaciones.
- Verificación funcional y de seguridad.
- Reducción de incidencias en producción.
3. Monitorización de vulnerabilidades
- Seguimiento de CVEs asociados a aplicaciones.
- Actualización proactiva ante riesgos.
4. Automatización del empaquetado
- Generación automática de paquetes Debian.
- Reducción de errores manuales.
- Homogeneidad en despliegue.
5. Integración avanzada con el ecosistema EducaMadrid
- Mejora de la interoperabilidad con servicios cloud.
- Adaptación a necesidades educativas.
- Evolución del catálogo de software.
Valor aportado Estas actuaciones permiten disponer de un sistema controlado, seguro y eficiente de integración de aplicaciones externas, garantizando su compatibilidad con MAX, reduciendo riesgos de seguridad y asegurando una experiencia homogénea para los usuarios. Requisito: II.1.7.7. Mantenimiento y mejora del servidor de gestión de accesos remotos Requerimiento EducaMadrid Es necesario poder ofrecer asistencia personalizada remota para facilitar el uso en centros educativos de MAX, aparte de otros usos que se le pueda dar (MAX7).


Para ello se solicita:
- La mejoras y adaptaciones requeridas por el sistema de gestión del acceso remoto basado
a los centros educativos por medio de un servidor propio de EducaMadrid .

- Mantener dicho gestor de acceso remoto.
Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el sistema de acceso remoto a centros educativos como una plataforma crítica de soporte, orientada a garantizar la asistencia eficiente, segura y controlada sobre los equipos con MAX desplegados en el entorno educativo. empresa_s realizará la implantación y mantenimiento de un sistema centralizado de acceso remoto, asegurando su correcta integración dentro de la infraestructura de EducaMadrid:
- Despliegue del servidor de acceso remoto:
o Infraestructura alojada en entorno controlado de EducaMadrid. o Configuración segura del servicio. o Integración con sistemas existentes.
- Gestión de accesos:
o Control de autenticación:
- Integración con sistemas de identidad (LDAP si aplica).
o Definición de permisos:
- Accesos por rol (técnicos, administradores, soporte).
o Registro de sesiones:
- Trazabilidad completa de accesos.
empresa_s garantizará la conectividad con los centros:
- Configuración de clientes de acceso remoto en equipos MAX.
- Validación de conectividad desde el servidor central.
- Resolución de incidencias de acceso:
o Problemas de red. o Configuración de clientes. o Restricciones de entorno. Se realizará mantenimiento continuo del sistema:
- Monitorización del servicio:
o Estado del servidor. o Disponibilidad de conexiones.
- Actualización del software:
o Aplicación de parches de seguridad. o Mejora de funcionalidades.
- Optimización del rendimiento:
o Gestión de sesiones concurrentes. o Ajustes de configuración. El sistema permitirá la asistencia remota eficiente:
- Acceso a equipos para:
o Diagnóstico de incidencias. o Configuración de sistemas. o Instalación de software.
- Reducción de intervenciones presenciales.
- Mejora en tiempos de resolución.
Propuesta de mejora, seguridad y optimización del acceso remoto


empresa_s propone evolucionar el sistema hacia un modelo avanzado de acceso remoto seguro y gestionado:
1. Plataforma centralizada de gestión de accesos
- Control unificado de conexiones.
- Gestión de usuarios y permisos.
- Mejora de la administración del sistema.
2. Refuerzo de seguridad
- Uso de cifrado en comunicaciones.
- Registro detallado de accesos.
- Control de sesiones activas.
3. Monitorización avanzada
- Seguimiento de conexiones en tiempo real.
- Detección de incidencias de acceso.
- Alertas ante fallos o usos anómalos.
4. Optimización del soporte remoto
- Reducción de tiempos de intervención.
- Mejora en la resolución de incidencias.
- Mayor eficiencia operativa.
5. Escalabilidad del sistema
- Adaptación al crecimiento de centros.
- Soporte para múltiples conexiones simultáneas.
- Evolución del servicio según necesidades.
Valor aportado Estas actuaciones permiten disponer de un sistema de acceso remoto seguro, eficiente y escalable, facilitando la asistencia a los centros educativos, reduciendo costes operativos y mejorando significativamente los tiempos de resolución de incidencias. Requisito: II.1.7.8. Soporte de asistencia telefónica y remota para incidencias de entornos MAX Requerimiento EducaMadrid Se necesita ofrecer un servicio de ayuda a los centros educativos con el sistema operativo MAX (MAX8) Para ello se solicita:
- La asistencia técnica telefónica y mediante acceso remoto para cubrir las posibles
incidencias y solicitudes de mantenimiento de cara al usuario final. Esta asistencia se integra dentro del servicio de soporte que se ofrece desde EducaMadrid a los Sistemas Operativos MAX instalados en los distintos centros de la comunidad de Madrid.

- Con la nueva implantación del sistema de gestión de repositorios de software dinámicos,
también se hace necesario el mantenimiento y actualización de dicho sistema.

Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el soporte de incidencias en entornos MAX como un servicio estructurado de atención al usuario, orientado a garantizar una resolución ágil, eficiente y trazable de las incidencias reportadas por los centros educativos. empresa_s integrará el soporte dentro del modelo global de atención de EducaMadrid, combinando asistencia telefónica y acceso remoto para maximizar la capacidad de resolución en primer nivel.


El servicio de soporte se estructurará en los siguientes ámbitos:
- Atención telefónica:
o Recepción de incidencias y consultas. o Identificación del problema. o Clasificación inicial según tipología. o Resolución directa en primer nivel cuando sea posible.
- Soporte remoto:
o Acceso a equipos mediante herramientas de acceso remoto. o Diagnóstico en tiempo real. o Resolución de incidencias sin necesidad de desplazamiento. o Validación de funcionamiento tras la intervención. empresa_s garantizará la correcta gestión de incidencias:
- Registro de incidencias:
o Alta en sistema CAU. o Clasificación por tipo, prioridad y centro.
- Seguimiento:
o Control del estado de resolución. o Actualización de información.
- Escalado:
o Derivación a niveles superiores cuando sea necesario. Se dará soporte a distintas versiones de MAX:
- Mantenimiento de compatibilidad con versiones soportadas.
- Actualización remota de paquetes:
o Aplicación de parches. o Resolución de incidencias funcionales.
- Asesoramiento técnico:
o Recomendaciones de actualización de sistema. o Orientación sobre mejoras de hardware. empresa_s gestionará el sistema de repositorios dinámicos:
- Mantenimiento de repositorios:
o Actualización de paquetes. o Validación de disponibilidad.
- Resolución de incidencias relacionadas con:
o Descarga de paquetes. o Instalaciones. o Configuración del sistema. Propuesta de mejora , eficiencia y calidad del soporte empresa_s propone evolucionar el servicio de soporte hacia un modelo más eficiente y proactivo:
1. Sistema de clasificación avanzada de incidencias
- Identificación rápida del tipo de problema.
- Priorización automática.
- Mejora en tiempos de respuesta.
2. Resolución en primer nivel optimizada
- Incremento del porcentaje de incidencias resueltas en primera intervención.
- Reducción de escalados innecesarios.
3. Base de conocimiento estructurada
- Registro de incidencias recurrentes.
- Guías de resolución.
- Mejora continua del servicio.
4. Monitorización del servicio de soporte


- Métricas clave:
o Tiempo de resolución. o Volumen de incidencias. o Tipología de problemas.
- Identificación de áreas de mejora.
5. Automatización de tareas repetitivas
- Scripts de resolución.
- Actualizaciones automatizadas.
- Mejora de eficiencia operativa.
Valor aportado Estas actuaciones permiten ofrecer un servicio de soporte ágil, eficiente y orientado al usuario, mejorando los tiempos de resolución, reduciendo la carga operativa y garantizando una atención de calidad a los centros educativos. Requisito: II.1.7.9. Asistencia presencial en los diferentes eventos MAX Requerimiento EducaMadrid En ocasiones es necesaria la asistencia presencial en eventos para ayuda directa con el sistema operativo MAX (MAX9). Por tanto, se pide, cuando sea necesario:
- Visita presencial a los eventos que tengan mayor complejidad.

- Realizar el soporte de sus equipos en el evento.

- Posibles instalaciones y actualizaciones de MAX durante los eventos.

Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la asistencia presencial en eventos MAX como un servicio técnico especializado, orientado a garantizar el correcto funcionamiento de los equipos, la resolución de incidencias in situ y el apoyo directo a los usuarios en entornos de alta interacción. empresa_s planificará cada intervención en eventos de forma estructurada:
- Preparación previa:
o Análisis del tipo de evento. o Identificación de necesidades técnicas. o Revisión de equipamiento disponible.
- Coordinación con la organización:
o Definición de puntos de soporte. o Planificación de recursos técnicos. o Establecimiento de procedimientos de actuación. Durante el evento, empresa_s proporcionará soporte técnico presencial especializado:
- Asistencia a usuarios:
o Resolución de incidencias en equipos. o Configuración de sistemas MAX. o Soporte en el uso de la distribución.
- Intervención sobre equipos:
o Instalación y actualización de MAX. o Configuración de aplicaciones. o Ajuste de configuraciones según necesidades.


empresa_s realizará validaciones técnicas en entorno real:
- Verificación de funcionamiento de los equipos.

- Comprobación de compatibilidad de hardware.

- Validación de conectividad y servicios.

Se garantizará una atención ágil y organizada:
- Priorización de incidencias.
- Resolución en tiempo real.
- Coordinación entre técnicos.
Tras el evento, empresa_s realizará tareas de cierre:
- Registro de incidencias atendidas.
- Identificación de problemas recurrentes.
- Elaboración de informe técnico del evento.
Propuesta de mejora, optimización y transferencia de conocimiento empresa_s propone evolucionar la asistencia en eventos hacia un modelo más eficiente y orientado a valor:
1. Preparación técnica previa al evento
- Diagnóstico anticipado de necesidades.
- Reducción de incidencias durante el evento.
2. Estandarización de intervenciones
- Procedimientos definidos para actuaciones comunes.
- Mejora en tiempos de resolución.
3. Generación de conocimiento
- Identificación de incidencias recurrentes.
- Incorporación a base de conocimiento.
4. Mejora de la experiencia de usuario
- Atención más ágil.
- Resolución inmediata de problemas.
5. Optimización de recursos técnicos
- Mejor planificación de equipos de soporte.
- Adaptación al tipo de evento.
Valor aportado Estas actuaciones permiten ofrecer un soporte presencial eficiente y organizado en eventos MAX, mejorando la experiencia de los usuarios, resolviendo incidencias en tiempo real y generando conocimiento útil para la mejora continua del servicio. Requisito: II.1.7.10. Soporte presencial en eventos especiales (MAX Install Party) Requerimiento EducaMadrid Se necesita dar a conocer las nuevas versiones y herramientas de MAX, para lo cual EducaMadrid realiza distintos eventos especiales, tales como las Install Party (MAX10). Para ello se solicita:
- Soporte presencial especializado en la distribución MAX vigente.


- Ofrecer instalación, actualización y configuración de los equipos de los diferentes
participantes que atiendan el evento. Estos eventos se organizarán en distintos momentos del año. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el soporte en eventos tipo MAX InstallParty como un servicio técnico especializado orientado a la instalación masiva, actualización y difusión de la distribución MAX, garantizando una experiencia fluida para los participantes y un correcto funcionamiento de los equipos. empresa_s planificará este tipo de eventos con un enfoque operativo y técnico:
- Preparación previa del evento:
o Análisis del volumen estimado de participantes. o Identificación de necesidades técnicas:
- Infraestructura de red.
- Equipos disponibles.
- Versiones de MAX a instalar.
o Preparación de recursos:
- Imágenes de instalación.
- Scripts de despliegue.
- Repositorios locales si es necesario.
Durante el evento, empresa_s ejecutará las tareas de soporte técnico:
- Instalación de MAX:
o Instalación en equipos de los participantes. o Actualización de versiones anteriores. o Configuración básica del sistema tras instalación.
- Configuración de equipos:
o Ajustes de hardware. o Instalación de drivers necesarios. o Configuración de periféricos básicos.
- Asistencia técnica:
o Resolución de incidencias durante la instalación. o Soporte en el uso inicial del sistema. o Orientación a usuarios sobre funcionalidades. empresa_s optimizará el proceso de instalación masiva:
- Uso de procedimientos estandarizados:
o Instalaciones rápidas. o Configuraciones predefinidas.
- Organización del flujo de trabajo:
o Priorización de intervenciones. o Distribución de técnicos por zonas.
- Reducción de tiempos de intervención:
o Preparación previa de herramientas. o Automatización de tareas repetitivas. Se garantizará la validación del sistema tras cada intervención:
- Comprobación de arranque.
- Validación de funcionamiento básico.
- Verificación de acceso a servicios.
Tras el evento, empresa_s realizará tareas de cierre:


- Registro de actuaciones realizadas.
- Identificación de incidencias recurrentes.
- Recogida de feedback técnico de los usuarios.
Propuesta de mejora, eficiencia y adopción del sistema empresa_s propone evolucionar estos eventos hacia un modelo más eficiente y orientado a la adopción de MAX:
1. Automatización de instalaciones
- Uso de imágenes preconfiguradas.
- Reducción de tiempos de instalación.
2. Preparación de entornos controlados
- Repositorios locales para evitar saturación de red.
- Mejora de la estabilidad durante el evento.
3. Estandarización de configuraciones
- Equipos con configuración homogénea.
- Mejora de la experiencia de usuario.
4. Transferencia de conocimiento
- Explicación práctica del uso de MAX.
- Mejora en la adopción del sistema por los usuarios.
5. Recogida estructurada de feedback
- Identificación de mejoras en la distribución.
- Adaptación a necesidades reales de los centros.
Valor aportado Estas actuaciones permiten transformar las InstallParty en eventos eficientes y organizados, facilitando la instalación masiva de MAX, mejorando la experiencia de los usuarios y favoreciendo la adopción del sistema en los centros educativos. Requisito: II.1.7.11. Gestión, mantenimiento y actualización de equipos MAX en remoto Requerimiento EducaMadrid Una de las grandes problemáticas que existen en algunos centros educativos es la falta de mantenimiento y actualización de los equipos, quedando estos expuestos (MAX11). Por lo tanto, se solicita:
- Tener un control de gestión de actualización para los centros educativos que lo soliciten.

- Mantenimiento de dicho control de gestión de actualización.

Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la gestión remota de equipos MAX como un servicio centralizado de administración, orientado a garantizar la actualización continua, la seguridad y la homogeneidad del parque de equipos en los centros educativos que lo soliciten. empresa_s implantará un modelo de gestión remota estructurado, basado en el control centralizado de equipos:
- Identificación de equipos gestionados:
o Registro de centros adheridos al servicio. o Inventario de equipos:
- Versión de MAX.
- Estado del sistema.


- Configuración general.
- Control de actualizaciones:
o Planificación de despliegues:
- Actualizaciones periódicas.
- Parches de seguridad.
o Ejecución remota:
- Instalación de paquetes.
- Actualización del sistema.
o Validación:
- Verificación de correcta instalación.
- Comprobación de funcionamiento.
empresa_s realizará mantenimiento continuo del parque:
- Supervisión de estado:
o Detección de equipos desactualizados. o Identificación de errores.
- Resolución de incidencias:
o Intervención remota. o Corrección de problemas detectados. Se garantizará la compatibilidad del sistema:
- Adaptación a distintas versiones de MAX.
- Validación de funcionamiento tras actualizaciones.
- Coordinación con repositorios y servicios asociados.
El servicio incluirá:
- Asesoramiento técnico a centros:
o Recomendaciones de actualización. o Orientación sobre estado de equipos.
- Mejora de la seguridad:
o Aplicación de parches. o Reducción de vulnerabilidades. Propuesta de mejora , automatización y control centralizado empresa_s propone evolucionar la gestión remota hacia un modelo más automatizado y eficiente:
1. Plataforma centralizada de gestión
- Control unificado de equipos.
- Visión global del parque.
- Mejora en la administración.
2. Automatización de actualizaciones
- Despliegue automático de parches.
- Reducción de intervención manual.
- Mejora de la seguridad.
3. Monitorización continua
- Estado de equipos en tiempo real.
- Detección proactiva de incidencias.
- Mejora en tiempos de respuesta.
4. Gestión eficiente del software
- Instalación remota de aplicaciones.
- Control de versiones.
- Homogeneización de entornos.
5. Escalabilidad del servicio
- Adaptación al crecimiento de centros.


- Gestión eficiente de grandes volúmenes de equipos.
Valor aportado Estas actuaciones permiten disponer de un sistema centralizado de gestión de equipos MAX, mejorando la seguridad, reduciendo incidencias y facilitando el mantenimiento continuo del parque tecnológico de los centros educativos. Requisito: II.1.7.12. Instalación y configuración de dispositivos solicitados por los centros educativos Requerimiento EducaMadrid Se necesita dar soporte de dispositivos a lo largo de cada curso a los diferentes tipos de centros educativos en la Comunidad de Madrid (MAX12). Por lo tanto, se solicita:
- Instalar y configuración de aplicaciones y dispositivos (pizarras, tabletas, etc.) específicas
para el buen desarrollo de sus aulas de clase.

Este soporte se ofrecerá a lo largo del curso escolar, según lo vayan solicitando de los centros educativos. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la instalación y configuración de dispositivos en entornos MAX como un servicio técnico especializado orientado a garantizar la plena operatividad de los equipos en el aula, asegurando la compatibilidad, estabilidad y correcto funcionamiento de todos los periféricos utilizados en los centros educativos. empresa_s realizará la gestión integral del ciclo de integración de dispositivos:
- Identificación de necesidades del centro:
o Tipología de dispositivos:
- Impresoras.
- Tablets.
- Pizarras digitales.
- Pantallas interactivas.
o Entorno de uso:
- Aula.
- Laboratorios.
- Espacios administrativos.
- Validación de compatibilidad:
o Verificación de soporte en Linux/MAX:
- Drivers disponibles.
- Compatibilidad con kernel.
o Evaluación de alternativas:
- Uso de drivers genéricos.
- Adaptación de soluciones existentes.
empresa_s ejecutará la instalación y configuración:
- Instalación de controladores:
o Drivers oficiales o adaptados. o Configuración específica del sistema.
- Integración con el entorno MAX:
o Configuración en aplicaciones educativas.


o Integración con servicios del sistema.
- Ajustes de funcionamiento:
o Configuración de parámetros. o Optimización según uso. Se realizará validación funcional completa:
- Pruebas de uso real:
o Impresión. o Interacción con pizarras. o Uso de dispositivos en aula.
- Verificación de estabilidad:
o Funcionamiento continuado. o Ausencia de errores. empresa_s gestionará incidencias relacionadas con dispositivos:
- Diagnóstico de problemas:
o Hardware. o Software.
- Resolución:
o Ajustes de configuración. o Sustitución de drivers.
- Recomendaciones:
o Dispositivos compatibles. o Mejores prácticas. Propuesta de mejora, compatibilidad y eficiencia operativa empresa_s propone evolucionar la gestión de dispositivos hacia un modelo más controlado y eficiente:
1. Catálogo de dispositivos compatibles
- Listado validado de periféricos.
- Reducción de incidencias en instalación.
- Mejora en la toma de decisiones de compra.
2. Estandarización de configuraciones
- Procedimientos definidos de instalación.
- Configuraciones homogéneas en centros.
- Reducción de errores.
3. Automatización de instalación de drivers
- Scripts de despliegue.
- Reducción de tiempos de intervención.
- Mejora de eficiencia.
4. Base de conocimiento técnica
- Documentación de incidencias y soluciones.
- Mejora continua del servicio.
5. Optimización del entorno educativo
- Mejora de la experiencia en aula.
- Integración fluida de dispositivos.
- Reducción de incidencias en uso diario.
Valor aportado Estas actuaciones permiten garantizar la correcta integración de dispositivos en entornos MAX, reduciendo incidencias, mejorando la compatibilidad y asegurando una experiencia estable y eficiente para el uso educativo.


Requisito: II.1.7.13. Mantenimiento y soporte del servidor de repositorio individual para los centros educativos Requerimiento EducaMadrid EducaMadrid ofrece un servidor de repositorio individual para los centros educativos que usen el Sistema Operativo MAX (MAX13). Por lo tanto, se solicita:
- Llevar a cabo un control de la gestión para los centros educativos que lo soliciten.

- Hacer el mantenimiento y el control de la gestión de las actualizaciones.

- Realizar una auditoría de los sistemas instalados en los centros (hardware y software).

- Monitorizar los errores en los equipos gestionados.

Este mantenimiento y soporte se ofrecerá a lo largo del curso escolar, según lo vayan solicitando de los centros educativos. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el mantenimiento del servidor de repositorio individual de centros como un sistema clave de gestión distribuida del parque MAX, orientado a garantizar el control del software, la trazabilidad de los equipos y la capacidad de administración remota a gran escala. empresa_s implantará y mantendrá un modelo de gestión centralizada basado en herramientas de software libre, con especial foco en soluciones como Migasfree, adaptadas al entorno de EducaMadrid. Se realizará la gestión completa del sistema de repositorios individuales:
- Administración del servidor:
o Mantenimiento del entorno Debian. o Aplicación de actualizaciones de seguridad. o Supervisión de disponibilidad del servicio.
- Gestión de repositorios:
o Publicación de paquetes. o Control de versiones. o Validación de integridad. empresa_s gestionará el control de los equipos de los centros:
- Inventario continuo:
o Registro de hardware:
- CPU, memoria, almacenamiento.
o Registro de software:
- Aplicaciones instaladas.
- Versiones.
- Identificación de estado:
o Equipos actualizados. o Equipos desactualizados. o Equipos con incidencias. Se implantará un sistema de gestión centralizada de políticas:
- Aplicación de políticas por:
o Centro.


o Grupo de equipos. o Tipología de uso.
- Control de despliegues:
o Instalación de software. o Actualizaciones. o Configuraciones específicas. empresa_s realizará monitorización continua:
- Detección de errores:
o Fallos de instalación. o Problemas de actualización.
- Registro de incidencias:
o Logs centralizados. o Seguimiento de eventos. Se garantizará la trazabilidad completa del sistema:
- Registro de acciones:
o Instalaciones. o Actualizaciones. o Cambios de configuración.
- Auditoría:
o Historial de operaciones. o Control de intervenciones. Propuesta de mejora, escalabilidad y gobierno del sistema empresa_s propone evolucionar el sistema hacia una plataforma avanzada de gestión del parque MAX:
1. Plataforma centralizada multi-centro
- Gestión unificada de todos los centros.
- Control global del parque.
- Mejora en la administración.
2. Automatización de políticas de software
- Despliegue automático de aplicaciones.
- Control de versiones homogéneo.
- Reducción de errores manuales.
3. Monitorización avanzada del parque
- Estado en tiempo real de equipos.
- Detección proactiva de incidencias.
- Alertas automáticas.
4. Sistema de auditoría y cumplimiento
- Control de instalaciones.
- Verificación de configuraciones.
- Cumplimiento de políticas de seguridad.
5. Escalabilidad y evolución del servicio
- Adaptación a nuevos centros.
- Gestión eficiente de grandes volúmenes de equipos.
- Preparación para crecimiento futuro.
Valor aportado Estas actuaciones permiten disponer de un sistema centralizado, controlado y escalable de gestión de equipos MAX, mejorando la visibilidad del parque tecnológico, optimizando la administración remota y garantizando el cumplimiento de políticas de seguridad y actualización en todos los centros educativos.


Requisito: II.1.7.14. Herramienta de gestión centralizada de maquetas de MAX Requerimiento EducaMadrid EducaMadrid cuenta con una solución interna de gestión centralizada de maquetas para Sistemas Operativos MAX basada en el Software Libre Migasfree. Como solución para los centros se necesita configurar y mantener la herramienta para que también permita la gestión centralizada y remota de los equipos desplegados en los diferentes centros (MAX14). Por lo tanto, se solicita:
- Mantener y mejorar la solución implementada en EducaMadrid permitiendo su uso por
parte de los centros educativos facilitando así una solución de gestión remota y centralizada de plataformas de Sistema Operativo MAX.

- Mantener, actualizar y dar soporte a la solución completa, incluyendo tanto a la parte que
afecta a los equipos internos como a la o que afecta a los equipos MAX de los centros educativos que lo hayan solicitado. Este soporte se ofrecerá a lo largo del curso escolar, según lo vayan solicitando de los centros educativos. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la gestión centralizada de maquetas de MAX como una plataforma estratégica de administración del puesto de trabajo, orientada a garantizar la homogeneidad de los entornos, el control del software desplegado y la capacidad de gestión remota a gran escala en los centros educativos. empresa_s implantará un modelo de gestión basado en Migasfree, evolucionándolo hacia una solución robusta y adaptada al ecosistema EducaMadrid:
- Gestión centralizada de maquetas:
o Definición de configuraciones base del sistema:
- Aplicaciones instaladas.
- Versiones de paquetes.
- Configuración del entorno.
o Control de versiones de maquetas:
- Histórico de cambios.
- Evolución controlada del sistema.
Se realizará la administración integral de la plataforma:
- Mantenimiento del sistema:
o Actualización del servidor Migasfree. o Aplicación de parches de seguridad. o Supervisión de disponibilidad.
- Gestión de agentes:
o Despliegue en equipos de centros. o Configuración y mantenimiento. o Validación de comunicación con el servidor. empresa_s permitirá la gestión remota completa de los equipos:
- Aplicación de políticas:
o Instalación de software. o Actualizaciones. o Configuraciones específicas.
- Control por segmentación:


o Por centro. o Por tipo de equipo. o Por perfil de usuario. Se garantizará el control del estado de los equipos:
- Inventario dinámico:
o Hardware. o Software.
- Estado de cumplimiento:
o Equipos alineados con la maqueta. o Equipos con desviaciones. Se realizará monitorización continua del sistema:
- Detección de errores:
o Fallos en despliegues. o Problemas de configuración.
- Registro de eventos:
o Logs centralizados. o Trazabilidad completa. Propuesta de mejora , gobierno del puesto y evolución del sistema empresa_s propone evolucionar la solución hacia una plataforma avanzada de gestión del puesto MAX:
1. Modelo de maquetas versionadas y controladas
- Gestión por versiones de entornos.
- Control de cambios estructurado.
- Mejora de estabilidad del sistema.
2. Gobierno del software desplegado
- Control total de aplicaciones instaladas.
- Eliminación de desviaciones.
- Homogeneización de entornos.
3. Automatización completa de despliegues
- Aplicación automática de políticas.
- Reducción de intervención manual.
- Mejora de eficiencia operativa.
4. Monitorización avanzada del cumplimiento
- Identificación de equipos fuera de estándar.
- Corrección proactiva.
- Mejora de la seguridad.
5. Plataforma escalable y multi-entorno
- Adaptación a crecimiento de centros.
- Gestión de distintos escenarios (aula, gestión, equipos antiguos).


Valor aportado Estas actuaciones permiten transformar Migasfree en una plataforma real de gobierno del puesto de trabajo, garantizando entornos homogéneos, controlados y seguros, facilitando la gestión masiva de equipos y mejorando la eficiencia operativa en todos los centros educativos.
##### APARTADO: AULAS VIRTUALES (AV)
Requisito: II.1.8.1. Actualización y comprobación periódica de servidores de BBDD en entornos de aulas virtuales Requerimiento EducaMadrid Actualmente EducaMadrid tiene más más de 2500 bases de datos de las diferentes aulas virtuales y otros sistemas de formación en línea, alojadas en distintos servidores tanto físicos en clúster como virtuales. La mayor parte de ellas son PostgreSQL, pero también MariaDB y MongoDB (AV1). Se solicita:
- Realizar de forma periódica actualizaciones de versión necesarias de los distintos
servidores de base de datos, teniendo en cuenta la compatibilidad con la versión de las Aulas Virtuales que tengan en cada momento.

- Comprobar el correcto funcionamiento y la estabilidad de los aplicativos en los entornos de
desarrollo y preproducción, así como un correcto rendimiento de estos.

Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la gestión de las bases de datos de Aulas Virtuales mediante un modelo altamente automatizado y orientado a garantizar estabilidad, rendimiento y continuidad operativa sobre infraestructuras PostgreSQL distribuidas. empresa_s realizará una gestión integral del ciclo de vida de los servidores BBDD:
- Actualización periódica y controlada de versiones PostgreSQL.

- Validación de compatibilidad con plataformas LMS y servicios asociados.

- Gestión homogénea de entornos físicos, virtualizados y clusterizados.

- Optimización continua de rendimiento y configuración.

Las actuaciones se ejecutarán mediante procedimientos seguros y controlados:
- Validación previa en entornos de desarrollo y preproducción.


![Imagen de la página 143](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0143-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0143-imagen-003.png -->
- Flujo de publicación desde el cambio de una aplicación hasta su despliegue por una organización.
- La aplicación recibe una petición, modifica ficheros y publica la actualización; la distribución solicita, empaqueta y libera el paquete.
- La organización pide o actualiza el paquete, lo personaliza, lo libera para despliegue y lo instala en producción.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0143-imagen-003.png -->

- Ejecución de backups completos y pruebas de restauración.

- Planes de rollback automatizados ante incidencias.

- Minimización del impacto en servicio durante actualizaciones.
Asimismo, se implantará un modelo continuo de supervisión:
- Monitorización del estado y rendimiento de servidores.

- Análisis de carga, latencia y concurrencia.

- Trazabilidad completa de cambios y configuraciones.

- Detección proactiva de degradaciones y riesgos operativos.

Propuesta de mejora y evolución del servicio empresa_s propone evolucionar el entorno hacia un modelo más escalable, resiliente y automatizado mediante:
1. Automatización masiva de actualizaciones y validaciones PostgreSQL.
2. Estandarización de configuraciones y despliegues sobre entornos homogéneos.
3. Evolución hacia despliegues basados en imágenes y automatización IaC.
4. Integración de métricas y observabilidad avanzada del entorno BBDD.
5. Automatización de backups, restores y validaciones post-migración.
6. Implantación de modelos predictivos de crecimiento y capacidad.
7. Refuerzo de gobernanza, trazabilidad y control operativo centralizado.

Valor aportado Estas mejoras permiten consolidar una infraestructura PostgreSQL robusta, optimizada y preparada para soportar el crecimiento continuo de las Aulas Virtuales de EducaMadrid. Asimismo, se incrementa la disponibilidad, la estabilidad y la capacidad de automatización del entorno, reduciendo riesgos operativos y garantizando una gestión eficiente de más de 2.500 bases de datos distribuidas. Requisito: II.1.8.2. Mantenimiento de los servidores frontend de los entornos de aulas virtuales Requerimiento EducaMadrid Se necesita la realización de las tareas para la migración y mantenimiento del entorno actual frontend del aplicativo de las aulas virtuales para guardar compatibilidad con las nuevas versiones de Moodle (AV2).


![Imagen de la página 144](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0144-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0144-imagen-003.png -->
- Esquema de clonación y reemplazo de una base de datos PostgreSQL.
- La versión anterior del motor se clona para crear la versión nueva y esta se clona de nuevo hacia otro entorno equivalente.
- La etiqueta final indica que la nueva versión sustituye a la anterior.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0144-imagen-003.png -->

Para ello se solicita:
- Realizar de forma periódica actualizaciones de versión mediante reinstalación de todos los
frontales que haya, manteniendo también los aplicativos necesarios actualizados a la última versión.

- Realizar la parametrización y optimización de los mismos, así como su mantenimiento.

Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la gestión de los frontales Moodle de EducaMadrid mediante un modelo basado en automatización, estandarización y renovación progresiva de infraestructura, garantizando disponibilidad, compatibilidad y alto rendimiento en todas las islas de producción. empresa_s realizará un mantenimiento continuo de los servidores frontend:
- Actualización periódica de sistemas y componentes asociados (PHP, Apache y Moodle).

- Reinstalación controlada y homogénea de servidores frontend.

- Ajuste continuo de configuraciones y optimización de rendimiento.

- Validación funcional completa antes de paso a producción.
La estrategia de despliegue estará basada en modelos reproducibles:
- Creación de imágenes base (“master”) para despliegues homogéneos.

- Clonado progresivo de nodos frontend.

- Sustitución gradual de servidores por islas o grupos de servicio.

- Integración validada con SSO, monitorización, correo y servicios corporativos.

Asimismo, se ejecutarán controles continuos de rendimiento:
- Validación post-migración y pruebas funcionales.

- Análisis de capacidad y concurrencia.

- Optimización de tiempos de respuesta y carga.

- Supervisión proactiva de disponibilidad y estabilidad.

Propuesta de mejora y evolución del servicio empresa_s propone evolucionar el entorno frontend hacia un modelo más eficiente, escalable y automatizado mediante:
1. Estandarización completa de despliegues mediante imágenes reutilizables.
2. Sustitución progresiva de nodos sin impacto sobre balanceadores ni red.
3. Automatización de despliegues y validaciones mediante Ansible y CI/CD.
4. Ejecución periódica de pruebas de carga y estrés sobre las islas Moodle.
5. Escalabilidad horizontal dinámica según demanda de usuarios concurrentes.
6. Optimización avanzada de rendimiento y tuning PHP/Apache.
7. Mejora de observabilidad y monitorización centralizada de frontales.


Valor aportado Estas mejoras permiten consolidar una infraestructura Moodle moderna, homogénea y altamente disponible, preparada para soportar el crecimiento continuo de usuarios y servicios de EducaMadrid. Asimismo, se reduce el impacto operativo de las actualizaciones, se mejora la capacidad de escalado y se incrementa la estabilidad global de los entornos de aulas virtuales.

Requisito: II.1.8.3. Despliegue periódico de nuevos grupos de aulas virtuales y ampliación de los actuales Requerimiento EducaMadrid Actualmente EducaMadrid tiene más de 1.900 instancias de Moodle distribuidas en 8 grupos o islas (AV3). Se solicita:
- Realizar las ampliaciones de los grupos (islas) actuales acorde a la demanda.

- Creación de nuevas islas de aulas virtuales para mantener la demanda creciente poniendo
especial atención al balanceo y reparto de la carga.

- Realizar las labores necesarias de monitorización del rendimiento de los frontales en
función de la carga de los centros. Estas tareas se realizarán periódicamente. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la evolución de las Aulas Virtuales de EducaMadrid mediante un modelo escalable y proactivo, orientado a garantizar el equilibrio de carga, la disponibilidad y el crecimiento ordenado de las más de 1.900 instancias Moodle distribuidas en múltiples “islas”. empresa_s realizará una supervisión continua de la capacidad del entorno: Página 146 de 239


![Imagen de la página 146](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0146-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0146-imagen-003.png -->
- Proceso de actualización de una aplicación web con alta disponibilidad.
- La versión anterior se clona a una versión nueva y luego a otro nodo nuevo.
- Durante el reemplazo, dos instancias de la nueva versión permanecen activas en producción mientras se retiran gradualmente las anteriores.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0146-imagen-003.png -->

![Imagen de la página 146](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0146-imagen-004.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0146-imagen-004.png -->
- Banda de beneficios operativos de una actualización.
- Destaca mejor experiencia de usuario, despliegue rápido y seguro, alta disponibilidad, seguridad reforzada y ausencia de impacto en el servicio.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0146-imagen-004.png -->

- Análisis periódico de carga, concurrencia y utilización de recursos.

- Identificación temprana de saturaciones en frontales, bases de datos y almacenamiento.

- Evaluación de crecimiento por centros educativos y servicios asociados.

- Planificación técnica de ampliaciones y redistribuciones.

La estrategia de crecimiento estará basada en despliegues controlados y homogéneos:
- Incorporación progresiva de nuevos frontales en grupos existentes.

- Despliegue de nuevas islas Moodle mediante arquitecturas estandarizadas.

- Balanceo eficiente de carga entre entornos distribuidos.

- Integración validada con bases de datos, monitorización, SSO y almacenamiento.

Asimismo, se implantará un modelo operativo orientado a la observabilidad:
- Supervisión continua de rendimiento y disponibilidad.

- Seguimiento de métricas de acceso y tiempos de respuesta.

- Validación funcional tras ampliaciones o redistribuciones.

- Trazabilidad completa de cambios y evolución del entorno.
Propuesta de mejora y evolución del servicio empresa_s propone evolucionar la plataforma hacia un modelo inteligente, automatizado y preparado para el crecimiento continuo mediante:
1. Automatización del análisis de capacidad y planificación predictiva.
2. Despliegue rápido de nuevas islas mediante modelos reutilizables e IaC.
3. Redistribución dinámica de carga entre grupos Moodle.
4. Escalabilidad horizontal automatizada de frontales y servicios asociados.
5. Integración de cuadros de mando operativos y métricas globales.
6. Optimización continua del rendimiento de las islas y balanceadores.
7. Evolución hacia arquitecturas más resilientes y cloud- native.


![Imagen de la página 147](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0147-imagen-003.jpg>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0147-imagen-003.jpg -->
- Infografía de escalabilidad predictiva organizada en cuatro etapas.
- Analiza capacidad y demanda, despliega nuevas islas de servicio con infraestructura como código, redistribuye carga entre grupos y escala horizontalmente frontales y servicios.
- La franja inferior representa monitorización, análisis de rendimiento, alertas, decisiones de escalado, ajuste y mejora continua.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0147-imagen-003.jpg -->

Valor aportado Estas mejoras permiten consolidar una infraestructura de aulas virtuales altamente escalable, equilibrada y preparada para absorber el crecimiento continuo de usuarios y servicios educativos. Asimismo, se mejora la capacidad de anticipación, la eficiencia operativa y la resiliencia global de la plataforma Moodle de EducaMadrid. Requisito: II.1.8.4. Redistribución periódica de los NFS de datos de las aulas virtuales Requerimiento EducaMadrid EducaMadrid cuenta con un gran número de aplicativos que utilizan NFS para su funcionamiento. Algunos de estos NFS tienen un tamaño que dificulta su control (AV4). Se solicita:
- Realizar de forma periódica una redistribución de los espacios ocupados por los centros
por los distintos NFS atendiendo a la ocupación de estos.

Para la realización de estas tareas se deben aprovechar los períodos no lectivos, tales como vacaciones de verano, Semana Santa y/o Navidad. Estas tareas se realizarán periódicamente. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la gestión del almacenamiento NFS de las Aulas Virtuales mediante un modelo proactivo orientado a garantizar equilibrio de carga, rendimiento y escalabilidad sobre un entorno distribuido de alta concurrencia. Se realizará un análisis continuo del estado de ocupación y rendimiento de las cabinas y sistemas NFS, evaluando métricas clave como utilización, I/O, latencias y throughput, permitiendo identificar de forma temprana situaciones de saturación o degradación del servicio. empresa_s implantará una estrategia de redistribución dinámica de datos basada en criterios objetivos de uso y capacidad:
- Balanceo inteligente entre cabinas y volúmenes NFS.

- Segmentación eficiente de grandes volúmenes de datos.

- Redistribución según carga real y tipología de uso de las aulas virtuales.

- Optimización de operaciones críticas de backup y restauración.
Las migraciones se ejecutarán mediante sincronizaciones progresivas y paralelizadas, minimizando ventanas de intervención y reduciendo el impacto sobre los usuarios finales. Todas las actuaciones incluirán validación de integridad, actualización automática de montajes y comprobación funcional de los servicios asociados. Asimismo, empresa_s garantizará la continuidad operativa mediante:
- Ejecución de actuaciones en periodos controlados o no lectivos.

- Automatización de tareas repetitivas de migración y redistribución.

- Coordinación continua con los equipos técnicos de EducaMadrid.

- Trazabilidad completa de cambios y actuaciones realizadas.
Propuesta de mejora y evolución del servicio


empresa_s propone evolucionar la plataforma de almacenamiento hacia un modelo inteligente, automatizado y orientado a la anticipación:
- Automatización del análisis de ocupación y crecimiento de los NFS.

- Redistribución preventiva basada en métricas históricas y tendencias de uso.

- Paralelización avanzada de migraciones para reducir tiempos de intervención.

- Integración con sistemas de monitorización y alertado en tiempo real.

- Estandarización de procedimientos de creación, ampliación y migración de NFS.

- Evolución hacia arquitecturas de almacenamiento más resilientes y escalables.

Valor aportado La propuesta de empresa_s permite consolidar un modelo de almacenamiento distribuido más eficiente, equilibrado y preparado para el crecimiento continuo de las Aulas Virtuales de EducaMadrid. La automatización de procesos, la redistribución dinámica de carga y la optimización continua del rendimiento reducen riesgos operativos, minimizan incidencias por saturación y mejoran significativamente la disponibilidad y capacidad de respuesta de la plataforma. Además, la implantación de mecanismos predictivos y arquitecturas escalables permite evolucionar el servicio hacia un entorno más robusto, resiliente y alineado con las necesidades futuras del ecosistema educativo digital.
##### APARTADO: SERVICIO DE LDAP Y PORTAL EDUCATIVO (POR)
Requisito: II.1.9.1. Ampliación periódica del sistema de esclavos LDAP de EducaMadrid Requerimiento EducaMadrid EducaMadrid cuenta con un servidor principal de LDAP y numerosos secundarios/esclavos (POR1). Se solicita:
- Mantener, ampliar y adaptar el número de servidores LDAP de forma que se mantengan
cubiertas las necesidades de todos los servicios ofrecidos por EducaMadrid.

- Analizar, estudiar las posibilidades y aplicar una redistribución de estos servidores,
dividiéndolos por servicios, para optimizar su rendimiento. Estas tareas se realizarán periódicamente. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la evolución del sistema LDAP como una arquitectura distribuida de alta disponibilidad, orientada a escalabilidad, segmentación de carga y resiliencia ante fallos, manteniendo la coherencia con la topología actual de EducaMadrid . Ampliación y dimensionamiento de nodos LDAP:
- Evolución del CPD principal:
o de 12 → 17 nodos esclavos LDAP
- Mantenimiento del MINI CPD:
o 3 nodos esclavos
- Ampliación en CPD Madrid Digital (prestar soporte a los técnicos de MD:


o de 4 → 6 nodos esclavos
- Incorporación de nodo especializado:
o esclavo dedicado a:
- sincronización interna
- consultas técnicas (reporting, extracción de datos)
Optimización de replicación y consistencia:
- Uso de replicación segura:
o syncrepl / delta-syncrepl
- Validación continua de:
o integridad del árbol LDAP o latencia de replicación
- Monitorización activa:
o detección de desfases o recuperación automática ante corrupción Redistribución de carga por servicio:
- Segmentación lógica de LDAP por uso:
o autenticación (correo, Moodle, etc.) o consultas internas o sincronización externa
- Balanceo mediante:
o DNS interno o pools de servidores
- Reducción de latencia y aislamiento de cargas.
Integración con sistemas externos:
- Gestión de LDAP de sincronización:
o extracción controlada desde master
- Servicios externos:
o Google (1 nodo LDAP) o Microsoft (2 nodos LDAP)
- Filtrado de información:
o solo datos necesarios o exclusión de información sensible Alta disponibilidad y contingencia:
- Segundo LDAP Master:
o preparado para asumir rol principal
- Infraestructura de respaldo:
o 2 esclavos asociados
- Procedimientos de conmutación:
o automáticos o asistidos
- Garantía de continuidad del servicio.


Propuesta de mejora y evolución del servicio empresa_s propone evolucionar el modelo LDAP hacia una arquitectura más segura y trazable:
1. Segmentación por servicio
Uso de credenciales específicas por aplicación.
2. Rotación de credenciales
Políticas de cambio periódico independientes.
3. Auditoría avanzada
Trazabilidad completa de accesos por servicio.
4. Reducción de riesgos
Aislamiento de impacto ante posibles compromisos. Valor aportado Estas mejoras permiten disponer de una infraestructura LDAP altamente escalable, segmentada y resiliente, capaz de soportar el crecimiento de servicios y usuarios, mejorar la seguridad mediante aislamiento funcional y garantizar la continuidad del servicio incluso ante fallos críticos. Requisito: II.1.9.2. Migración del sistema LDAP Master de EducaMadrid Requerimiento EducaMadrid EducaMadrid cuenta con un servidor principal de LDAP y numerosos secundarios/esclavos (POR2). Se solicita:
- Realizar las tareas de mantenimiento y actualización sobre los LDAP Master físicos yendo
a una versión LDAP Master virtualizada que se ejecute sobre la última versión de sistema operativo compatible con el esquema actual de LDAP.

- Mejorar la funcionalidad del sistema de correo configurándolo para que pueda integrarse
con el sistema de acceso a EducaMadrid por SSO, permitiendo adicionalmente el uso de 2FA.


![Imagen de la página 151](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0151-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0151-imagen-003.png -->
- Arquitectura LDAP actual y futura de EducaMadrid con un maestro principal y numerosos esclavos distribuidos entre varios centros de datos.
- Integra sincronización con Google y Microsoft, un esclavo especial para consultas internas y un maestro secundario de alta disponibilidad con dos réplicas.
- Las conexiones representan autenticación, replicación continua, comunicación cifrada y conmutación ante fallos.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0151-imagen-003.png -->

Estas tareas se realizarán periódicamente para mantener los LDAP Master lo más actualizados posible, tanto en versiones como en funcionalidades. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la migración del LDAP Master como una evolución estratégica hacia una arquitectura virtualizada, altamente disponible y preparada para integración con sistemas de identidad modernos, garantizando la continuidad del servicio en todo momento. Despliegue de un nuevo Ldap Master virtualizado.
- Implementación en infraestructura virtual:
o alineada con el entorno de EducaMadrid
- Uso de sistema operativo actualizado:
o compatible con el esquema LDAP actual
- Aplicación de hardening:
o refuerzo de seguridad o segmentación de red
- Configuración de comunicaciones seguras:
o LDAPS / TLS Migración controlada del entorno anterior.
- Exportación del directorio LDAP:
o datos o esquemas personalizados
- Validación previa de integridad.
- Importación en nuevo entorno:
o sin pérdida de información
- Reconfiguración de replicación:
o integración con todos los esclavos existentes Validación funcional completa.
- Verificación de servicios integrados:
o correo o Moodle o cloud o autenticación web
- Pruebas técnicas:
o autenticación o búsquedas o replicación
- Pruebas de carga:
o comportamiento en escenarios reales Plan de mantenimiento y actualización.
- Definición de ciclo de actualización:
o sistema operativo o servicio LDAP
- Documentación completa:
o configuración o procedimientos
- Plan de recuperación:
o restauración ante fallo Propuesta de mejora y evolución del servicio


empresa_s propone evolucionar el sistema LDAP hacia un modelo de alta disponibilidad y seguridad avanzada:
1. Alta disponibilidad. Implementación de un segundo nodo Master con failover.
2. Entorno de preproducción. Validación de cambios sin impacto en producción.
3. Sistema de copias de seguridad avanzado. Copias completas y selectivas del directorio.
Uso de:
- slapcat → backup completo
- slapsearch → recuperación selectiva
4. Restauración flexible y rápida.
5. Integración con SSO y 2FA. Adaptación a sistemas modernos de autenticación.
6. Coordinación con Madrid Digital. Sincronización operativa:
- replicación
- mantenimientos
7. Gestión conjunta de incidencias.

Valor aportado Estas mejoras permiten transformar el LDAP Master en un sistema moderno, virtualizado y altamente disponible, preparado para integrarse con soluciones de identidad avanzadas (SSO y 2FA), mejorando la seguridad global, la resiliencia ante fallos y la capacidad de evolución futura de la plataforma EducaMadrid.
##### APARTADO: SEGURIDAD (SEG)
Requisito: II.1.10.1. Mantenimiento y mejora del sistema de control de cambios en DNS Requerimiento EducaMadrid Actualmente EducaMadrid cuenta con un servicio DNS de cierto tamaño y que necesita un sistema de revisión (SEG1). Se solicita:
- Realizar las labores de mejora continua del sistema de control de modificaciones del DNS
público, para securizar el control de cambios.


![Imagen de la página 153](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0153-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0153-imagen-003.png -->
- Clúster LDAP activo y pasivo con dos maestros sincronizados.
- El maestro uno está activo y el segundo permanece pasivo para asumir el servicio ante fallos.
- Cuatro o más esclavos replican el directorio y atienden a usuarios, correo, Moodle, aplicaciones y otros servicios.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0153-imagen-003.png -->

- Realizar el mantenimiento periódico de dicha aplicación, para asegurar su correcto
funcionamiento. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el control de cambios del servicio DNS público de EducaMadrid mediante un modelo centralizado, automatizado y orientado a garantizar la trazabilidad, integridad y supervisión continua de los registros críticos de la plataforma. Se implantará un sistema automatizado de captura y análisis periódico de configuraciones DNS, permitiendo:
- Registro histórico y auditoría de modificaciones.

- Comparación automática de configuraciones y detección de cambios no autorizados.

- Generación de alertas y notificaciones ante incidencias o desviaciones.

- Supervisión continua de disponibilidad y coherencia de registros DNS.

empresa_s desarrollará mecanismos de monitorización y reporting integrados con el ecosistema operativo de EducaMadrid:
- Integración con sistemas de monitorización y ticketing.

- Validación periódica de configuraciones y zonas DNS.

- Identificación de configuraciones obsoletas o inconsistentes.

- Refuerzo de seguridad y gobernanza del servicio.

Asimismo, se garantizará la adaptación continua del sistema de control ante cambios de infraestructura o evolución de servicios corporativos. Propuesta de mejora y evolución del servicio empresa_s propone evolucionar el modelo actual hacia una plataforma avanzada de control y gobierno DNS:
- Automatización integral del análisis y trazabilidad de cambios DNS.

- Sistema proactivo de alertado y correlación de eventos.

- Integración con plataformas de monitorización, CMDB y gestión de incidencias.

- Auditoría continua de registros y validación automática de coherencia.

- Estandarización de procedimientos de gestión y aprobación de cambios.

- Mejora de la visibilidad operativa mediante cuadros de mando y reporting centralizado.


Valor aportado La propuesta de empresa_s permite disponer de un sistema DNS más seguro, gobernado y resiliente, reduciendo riesgos derivados de cambios no controlados o configuraciones inconsistentes. La automatización del control de cambios y la integración con herramientas de monitorización y auditoría mejoran significativamente la capacidad de detección temprana, trazabilidad y respuesta ante incidencias. Además, el modelo propuesto facilita una gestión más eficiente y centralizada del servicio DNS, alineada con las mejores prácticas de operación y continuidad de servicios críticos. Requisito: II.1.10.2. Mantenimiento y mejora de un LDAP Máster independiente para usuarios privilegiados Requerimiento EducaMadrid Actualmente EducaMadrid cuenta con LDAP Master donde se guardan los usuarios que de alguna forma tienen privilegios especiales sobre los sistemas TI de EducaMadrid. ( SEG2). Se solicita:
- Gestionar, mantener y actualizar el sistema LDAP independiente al que se conectan los
servidores para permitir el login de los usuarios privilegiados del sistema, poniendo especial cuidado en su correlación con el PAM de EducaMadrid.

- Mantener de forma periódica dicho LDAP, para asegurar su correcto funcionamiento.

Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el mantenimiento del LDAP Máster de usuarios privilegiados como un sistema crítico de control de accesos, tratándolo como un componente independiente, securizado y alineado con los mecanismos de autenticación del entorno. Se definirá una arquitectura específica orientada a separar completamente el directorio de usuarios privilegiados del LDAP general, garantizando aislamiento, trazabilidad y control de accesos. Se implementará y mantendrá un entorno LDAP Master dedicado, incluyendo:
- Despliegue sobre sistema operativo actualizado y endurecido.

- Configuración de servicios LDAP con políticas de seguridad reforzadas.

- Segmentación de red y control de accesos a nivel de servicio.
Se realizará la integración con el sistema PAM de EducaMadrid, asegurando:
- Correlación directa entre identidades LDAP y cuentas del sistema.


![Imagen de la página 155](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0155-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0155-imagen-003.png -->
- Flujo de ingesta de datos DNS en una CMDB con control de cambios.
- La información se recopila automáticamente, se normaliza, se compara con el estado anterior, se registra con sus relaciones y se somete a aprobación, ejecución y documentación.
- Una línea inferior indica un ciclo continuo de control y mejora.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0155-imagen-003.png -->

- Mapeo de grupos LDAP a perfiles de acceso en servidores.

- Validación de autenticación en servicios críticos.
Se establecerá un modelo de mantenimiento continuo:
- Monitorización del servicio LDAP y logs de autenticación

- Validación de consistencia del directorio (usuarios, grupos, atributos)

- Aplicación de actualizaciones de sistema y servidor LDAP

- Revisión de políticas de acceso en coordinación con ciberseguridad
Se garantizará la trazabilidad completa de accesos privilegiados mediante análisis de logs y control de cambios en el directorio. Propuesta de mejora, optimización y evolución del servicio empresa_s propone evolucionar el sistema hacia un modelo altamente seguro y resiliente:
1. Alta disponibilidad del LDAP privilegiado. Despliegue de clúster activo-pasivo con failover
automático.
2. Diseño de esquema optimizado para PAM. Estructuración avanzada de OU, grupos
jerárquicos y atributos específicos para control de accesos.
3. Implantación de LDAPS. Cifrado completo de comunicaciones mediante TLS, garantizando
seguridad en autenticación.
4. Documentación operativa avanzada. Procedimientos completos de gestión, mantenimiento
y control de accesos privilegiados. Valor aportado Estas actuaciones permiten convertir el LDAP de usuarios privilegiados en un sistema de control de accesos robusto, seguro y trazable, alineado con las políticas de ciberseguridad y preparado para gestionar accesos críticos con garantías.

Requisito: II.1.10.3. Gestión, mantenimiento e implantación anual de certificados Requerimiento EducaMadrid EducaMadrid cuenta con certificados de seguridad instalados para la gestión de su seguridad (SEG3). Se solicita:


![Imagen de la página 156](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0156-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0156-imagen-003.png -->
- Arquitectura de un LDAP maestro aislado para usuarios privilegiados.
- Administradores y cuentas privilegiadas acceden con autenticación segura a un OpenLDAP separado del directorio general, protegido por firewall, segmentación y control de accesos.
- El directorio mantiene políticas, grupos, trazabilidad y auditoría y se integra con una solución PAM.
- PAM correlaciona identidades y perfiles y habilita acceso validado a servidores, aplicaciones, bases de datos y servicios críticos.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0156-imagen-003.png -->

- Comprobar activamente los estados y fechas de caducidad y de renovación de los
certificados, la integridad del no repudio y el cumplimiento de la robustez y fortaleza de los mismos.

- Actualizar mediante sustitución antes del plazo de caducidad y aplicar las renovaciones y
nuevas inclusiones de nuevos certificados, aplicando el control habitual sobre el estado de los mismos.

- Realizar la gestión, mantenimiento, e implantación anual de los certificados de
EducaMadrid instalados, tanto en la electrónica de red como en los diferentes servidores para su correcto funcionamiento. Estas tareas se realizarán periódicamente. Las actualizaciones de los certificados de toda la plataforma se realizarán, al menos, una vez al año. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la gestión de certificados digitales como un proceso centralizado y continuo, orientado a garantizar la validez criptográfica, la disponibilidad de los servicios y el cumplimiento de las políticas de seguridad del entorno EducaMadrid. Se establecerá un sistema de control completo del ciclo de vida de los certificados, incluyendo inventario, monitorización, renovación e implantación. Se realizará una monitorización activa del estado de los certificados:
- Supervisión continua de fechas de expiración.

- Validación de cadena de confianza y autoridades emisoras.

- Verificación de algoritmos criptográficos y longitudes de clave.

- Control del cumplimiento de estándares de seguridad (TLS 1.2/1.3).

Se ejecutará un proceso de renovación proactiva:
- Sustitución de certificados antes de su caducidad.

- Generación de CSR y gestión con autoridades certificadoras.

- Validación previa de certificados emitidos.

- Implantación coordinada en servicios.

La implantación se realizará sobre todos los sistemas críticos:
- Servicios de correo (SMTP, IMAP, POP).

- Plataformas web y APIs (Apache, Nginx).

- Infraestructura de colaboración (Nextcloud, edición online).

- Videoconferencia y servicios interactivos.

- Electrónica de red (balanceadores, WAF, proxies).

Se garantizará la correcta instalación mediante:
- Verificación de endpoints seguros.


- Validación de protocolos y cifrados activos.

- Comprobación de no repudio y atributos del certificado.
Se mantendrá un inventario centralizado de certificados:
- Registro de emisión, expiración y servicios asociados.

- Control de renovaciones y revocaciones.

- Trazabilidad completa de intervenciones.

Propuesta de mejora, automatización y evolución del servicio empresa_s propone evolucionar la gestión de certificados hacia un modelo automatizado y proactivo:
1. Monitorización automatizada de certificados. Sistema centralizado que analiza dominios y
servicios, generando alertas anticipadas.
2. Segmentación por servicios. Organización del inventario por tipología (correo, web, nube),
facilitando gestión y control.
3. Automatización del despliegue. Integración con herramientas como Ansible para
distribución segura y sin intervención manual.
4. Integración con sistemas ACME. Automatización de renovación en entornos compatibles,
reduciendo carga operativa.
5. Documentación operativa avanzada. Procedimientos detallados de renovación, validación
y rollback por tipo de certificado. Valor aportado Estas actuaciones permiten disponer de un sistema de certificados completamente controlado, evitando caducidades no previstas, garantizando la seguridad de las comunicaciones y reduciendo la carga operativa mediante automatización. Requisito: II.1.10.4. Gestión y mantenimiento periódico de dominios DNS Requerimiento EducaMadrid Se necesita en EducaMadrid realizar la gestión y el mantenimiento periódico de los Dominios DNS con el fin de evitar vulnerabilidades. (SEG4). Para ello se solicita:
- Supervisar y auditar de forma continua los dominios existentes en busca de permutaciones
de control, detección de phishing, control de subdominios y verificando los certificados y protocolos vigentes sobre los mismos. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la gestión de dominios DNS como un elemento crítico de seguridad y disponibilidad, estableciendo un control continuo sobre la integridad de las zonas, la exposición de servicios y la correcta configuración de los registros. Se implantará un modelo de supervisión activa del ecosistema DNS, alineado con la infraestructura real de EducaMadrid. Se realizará una supervisión periódica de los registros DNS:
- Revisión de registros A, AAAA, MX, TXT, CNAME y SRV.

- Validación de correspondencia entre DNS y servicios activos.


- Detección de modificaciones no autorizadas en zonas.

Se ejecutará una auditoría continua de subdominios:
- Identificación de subdominios activos y su uso real.

- Detección de subdominios huérfanos o sin servicio asociado.

- Prevención de ataques de tipo subdomain takeover.

Se realizará la verificación de seguridad de servicios asociados:
- Validación de certificados digitales vinculados a dominios.

- Revisión de protocolos TLS y configuraciones de cifrado.

- Comprobación de compatibilidad con estándares actuales.
Se analizarán vectores de ataque asociados al DNS:
- Revisión de políticas SPF, DKIM y DMARC en dominios de correo.

- Identificación de configuraciones débiles o incompletas.

- Detección de posibles escenarios de phishing o suplantación.
Se mantendrá un control continuo mediante:
- Monitorización de cambios en registros DNS.

- Revisión de logs y eventos relacionados con resolución de dominios.

- Coordinación con el equipo de ciberseguridad.

Propuesta de mejora, seguridad y evolución del servicio empresa_s propone evolucionar la gestión DNS hacia un modelo automatizado y proactivo:
1. Sistema automatizado de detección de cambios DNS. Monitorización continua de registros
con alertas en tiempo real ante modificaciones.
2. Auditoría avanzada de seguridad TLS. Evaluación periódica con herramientas tipo SSL
Labs para detectar vulnerabilidades y debilidades criptográficas.
3. Detección de uso indebido de dominios. Identificación de cargas externas no autorizadas
(iframes, embeds) para prevenir ataques de tipo clickjacking.
4. Informes técnicos automatizados. Generación de reportes periódicos con estado de
dominios, certificados y posibles riesgos.
5. Refuerzo de políticas de seguridad DNS. Evaluación de DNSSEC, mejora de
SPF/DKIM/DMARC y aplicación de políticas de seguridad web (CSP, CORS). Valor aportado Estas actuaciones permiten disponer de un control completo sobre los dominios de EducaMadrid , reduciendo riesgos de suplantación, evitando exposiciones innecesarias y garantizando la seguridad de los servicios asociados. Requisito: II.1.10.5. Análisis y corrección de vulnerabilidades Requerimiento EducaMadrid


Es necesaria la gestión de seguridad mediante el análisis y corrección de vulnerabilidades en los servicios de EducaMadrid (SEG5). Para ello se solicita:
- Colaborar con el SOC para la detección y resolución de vulnerabilidades.

- Supervisar y auditar continuamente los activos, realizar el escaneo de servidores, la
detección de vulnerabilidades, la solicitud y recomendaciones de corrección, las correlaciones con notificaciones de vulnerabilidades de organismos oficiales, la clasificación de criticidades y la categorización según estándares NIST CVE.

- Hacer seguimiento y comprobación de las posibles correcciones de los activos y chequeo
de evoluciones de estado.

Estas tareas se realizarán periódicamente, y específicamente cuando surja la necesidad. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la gestión de vulnerabilidades como un proceso continuo y estructurado, alineado con los flujos del SOC de EducaMadrid y basado en estándares reconocidos de clasificación y tratamiento de riesgos. Se implantará un modelo operativo de gestión de vulnerabilidades que cubre todo el ciclo: detección, análisis, priorización, corrección y validación. Se establecerá una integración directa con el SOC:
- Recepción de alertas de vulnerabilidades detectadas.

- Correlación con eventos de seguridad y logs.

- Coordinación en la priorización de incidencias críticas.
Se realizará un proceso continuo de escaneo de activos:
- Escaneo periódico de servidores y servicios.

- Análisis de vulnerabilidades en sistemas operativos y aplicaciones.

- Identificación de paquetes vulnerables (ej. Red Hat, librerías, servicios web).
Se integrarán fuentes externas de información:
- Boletines de seguridad de fabricantes (Red Hat, etc.).

- Bases de datos de vulnerabilidades (CVE, NVD).

- Alertas de organismos oficiales de ciberseguridad.

Se aplicará un modelo de clasificación y priorización:
- Categorización según CVE y estándares NIST.

- Evaluación de criticidad (CVSS).

- Priorización basada en impacto y exposición del activo.

Se ejecutará el proceso de remediación:


- Aplicación de parches de seguridad.

- Actualización de paquetes y servicios vulnerables.

- Corrección de configuraciones inseguras.

- Coordinación con equipos responsables de cada servicio.

Se realizará validación post-corrección:
- Reescaneo del activo afectado.

- Verificación de eliminación de la vulnerabilidad.

- Control de posibles efectos colaterales.

Se mantendrá trazabilidad completa del proceso:
- Registro de vulnerabilidades detectadas.

- Estado de cada incidencia (abierta, en proceso, resuelta).

- Historial de actuaciones y tiempos de resolución.
Propuesta de mejora , automatización y evolución del servicio empresa_s propone evolucionar el sistema hacia un modelo avanzado de gestión de vulnerabilidades:
1. Plataforma centralizada de gestión de vulnerabilidades. Integración de herramientas como
OpenVAS, Nessus o equivalentes para consolidar escaneos y resultados.
2. Automatización del ciclo de remediación. Integración con herramientas de configuración
(Ansible) para aplicar parches de forma controlada.
3. Correlación avanzada con el SOC. Enlace entre vulnerabilidades detectadas y eventos
reales de seguridad para priorización dinámica.
4. Cuadros de mando y reporting. Dashboards con métricas de exposición, criticidad, tiempos
de resolución y evolución del riesgo.
5. Gestión proactiva del riesgo. Identificación de tendencias y anticipación a vulnerabilidades
recurrentes en la plataforma. Valor aportado Estas actuaciones permiten disponer de un sistema de gestión de vulnerabilidades estructurado, trazable y alineado con estándares internacionales, reduciendo la superficie de ataque y mejorando la capacidad de respuesta ante amenazas reales. Requisito: II.1.10.6. Gestión, mantenimiento y ajuste de herramienta de detección de intrusiones, integridad, logs y respuesta ante incidentes Requerimiento EducaMadrid Para ello se solicita (SEG6):
- Supervisar de forma continua y automática los activos

- Revisar el estado e integridad de los logs

- Detectar intrusiones y establecer alertas de diversos tipos y alarmas prioritarias


- Ejecutar acciones de respuesta a los incidentes y notificación de los mismos a los
responsables de EducaMadrid.

- Calibrar, adecuar e implementar mejoras en los desarrollos con el fin de mejorar su
seguridad. Estas tareas se realizarán periódicamente, y específicamente cuando surja la necesidad. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la detección de intrusiones, monitorización de integridad, análisis de logs y respuesta ante incidentes como un sistema continuo de vigilancia, correlación y actuación temprana sobre los activos críticos de EducaMadrid. Se implantará un modelo de supervisión automática de activos basado en la combinación de monitorización de procesos, análisis de logs, control de integridad y generación de alertas priorizadas. Se realizará supervisión continua de los servidores:
- Control de procesos sospechosos o ejecutados desde ubicaciones no habituales.

- Detección de uso de herramientas sensibles asociadas a cifrado, exfiltración, borrado
seguro o manipulación del sistema.

- Identificación de cambios en ficheros críticos del sistema.

- Control de modificaciones en SSH, cron, sudoers, cuentas y grupos.

- Detección de alteraciones en servicios de seguridad, backup o monitorización.

Se revisará la integridad y disponibilidad de los logs:
- Validación del correcto registro de eventos del sistema.

- Supervisión de logs de autenticación, auditoría y servicios críticos.

- Detección de patrones anómalos o alteraciones inesperadas.

- Conservación de evidencias para análisis posterior.

Se configurará un sistema de alertas y alarmas:
- Alertas por cambios críticos en configuración.

- Alarmas por ejecución de binarios sensibles.

- Detección de ráfagas anómalas de escritura que puedan indicar cifrado masivo.

- Notificaciones a responsables técnicos y de ciberseguridad.

- Priorización según criticidad del activo y tipo de evento.

Se ejecutarán acciones de respuesta ante incidentes:
- Registro detallado del evento detectado.

- Notificación inmediata a los responsables de EducaMadrid.


- Revisión del activo afectado.

- Recomendación de contención, aislamiento o corrección.

- Seguimiento hasta cierre del incidente.
Como parte del servicio, empresa_s adaptará y calibrará los mecanismos de detección para reducir falsos positivos, incorporando reglas específicas para el entorno de EducaMadrid y ajustando umbrales según comportamiento real de los servidores. Propuesta de mejora, detección avanzada y respuesta operativa empresa_s propone evolucionar el sistema hacia un modelo avanzado de detección y respuesta temprana:
1. Implantación de agente ligero de detección en servidores. Despliegue de un servicio
específico capaz de detectar comportamientos anómalos, cambios críticos y posibles indicios de compromiso.
2. Monitorización frente a ransomware y actividad maliciosa. Detección de escritura masiva,
extensiones sospechosas, ejecución de herramientas de cifrado y manipulación de servicios de backup o seguridad.
3. Integración con sistemas de alertas y correo técnico. Notificación automática a
responsables de sistemas y ciberseguridad ante eventos relevantes, con control de frecuencia para evitar saturación.
4. Correlación con logs y auditoría del sistema. Uso de auditd, journald y registros del sistema
para reconstruir eventos y mejorar el análisis forense inicial.
5. Calibración continua de reglas. Ajuste de umbrales, listas blancas y patrones de detección
para adaptarse al comportamiento real de los servicios.
6. Procedimientos de respuesta documentados. Definición de acciones de contención,
validación, escalado y cierre de incidentes. Valor aportado Estas actuaciones permiten disponer de una capa adicional de detección temprana sobre los servidores de EducaMadrid, mejorando la capacidad de identificación de intrusiones, reduciendo tiempos de respuesta y facilitando la actuación coordinada ante incidentes de seguridad. Requisito: II.1.10.7. Realización de auditorías internas de aplicaciones Requerimiento EducaMadrid Para chequear su seguridad y prevenir ataques, EducaMadrid necesita realizar auditorías internas de seguridad en sus aplicaciones. (SEG7). Para ello se solicita:
- Auditar el estado y detectar las posibles vulnerabilidades según los estándares OWASP,
tanto de los aplicativos propios como de los usados en EducaMadrid.

- Realizar pruebas de clasificación y explotación de vulnerabilidades.

- Ejecutar las correcciones pertinentes en función de las anomalías detectadas.

- Hacer seguimiento y comprobación de la corrección de los aplicativos y chequear las
evoluciones de estado.

Estas tareas se realizarán periódicamente, y específicamente cuando surja la necesidad.


Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la seguridad de las aplicaciones de EducaMadrid mediante un modelo continuo de auditoría y mejora, orientado a garantizar la detección temprana de vulnerabilidades, la reducción del riesgo y el refuerzo de la ciberseguridad de la plataforma. Se ejecutarán auditorías periódicas basadas en estándares OWASP y buenas prácticas de seguridad:
- Evaluación de aplicaciones propias y de terceros.

- Identificación de vulnerabilidades críticas y riesgos asociados.

- Validación técnica mediante herramientas especializadas como Burp Suite y análisis
complementarios.

- Clasificación y priorización de incidencias según criticidad e impacto.
empresa_s coordinará las acciones de remediación junto a los equipos técnicos y de desarrollo:
- Definición de medidas correctivas.

- Validación posterior de las correcciones implantadas.

- Reevaluación continua del estado de seguridad.

- Generación de informes técnicos y trazabilidad de actuaciones.

Asimismo, se implantará un modelo de revisión recurrente que permita mantener un ciclo continuo de identificación, corrección y validación de vulnerabilidades. Propuesta de mejora y evolución del servicio empresa_s propone evolucionar el modelo actual hacia una estrategia de seguridad continua integrada en todo el ciclo de vida del desarrollo:
- Integración de controles de seguridad dentro de pipelines DevSecOps.

- Automatización de auditorías y análisis recurrentes de vulnerabilidades.

- Implantación de métricas y cuadros de mando de ciberseguridad.

- Centralización del seguimiento de vulnerabilidades y remediaciones.

- Refuerzo de la cultura de desarrollo seguro mediante formación especializada.

- Mejora de la gobernanza y trazabilidad del estado de seguridad de las aplicaciones.
Valor aportado La propuesta de empresa_s permite evolucionar desde un modelo reactivo de auditoría hacia un enfoque preventivo y continuo de seguridad, reduciendo significativamente la exposición frente a amenazas y vulnerabilidades. La automatización de controles, la integración de seguridad en el ciclo de desarrollo y la monitorización continua mejoran la capacidad de detección temprana y aceleran los procesos de remediación. Además, el modelo propuesto refuerza la gobernanza de ciberseguridad de EducaMadrid , incrementando la resiliencia, trazabilidad y calidad global de las aplicaciones corporativas.


Requisito: II.1.10.8. Realización de auditorías internas continuas de los sistemas Requerimiento EducaMadrid Para chequear su propia seguridad y prevenir ataques, EducaMadrid necesita realizar auditorías internas de seguridad en sus sistemas. (SEG8). Para ello se solicita:
- Auditar de forma continua los sistemas, según los estándares vigentes.

- Cotejar los resultados con el cumplimiento de los requisitos exigidos en el ENS.

- Clasificar los resultados y evaluar la estrategia y pasos necesarios para la corrección de
las anomalías encontradas

- Ejecutar las correcciones pertinentes a los problemas, comprobando la remediación de las
anomalías y chequear continuamente la evolución del estado de los problemas encontrados. Estas tareas se realizarán periódicamente, y específicamente cuando surja la necesidad. Propuesta técnica de empresa_s empresa_s propone un modelo de auditoría continua orientado a garantizar la seguridad, trazabilidad y cumplimiento normativo de la infraestructura tecnológica de EducaMadrid, mediante procesos automatizados de análisis, validación y remediación continua alineados con el ENS y buenas prácticas de ciberseguridad. La solución contempla una supervisión permanente de servidores, servicios, sistemas operativos y configuraciones críticas, permitiendo identificar vulnerabilidades, desviaciones de seguridad y riesgos operativos antes de que impacten sobre la plataforma. Auditoría continua y análisis automatizado
- Ejecución recurrente de auditorías de seguridad sobre sistemas, servicios y activos críticos.

- Detección automatizada de vulnerabilidades mediante herramientas especializadas de
escaneo y análisis continuo.

- Identificación de exposición de puertos, servicios inseguros, configuraciones incorrectas y
vulnerabilidades conocidas (CVE).


![Imagen de la página 165](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0165-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0165-imagen-003.png -->
- Modelo integral para crear aplicaciones más seguras.
- Combina DevSecOps en todo el ciclo, auditorías automatizadas con BurpSuite, Nessus y Trivy, métricas y cuadros de mando y seguimiento centralizado de vulnerabilidades.
- Añade cultura de desarrollo seguro, formación y gobierno con políticas, trazabilidad, cumplimiento y reporting.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0165-imagen-003.png -->

- Evaluación continua del nivel de riesgo y priorización de actuaciones.

Gestión de vulnerabilidades y remediación
- Clasificación de incidencias según criticidad, impacto y riesgo operativo.

- Definición y seguimiento de planes de remediación y parcheo.

- Validación posterior mediante nuevas auditorías automáticas.

- Registro histórico de actuaciones y evolución del estado de seguridad.

Cumplimiento ENS y gobernanza
- Verificación continua de cumplimiento respecto al ENS y políticas corporativas.

- Generación de evidencias técnicas y trazabilidad de auditorías.

- Centralización de métricas de seguridad y cuadros de mando operativos.

- Integración con sistemas corporativos de monitorización, CMDB y ticketing.

Observabilidad y operación continua
- Integración con plataformas de observabilidad y análisis centralizado.

- Correlación entre vulnerabilidades, activos y servicios afectados.

- Alertado proactivo ante riesgos críticos o desviaciones de seguridad.

- Supervisión continua del estado de cumplimiento y exposición de la infraestructura.
Propuesta de mejora y evolución del servicio empresa_s propone evolucionar el modelo actual hacia una plataforma de seguridad continua automatizada y gobernada, basada en principios DevSecOps y observabilidad avanzada:
- Integración de controles de seguridad dentro de pipelines DevSecOps.

- Automatización de auditorías y análisis recurrentes de vulnerabilidades.

- Implantación de métricas y cuadros de mando de ciberseguridad.

- Centralización del seguimiento de vulnerabilidades y remediaciones.

- Integración con herramientas especializadas como Burp Suite, Nessus o Trivy.

- Automatización de generación de evidencias ENS y reporting técnico.

- Correlación de eventos de seguridad con CMDB, monitorización y sistemas ITSM.

- Refuerzo de la cultura de seguridad mediante formación continua a equipos técnicos.

- Evolución hacia un modelo de seguridad preventiva y mejora continua.


Valor aportado La propuesta de empresa_s permite evolucionar el modelo de auditoría hacia un sistema centralizado, automatizado y proactivo, incrementando significativamente la capacidad de detección temprana, control operativo y cumplimiento normativo. Además, mejora la trazabilidad de las actuaciones, reduce tiempos de respuesta ante vulnerabilidades y refuerza la postura global de ciberseguridad de EducaMadrid mediante una operación continúa alineada con estándares ENS y mejores prácticas del sector. Esta aproximación aporta una visión integral de la seguridad de sistemas, permitiendo anticipar riesgos, optimizar procesos de remediación y consolidar una infraestructura más resiliente, gobernada y preparada para futuras amenazas. Requisito: II.1.10.9. Mantenimiento y uso de logs centralizados Requerimiento EducaMadrid Se solicita (SEG9):
- Almacenar de forma centralizada los logs de los sistemas.

- Controlar y supervisar continuamente la integridad y calibración de los logs.

- Gestionar el almacenamiento de la información en unidades externas, por sistema
rotatorio, durante el periodo que fija el ENS relativos a tiempo de conservación de los mismos para posteriores comprobaciones de posibles incidentes y realización de análisis de tipo forense si fuera requerido. Estas tareas se realizarán periódicamente, y específicamente cuando surja la necesidad. Propuesta técnica de empresa_s EducaMadrid requiere un sistema robusto de gestión de logs que permita centralizar, supervisar y preservar la información generada por sus sistemas, garantizando tanto la detección temprana de incidentes como la capacidad de análisis forense. Este sistema debe estar alineado con los requisitos del Esquema Nacional de Seguridad (ENS), especialmente en lo relativo a la integridad, trazabilidad y conservación de la información. empresa_s propone un modelo integral de gestión de logs basado en centralización, monitorización continua y cumplimiento normativo. Centralización de logs


![Imagen de la página 167](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0165-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0165-imagen-003.png -->
- Modelo integral para crear aplicaciones más seguras.
- Combina DevSecOps en todo el ciclo, auditorías automatizadas con BurpSuite, Nessus y Trivy, métricas y cuadros de mando y seguimiento centralizado de vulnerabilidades.
- Añade cultura de desarrollo seguro, formación y gobierno con políticas, trazabilidad, cumplimiento y reporting.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0165-imagen-003.png -->

- Recopilación centralizada de logs procedentes de sistemas, aplicaciones y dispositivos.

- Normalización y estructuración de los eventos para su tratamiento unificado.

- Uso de agentes ligeros de recolección para minimizar impacto en los sistemas origen.

- Consolidación de la información en una plataforma centralizada de análisis.

Supervisión continua e integridad
- Monitorización continua del estado y calidad de los logs recopilados.

- Verificación de la integridad de los registros mediante mecanismos de control y validación.

- Calibración y ajuste de las fuentes de log para garantizar la fiabilidad de la información.

- Detección de anomalías, pérdidas de información o inconsistencias en la generación de
eventos.

Almacenamiento y cumplimiento ENS
- Gestión del almacenamiento de logs conforme a los requisitos de conservación del ENS.

- Implementación de políticas de retención y rotación de logs.

- Almacenamiento en sistemas externos para garantizar disponibilidad y resiliencia.

- Preservación de la información para su uso en auditorías o investigaciones.

Soporte a análisis forense y respuesta a incidentes
- Disponibilidad de históricos de logs para análisis de incidentes de seguridad.

- Capacidad de reconstrucción de eventos ante posibles brechas o anomalías.

- Soporte a investigaciones forenses mediante acceso estructurado a la información.

Propuesta de mejora y evolución del servicio empresa_s propone evolucionar hacia un modelo avanzado de gestión de logs, orientado a la detección temprana, eficiencia operativa y mejora continua: Implantación de plataforma SIEM
- Uso de soluciones avanzadas de gestión de logs (como Wazuh integrado con stack
Elastic).

- Correlación de eventos para la detección de incidentes de seguridad.

- Centralización avanzada con capacidades de análisis en tiempo real.
Optimización y tuning del sistema de logs
- Ajuste fino de las fuentes de generación de logs para recoger únicamente información
relevante.

- Reducción del volumen de datos innecesarios, optimizando almacenamiento y
procesamiento.


- Mejora de la calidad de la información recopilada.

Automatización y eficiencia del almacenamiento
- Definición de políticas automáticas de rotación, archivado y backup.

- Optimización del almacenamiento externo para mejorar tiempos de acceso y recuperación.

- Garantía de disponibilidad y eficiencia en la gestión del histórico.
Mejora de la supervisión y detección
- Implementación de mecanismos de alerta ante eventos críticos o anomalías.

- Mejora de la capacidad de detección temprana de incidentes.

- Integración con otros sistemas de seguridad y monitorización.

Valor aportado La propuesta permite evolucionar el sistema de gestión de logs hacia una plataforma centralizada, inteligente y orientada a la detección temprana de incidentes, mejorando significativamente la capacidad de supervisión, trazabilidad y respuesta operativa. La implantación de un modelo SIEM avanzado, junto con la automatización del ciclo de vida de los logs y la optimización del almacenamiento, permite reducir costes operativos, mejorar la eficiencia del procesamiento y reforzar la seguridad global de la plataforma. Además, la integración con sistemas de monitorización y seguridad proporciona una visión unificada del entorno, facilitando la correlación de eventos, el análisis en tiempo real y la mejora continua de la capacidad de detección y respuesta ante amenazas. Requisito: II.1.10.10. Implementación y mantenimiento de claves RSA unificadas Requerimiento EducaMadrid Para garantizar la seguridad, coherencia e integridad de los servicios de EducaMadrid , se requiere la gestión unificada de las claves RSA utilizadas en los distintos entornos y aplicaciones. La intervención sobre dichas claves queda condicionada a la observación de los flujos de comunicación entre servicios, cuya falta de visibilidad puede invalidar la actuación (SEG10). Se solicita:


![Imagen de la página 169](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0169-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0169-imagen-003.png -->
- Esquema de la plataforma ELK Stack.
- Elasticsearch almacena e indexa datos de forma escalable, Logstash procesa y normaliza los registros y Kibana los visualiza y analiza en tiempo real.
- La base destaca alta disponibilidad, escalabilidad, seguridad y balanceo de carga.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0169-imagen-003.png -->

- Establecer un régimen de gestión y supervisión de claves RSA, garantizando coherencia y
seguridad de los procesos que las utilizan, considerando que la ausencia de información sobre comunicaciones puede limitar o invalidar la intervención.

- Supervisar de forma periódica el estado y la validez de las claves, identificando potenciales
riesgos, vulnerabilidades o situaciones que puedan afectar a la integridad de los servicios.

- Ejecutar las acciones correctivas o preventivas necesarias para garantizar el
funcionamiento seguro de los sistemas que dependen de dichas claves.

- Mantener un seguimiento de los cambios, actualizaciones o migraciones de claves,
asegurando que los servicios continúan operando de forma coherente y segura Estas tareas se realizarán de manera periódica y cada vez que se identifique la necesidad. Propuesta técnica de empresa_s empresa_s propone un modelo centralizado y automatizado de gestión de claves RSA, orientado a garantizar la seguridad, trazabilidad y continuidad operativa de los servicios críticos de EducaMadrid, eliminando configuraciones dispersas y reduciendo riesgos asociados a la gestión manual de credenciales. Gestión centralizada y segura de claves
- Implantación de un repositorio seguro de secretos tipo Vault para almacenamiento cifrado
y controlado.

- Unificación de políticas de gestión de claves RSA para usuarios, aplicativos y servicios.

- Control granular de accesos y auditoría completa de operaciones realizadas sobre las
claves.

- Estandarización de nomenclaturas y procedimientos de despliegue.
Automatización del ciclo de vida

- Automatización mediante Ansible de:
o generación o distribución o rotación o revocación de claves
- Integración con procesos de despliegue y operación de sistemas.

- Reducción de errores manuales y mejora de la coherencia operativa.

- Trazabilidad completa de cambios y operaciones.

Supervisión y control continuo
- Monitorización periódica de validez, caducidad y uso de claves RSA.

- Identificación de claves obsoletas, duplicadas o inseguras.

- Análisis de dependencias entre servicios para evitar impactos en autenticación y cifrado.

- Validación funcional tras procesos de rotación o renovación.


Seguridad y continuidad operativa
- Definición de políticas de rotación según criticidad del servicio.

- Renovación controlada sin interrupciones.

- Verificación automática de compatibilidad entre sistemas.

- Refuerzo de la seguridad global del ecosistema de autenticación.
Propuesta de mejora y evolución del servicio empresa_s propone evolucionar hacia un modelo avanzado de gestión de secretos y autenticación segura, plenamente automatizado y alineado con entornos modernos y normativas de seguridad. Evolución del modelo de secretos
- Centralización completa de secretos y credenciales mediante Vault.

- Eliminación de almacenamiento distribuido e inseguro de claves.

- Refuerzo de auditoría y control de accesos privilegiados.
Automatización avanzada y operación eficiente
- Playbooks reutilizables para gestión integral del ciclo de vida de claves RSA.

- Integración con pipelines DevOps e infraestructuras automatizadas.

- Reducción de tiempos de operación y riesgo humano.

Gobernanza y trazabilidad
- Inventario centralizado de claves y relaciones entre sistemas.

- Auditoría continua del estado de certificados y claves.

- Análisis preventivo de impactos antes de cualquier cambio.

Seguridad y cumplimiento
- Alineación con buenas prácticas criptográficas y requisitos ENS.

- Refuerzo del control de autenticación y cifrado entre servicios.

- Mejora continua de la postura global de seguridad.


![Imagen de la página 171](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0171-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0171-imagen-003.png -->
- Arquitectura de un repositorio centralizado de secretos basado en Vault RSA.
- Aplicaciones, usuarios, SSO, sistemas y API consumen secretos desde un almacén con control de accesos y auditoría.
- Ansible automatiza generación, distribución, rotación y revocación.
- La supervisión continua cubre uso, dependencias, políticas de rotación, trazabilidad y auditoría.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0171-imagen-003.png -->

Valor aportado

- Centralización y control unificado de claves RSA y secretos.

- Automatización completa del ciclo de vida criptográfico.

- Reducción de riesgos operativos y configuraciones inseguras.

- Mayor trazabilidad, auditoría y cumplimiento normativo.

- Continuidad operativa garantizada durante rotaciones y renovaciones.

- Plataforma preparada para arquitecturas modernas y automatizadas.
Requisito: II.1.10.11. Asistencia y soporte presencial en los diferentes eventos de Ciberseguridad de EducaMadrid Requerimiento EducaMadrid EducaMadrid es pionero en su estrategia de concienciación y transmisión de la información a sus equipos en materias de seguridad. Como base de su estrategia están los “Ciberjueves” que son eventos que, con una periodicidad mensual (aproximadamente), reúnen a todo el equipo de EducaMadrid para actualizarles sobre asuntos relativos a la Ciberseguridad y las ciberamenazas. Suele contar con ponentes experimentados en los ámbitos de la ciberseguridad para, en una charla de una hora aproximadamente, hablen a todo el equipo acerca de asuntos de actualidad y novedades en el sector (SEG11). Para ello se solicita:
- Realizar acciones de concienciación en ciberseguridad con la periodicidad establecida en
el departamento de Ciberseguridad de EducaMadrid.

- Proponer ciber consejos y acciones de difusión de la Ciberseguridad.

- Preparar y coordinar todo lo relativo a los “Ciberjueves”: organizar, controlar y supervisar
los diferentes eventos, así como gestionar asistentes y espacios.

Estas tareas se realizarán periódicamente, y específicamente cuando surja la necesidad. Propuesta técnica de empresa_s empresa_s propone un modelo integral de soporte y dinamización de los eventos de ciberseguridad de EducaMadrid, orientado a reforzar la concienciación, mejorar la participación y fomentar una cultura continua de seguridad entre los distintos perfiles de usuarios y equipos técnicos. Organización y coordinación de eventos
- Planificación y soporte integral de los “Ciberjueves”.

- Coordinación de ponentes, contenidos, espacios y medios técnicos.

- Supervisión operativa de sesiones presenciales y online.

- Garantía de continuidad y calidad en cada evento.
Concienciación y divulgación continua
- Elaboración de contenidos actualizados sobre amenazas, buenas prácticas y tendencias
de ciberseguridad. Página 172 de 239


- Difusión de:
o píldoras formativas o vídeos o guías rápidas o consejos de seguridad
- Adaptación de contenidos según perfil técnico o funcional.
Soporte técnico y operativo
- Asistencia presencial y remota durante los eventos.

- Gestión de plataformas de difusión y participación.

- Resolución de incidencias técnicas y apoyo a usuarios.

Seguimiento y mejora continua
- Evaluación de participación e impacto de las sesiones.

- Recogida de feedback y propuestas de mejora.

- Evolución continua de formatos y metodologías de concienciación.

Propuesta de mejora y evolución del servicio empresa_s propone evolucionar el modelo actual hacia una plataforma continua de concienciación y capacitación en ciberseguridad, más dinámica, participativa y orientada a la prevención. Modelo multiformato y bajo demanda
- Evolución hacia sesiones híbridas, microcontenidos y formación reutilizable.

- Disponibilidad de contenidos bajo demanda.

- Incremento del alcance y reutilización del conocimiento generado.

Gamificación y participación
- Dinámicas participativas y simulaciones prácticas.

- Integración de retos y ejercicios de concienciación.

- Mejora del nivel de implicación de los asistentes.
Integración con el ecosistema EducaMadrid
- Coordinación con plataformas corporativas de comunicación y formación.

- Difusión centralizada de contenidos y alertas de ciberseguridad.

- Refuerzo de la cultura corporativa de seguridad.
Valor aportado

- Refuerzo continuo de la cultura de ciberseguridad.

- Mayor participación y alcance de las acciones formativas.


- Contenidos dinámicos y adaptados a amenazas actuales.

- Mejora de la prevención frente a riesgos y ataques.

- Incremento de la capacidad de respuesta y concienciación de usuarios y equipos.

- Modelo evolutivo, reutilizable y alineado con las necesidades de EducaMadrid.

##### APARTADO: AUTOMATIZACIÓN Y CONTENEDORES (CON)
Requisito: II.1.11.1. Mantenimiento y mejora del sistema de gestión de contenedores Requerimiento EducaMadrid Actualmente EducaMadrid se encuentra en proceso de migración de algunas de sus aplicaciones a entornos contenerizados. (CON1). Se solicita:
- Realizar las labores de mejora continua del sistema de control y gestión de contenedores.

- Realizar el mantenimiento periódico de dicho entorno, para asegurar su correcto
funcionamiento. Propuesta técnica de empresa_s empresa_s propone un modelo integral de mantenimiento y evolución de la plataforma de contenedores de EducaMadrid, orientado a consolidar un entorno moderno, automatizado y altamente eficiente para la ejecución de aplicaciones y servicios corporativos. La propuesta contempla la operación continua de los entornos basados en Docker y tecnologías asociadas, garantizando la estabilidad de los servicios, la optimización del rendimiento y la correcta gestión de los recursos de infraestructura. Para ello, se realizará una supervisión permanente del estado de los nodos y contenedores, aplicando tareas preventivas y correctivas que permitan anticipar incidencias y minimizar el impacto operativo. Asimismo, empresa_s impulsará un modelo homogéneo de despliegue basado en imágenes estandarizadas y procesos automatizados, facilitando la mantenibilidad y reduciendo desviaciones entre entornos. Esta estrategia permitirá evolucionar progresivamente los servicios actuales hacia arquitecturas contenerizadas, manteniendo compatibilidad con la infraestructura existente y asegurando la continuidad del servicio durante las migraciones. La propuesta incluye también la integración de la plataforma con procesos DevOps y pipelines CI/CD, automatizando el ciclo completo de construcción, validación, despliegue y rollback de aplicaciones. Esto permitirá mejorar la trazabilidad, acelerar la entrega de cambios y reducir errores derivados de operaciones manuales. Adicionalmente, se reforzará la observabilidad del entorno mediante mecanismos de monitorización, análisis de logs y supervisión del rendimiento, proporcionando una visión centralizada del estado de la plataforma y facilitando la detección temprana de degradaciones o cuellos de botella. Propuesta de mejora y evolución del servicio empresa_s propone evolucionar el sistema actual hacia una plataforma cloud- native más automatizada, escalable y resiliente, preparada para soportar el crecimiento continuo de servicios y aplicaciones de EducaMadrid. La evolución del servicio estará orientada a la estandarización completa de despliegues mediante imágenes reutilizables y configuraciones homogéneas, facilitando la portabilidad entre entornos


de desarrollo, preproducción y producción. Esto permitirá reducir significativamente los tiempos de provisión y mejorar la capacidad de recuperación ante incidencias. Además, se avanzará hacia un modelo de automatización integral basado en infraestructura como código y despliegues continuos, permitiendo gestionar configuraciones, actualizaciones y operaciones recurrentes de forma controlada y reproducible. La integración con herramientas DevOps y sistemas de automatización mejorará la eficiencia operativa y reducirá la dependencia de tareas manuales. En paralelo, empresa_s reforzará la seguridad del entorno mediante políticas de control sobre imágenes y configuraciones, análisis automatizado de vulnerabilidades y alineamiento con buenas prácticas y normativas aplicables. Todo ello estará complementado con una capa avanzada de observabilidad que permitirá analizar métricas, consumo de recursos y comportamiento de los servicios en tiempo real. Valor aportado Esta evolución permitirá a EducaMadrid disponer de una plataforma moderna, flexible y preparada para futuras arquitecturas distribuidas y modelos avanzados de operación tecnológica. Requisito: II.1.11.2. Mantenimiento y mejora de los scripts y sistemas de automatización de tareas Requerimiento EducaMadrid Actualmente EducaMadrid dispone de cientos de scripts de automatización de tareas, así como de herramientas específicas para automatizar determinadas acciones sobre su infraestructura de sistemas. (CON2). Se solicita:
- Gestionar, mantener y actualizar el sistema de scripts, modificando y actualizando aquellos
que sean necesarios.

- Gestionar, mantener y actualizar las aplicaciones de automatización integradas en la
infraestructura de EducaMadrid.

- Realizar los mantenimientos periódicos, tanto reactivos como proactivos, de estos
elementos, incluyendo la aplicación de parches de seguridad y las configuraciones que, desde el departamento de ciberseguridad, sean requeridas. Propuesta técnica de empresa_s empresa_s propone una evolución integral del ecosistema de automatización de EducaMadrid , orientada a consolidar un modelo centralizado, seguro y altamente eficiente para la ejecución de tareas operativas, despliegues y procesos recurrentes de infraestructura. La propuesta contempla el mantenimiento evolutivo y correctivo de scripts existentes, garantizando su adaptación continua a cambios en sistemas, plataformas y necesidades operativas. Para ello, se realizará un proceso de inventariado, revisión y normalización de automatizaciones, facilitando su trazabilidad, mantenibilidad y reutilización. La estrategia de empresa_s evoluciona el modelo actual basado en scripts dispersos hacia una arquitectura de automatización centralizada y gobernada, apoyada en herramientas estándar como Ansible y repositorios versionados. Este enfoque permite transformar tareas manuales en procesos declarativos, repetibles y auditables, reduciendo significativamente riesgos operativos y tiempos de intervención. Asimismo, se incorporarán mecanismos avanzados de observabilidad y control operativo:


- Supervisión centralizada de ejecuciones y estados.

- Generación estructurada de logs y alertas.

- Integración con pipelines CI/CD y repositorios Git.

- Control de accesos y auditoría alineados con ENS.

- Gestión diferenciada de entornos de desarrollo, preproducción y producción.
Todo ello permitirá disponer de una plataforma de automatización moderna, preparada para integrarse con infraestructuras híbridas, entornos contenerizados y futuros modelos cloud- native. Propuesta de mejora y evolución del servicio Con el objetivo de maximizar la eficiencia operativa y reducir la dependencia de procesos manuales, empresa_s propone evolucionar el modelo actual hacia una plataforma avanzada de automatización y orquestación:
- Centralización completa de automatizaciones mediante Ansible y ejecución controlada.

- Migración progresiva de scripts legacy hacia playbooks reutilizables y versionados.

- Integración con GitLab CI/CD para automatizar despliegues y operaciones.

- Automatización de validaciones, rollback y control de errores.

- Observabilidad avanzada mediante dashboards, logs estructurados y alertado automático.

- Refuerzo de seguridad mediante bastionado, segregación de accesos y trazabilidad
completa.

- Evolución hacia modelos Infrastructure as Code (IaC) y automatización declarativa.
Esta aproximación permitirá a EducaMadrid disponer de un ecosistema automatizado más robusto, escalable y alineado con las mejores prácticas DevOps y de operación moderna.

Valor aportado La propuesta de empresa_s aporta una mejora directa en la eficiencia, gobernanza y fiabilidad de la operación técnica de EducaMadrid, permitiendo:
- Reducción significativa de tareas manuales y errores operativos.

- Mayor rapidez y homogeneidad en despliegues y configuraciones.

- Trazabilidad completa de cambios y ejecuciones.

- Incremento de la seguridad y cumplimiento ENS.


![Imagen de la página 176](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0176-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0176-imagen-003.png -->
- Centro de automatización basado en playbooks estructurados de Ansible.
- Convierte scripts existentes, herramientas heredadas, tareas, procesos e inventarios en automatización declarativa, reutilizable y versionada.
- Incluye ejecución controlada, gestión de errores, idempotencia, escalabilidad, estándares, GitLab, CI/CD y mecanismos de reversión y recuperación.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0176-imagen-003.png -->

- Escalabilidad operativa para soportar el crecimiento continuo de la plataforma.

Requisito: II.1.11.3. Mantenimiento y mejora del sistema auxiliar de automatización Requerimiento EducaMadrid Actualmente, EducaMadrid dispone de un sistema auxiliar de automatización basado en llamadas HTTP (POST/GET) que permite automatizar distintos servicios y procesos internos. Se solicita garantizar su correcto funcionamiento mediante mantenimiento, actualización y optimización. (CON3). Se solicita:
- Mantener, actualizar y mejorar los scripts y flujos que interactúan con el sistema auxiliar,
asegurando compatibilidad con la infraestructura y servicios existentes.

- Realizar mantenimientos periódicos, tanto proactivos como reactivos, incluyendo
aplicación de parches de seguridad y ajustes de configuración según indicaciones de ciberseguridad y operaciones.

- Documentar los endpoints, flujos y dependencias del sistema auxiliar, asegurando
trazabilidad, coherencia de datos y facilidad de mantenimiento futuro.

Propuesta técnica de empresa_s empresa_s propone evolucionar el sistema auxiliar de automatización CON3 hacia una plataforma más robusta, resiliente y plenamente integrada dentro del ecosistema tecnológico de EducaMadrid, garantizando la automatización segura y trazable de procesos internos mediante servicios HTTP y APIs. La propuesta contempla el mantenimiento continuo de los flujos de automatización existentes, asegurando su adaptación progresiva a cambios en aplicaciones, servicios y arquitecturas corporativas. Para ello, se establecerá un modelo homogéneo de integración basado en APIs desacopladas, controladas y documentadas, mejorando la interoperabilidad entre sistemas y reduciendo dependencias manuales. Asimismo, se reforzará la estabilidad operativa mediante:
- Supervisión continua de endpoints y servicios.

- Gestión avanzada de errores, validaciones y reintentos automáticos.

- Registro estructurado de eventos y trazabilidad completa de ejecuciones.

- Protección de APIs y control de accesos alineados con ENS.

- Integración con herramientas de automatización, monitorización y CI/CD.

El modelo permitirá transformar CON3 en un bus ligero de automatización e integración, preparado para soportar nuevos flujos, aplicaciones y procesos corporativos de forma escalable y segura. Propuesta de mejora y evolución del servicio Con el objetivo de modernizar y consolidar el sistema auxiliar de automatización, empresa_s propone evolucionar la plataforma hacia un modelo orientado a APIs gobernadas, automatización desacoplada y observabilidad avanzada:
- Estandarización de integraciones mediante APIs REST versionadas.

- Integración con Ansible, GitLab CI/CD y sistemas de orquestación.


- Implantación de logging centralizado, monitorización y alertado en tiempo real.

- Creación de entornos de preproducción para validación segura de cambios.

- Automatización de validaciones, despliegues y control de versiones.

- Refuerzo de seguridad mediante autenticación, validación de entradas y auditoría de
eventos.

- Evolución hacia arquitecturas más resilientes y orientadas a servicios.

Esta aproximación permitirá disponer de un sistema de automatización mucho más mantenible, trazable y preparado para futuras evoluciones cloud- native y DevOps. Valor aportado La propuesta de empresa_s aporta una mejora directa en la eficiencia operativa y gobernanza de las automatizaciones de EducaMadrid, permitiendo:
- Reducción de errores manuales y dependencias entre sistemas.

- Mayor resiliencia y estabilidad de procesos automatizados.

- Incremento de la trazabilidad y control operativo.

- Integración sencilla con nuevos aplicativos y servicios.

- Mejora de la seguridad y cumplimiento ENS.

- Base sólida para la evolución hacia automatización moderna y desacoplada.
##### APARTADO: GESTIÓN DE LA MIGRACIÓN DE SERVIDORES ENTRE CPDS (MIG)
Requisito: II.1.12.1. Coordinación y planificación de la migración Requerimiento EducaMadrid Se requiere una coordinación y planificación para asegurar que todos los equipos implicados actúen de forma alineada y que se minimicen los riesgos tanto durante la migración como después de la migración desde el punto de vista de los sistemas y servicios. (MIG1). Se solicita:
- Participar en reuniones de coordinación con el personal del CPD y del proveedor de
servicio de Infraestructuras.

- Documentar las decisiones, los diferentes riesgos y las recomendaciones.

- Asegurar la comunicación y el seguimiento de las acciones que afecten a sistemas y
aplicaciones entre los equipos implicados. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la coordinación y planificación de la migración como un proceso estructurado de gobierno técnico, orientado a alinear a todos los equipos implicados y a reducir los riesgos operativos durante el traslado de la infraestructura entre CPDs. empresa_s actuará como punto de referencia desde el ámbito de sistemas, participando activamente en las reuniones de coordinación junto con:


- Equipo de infraestructura del CPD.

- Proveedor de servicios de infraestructura.

- Equipo de comunicaciones.

- Equipos responsables de almacenamiento y backup.

- Responsables de aplicaciones y servicios.
En estas reuniones se definirán y validarán los aspectos clave de la migración:
- Alcance funcional de los sistemas afectados.

- Dependencias entre servicios.

- Ventanas de intervención.

- Secuencia de actuaciones.

- Identificación de puntos críticos.

- Responsables técnicos por cada área.
Se establecerá un modelo de documentación estructurada que recogerá:
- Decisiones adoptadas durante la planificación.
- Identificación y clasificación de riesgos:
o Riesgos de parada. o Riesgos de pérdida de datos. o Riesgos de incompatibilidad. o Riesgos de dependencia entre sistemas.
- Recomendaciones técnicas previas a la migración.

- Acciones necesarias para mitigar riesgos.
Esta documentación será versionada y compartida con todos los equipos implicados, asegurando un marco común de trabajo. empresa_s garantizará la comunicación continua entre equipos mediante:
- Seguimiento de tareas técnicas relacionadas con sistemas.

- Validación de que las acciones de otros equipos (infraestructura, comunicaciones,
almacenamiento) no afectan negativamente a los servicios.

- Coordinación de dependencias entre sistemas y aplicaciones.
Se realizará un seguimiento activo de todas las acciones que impacten en:
- Parada de servicios.

- Cambios en configuración.

- Modificaciones de red.

- Preparación de entornos en CPD destino.


Asimismo, se establecerán mecanismos de control del avance:
- Listado de tareas planificadas.

- Estado de ejecución.

- Identificación de bloqueos.

- Validación de hitos previos a la migración.
Propuesta de mejora, control y gobierno del proceso empresa_s propone reforzar la coordinación mediante un modelo avanzado de control y gestión del proceso:
1. Comité técnico de migración. Definición de un grupo de trabajo con representantes de cada
área, con reuniones periódicas y toma de decisiones coordinada.
2. Matriz de riesgos y plan de mitigación. Clasificación de riesgos por criticidad y definición de
acciones preventivas y correctivas.
3. Herramienta de seguimiento centralizado. Uso de una herramienta compartida para el
control de tareas, responsables y estado de ejecución.
4. Control de dependencias entre servicios. Identificación explícita de relaciones entre
sistemas para evitar paradas descoordinadas o impactos cruzados.
5. Plan de comunicación estructurado. Definición de canales, responsables y frecuencia de
comunicación durante todas las fases de la migración. Valor aportado Estas actuaciones permiten que la migración se ejecute de forma coordinada, controlada y predecible, evitando errores derivados de falta de comunicación entre equipos y reduciendo significativamente los riesgos operativos asociados a la parada y traslado de sistemas críticos. Requisito: II.1.12.2. Fases preparatorias y planificación técnica de la migración Requerimiento EducaMadrid En relación con la migración, será necesario realizar tareas de análisis y planificación técnica que permitan al equipo de sistemas disponer de una visión clara del entorno y de la secuencia de actuación después de la migración. (MIG2). Se solicita:
- Analizar y documentar los mapas del CPD desde el punto de vista lógico de sistemas y
servicios (servidores, aplicaciones, dependencias y relaciones entre servicios).

- Revisar el Plan de Migración, aportando la visión funcional de los sistemas y aplicaciones.

- Validar el Plan de Migración definitivo en lo relativo a sistemas y servicios tanto para el
traslado (si fuera necesario) como para las comprobaciones posteriores.

- Coordinar con el equipo responsable de infraestructura la idoneidad del CPD de destino
desde el punto de vista de la disponibilidad y correcta ubicación de los sistemas y servicios.

Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la fase preparatoria de la migración como un proceso de análisis técnico exhaustivo y planificación estructurada, cuyo objetivo es disponer de una visión


completa del entorno y definir una secuencia de actuación precisa que garantice la continuidad de los servicios durante el traslado entre CPDs. Como punto de partida, empresa_s realizará un análisis lógico del CPD desde la perspectiva de sistemas y servicios, incluyendo:
- Inventario detallado de servidores físicos y virtuales.

- Identificación de aplicaciones desplegadas.

- Catalogación de servicios activos.

- Análisis de dependencias entre sistemas.

- Relación entre capas:
o Frontend (web). o Aplicativa. o Bases de datos. o Servicios de infraestructura (DNS, autenticación, almacenamiento).
- Identificación de puntos críticos y servicios sensibles.
Esta información se consolidará en mapas lógicos de sistemas que reflejen:
- Interrelaciones entre servicios.

- Flujos de comunicación.

- Dependencias técnicas.

- Impacto potencial de la parada de cada componente.
A partir de este análisis, empresa_s elaborará el borrador del Plan de Migración, aportando una visión funcional completa que incluirá:
- Secuencia de parada de sistemas basada en dependencias reales.

- Identificación de ventanas de intervención.

- Definición de hitos técnicos.

- Identificación de riesgos asociados a cada fase.

- Procedimientos de validación por servicio.

Este borrador será revisado junto con los equipos implicados, validando:
- Coherencia técnica del plan.

- Compatibilidad con la planificación de infraestructura.

- Viabilidad operativa de las secuencias definidas.

empresa_s participará activamente en la validación del Plan de Migración definitivo, asegurando que:
- Se respetan las dependencias entre sistemas.

- Se minimizan los riesgos de indisponibilidad.

- Se contemplan mecanismos de control y verificación.


- Se incluyen procedimientos de contingencia.

En paralelo, empresa_s coordinará con el equipo de infraestructura la preparación del CPD de destino, validando:
- Disponibilidad de recursos necesarios (rack, energía, red).

- Correcta ubicación de servidores y cabinas.

- Preparación de redes y segmentación.

- Accesibilidad entre sistemas.

- Compatibilidad con los requisitos de los servicios.

Se verificará que el CPD de destino esté preparado desde el punto de vista lógico para recibir los sistemas, garantizando que el arranque posterior pueda realizarse sin bloqueos ni dependencias no resueltas.

Propuesta de mejora , planificación avanzada y reducción de riesgos empresa_s propone reforzar la fase preparatoria mediante un modelo avanzado de análisis y planificación técnica:
1. Mapa de dependencias detallado. Representación completa de relaciones entre servicios,
permitiendo definir un orden de migración sin conflictos.
2. Plan de migración basado en capas. Estructuración de la migración en niveles (web,
aplicación, base de datos, infraestructura) para facilitar ejecución controlada.
3. Simulación previa de la migración. Validación teórica del plan mediante escenarios de
ejecución, identificando posibles puntos de fallo.
4. Validación cruzada con equipos implicados. Revisión conjunta con infraestructura,
comunicaciones y aplicaciones para asegurar alineación total.


![Imagen de la página 182](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0182-imagen-003.jpg>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0182-imagen-003.jpg -->
- Infografía de planificación técnica de una migración con visión integral de sistemas y servicios.
- El mapa conecta usuarios, internet, firewall, web, aplicaciones, base de datos, DNS y almacenamiento.
- El plan incluye inventario y dependencias, borrador y validación, coordinación del centro de destino y cinco fases desde análisis hasta validación.
- La conclusión destaca planificación clara, dependencias identificadas y riesgos minimizados.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0182-imagen-003.jpg -->

5. Checklist técnico de preparación del CPD destino. Verificación previa de todos los
elementos necesarios antes del traslado físico. Valor aportado Estas actuaciones permiten disponer de una planificación técnica precisa, basada en el conocimiento real del entorno, reduciendo incertidumbre durante la migración y asegurando que cada sistema se detiene y arranca en el momento adecuado sin comprometer la integridad del servicio. Requisito: II.1.12.3. Preparación de servidores y documentación de sistemas Requerimiento EducaMadrid Se necesita una preparación de servidores y la documentación asociada que permita conocer el estado de los sistemas y definir procedimientos claros para la gestión de los servicios durante la migración (MIG3). Se solicita:
- Comprobar la información técnica que se tiene de los servidores desde el punto de vista
de sistemas y servicios (CPU, memoria, almacenamiento lógico, servicios y aplicaciones).

- Elaborar y revisar la documentación de procedimientos de parada y arranque lógicos y
validación de servicios.

- Preparar y revisar los listados de comprobación para la verificación de servicios y
aplicaciones antes y después de la migración.

Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la preparación de servidores y la documentación de sistemas como una fase crítica orientada a garantizar el conocimiento completo del estado de la plataforma y a definir procedimientos claros, repetibles y verificables durante la migración entre CPDs. Como primer paso, empresa_s realizará una recopilación exhaustiva de información técnica de todos los servidores, tanto físicos como virtuales, incluyendo:
- Recursos hardware:
o CPU (modelo, cores, carga habitual). o Memoria (capacidad y uso). o Almacenamiento lógico (volúmenes, LVM, sistemas de ficheros).
- Configuración de sistema:
o Sistema operativo y versión. o Servicios activos. o Usuarios y accesos relevantes.
- Servicios y aplicaciones:
o Aplicaciones desplegadas. o Servicios dependientes. o Puertos utilizados. o Configuraciones específicas.
- Dependencias:
o Conexiones a bases de datos. o Integraciones entre sistemas. o Dependencias externas.


Toda esta información será consolidada en fichas técnicas por servidor, permitiendo disponer de una visión clara y estructurada del entorno. A partir de este conocimiento, empresa_s elaborará procedimientos detallados de parada lógica de los sistemas, definiendo:
- Orden de parada por servicio.

- Dependencias a respetar durante el apagado.

- Validaciones previas a la parada.

- Verificación de detención completa de servicios.

- Consideraciones específicas por tipo de sistema (web, aplicación, base de datos,
almacenamiento).

De igual forma, se definirán procedimientos de validación de servicios, incluyendo:
- Comprobación de estado antes de la parada.

- Validación tras el arranque en CPD destino.

- Pruebas funcionales básicas por aplicación.

- Verificación de conectividad entre sistemas.

- Validación de acceso de usuarios cuando aplique.

empresa_s preparará listados de comprobación (checklists) estructurados que se utilizarán durante toda la migración:
- Checklist previo a la parada:
o Estado de servicios. o Validación de backups. o Confirmación de dependencias.
- Checklist durante la migración:
o Estado de apagado. o Control de incidencias.
- Checklist posterior al arranque:
o Estado de servicios. o Integridad de datos. o Funcionamiento de aplicaciones. o Validación de accesos. Estos listados permitirán ejecutar la migración de forma controlada, homogénea y trazable, reduciendo errores humanos y asegurando que ningún paso crítico quede sin validar. Propuesta de mejora , estandarización y control operativo empresa_s propone reforzar esta fase mediante un modelo estructurado de documentación y validación técnica:
1. Fichas técnicas normalizadas por servidor. Documentación homogénea que facilite la
identificación rápida de cada sistema y su función.
2. Procedimientos reutilizables. Definición de plantillas estándar de parada y validación
aplicables a distintos tipos de servicios.
3. Automatización de recopilación de información. Uso de scripts para extracción de datos de
sistema, reduciendo errores manuales y mejorando la precisión. Página 184 de 239


4. Checklists operativos en tiempo real. Uso de listas de verificación durante la ejecución para
asegurar cumplimiento de cada paso.
5. Trazabilidad completa de la migración. Registro de validaciones realizadas, incidencias
detectadas y acciones ejecutadas. Valor aportado Estas actuaciones permiten afrontar la migración con un conocimiento completo del entorno, procedimientos claros y mecanismos de verificación estructurados, reduciendo significativamente el riesgo de errores operativos y asegurando que todos los sistemas se gestionan de forma controlada durante el proceso. Requisito: II.1.12.4. Verificación de la migración Requerimiento EducaMadrid Durante la ejecución de la migración, el equipo de sistemas y soporte se encarga de supervisar el estado de los servicios y validar el correcto funcionamiento de las aplicaciones. (MIG4). Se solicita:
- Ejecutar scripts de recopilación de información y diagnóstico para verificar el estado de los
sistemas después del traslado, una vez estabilizados los sistemas, y comparar esos datos con los mismos datos recogidos antes y durante el traslado de CPD.

- Supervisar la disponibilidad de servicios y aplicaciones, detectando incidencias
relacionadas con software o configuración.

- Registrar y documentar incidencias de sistemas y servicios, coordinando su resolución con
los equipos responsables de infraestructura cuando sea necesario.

- Verificar la integridad de datos, configuraciones y funcionamiento de aplicaciones desde el
punto de vista del sistema operativo y los servicios. Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la verificación de la migración como una fase crítica de control operativo en tiempo real, orientada a validar el estado de los sistemas, garantizar la continuidad de los servicios y detectar de forma temprana cualquier incidencia derivada del traslado entre CPDs. Durante toda la ejecución de la migración, empresa_s realizará una supervisión continua basada en la ejecución de scripts de diagnóstico y recopilación de información, diseñados específicamente para comparar el estado de los sistemas en las distintas fases del proceso:
- Antes de la migración:
o Estado de servicios activos. o Conectividad entre sistemas. o Estado de bases de datos. o Integridad de almacenamiento.
- Durante la migración:
o Confirmación de parada controlada. o Verificación de ausencia de procesos activos críticos. o Validación de consistencia previa al traslado.
- Después de la migración:
o Estado de arranque de sistemas. o Disponibilidad de servicios. o Validación de comunicaciones internas.


o Acceso a aplicaciones. Estos scripts permitirán detectar desviaciones entre el estado previo y posterior, facilitando la identificación rápida de problemas. empresa_s supervisará activamente la disponibilidad de servicios y aplicaciones durante todas las fases, verificando:
- Servicios web (Apache, Nginx, balanceadores).

- Servicios de aplicación.

- Bases de datos.

- Servicios de autenticación y DNS.

- Integraciones entre sistemas.

- Accesos de usuarios.

Se realizará una detección proactiva de incidencias relacionadas con:
- Fallos de arranque.

- Problemas de configuración.

- Errores de conectividad.

- Dependencias no satisfechas.

- Servicios degradados.

Todas las incidencias detectadas serán registradas de forma estructurada, incluyendo:
- Sistema afectado.

- Tipo de incidencia.

- Momento de detección.

- Impacto.

- Acción realizada.

- Estado de resolución.

empresa_s coordinará la resolución de incidencias con los equipos responsables:
- Infraestructura (rack, red, conectividad).

- Comunicaciones.

- Almacenamiento (cabinas).

- Aplicaciones.

Se realizará una verificación completa de la integridad de datos y configuraciones, incluyendo:
- Validación de sistemas de ficheros.


- Comprobación de montajes de almacenamiento.

- Integridad de bases de datos.

- Consistencia de configuraciones de sistema.

- Validación de logs de arranque.

Asimismo, se verificará el correcto funcionamiento de las aplicaciones desde el punto de vista del sistema operativo y los servicios, asegurando que:
- Las aplicaciones responden correctamente.

- Las dependencias están operativas.

- Los flujos de funcionamiento son correctos.

Propuesta de mejora, automatización y control en tiempo real empresa_s propone reforzar la verificación mediante un modelo avanzado de monitorización y diagnóstico:
1. Framework de scripts de validación automatizada. Ejecución de scripts estandarizados
para comprobar estado de servicios, conectividad y rendimiento en cada fase.
2. Comparativa pre y post migración. Generación de informes que permitan identificar
diferencias entre el estado previo y posterior de los sistemas.
3. Panel de seguimiento en tiempo real. Visualización centralizada del estado de todos los
sistemas durante la migración.


![Imagen de la página 187](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0187-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0187-imagen-003.png -->
- Proceso de verificación de una migración antes, durante y después.
- Parte de recopilación y diagnóstico, continúa con supervisión en tiempo real y termina con validación y verificación.
- Las actividades comprenden scripts, estado, métricas, disponibilidad, alertas, incidencias, documentación, coordinación, integridad de datos y funcionamiento de servicios.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0187-imagen-003.png -->

4. Clasificación y priorización de incidencias. Identificación de incidencias críticas frente a no
críticas para optimizar la resolución.
5. Validación funcional por capas. Verificación independiente de:
- Infraestructura.

- Sistemas.

- Aplicaciones.
Valor aportado Estas actuaciones permiten detectar y corregir incidencias de forma inmediata durante la migración, asegurando que los sistemas arrancan correctamente en el CPD destino y que los servicios mantienen su funcionalidad sin comprometer la integridad de los datos.

Requisito: II.1.12.5. Mantenimiento y soporte durante y tras la migración Requerimiento EducaMadrid Después de la ejecución de la migración, el equipo de sistemas y soporte se encargará de supervisar el estado de los servicios y validar el correcto funcionamiento de las aplicaciones. (MIG5). Se solicita:
- Supervisar la disponibilidad de servicios y aplicaciones, detectando incidencias
relacionadas con software o configuración.

- Verificar la integridad de datos, configuraciones y funcionamiento de aplicaciones desde el
punto de vista de los sistemas y los servicios.

Supervisar la estabilidad de los servicios tras la migración y documentar las acciones correctivas realizadas.

Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán el mantenimiento y soporte durante y tras la migración como una fase de estabilización operativa, orientada a garantizar la continuidad de los servicios, la detección temprana de incidencias y la consolidación del correcto funcionamiento de la plataforma en el CPD de destino. Durante la ejecución de la migración y en la fase inmediatamente posterior, empresa_s realizará una supervisión continua de los sistemas y servicios, centrada en:
- Disponibilidad de servicios:
o Servicios web (Apache, Nginx, balanceadores). o Servicios de aplicación. o Bases de datos. o Servicios de autenticación y DNS.
- Accesibilidad de aplicaciones por parte de usuarios.

- Estado de procesos críticos.

- Conectividad entre sistemas.


Se establecerá un modelo de monitorización intensiva durante la ventana de migración, permitiendo detectar incidencias relacionadas con:
- Errores de configuración tras el arranque.

- Problemas de dependencias entre servicios.

- Fallos en integraciones.

- Degradaciones de rendimiento inicial.
empresa_s realizará la verificación de la integridad de los sistemas, incluyendo:
- Validación de sistemas de ficheros y volúmenes.

- Comprobación de montajes de almacenamiento.

- Integridad de datos en bases de datos.

- Consistencia de configuraciones de sistema.

- Revisión de logs de arranque y ejecución.

Se validará el correcto funcionamiento de las aplicaciones desde el punto de vista del sistema operativo y los servicios, asegurando que:
- Las aplicaciones responden correctamente.

- Los flujos funcionales son operativos.

- Las dependencias están resueltas.

- No existen errores críticos en producción.

Durante la fase de estabilización, empresa_s supervisará el comportamiento de los sistemas para detectar:
- Incidencias recurrentes.

- Problemas intermitentes.

- Cuellos de botella derivados del cambio de entorno.

- Desajustes de configuración.
Todas las incidencias detectadas serán registradas y documentadas de forma estructurada, incluyendo:
- Sistema afectado.

- Descripción del problema.

- Causa identificada.

- Acción correctiva aplicada.

- Estado final.


Se realizará un seguimiento activo de las acciones correctivas, verificando su eficacia y asegurando la estabilidad final de los servicios. Propuesta de mejora, estabilización y control post -migración empresa_s propone reforzar esta fase mediante un modelo de estabilización avanzada y control continuo:
1. Ventana de hiper-supervisión post-migración. Establecimiento de un periodo de
monitorización intensiva tras el arranque completo del sistema.
2. Análisis de comportamiento post-arranque. Evaluación de rendimiento, tiempos de
respuesta y estabilidad de servicios.
3. Registro estructurado de incidencias. Sistema de documentación que permita analizar
patrones y mejorar futuras migraciones.
4. Ajuste fino de configuraciones. Optimización de parámetros de sistema, red y aplicaciones
tras la migración.
5. Informe de cierre de migración. Documento final con:
- Estado de sistemas.

- Incidencias detectadas.

- Acciones realizadas.

- Recomendaciones futuras.

Valor aportado Estas actuaciones permiten asegurar que la migración no solo finaliza correctamente desde el punto de vista técnico, sino que los sistemas quedan estables, operativos y optimizados en el nuevo CPD, reduciendo riesgos de incidencias posteriores.
##### APARTADO: INTELIGENCIA ARTIFICIAL (IA)
Requisito: II.1.13.1. Evaluar el rendimiento de los modelos seleccionados Requerimiento EducaMadrid Evaluar el rendimiento de los modelos de IA seleccionados en un entorno de prueba que simule las condiciones operativas de la plataforma EducaMadrid (IA1). Para ello se requiere estudiar:
- Métricas de Rendimiento: Utilizar métricas como la precisión, recall, F1-score, tiempo de
respuesta, y consumo de recursos (CPU, GPU, memoria) para evaluar el rendimiento.

- Escenarios de Prueba: Diseñar escenarios de prueba que representen las diferentes
funcionalidades y cargas de trabajo de la plataforma EducaMadrid.

- Herramientas de Evaluación: Utilizar herramientas de benchmarking y análisis de
rendimiento para medir y comparar el rendimiento de los modelos.

Se solicita:

- Diseñar y ejecutar pruebas de rendimiento.

- Recopilar y analizar los datos de rendimiento.

- Generar informes de rendimiento comparativo.

Propuesta técnica de empresa_s


Los especialistas de empresa_s realizarán la evaluación técnica y operativa de modelos de Inteligencia Artificial en entornos controlados que reproduzcan las condiciones reales de funcionamiento de EducaMadrid, garantizando una validación precisa de rendimiento, escalabilidad, consumo de recursos y calidad funcional. Se desplegará una plataforma de benchmarking y validación compatible con distintos tipos de modelos: LLMs, modelos NLP, modelos multimodales, modelos de embeddings, sistemas RAG y modelos de clasificación. Las pruebas incluirán:
- Métricas funcionales: precisión, recall, F1-score, accuracy, coherencia de respuesta y tasa
de alucinación.

- Métricas operativas: latencia, throughput, concurrencia, tiempo de inferencia y estabilidad
bajo carga.

- Métricas de infraestructura: uso de CPU/GPU, consumo de VRAM/RAM, almacenamiento
temporal y eficiencia computacional.

empresa_s diseñará escenarios de prueba representativos de EducaMadrid: asistentes virtuales, generación documental, búsqueda contextual, consultas concurrentes, escenarios de alta carga y degradación parcial de recursos. Para la evaluación se utilizarán herramientas especializadas como LM Evaluation Harness, DeepEval, RAGAS, Prometheus, Grafana y OpenTelemetry, permitiendo la captura centralizada de métricas, trazabilidad de inferencias y análisis detallado de comportamiento. Se ejecutarán comparativas entre modelos open-source, comerciales y modelos ajustados/finetuned, analizando:
- Calidad de respuesta,

- Coste computacional,

- Consumo de recursos,

- Escalabilidad,

- Adecuación funcional a escenarios educativos.

Finalmente se generarán informes técnicos comparativos con resultados de rendimiento, análisis de viabilidad, recomendaciones de implantación y necesidades de infraestructura para cada tipología de modelo evaluado. Propuesta de mejora , automatización y gobierno IA empresa_s propone evolucionar el sistema hacia una plataforma continua de evaluación y gobierno de modelos IA:
1. Plataforma automatizada de benchmarking IA:
- ejecución periódica de pruebas,

- comparativas automáticas entre modelos,

- detección de regresiones funcionales y de rendimiento.
2. Observabilidad avanzada de inferencias:
- monitorización en tiempo real,


- métricas GPU/CPU,

- trazabilidad completa de peticiones y respuestas.
3. Evaluación avanzada de LLMs y sistemas RAG:
- validación contextual,

- detección de alucinaciones,

- análisis de grounding y relevancia documental.

4. Optimización de costes e infraestructura:
- análisis coste/rendimiento,

- dimensionamiento GPU,

- evaluación de eficiencia operativa.

5. Gobierno del ciclo de vida IA:
- versionado de modelos,

- trazabilidad de datasets,

- auditoría de evaluaciones y resultados.
Valor aportado Estas actuaciones permitirán disponer de un entorno avanzado y controlado de validación IA, asegurando que los modelos implantados en EducaMadrid sean técnicamente viables, escalables y adecuados para entornos educativos de alta concurrencia. Requisito: II.1.13.2. Ingeniería de prompts adaptados para cada servicio Requerimiento EducaMadrid Desarrollar y optimizar prompts (instrucciones) específicos para cada servicio de la plataforma EducaMadrid, asegurando que los modelos de IA respondan de manera precisa y relevante (IA2). Para ello se requiere:
- Analizar Requisitos: Identificar los requisitos específicos de cada servicio y las expectativas
de los usuarios.

- Diseñar Prompts: Crear prompts detallados y claros que guíen a los modelos de IA para
generar respuestas adecuadas.

- Pruebas y Ajustes: Realizar pruebas iterativas para ajustar y optimizar los prompts en
función de los resultados obtenidos.

Se solicita:

- Analizar los requisitos de cada servicio.

- Diseñar y desarrollar prompts específicos.

- Realizar pruebas y ajustes iterativos.
Propuesta técnica de empresa_s


Los especialistas de empresa_s abordarán la ingeniería de prompts como un proceso estructurado de diseño, validación y optimización continua, orientado a garantizar que los modelos de IA respondan de forma precisa, contextual y alineada con las necesidades funcionales de los distintos servicios de EducaMadrid. empresa_s realizará un análisis funcional previo de cada servicio:
- Tipología de usuario,

- Objetivos del servicio,

- Nivel de precisión requerido,

- sensibilidad de la información,

- Casos de uso esperados,

- Restricciones funcionales y normativas.

Se diseñarán prompts específicos adaptados a cada escenario operativo:
- Asistentes virtuales,

- Soporte al usuario,

- Generación documental,

- Búsqueda contextual,

- Clasificación automática,

- Ayuda educativa y administrativa.

Los prompts incluirán:
- Definición de rol y comportamiento del modelo,

- Contexto funcional,

- Restricciones de respuesta,

- Formatos estructurados de salida,

- Control de tono y lenguaje,

- Mecanismos de reducción de alucinaciones.

empresa_s implantará metodologías avanzadas de prompt engineering:
- zero- shot,

- few-shot,

- chain- of-thought,

- contextual prompting,

- retrieval-augmented prompting (RAG).


Se desarrollará un proceso iterativo de validación y optimización:
- Ejecución de pruebas controladas,

- Análisis de calidad de respuesta,

- Evaluación de precisión y relevancia,

- Ajuste progresivo de prompts,

- Comparación entre variantes.

Las pruebas se realizarán utilizando datasets representativos y escenarios reales de EducaMadrid, evaluando:
- Coherencia,

- Estabilidad,

- Capacidad contextual,

- Robustez ante entradas ambiguas,

- Comportamiento bajo distintas cargas de uso.
empresa_s documentará el ciclo completo de ingeniería de prompts:
- Versiones,

- Cambios realizados,

- Resultados obtenidos,

- Recomendaciones de mejora,

- Trazabilidad funcional y técnica.

Propuesta de mejora , optimización y gobierno de prompts IA empresa_s propone evolucionar la ingeniería de prompts hacia una plataforma avanzada de gestión y gobierno de interacción IA:
1. Biblioteca centralizada de prompts:
- versionado de prompts,

- reutilización controlada,

- clasificación por servicios y casos de uso.

2. Sistema automatizado de evaluación:
- validación continua de respuestas,

- comparación automática entre variantes,

- detección de degradaciones funcionales.
3. Optimización contextual dinámica:
- adaptación de prompts según perfil de usuario,


- ajuste automático de contexto,

- mejora de precisión y relevancia.
4. Gobierno y trazabilidad:
- auditoría de cambios,

- histórico de versiones,

- control de calidad y aprobación.

5. Reducción de riesgos IA:
- mitigación de alucinaciones,

- control de respuestas no deseadas,

- refuerzo de seguridad y cumplimiento normativo.

Valor aportado Estas actuaciones permitirán disponer de un sistema avanzado y gobernado de ingeniería de prompts, asegurando respuestas más precisas, contextualizadas y alineadas con los servicios de EducaMadrid, mejorando la experiencia de usuario y reduciendo riesgos funcionales asociados al uso de IA generativa. Requisito: II.1.13.3. Testeo de los guardarraíles para el entorno educativo Requerimiento EducaMadrid Asegurar que los modelos de IA implementados en la plataforma EducaMadrid cumplan con las normativas y políticas educativas, incluyendo la protección de datos y la ética en el uso de la IA. (IA3). Para ello se requiere:
- Normativas y Políticas: Revisar las normativas y políticas educativas relevantes, incluyendo
la protección de datos personales (GDPR, LOPDGDD) y las directrices éticas.

- Guardarraíles Técnicos: Implementar mecanismos de control y monitoreo para asegurar
que los modelos de IA no generen respuestas inapropiadas o perjudiciales.

- Pruebas de Seguridad: Realizar pruebas de seguridad y privacidad para identificar y mitigar
posibles vulnerabilidades. Se solicita:

- Revisar y documentar las normativas y políticas relevantes.

- Implementar y configurar los guardarraíles técnicos.

- Realizar pruebas de seguridad y privacidad.
Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la implantación y validación de guardarraíles IA como un sistema integral de protección, control y supervisión, orientado a garantizar un uso seguro, ético y alineado con el marco normativo educativo de EducaMadrid. empresa_s realizará una revisión completa del marco regulatorio aplicable:
- GDPR,


- LOPDGDD,

- ENS,

- AI Act europeo,

- directrices éticas de IA,

- políticas internas de seguridad y protección del menor.
Se definirán políticas específicas de comportamiento IA para entornos educativos:
- control de lenguaje inapropiado,

- prevención de generación de contenido sensible,

- limitación de respuestas sesgadas,

- protección frente a fuga de información,

- control de generación de contenido perjudicial o no permitido.

empresa_s implantará guardarraíles técnicos multinivel:
- filtros de entrada y salida,

- validación contextual de prompts,

- detección de jailbreaks y prompt injection,

- sistemas de moderación automática,

- validación semántica de respuestas,

- limitación de acceso a información sensible.

Las pruebas de validación incluirán:
- ataques de evasión de restricciones,

- generación de contenido inapropiado,

- pruebas de extracción de datos,

- validación de anonimización,

- simulaciones de uso malicioso,

- pruebas de robustez contextual.

Se utilizarán herramientas y frameworks especializados de AI Safety y observabilidad:
- NeMo Guardrails,

- Llama Guard,

- Langfuse,

- OpenTelemetry,


- sistemas SIEM y monitorización centralizada.

empresa_s realizará pruebas continuas de seguridad y privacidad:
- análisis de vulnerabilidades,

- validación de cumplimiento normativo,

- revisión de trazabilidad,

- pruebas de exposición de datos personales,

- auditoría de respuestas generadas.
Finalmente se elaborará documentación técnica y normativa incluyendo:
- políticas de uso IA,

- configuración de guardarraíles,

- escenarios de riesgo,

- resultados de pruebas,

- recomendaciones de mitigación y mejora.

Propuesta de mejora, seguridad y gobierno IA empresa_s propone evolucionar el sistema hacia una plataforma avanzada de AI Safety y gobierno de modelos:
1. Plataforma centralizada de guardarraíles:
- políticas unificadas,
- control transversal de modelos,
- gestión centralizada de restricciones.
2. Supervisión continua de comportamiento IA:
- monitorización de respuestas,
- detección automática de anomalías,
- análisis de riesgos emergentes.
3. Protección avanzada frente a ataques IA:
- detección de prompt injection,
- mitigación de jailbreaks,
- protección frente a exfiltración de datos.
4. Gobierno y cumplimiento normativo:
- trazabilidad de inferencias,
- auditoría completa,
- adaptación continua al AI Act y ENS.
5. Evaluación ética y contextual:
- control de sesgos,
- protección del entorno educativo,
- validación de respuestas seguras para menores.
Valor aportado Estas actuaciones permitirán disponer de un entorno IA seguro, gobernado y alineado con las normativas educativas y de protección de datos, garantizando que los modelos desplegados en EducaMadrid operen bajo criterios de seguridad, ética y control continuo.


Requisito: II.1.13.4. Evaluar posibilidades de integración en distintos aplicativos Requerimiento EducaMadrid Evaluar la viabilidad de integrar los modelos de IA en diferentes aplicativos y servicios de la plataforma EducaMadrid (IA4). Para ello se requiere:
- Compatibilidad Técnica: Evaluar la compatibilidad técnica de los modelos de IA con los
diferentes aplicativos y servicios.

- Interfaz de Integración: Diseñar y desarrollar interfaces de integración que permitan la
comunicación y el intercambio de datos entre los modelos de IA y los aplicativos.

- Pruebas de Integración: Realizar pruebas de integración para asegurar que los modelos
de IA funcionen correctamente en el contexto de los diferentes aplicativos.

Se solicita:

- Evaluar la compatibilidad técnica de los modelos de IA.

- Diseñar y desarrollar interfaces de integración.

- Realizar pruebas de integración.
Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la integración de modelos de Inteligencia Artificial como un proceso de interoperabilidad y adaptación tecnológica orientado a garantizar su incorporación eficiente, segura y escalable dentro del ecosistema de aplicaciones y servicios de EducaMadrid . empresa_s realizará un análisis de compatibilidad técnica entre los modelos IA y los distintos entornos de la plataforma:
- aplicativos web,
- plataformas educativas,
- sistemas documentales,
- servicios cloud,
- herramientas colaborativas,
- sistemas de autenticación y APIs existentes.
La evaluación contemplará:
- compatibilidad de protocolos,
- formatos de intercambio de datos,
- requisitos de infraestructura,
- latencia y tiempos de respuesta,
- necesidades GPU/CPU,
- escalabilidad y concurrencia.
Se analizarán distintos mecanismos de integración:
- APIs REST,
- gRPC,
- WebSockets,
- colas de mensajería,
- integración mediante microservicios,
- arquitecturas orientadas a eventos.
empresa_s diseñará interfaces de integración desacopladas y reutilizables:


- pasarelas de comunicación IA,
- servicios middleware,
- normalización de peticiones,
- control de autenticación y autorización,
- gestión de sesiones y contexto conversacional.
Las pruebas de integración incluirán:
- validación funcional,
- pruebas de carga,
- interoperabilidad entre sistemas,
- tolerancia a fallos,
- continuidad operativa ante degradaciones parciales.
Se evaluarán distintos escenarios de despliegue:
- inferencia local,
- entornos híbridos,
- integración cloud,
- modelos on-premise,
- arquitecturas GPU compartidas.
empresa_s documentará la arquitectura de integración:
- diagramas de flujo,
- dependencias entre servicios,
- requisitos técnicos,
- recomendaciones de implantación,
- procedimientos de escalado y mantenimiento.
Propuesta de mejora, interoperabilidad y arquitectura IA empresa_s propone evolucionar la integración IA hacia una arquitectura modular y gobernada de servicios inteligentes:
1. Plataforma centralizada de integración IA:
- APIs unificadas,
- servicios desacoplados,
- reutilización transversal de capacidades IA.
2. Arquitectura escalable basada en microservicios:
- despliegue independiente de modelos,
- balanceo de carga,
- alta disponibilidad y tolerancia a fallos.
3. Middleware inteligente de orquestación:
- gestión de contexto,
- enrutamiento dinámico de peticiones,
- selección automática de modelos.
4. Observabilidad y trazabilidad completa:
- monitorización de integraciones,
- métricas de uso y latencia,
- auditoría de peticiones e inferencias.
5. Optimización de costes y recursos:
- compartición eficiente de GPU,
- escalado dinámico,
- optimización de consumo computacional.
Valor aportado


Estas actuaciones permitirán disponer de una arquitectura de integración IA flexible, segura y escalable, facilitando la incorporación progresiva de capacidades de Inteligencia Artificial dentro de los distintos servicios de EducaMadrid sin comprometer estabilidad, rendimiento ni seguridad operativa. Requisito: II.1.13.5. Evaluación de capacidades de respuesta y límites por usuario Requerimiento EducaMadrid Evaluar las capacidades de respuesta de los modelos de IA y establecer límites razonables para el uso por parte de los usuarios, asegurando un rendimiento óptimo y una experiencia de usuario satisfactoria (IA5). Para ello se requiere:
- Capacidades de Respuesta: Medir el tiempo de respuesta de los modelos de IA bajo
diferentes condiciones de carga y uso.

- Límites por Usuario: Establecer límites en función del número de solicitudes por usuario y
el tiempo de inactividad para evitar sobrecargas y asegurar un uso equitativo.

- Pruebas de Estrés: Realizar pruebas de estrés para evaluar el comportamiento de los
modelos de IA bajo condiciones de alta demanda. Se solicita:

- Medir y analizar las capacidades de respuesta de los modelos de IA.

- Establecer y documentar los límites por usuario.

- Realizar pruebas de estrés y ajustar los límites según sea necesario.

Propuesta técnica de empresa_s Los especialistas de empresa_s abordarán la evaluación de capacidades de respuesta y control de uso de modelos IA como un proceso integral de dimensionamiento, gobernanza y optimización operativa, orientado a garantizar estabilidad, escalabilidad y calidad de servicio dentro de EducaMadrid. empresa_s realizará pruebas de rendimiento e inferencia sobre distintos escenarios de utilización:
- consultas concurrentes,
- generación de contenido,
- procesamiento documental,
- asistentes conversacionales,
- búsquedas contextuales,
- cargas mixtas de usuarios.
La evaluación incluirá:
- tiempo medio de respuesta,
- latencia por token,
- throughput,
- sesiones concurrentes soportadas,
- consumo CPU/GPU,
- uso de VRAM/RAM,
- comportamiento ante saturación.
Se diseñarán escenarios de estrés progresivo para validar:
- degradación controlada del servicio,


- estabilidad bajo alta demanda,
- recuperación tras sobrecarga,
- tolerancia a fallos,
- impacto sobre otros servicios compartidos.
empresa_s establecerá políticas de límites de uso adaptadas a perfiles y servicios:
- número máximo de solicitudes,
- límites de concurrencia,
- ventanas temporales de uso,
- límites por sesiones activas,
- control de tiempo de inactividad,
- cuotas diferenciadas según tipología de usuario.
Se implementarán mecanismos técnicos de control y rate limiting:
- limitación dinámica de peticiones,
- colas de inferencia,
- priorización de servicios críticos,
- balanceo de carga,
- control de sesiones persistentes.
Para la monitorización y análisis se utilizarán herramientas especializadas como Prometheus, Grafana, OpenTelemetry y sistemas de observabilidad de inferencia IA, permitiendo trazabilidad completa del comportamiento del sistema. Finalmente se generará documentación técnica con:
- capacidades máximas soportadas,
- límites operativos recomendados,
- análisis de comportamiento bajo carga,
- recomendaciones de escalabilidad,
- criterios de dimensionamiento futuro.
Propuesta de mejora, optimización y gobierno de consumo IA empresa_s propone evolucionar la gestión de capacidades IA hacia una plataforma inteligente de control de consumo y calidad de servicio:
1. Sistema dinámico de rate limiting:
- adaptación automática según carga,
- priorización de usuarios y servicios,
- prevención de saturaciones.
2. Gestión avanzada de concurrencia:
- colas inteligentes de inferencia,
- distribución equilibrada de carga,
- control de sesiones activas.
3. Observabilidad avanzada de rendimiento:
- métricas en tiempo real,
- análisis predictivo de saturación,
- detección temprana de degradaciones.
4. Optimización de costes computacionales:
- uso eficiente de GPU,
- autoescalado de recursos,
- optimización de inferencia.
5. Gobierno y trazabilidad del consumo:
- auditoría de uso por usuario,


- métricas de consumo IA,
- generación de informes de capacidad y utilización.
Valor aportado Estas actuaciones permitirán disponer de una plataforma IA estable, escalable y gobernada, garantizando tiempos de respuesta adecuados, control eficiente del consumo de recursos y una experiencia de usuario óptima incluso en escenarios de alta concurrencia. 3.1.6.2 Servicio de Mantenimiento 24/7 y CAU Dentro de las labores de desarrollo correctivo y gestión de incidencias, empresa_s no sólo garantizará la resolución técnica de los problemas detectados, sino que también llevará a cabo una actualización continua de la documentación funcional y técnica de la plataforma EducaMadrid. Esta documentación, que podrá generarse tanto en formato textual como audiovisual, estará orientada a facilitar la correcta utilización de los servicios por parte de la comunidad educativa (docentes, alumnado y familias), así como a mejorar la capacidad de autoservicio del usuario a través del portal CAU. En este contexto, el servicio se prestará conforme a un modelo integral que combina:

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
funcional de EducaMadrid, responsables de la resolución de incidencias de primer nivel, atención a consultas, asistencia a usuarios y canalización de incidencias. Página 202 de 239


- Nivel 2/3 (Soporte técnico especializado): Integrado por analistas programadores y
técnicos de sistemas, que abordarán incidencias de carácter técnico o aquellas que requieran intervención en código, arquitectura o infraestructuras. Este modelo garantiza una atención eficiente, escalable y especializada, optimizando los tiempos de resolución y asegurando la calidad del servicio.

3. Cobertura funcional y soporte a usuarios. Modelo CAU
El Centro de Atención a Usuarios (CAU) constituye el eje central del servicio de soporte de EducaMadrid, actuando como punto único de contacto (Single Point of Contact – SPOC) para la gestión de incidencias, consultas, solicitudes y comunicaciones con los usuarios finales (docentes, alumnado y familias). Su diseño responde a un modelo estructurado, trazable y orientado a servicio, que garantiza la calidad, eficiencia y control en la atención a los centros educativos. Principios del modelo CAU El modelo CAU se basa en los siguientes principios fundamentales:
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


3.2 Planificación del Servicio 3.2.1 Calendario de los trabajos a desarrollar


![Imagen de la página 207](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0207-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0207-imagen-003.png -->
- Leyenda de perfiles, fases, niveles de participación e hitos de un cronograma.
- Define abreviaturas para arquitectura, sistemas, bases de datos, desarrollo Linux e inteligencia artificial.
- Los colores distinguen inicio, ejecución, mantenimiento y cierre; los puntos indican participación alta, media o baja.
- Los hitos globales cubren bases de datos, monitorización, servicios, nube, sistemas, correo, aulas, LDAP, seguridad e IA.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0207-imagen-003.png -->

![Imagen de la página 207](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0207-imagen-004.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0207-imagen-004.png -->
- Cronograma de doce meses para gestionar una migración de servidores entre centros de proceso de datos, desde septiembre de 2026.
- Planifica coordinación, preparación técnica, documentación, ejecución, verificación y soporte posterior.
- Las barras separan planificación, ejecución, mantenimiento y cierre, y los hitos marcan finalización técnica, migración, validación y soporte en agosto de 2027.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0207-imagen-004.png -->


![Imagen de la página 208](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0208-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0208-imagen-003.png -->
- Cronograma de doce meses para ciberseguridad, sistema operativo MAX e inteligencia artificial.
- Seguridad incluye DNS, LDAP privilegiado, certificados, vulnerabilidades, detección, auditorías, registros, claves RSA y soporte; MAX cubre mantenimiento, distribuciones, aplicaciones y asistencia; IA cubre modelos, prompts, guardarraíles e integraciones.
- Las barras muestran planificación, ejecución, soporte y cierre, con hitos desde noviembre de 2026 hasta agosto de 2027.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0208-imagen-003.png -->


![Imagen de la página 209](<oferta_tecnica_sistemas_empresa_s_assets/pagina-0209-imagen-003.png>)

<!-- INICIO DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0209-imagen-003.png -->
- Cronograma de doce meses para el resto de áreas de trabajo entre septiembre de 2026 y agosto de 2027.
- Incluye bases de datos, monitorización, servicios y herramientas, nube, SSO y datos, correo, aulas virtuales y LDAP.
- Cada bloque combina planificación, ejecución principal, mantenimiento continuo y cierre.
- Los hitos de agosto de 2027 señalan entornos optimizados, monitorización completa, servicios operativos, nube estable, correo escalado, aulas ampliadas y LDAP actualizado.
<!-- FIN DESCRIPCIÓN DE LA IMAGEN: oferta_tecnica_sistemas_empresa_s_assets/pagina-0209-imagen-003.png -->

3.2.2 Análisis de riesgos del proyecto Enfoque General y Objetivos La Gestión de Riesgos del servicio tiene como objetivo identificar, analizar, evaluar, planificar y controlar de manera sistemática y proactiva todos los riesgos que puedan afectar a la continuidad, disponibilidad, seguridad, rendimiento, calidad y evolución de los sistemas que conforman la plataforma EducaMadrid, garantizando en todo momento la prestación óptima del servicio y la protección de los activos tecnológicos y de la información. Este proceso se orienta no solo a la mitigación de amenazas, sino también a la anticipación de situaciones adversas, mediante la implantación de mecanismos de detección temprana, monitorización continua y análisis predictivo, que permitan reducir la probabilidad de ocurrencia de incidencias y minimizar su impacto en caso de materializarse. Dado el carácter crítico de los servicios prestados que incluyen sistemas clave como el Portal Educativo, Aulas Virtuales, sistemas de correo electrónico, infraestructura cloud, autenticación centralizada (LDAP/SSO) y servicios de inteligencia artificial, la gestión de riesgos se concibe como un proceso transversal e integrado en la operación diaria del servicio, alineado con las mejores prácticas de gestión de servicios TI (ITSM) y gestión de proyectos. Asimismo, se garantizará que todas las actividades de gestión de riesgos estén plenamente alineadas con los Acuerdos de Nivel de Servicio (ANS), de manera que cualquier riesgo identificado sea evaluado en términos de su impacto sobre la disponibilidad, capacidad de respuesta y tiempos de resolución establecidos contractualmente, permitiendo la activación inmediata de mecanismos de contingencia cuando proceda. De igual forma, la gestión de riesgos se integrará con los requisitos del Esquema Nacional de Seguridad (ENS), en categoría MEDIA, asegurando que los riesgos relacionados con la seguridad de la información, la confidencialidad, integridad, disponibilidad, autenticidad y trazabilidad sean identificados, analizados y tratados conforme a los principios de:
- Seguridad desde el diseño y por defecto.

- Principio de mínimo privilegio.

- Defensa en profundidad.

- Mejora continua.

En este contexto, el Plan de Gestión de Riesgos permitirá:
- Establecer un marco estructurado y repetible para la toma de decisiones ante
incertidumbre.

- Priorizar los esfuerzos sobre los riesgos que puedan comprometer los servicios críticos.

- Optimizar la asignación de recursos técnicos y humanos.

- Reducir el impacto económico, operativo y reputacional asociado a incidencias.

- Garantizar la continuidad del servicio incluso en escenarios adversos.

Finalmente, se adopta un enfoque de mejora continua, en el que los riesgos son revisados de forma periódica, actualizados en base a la evolución del servicio y retroalimentados mediante el análisis de incidencias reales, auditorías y métricas operativas, asegurando así que el sistema de gestión de riesgos evoluciona de forma coherente con la complejidad y criticidad del entorno EducaMadrid.


Fecha: 21/05/2026

Dada la criticidad del servicio (portal educativo, correo, aulas virtuales, cloud, LDAP, etc.), la gestión de riesgos adoptará un enfoque:
- Preventivo y continuo;

- Basado en criticidad del servicio;

- Integrado con seguridad (ENS nivel MEDIO);

- Orientado a servicio 24x7.
Se establece una gestión viva del riesgo, integrada en la operación diaria. Alcance del Plan de Riesgos Aplica a:
- Servicios críticos:

o Portal Educativo (Liferay). o Aulas Virtuales (Moodle).

o Correo electrónico (≈2M usuarios).

o Cloud (NextCloud). o LDAP / SSO.

o MAX Linux. o IA y sistemas analíticos.

- Infraestructura:
o ~700 servidores.

o 3.500 bases de datos.

- Procesos:

o Mantenimiento evolutivo y correctivo.

o Migraciones CPD. o Seguridad y ENS.

o Operación bajo ANS.

Organización y Gobierno del Riesgo

##### Roles y Responsabilidades:

Rol Responsabilidades Jefe de Proyecto (empresa_s) Responsable global del plan y decisiones Responsable del contrato (EducaMadrid) Priorización y validación


Fecha: 21/05/2026

Equipo técnico Identificación y tratamiento activo Responsable de seguridad Riesgos ENS / ciberseguridad Propietario del riesgo Responsable de mitigación

Se asignar á un propietario a todos los riesgos críticos (accountability clara).

##### Comités y Cadencia:

- Comité mensual de riesgos

- Revisión semanal en comité técnico

- Revisión extraordinaria ante incidencias críticas
Metodología de Gestión de Riesgos

Proceso aplicado:

Se estructura en 6 fases:
- Planificación;

- Identificación;

- Análisis cualitativo;

- Análisis cuantitativo (para riesgos críticos);

- Respuesta;

- Seguimiento y control.

Identificación de Riesgos

##### Enfoque

- Identificación continua (iterativa, mensual y ad- hoc).

- Implicación de todo el equipo.

- Fuentes:
o Experiencia previa.

o Históricos Redmine. o ANS e incidencias reales.

o ENS (riesgos de seguridad)

##### Principales categorías de riesgo

Se definen categorías específicas del contexto EducaMadrid:


Fecha: 21/05/2026

- Operacionales.

- Tecnológicos.

- Seguridad / ENS.

- Datos.

- Personas / equipo.

- Cumplimiento.

- Dependencias externas.

##### Catálogo inicial de riesgos (muy valorable en pliego)

Código Riesgo Impacto R1 Caída del portal educativo Crítico R2 Indisponibilidad de aulas virtuales Crítico R3 Fallo masivo de correo Crítico R4 Brecha de seguridad (ENS) Crítico R5 Corrupción de bases de datos Crítico R6 Error en migración CPD Alto R7 Fallo en SSO/LDAP Crítico R8 Saturación de infraestructura Alto R9 Fallos en despliegues/actualizaciones Alto R10 Pérdida de personal clave Medio R11 Riesgos derivados de IA (modelos locales) Medio R12 Incumplimiento ANS Crítico

Análisis Cualitativo de Riesgos

##### Matriz Probabilidad- Impacto

Se establece matriz 5x5: Impacto \\ Probabilidad Muy baja Baja Media Alta Muy alta Impacto evaluado sobre:
- Servicio

- Usuarios

- Seguridad

- ANS


- Imagen institucional

##### Factores adicionales

- Urgencia.

- Detectabilidad.

- Reputación.

- Cumplimiento ENS.

##### Priorización

Clasificación: � Crítico → acción inmediata. � Alto → plan de mitigación. � Medio → seguimiento. � Bajo → monitorización. Análisis Cuantitativo de Riesgos Aplicado a:
- Caídas de servicio.

- Pérdida de datos.

- Impacto ANS.
Técnicas:
- Simulación de impacto (Monte Carlo en planificación).

- Análisis de disponibilidad vs ANS.

- Árboles de decisión para contingencias.

Planificación de Respuesta a Riesgos

##### Estrategias para amenazas

- Evitar.

- Mitigar.

- Transferir.

- Aceptar.

##### Ejemplos concretos


Fecha: 21/05/2026

Riesgo Estrategia Acción Caída portal Mitigar Alta disponibilidad + balanceo Corrupción BBDD Mitigar Backups + replicación Brecha seguridad Evitar Hardening + auditorías Migración CPD Mitigar Plan piloto + rollback

Planes de mitigación Incluyen:
- Procedimiento de rollback.

- Sistema alternativo operativo.

- Activación escalado N2/N3.

- Comunicación institucional.

Seguimiento y Control de Riesgos

##### Monitorización continua

Basada en:
- Sistemas de monitorización.

- Logs centralizados.

- Métricas de servicio.

##### Indicadores (KPIs de riesgo)

- Nº incidencias críticas.

- Tiempo medio de resolución.

- % cumplimiento ANS.

- Nº vulnerabilidades abiertas.

- Disponibilidad servicios críticos.

##### Revisión de riesgos

- Reevaluación mensual.

- Reevaluación tras incidencia crítica.

- Auditorías periódicas (ENS).

Integración con Seguridad (ENS) El plan incorpora plenamente el ENS: Página 215 de 239


- Mínimo privilegio.

- Seguridad desde el diseño.

- Desarrollo seguro.
Incluye:
- Análisis de vulnerabilidades.

- Auditorías internas.

- Gestión de certificados.

- Monitorización de intrusiones.

Integración con ANS El plan de riesgos está conectado con ANS:
- Identificación de riesgos = base de ANS.

- Respuestas = procedimientos de incidentes.

- Seguimiento = cumplimiento SLA:
o Respuesta ≤ 2h.

o Resolución:

- Crítico ≤ 6h.

- Grave ≤ 12h.

- Leve ≤ 24h.

Herramientas de Gestión
- Redmine (registro y trazabilidad).

- Sistemas de monitorización.

- CMDB.

- Herramientas de ticketing.

Entregables del Plan de Riesgos
- Registro de riesgos (vivo).

- Informes mensuales.

- Informes post-incidente.

- Actualizaciones del plan.

- Cuadro de mando de riesgos.


3.2.3 Plan de gestión de contingencias Objetivo del Plan El presente Plan de Gestión de Contingencias se establece como un instrumento estratégico y operativo cuyo propósito es garantizar de forma integral la continuidad, disponibilidad, integridad y seguridad de todos los sistemas que conforman la plataforma EducaMadrid ante cualquier evento adverso, ya sea de origen técnico, organizativo, funcional o de ciberseguridad. Este Plan no se limita a la reacción ante contingencias, sino que establece un modelo integral basado en:
- Prevención inteligente.

- Respuesta rápida y automatizada.

- Recuperación garantizada.

- Mejora continua.

Asegurando así que la plataforma EducaMadrid mantenga en todo momento los más altos niveles de calidad, seguridad y disponibilidad exigidos en el pliego. Dada la criticidad de la plataforma que presta servicio a millones de usuarios de la comunidad educativa y soporta procesos clave de enseñanza, comunicación y gestión este plan se diseña bajo un enfoque de resiliencia operativa avanzada, orientado no sólo a la recuperación, sino a la anticipación, mitigación y adaptación dinámica frente a situaciones de riesgo. En este sentido, el plan persigue:
- Minimizar el impacto de cualquier interrupción en los servicios.

- Garantizar el cumplimiento estricto de los ANS y requisitos del ENS.

- Reducir los tiempos de recuperación (RTO) y pérdida de datos (RPO).

- Asegurar una respuesta coordinada, rápida y eficaz ante incidentes.

Asimismo, este plan se encuentra completamente alineado con:
- El modelo de prestación del servicio (TIPO A, B y C).

- Los requerimientos de continuidad del servicio en entornos productivos.

- La necesidad de soporte 24/7 y gestión de incidencias bajo SLA definidos.

Cobertura del Plan El plan se articula en torno a cuatro grandes ejes de actuación que cubren de manera transversal toda la operación del servicio:

##### Mantenimiento correctivo, evolutivo y adaptativo

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
Enfoque de contingencia Diseño de entornos de preproducción y pruebas para evitar impactos en producción.
- Uso de estrategias de despliegue seguro (blue/green, rolling updates).

- Definición de procedimientos rollback automáticos.

- Validación mediante pruebas funcionales, de rendimiento y seguridad antes de producción.

Este enfoque reduce el riesgo de introducción de fallos y garantiza la continuidad del servicio durante cualquier cambio.

##### Gestión de incidencias bajo ANS (Acuerdos de Nivel de Servicio)

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
o Alta disponibilidad (HA).

o Redundancia de componentes.

o Escalabilidad horizontal y vertical.

- Sistemas priorizados:

o Portal educativo. o Aulas virtuales.

o Cloud educativo.

o Correo electrónico. o LDAP/SSO.

- Medidas implementadas:
o Balanceadores de carga.

o Clustering de servicios críticos.

o Replicación de bases de datos. o Redistribución dinámica de cargas.

- Optimización para entorno educativo:


o Planificación de tareas críticas fuera de periodos lectivos.

o Adaptación a picos de demanda (inicio de curso, evaluaciones).

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

o Activación de sistemas redundantes.

o Failover automático o manual. o Validación post-recuperación.

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

o Pruebas funcionales completas.

o Verificación de integridad de datos. o Confirmación de disponibilidad del servicio.

Catálogo de riesgos y su integración con contingencias A continuación se presenta el núcleo del modelo integrado:

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


Fecha: 21/05/2026

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
Integración operativa riesgos ↔ contingencias El modelo se materializa mediante la siguiente correspondencia: Gestión de riesgos Gestión de contingencias


Fecha: 21/05/2026

Identificación Protocolos definidos Evaluación Prioridad de actuación Prevención Medidas arquitectónicas Riesgo materializado Activación contingencia Seguimiento Mejora continua

La integración entre el Plan de Riesgos y el Plan de Contingencias permite:

- Anticipar problemas antes de que ocurran.

- Reducir drásticamente el impacto de incidentes.
- Garantizar la continuidad de servicios críticos.

- Cumplir estrictamente ANS y ENS.
En definitiva, se establece un modelo que no solo gestiona incidencias, sino que controla el riesgo estructural del servicio, posicionando la operación de EducaMadrid en un nivel de madurez y excelencia operativa superior. Monitorización y detección temprana Elemento clave de integración:

- Monitorización técnica (infraestructura).
- Monitorización funcional (servicio).

- Monitorización de seguridad (logs, IDS).
Permite detectar riesgos antes de que se conviertan en incidencias. Gobierno y roles

- Jefe de Proyecto: supervisión global.

- Arquitecto IT: gestión de riesgos técnicos.
- Equipo sistemas: contingencias operativas.

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
seleccionando proveedores clave y fomentando la colaboración para la mejora conjunta. El modelo de gestión se basa en tres pilares principales: procesos, servicios y personas. Pensamiento basado en riesgos empresa_s considera fundamental la integración del enfoque basado en riesgos como elemento clave para garantizar la eficacia, solidez y capacidad de adaptación del Sistema de Gestión de la Calidad. Este enfoque permite anticipar posibles desviaciones antes de que se materialicen, así como identificar oportunidades de mejora que aporten un valor añadido al servicio. En este sentido, la organización adopta una visión proactiva de la gestión, basada en la identificación sistemática de riesgos e incertidumbres asociados a los procesos, actividades y entregables. Esto implica no solo reaccionar ante incidencias una vez producidas, sino también establecer medidas preventivas orientadas a minimizar su probabilidad de ocurrencia o mitigar su impacto. Durante todo el ciclo de vida del servicio, se aplicará un procedimiento estructurado para la gestión de riesgos y oportunidades, que incluye las siguientes actividades: identificación, análisis, evaluación, planificación de respuestas, seguimiento y revisión continua. Este proceso permitirá priorizar los riesgos en función de su criticidad, asignar responsables y definir acciones concretas para su tratamiento. Asimismo, se contemplará la gestión de oportunidades como parte integral del sistema, promoviendo la identificación de mejoras potenciales en los procesos, la optimización de recursos


y la innovación en la prestación del servicio. En este contexto, cada oportunidad será evaluada considerando también los riesgos asociados a su implementación, asegurando una toma de decisiones equilibrada y fundamentada. Para reforzar la eficacia de este enfoque, se utilizarán herramientas de apoyo como matrices de riesgos, análisis cualitativos y cuantitativos, indicadores de seguimiento y mecanismos de control integrados en los procesos operativos. Todo ello permitirá disponer de información fiable y actualizada para la toma de decisiones. Este enfoque basado en riesgos se encuentra plenamente integrado en el ciclo PHVA y en la gestión por procesos, lo que garantiza su aplicación transversal en todas las fases del proyecto. De este modo, se contribuye a mejorar el rendimiento global del sistema, incrementar la calidad de los resultados y reforzar la capacidad de la organización para adaptarse a entornos cambiantes. En definitiva, la adopción de este enfoque no solo permite prevenir incidencias y asegurar el cumplimiento de los requisitos, sino que también impulsa una cultura organizativa orientada a la anticipación, la mejora continua y la excelencia en la prestación del servicio. Enfoque por procesos y mejora continua La organización adopta un enfoque de gestión basado en procesos como pilar fundamental de su sistema de calidad, estructurando todas sus actividades mediante procesos claramente definidos, documentados y gestionados de forma interrelacionada. Este modelo permite garantizar la coherencia, eficiencia y trazabilidad de todas las actuaciones, asegurando su alineación tanto con la política de calidad como con la estrategia global de la organización. Cada proceso se concibe como un conjunto de actividades interconectadas que transforman entradas en resultados, con responsabilidades, recursos y criterios de control previamente establecidos. Esta visión facilita una gestión integral que va más allá de áreas funcionales aisladas, promoviendo la coordinación entre equipos, la optimización de recursos y la eliminación de ineficiencias. Asimismo, se definen indicadores específicos para cada proceso, lo que permite evaluar su desempeño de manera objetiva y continua. El enfoque por procesos se complementa con una gestión activa de sus interrelaciones, garantizando que las salidas de un proceso constituyan entradas adecuadas para los siguientes. Esto contribuye a asegurar la calidad global del servicio, minimizando errores derivados de descoordinaciones o falta de alineamiento entre actividades. Sobre esta base, se integra de forma transversal el principio de mejora continua , entendido como un proceso sistemático y permanente orientado a incrementar la eficacia y eficiencia del sistema de gestión. Para ello, se establecen mecanismos de seguimiento, revisión y retroalimentación que permiten identificar oportunidades de mejora, implementar acciones correctivas y preventivas, y consolidar las lecciones aprendidas. Este modelo se sustenta en la aplicación rigurosa del ciclo PHVA (Planificar, Hacer, Verificar y Actuar), que proporciona una metodología estructurada para la gestión y optimización de los procesos. A través de este ciclo, la organización planifica sus actuaciones, ejecuta las actividades definidas, evalúa los resultados obtenidos y adopta medidas de mejora que se integran nuevamente en el sistema, generando un proceso continuo de evolución y aprendizaje. Adicionalmente, el enfoque incorpora de manera explícita una visión basada en riesgos y oportunidades, lo que permite anticipar posibles desviaciones antes de que se materialicen, así como identificar aquellas áreas donde se puede generar un mayor valor. Este análisis se integra en todas las fases del proceso, desde la planificación hasta la evaluación, reforzando la capacidad de anticipación y la resiliencia del sistema. En conjunto, este enfoque por procesos, apoyado en el ciclo PHVA y en la gestión de riesgos, permite disponer de un sistema de calidad robusto, dinámico y orientado a resultados, que no solo


garantiza el cumplimiento de los requisitos, sino que impulsa de manera constante la mejora continua, la innovación y la excelencia en la prestación del servicio. Ciclo PHVA El ciclo PHVA constituye el eje fundamental sobre el que se articula el sistema de gestión de la calidad de empresa_s , permitiendo asegurar un enfoque sistemático, estructurado y orientado a la mejora continua en la ejecución de los servicios. Su aplicación garantiza no solo el cumplimiento de los requisitos establecidos, sino también la capacidad de adaptación y optimización constante del desempeño del proyecto. Este modelo se aplica de manera transversal a todos los procesos y actividades del servicio, integrando el enfoque basado en riesgos y la orientación a resultados, lo que permite anticipar desviaciones, maximizar oportunidades y reforzar la eficiencia operativa. El ciclo se desarrolla a través de las siguientes fases:
- Planificar (Plan): En esta fase se establecen las bases del sistema de calidad, definiendo
los objetivos específicos del proyecto, alineados con las necesidades del cliente y la estrategia de la organización. Se identifican y asignan los recursos necesarios (humanos, técnicos y organizativos), así como los indicadores clave de rendimiento (KPIs) que permitirán evaluar el grado de cumplimiento. Asimismo, se realiza un análisis exhaustivo de riesgos y oportunidades, diseñando planes de acción orientados a prevenir posibles incidencias y a potenciar aquellos factores que puedan generar valor añadido. También se definen los procedimientos, metodologías y controles que regirán la ejecución del servicio, garantizando una planificación robusta, coherente y orientada a resultados.
- Hacer (Do): Esta fase corresponde a la implementación de lo planificado, asegurando que
todos los procesos se ejecutan conforme a los procedimientos definidos y a los estándares de calidad establecidos. Durante esta etapa, se coordina el trabajo de los equipos, se gestionan los recursos asignados y se aplican las herramientas y metodologías previstas. Se garantiza, además, la adecuada comunicación entre los distintos actores implicados, así como la correct a gestión de la información y la documentación generada. Todo ello se realiza bajo un enfoque de control continuo que permite mantener la alineación con los objetivos definidos.
- Verificar (Check): En esta fase se lleva a cabo el seguimiento y evaluación del desempeño
del proyecto mediante la medición sistemática de los indicadores definidos. Se analizan los resultados obtenidos, comparándolos con los objetivos establecidos, con el fin de detectar posibles desviaciones, no conformidades o áreas de mejora. Este proceso de verificación se apoya en herramientas de control, auditorías internas, revisiones periódicas y análisis de datos, lo que permite disponer de una visión objetiva y actualizada del estado del servicio. Asimismo, facilita la identificación de tendencias y la evaluación de la eficacia de las acciones implementadas.
- Actuar (Act): En función de los resultados obtenidos en la fase de verificación, se definen
e implementan las acciones necesarias para corregir desviaciones, prevenir su recurrencia y mejorar el desempeño global del sistema. Estas acciones pueden incluir ajustes en los procesos, optimización de recursos, revisión de metodologías o actualización de los objetivos establecidos. Además, las lecciones aprendidas y las mejoras identificadas se integran en el sistema de gestión, garantizando su aplicación en futuros proyectos y consolidando así un proceso de aprendizaje organizativo continuo. En conjunto, la aplicación rigurosa del ciclo PHVA permite establecer un modelo de gestión dinámico, orientado a la excelencia y basado en la mejora continua, asegurando la calidad del servicio, la satisfacción del cliente y la optimización permanente de los resultados.


Auditorías empresa_s dispone de un proceso estructurado de auditoría interna alineado con los requisitos de la norma ISO 9001, cuyo objetivo es garantizar el cumplimiento de los estándares de calidad definidos, así como verificar la eficacia del sistema de gestión a lo largo de todo el ciclo de vida del proyecto. Este proceso se configura como una herramienta clave para la mejora continua, la detección de desviaciones y el aseguramiento del servicio prestado. Para cada proyecto, se designan de forma expresa dos figuras fundamentales: un auditor interno, responsable de la planificación, ejecución y seguimiento de las auditorías, y un responsable de calidad del proyecto, encargado de coordinar las acciones necesarias y asegurar la correcta implementación de las mejoras derivadas de las auditorías. Esta separación de funciones garantiza la objetividad, independencia y rigor del proceso. El modelo de auditoría contempla tres tipologías principales, diseñadas para cubrir todas las fases del servicio:
- Auditoría inicial (o de arranque): Se realiza en las etapas iniciales del proyecto con el
objetivo de validar la correcta puesta en marcha del servicio. Permite analizar la adecuación de los procesos definidos, la correcta interpretación de los requisitos de calidad y la disponibilidad de los recursos necesarios. Asimismo, facilita la identificación temprana de posibles áreas de mejora o riesgos que puedan afectar al desarrollo del proyecto.
- Auditorías periódicas de seguimiento: Se llevan a cabo con una frecuencia establecida
(cada cuatro meses) y tienen como finalidad evaluar de forma continua el grado de cumplimiento de los procedimientos, estándares y objetivos de calidad. Estas auditorías permiten detectar posibles desviaciones, no conformidades o ineficiencias, así como verificar la correcta implementación de las acciones correctoras previamente definidas. Constituyen, además, un mecanismo clave para asegurar la estabilidad y control del servicio.
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
desarrollan conforme al marco metodológico definido.


Adicionalmente, los resultados de las auditorías se documentan en informes detallados que incluyen hallazgos, evidencias, posibles no conformidades y recomendaciones de mejora. Estos informes sirven como base para la definición de planes de acción específicos, cuyo seguimiento se realiza de manera sistemática hasta su completa resolución. En conjunto, este enfoque de auditoría no solo asegura el cumplimiento normativo y contractual, sino que también aporta valor añadido al proyecto, al favorecer la transparencia, reforzar la confianza del cliente y promover una cultura de mejora continua orientada a la excelencia. Gestión de no conformidades La gestión de no conformidades constituye un pilar esencial del sistema de control de calidad, orientado a asegurar la detección temprana de desviaciones, su adecuada resolución y la prevención de su recurrencia. Este proceso se basa en un enfoque sistemático, proactivo y alineado con los principios de mejora continua, garantizando la calidad del servicio a lo largo de todo su ciclo de vida. Para ello, se establecen sesiones periódicas de revisión y seguimiento en las que participan las distintas partes implicadas en el proyecto, incluyendo responsables técnicos, de calidad y representantes del cliente. Estas sesiones permiten evaluar de forma conjunta el estado del servicio, identificar incidencias de manera temprana y priorizar su tratamiento en función de su impacto y criticidad. Asimismo, se contempla la posibilidad de convocar sesiones extraordinarias ante la detección de no conformidades de carácter crítico, asegurando una respuesta ágil y eficaz. El proceso de gestión de no conformidades se articula en las siguientes fases:
- Identificación: Se lleva a cabo la detección sistemática de no conformidades reales o
potenciales a través de diferentes mecanismos, como revisiones internas, auditorías, controles de calidad, seguimiento de indicadores o feedback del cliente. Este enfoque integral permite no solo detectar incidencias ya materializadas, sino también anticiparse a posibles desviaciones antes de que impacten en el servicio.
- Análisis y definición de acciones correctoras: Una vez identificada la no conformidad,
se realiza un análisis detallado de sus causas raíz mediante técnicas específicas (como análisis causa- efecto o metodologías de resolución de problemas). A partir de este análisis, se definen las acciones correctoras necesarias para resolver la incidencia y evitar su repetición. Estas acciones incluyen la asignación de responsables, la definición de plazos y la priorización en función del nivel de riesgo asociado.
- Implementación: Se ejecutan las acciones correctoras y, en su caso, preventivas,
asegurando su correcta integración en la operativa del proyecto. Esta fase incluye la coordinación de los equipos implicados, la asignación de recursos necesarios y la adecuada comunicación de las medidas adoptadas.
- Seguimiento y verificación: Se realiza un seguimiento continuo de las acciones
implementadas con el fin de verificar su eficacia. Para ello, se utilizan indicadores de control y mecanismos de validación que permiten comprobar si la no conformidad ha sido resuelta de manera definitiva y si las medidas aplicadas han evitado su reaparición.
- Actualización y mejora del sistema: En función de los resultados obtenidos, se procede
a la actualización de los registros de riesgos, procedimientos y documentación del sistema de gestión de calidad, si fuera necesario. De este modo, las lecciones aprendidas se integran en la operativa habitual, fortaleciendo el sistema y contribuyendo a la mejora continua. Adicionalmente, todas las no conformidades y las acciones asociadas quedan registradas en herramientas de gestión específicas, lo que permite garantizar su trazabilidad completa, facilitar su análisis agregado y generar conocimiento reutilizable para futuros proyectos.


En conjunto, este enfoque estructurado y orientado a resultados permite no solo corregir incidencias de manera eficaz, sino también transformar cada no conformidad en una oportunidad de mejora, incrementando la madurez del sistema de calidad y reforzando la confianza del cliente. Enfoque a productos y servicios La gestión de calidad se aplica a todas las fases del servicio mediante procesos específicos. Planificación La fase de planificación de la calidad constituye un elemento clave para garantizar el éxito del proyecto, ya que permite establecer de forma anticipada los criterios, mecanismos y herramientas necesarios para asegurar el cumplimiento de los niveles de excelencia requeridos. En este sentido, se identificarán de manera exhaustiva todos los estándares de calidad aplicables, tanto normativos (como ISO 9001 u otros marcos de referencia) como específicos del cliente y del propio proyecto. A partir de este análisis, se definirán métricas e indicadores de rendimiento (KPIs) que permitan evaluar de forma objetiva el grado de cumplimiento de los requisitos establecidos. Estos indicadores estarán alineados con los objetivos estratégicos del servicio y cubrirán aspectos como la calidad técnica, la eficiencia operativa, la satisfacción del cliente y el cumplimiento de plazos. Asimismo, durante esta fase se diseñarán los mecanismos de seguimiento y control que permitirán medir de forma continua el desempeño del proyecto, facilitando la detección temprana de desviaciones y la adopción de medidas correctoras. Para ello, se establecerán cuadros de mando y sistemas de reporting adaptados a las necesidades de los distintos niveles de gestión. Con el fin de optimizar la toma de decisiones, se emplearán diversas herramientas y técnicas de análisis, entre las que destacan:
- Análisis coste- beneficio, que permitirá evaluar la viabilidad de las acciones de calidad,
garantizando un equilibrio adecuado entre la inversión realizada y el Valor aportado.

- Benchmarking o estudios comparativos, mediante los cuales se contrastarán prácticas,
metodologías y resultados con proyectos similares o referentes del sector, identificando oportunidades de mejora y factores de éxito.

- Diseño de experimentos, enfocado a determinar de manera objetiva qué variables
influyen en la calidad del producto o servicio, permitiendo optimizar procesos y minimizar riesgos.

- Técnicas de análisis y priorización, como matrices de decisión, análisis multicriterio o
metodologías colaborativas (tormentas de ideas, análisis de afinidad, etc.), que facilitarán la identificación y priorización de las acciones más relevantes. Adicionalmente, se integrará un enfoque preventivo basado en riesgos, mediante el cual se identificarán posibles amenazas y oportunidades desde el inicio del proyecto, definiendo planes de acción específicos para su mitigación o aprovechamiento. Esto permite no solo mejorar la calidad final, sino también incrementar la capacidad de anticipación y adaptación del equipo. En conjunto, esta planificación proporciona un marco estructurado, medible y orientado a resultados, que sirve como base para asegurar la calidad a lo largo de todo el ciclo de vida del servicio y fomentar una mejora continua sólida y sostenible. Apoyo La fase de apoyo resulta fundamental para asegurar la correcta implantación, mantenimiento y evolución del Sistema de Gestión de la Calidad, al garantizar que la organización dispone en todo momento de los recursos adecuados y alineados con los objetivos del proyecto.


En este contexto, se llevará a cabo una planificación detallada de los recursos necesarios, abarcando tanto los recursos humanos como los técnicos, tecnológicos y organizativos. Se definirá la estructura del equipo de trabajo, asegurando la asignación de perfiles con la cualificación, experiencia y competencias adecuadas para cada una de las funciones del proyecto. Asimismo, se promoverá el desarrollo continuo del equipo mediante acciones formativas específicas que permitan mantener y mejorar sus capacidades en materia de calidad, metodologías y herramientas. Por otro lado, se garantizará la disponibilidad de los medios técnicos y tecnológicos necesarios para el correcto desempeño de las actividades, incluyendo herramientas de gestión, plataformas de seguimiento, sistemas de control de calidad y entornos de desarrollo adecuados. Todo ello estará orientado a facilitar la eficiencia operativa, la trazabilidad de las actuaciones y la estandarización de los procesos. Un aspecto diferencial de esta fase es la implicación activa del cliente, que participará de forma directa en los principales hitos del proyecto, tales como la validación de entregables, la definición de requisitos de calidad, el seguimiento del servicio y la evaluación de resultados. Esta colaboración continua permitirá alinear las expectativas, mejorar la comunicación y garantizar que el servicio evoluciona conforme a las necesidades reales. Asimismo, se establecerán canales de comunicación fluidos y mecanismos de coordinación eficaces, que aseguren la transparencia en la gestión, la rápida resolución de incidencias y la adecuada toma de decisiones. Estos mecanismos incluirán reuniones periódicas de seguimiento, informes de estado y cuadros de mando compartidos. La fase de apoyo integrará, además, un enfoque de mejora continua, mediante la revisión periódica del desempeño del sistema, la identificación de oportunidades de optimización y la implantación de acciones correctivas y preventivas. De este modo, no solo se garantiza la estabilidad del sistema de gestión, sino también su capacidad de adaptación y evolución a lo largo del tiempo. En definitiva, esta fase asegura que todos los elementos necesarios personas, recursos, herramientas y colaboración con el cliente estén perfectamente coordinados para sostener un sistema de calidad robusto, eficiente y orientado a la excelencia. Operación La fase de operación constituye el núcleo de la ejecución del servicio, donde se materializan los procesos definidos y se aplican los mecanismos necesarios para garantizar el cumplimiento de los niveles de calidad establecidos. En esta etapa, empresa_s despliega un enfoque sistemático y basado en datos, apoyado en herramientas avanzadas de análisis y control que permiten supervisar de manera continua el desempeño del servicio y asegurar su alineación con los requisitos del cliente. Para ello, se emplea un conjunto integrado de técnicas de control de calidad que facilitan tanto la detección temprana de incidencias como la identificación de sus causas raíz. Entre estas herramientas destacan:

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
los requisitos definidos, tanto a nivel técnico como funcional, antes de su validación por parte del cliente. Estas herramientas no se utilizan de forma aislada, sino integradas dentro de un modelo de seguimiento continuo que permite obtener una visión global y en tiempo real del estado del servicio. Este enfoque facilita la toma de decisiones basada en evidencias, incrementa la capacidad de respuesta ante incidencias y refuerza la prevención frente a posibles desviaciones. Asimismo, durante la fase de operación se fomenta una cultura de calidad proactiva, en la que el equipo participa activamente en la identificación de mejoras, la optimización de procesos y la mejora del rendimiento global. Todo ello se complementa con mecanismos de comunicación y coordinación que garantizan la transparencia y el alineamiento continuo con el cliente. En definitiva, la fase de operación no solo asegura la correcta ejecución del servicio conforme a los estándares establecidos, sino que también actúa como motor de mejora continua, contribuyendo a maximizar la calidad, la eficiencia y la satisfacción del cliente. Producción y provisión La fase de producción y provisión tiene como objetivo garantizar que todos los productos y servicios comprometidos se generan y entregan cumpliendo estrictamente los requisitos de calidad, alcance y plazos establecidos. Para ello, empresa_s establece un conjunto de mecanismos de control, seguimiento y aseguramiento que permiten supervisar de forma integral la ejecución del servicio. En primer lugar, se definen y documentan de manera detallada los procesos de producción y prestación del servicio, asegurando que cada actividad se realiza conforme a procedimientos estandarizados y previamente validados. Esto incluye la identificación de responsables, la asignación de tareas y la definición de criterios de aceptación claros para cada entregable, lo que permite garantizar la trazabilidad completa a lo largo de todo el ciclo de ejecución. Asimismo, se implantan mecanismos de planificación y control que permiten gestionar de forma efectiva los tiempos y recursos, asegurando el cumplimiento de los hitos definidos en el cronograma. Estos mecanismos incluyen herramientas de seguimiento continuo, revisión periódica del avance y evaluación de desviaciones, lo que facilita la adopción temprana de medidas correctoras en caso necesario. Con el fin de reforzar la calidad en la ejecución, se establecen controles intermedios a lo largo de las distintas fases de producción, que permiten validar los entregables de forma progresiva antes de su aceptación final. Estos puntos de control aseguran que cualquier posible desviación se detecte y subsane en fases tempranas, reduciendo riesgos y evitando reprocesos.


De igual forma, se garantiza una adecuada gestión de la configuración y de la documentación asociada, asegurando que todos los entregables se generan, identifican, versionan y almacenan conforme a los estándares establecidos. Esto contribuye a mantener la coherencia, integridad y accesibilidad de la información en todo momento. Un elemento clave en esta fase es la coordinación continua con el cliente, quien participa activamente en la validación de los resultados y en el seguimiento del servicio. Esta colaboración permite ajustar la producción a las necesidades reales y asegurar que los entregables cumplen plenamente con las expectativas. Adicionalmente, se integran mecanismos de aseguramiento de la calidad, como revisiones internas, validaciones técnicas y controles de conformidad, que verifican que los productos y servicios cumplen con los requisitos definidos antes de su entrega. En conjunto, este enfoque permite no solo garantizar la correcta ejecución y provisión del servicio en tiempo y forma, sino también asegurar un alto nivel de calidad de los entregables, minimizar riesgos operativos y mantener una orientación constante a la satisfacción del cliente. Evaluación
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
relevante en una base de datos corporativa de experiencias. Este repositorio incluirá tanto las lecciones aprendidas como los indicadores de desempeño, las soluciones aplicadas y las recomendaciones identificadas. Su objetivo es facilitar la reutilización del conocimiento en proyectos futuros, reduciendo tiempos de arranque, evitando la repetición de errores y promoviendo la mejora continua a nivel organizativo.


Adicionalmente, se elaborará un informe final de evaluación que integrará los principales resultados del proyecto, el grado de cumplimiento de los objetivos de calidad y las conclusiones más relevantes. Este documento servirá como referencia tanto para el cliente como para la propia organización, consolidando la transparencia y la orientación a resultados. En conjunto, esta fase permite no solo valorar el éxito del proyecto, sino también transformar la experiencia adquirida en un activo estratégico, impulsando la excelencia operativa y la evolución continua de los servicios prestados. 3.2.5 Trazabilidad del servicio Con el objetivo de garantizar el control integral del servicio, la visibilidad completa del estado del proyecto y el cumplimiento de los niveles de calidad exigidos, empresa_s implantará un modelo avanzado de trazabilidad y seguimiento continuo, basado en gobierno multinivel, control operativo diario y mecanismos formales de reporte y validación. Este modelo permite asegurar la alineación constante con las prioridades de la Consejería de Digitalización, facilitando la toma de decisiones, la gestión de riesgos y la mejora continua del servicio. Enfoque de seguimiento continuo y comunicación estructurada El Jefe de Proyecto de empresa_s asumirá la responsabilidad global del seguimiento del servicio, realizando una supervisión continua de todas las actividades, hitos y entregables . Se establecerá un sistema de comunicación fluido con los responsables designados por la Consejería de Digitalización, garantizando:

- Información periódica sobre el estado del servicio

- Visibilidad de avances, desviaciones e incidencias
- Anticipación de riesgos y necesidades futuras

- Toma ágil de decisiones
Para ello, se celebrarán reuniones periódicas de seguimiento, de las que se generará acta formal, asegurando la trazabilidad completa de acuerdos, acciones y decisiones. Asimismo, se utilizarán las herramientas y metodologías que determine la Consejería , integrando la planificación, seguimiento y control en un ecosistema común de gestión. Modelo de Gobierno del servicio empresa_s implantará un modelo de gobierno estructurado en tres niveles, que aseguran una gestión eficaz desde la estrategia hasta la operación, alineado con las buenas prácticas en gestión de servicios TI:

- Nivel estratégico.
- Nivel táctico.

- Nivel operativo.
Este modelo se ajustará durante la fase inicial del proyecto (kick-off), adaptándose a las necesidades específicas de la Consejería de Digitalización. La organización se articulará mediante una estructura jerárquica coordinada, donde los responsables de ambas partes dirigirán el proyecto a nivel estratégico, apoyados por los responsables de proyecto en la gestión táctica y la coordinación del equipo. Niveles de relación y responsabilidades


Nivel estratégico Orienta la dirección global del proyecto y el alineamiento con los objetivos de la Consejería. Principales funciones:
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
Se realizarán reuniones internas periódicas para garantizar la eficiencia operativa y la correcta ejecución del servicio. Comités de seguimiento y gobernanza


Cada nivel se materializa en un comité específico, con reuniones periódicas, actas formales y seguimiento de acuerdos. Comité Estratégico Focalizado en la evolución del contrato y la alineación global del servicio. Responsabilidades:

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
Comité de Seguimiento y Control (táctico) Centrado en la ejecución del servicio. Responsabilidades:

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
Se apoyará en informes periódicos que reflejen la situación actual y posibles desviaciones.


Sistema de trazabilidad integral empresa_s implantará un modelo de trazabilidad completa, continua y auditable , que permitirá el seguimiento exhaustivo de todas las actividades, decisiones y entregables del proyecto a lo largo de todo su ciclo de vida. Este sistema de trazabilidad constituye un elemento central del modelo de prestación, garantizando transparencia total, control operativo y capacidad de auditoría en cualquier momento, en línea con los requisitos del pliego. Trazabilidad end- to-end del ciclo de vida La trazabilidad cubrirá de manera integral todas las fases del servicio:

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
De este modo, se asegura la trazabilidad completa de la gobernanza del proyecto, evitando pérdida de información y asegurando coherencia en la toma de decisiones. Trazabilidad técnica y de cambios Se garantizará la trazabilidad de todos los cambios técnicos realizados en la plataforma, incluyendo:

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
