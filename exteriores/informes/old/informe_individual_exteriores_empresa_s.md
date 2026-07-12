# INTRODUCCIÓN

**El presente documento tiene por objeto la realización de una evaluación técnica detallada de la memoria presentada por la empresa empresa_s** en el marco del procedimiento de contratación correspondiente al expediente BAC01\_2026, relativo a los servicios de mantenimiento y soporte para proyectos exteriores alojados en la plataforma EducaMadrid.

La valoración se ha llevado a cabo atendiendo de forma estricta a lo establecido en el Documento de Invitación, y en particular a los criterios de adjudicación sujetos a juicio de valor descritos en el apartado 7.2, los cuales definen tanto la estructura de la evaluación como el baremo cualitativo aplicable en cada uno de los apartados considerados. **En este sentido, resulta especialmente relevante señalar que la valoración no se basa en una verificación binaria de cumplimiento, sino en un análisis cualitativo del grado de adecuación, profundidad, viabilidad y rigor técnico de la propuesta presentada, situando cada uno de los aspectos evaluados dentro de los niveles de excelencia, alta, media, baja o muy baja definidos en el pliego.**

**El análisis se articula sobre una doble dimensión.** Por un lado, se desarrolla un examen pormenorizado de la solución técnica ofertada, estructurado por bloques funcionales y subproyectos conforme a lo recogido en el Anexo II del pliego, lo que permite valorar individualmente el grado de respuesta a cada uno de los requisitos específicos exigidos. Por otro lado, se realiza una evaluación global alineada con los criterios del apartado 7.2, integrando las conclusiones parciales en una valoración consolidada de la solución en términos de arquitectura, comprensión, viabilidad, metodología, rendimiento y grado de satisfacción de los requisitos.

La metodología empleada para la elaboración del presente informe se fundamenta en un análisis comparativo entre los requisitos establecidos en el pliego y la propuesta técnica descrita en la memoria presentada por el licitador, prestando especial atención a aquellos aspectos que permiten evaluar la calidad real de la solución, tales como el nivel de detalle técnico, la concreción de las actuaciones propuestas, la existencia de metodologías definidas, la identificación de herramientas y tecnologías específicas, la inclusión de métricas de control y la coherencia global de la arquitectura planteada.

Asimismo, el análisis incorpora como elemento relevante la identificación de fortalezas y debilidades en cada uno de los subproyectos evaluados, con el objetivo de proporcionar una justificación suficientemente detallada y defendible de las valoraciones asignadas, permitiendo su trazabilidad en caso de revisión o eventual alegación.

**Hay que destacar que la ausencia de métricas, indicadores o criterios objetivos de validación no ha sido ponderada de forma uniforme en todos los subproyectos, sino en función de la relevancia que dichos elementos tienen para cada tipo de actuación.** Así, su impacto se ha considerado especialmente significativo en ámbitos relacionados con rendimiento, seguridad, escalabilidad, operación o cumplimiento normativo, mientras que en actuaciones de carácter más funcional o visual se ha valorado principalmente como una limitación de verificabilidad y seguimiento.

En conjunto, el presente informe tiene como finalidad ofrecer una evaluación técnica rigurosa, exhaustiva y coherente con los criterios establecidos en el pliego, permitiendo fundamentar de manera sólida la valoración final de la propuesta presentada por empresa_s

## ANÁLISIS DETALLADO DE LA SOLUCIÓN TÉCNICA

### PROYECTOS WEB LIFERAY (ELIF)

### ELIF1 – Adaptaciones de las páginas web Liferay

El requisito asociado a este subproyecto contempla la necesidad de llevar a cabo actuaciones de adaptación sobre las páginas web desarrolladas en Liferay, incluyendo tanto la revisión de plantillas como la modernización de su presentación y la mejora de la experiencia de uso tanto para usuarios finales como para perfiles de edición.

La propuesta presentada por empresa_s aborda este requisito mediante la definición de un conjunto de actuaciones orientadas a la revisión de las plantillas existentes, incluyendo el tratamiento de tecnologías JSP y JSTL, la adaptación de las vistas públicas y privadas, la modernización de estilos y la mejora del comportamiento responsive, incorporando asimismo referencias a la homogeneización de la apariencia visual y a la mejora de la experiencia de edición para los gestores de contenidos.

**Desde un punto de vista técnico, resulta destacable que la memoria no se limita a reformular el requisito, sino que introduce conceptos adicionales como la reutilización de componentes y la mejora de la mantenibilidad del código, lo que evidencia una cierta orientación hacia la reducción de la complejidad futura y hacia la sostenibilidad de la solución en el tiempo.** Asimismo, la mención a la adaptación a estándares HTML5 y a la optimización de la estructura de las páginas sugiere una comprensión adecuada de las necesidades de modernización de este tipo de entornos.

**No obstante, a pesar de estos aspectos positivos, el análisis detallado de la propuesta pone de manifiesto una serie de carencias relevantes que afectan al grado de concreción de la solución.** En particular, no se describe de forma explícita la metodología que se seguiría para llevar a cabo la adaptación de las páginas, ni se definen procedimientos estructurados para el análisis previo de las plantillas existentes, la catalogación de variantes, la identificación de dependencias o la priorización de actuaciones. Del mismo modo, no se identifican entregables concretos asociados a este subproyecto, ni se establecen criterios de validación que permitan verificar de forma objetiva el grado de cumplimiento de las adaptaciones realizadas.

**Asimismo, la propuesta no profundiza en el funcionamiento específico del sistema Scribe CMS ni en su integración con Liferay, lo que limita la capacidad de evaluar la viabilidad real de ciertas actuaciones planteadas en entornos donde el CMS introduce restricciones adicionales.** Tampoco se incluyen estimaciones de esfuerzo, ni se establecen mecanismos de control de calidad o validación funcional más allá de referencias genéricas.

En consecuencia, aunque la propuesta presenta una cobertura clara del requisito y demuestra un conocimiento razonable de las tecnologías implicadas, el nivel de detalle técnico resulta insuficiente para alcanzar una valoración de excelencia, situándose en un nivel intermedio en el que existe una respuesta adecuada pero no completamente desarrollada.

**MEDIA-ALTA**

### ELIF2 – Barra de herramientas y pie de EducaMadrid

El subproyecto relativo a la barra de herramientas y el pie corporativo tiene como objetivo principal garantizar la integración homogénea de estos elementos en los distintos sitios web, asegurando la coherencia visual y funcional dentro del ecosistema EducaMadrid.

La memoria presentada por empresa_s responde de forma directa a este requisito, identificando de manera explícita la necesidad de integrar la barra corporativa y el pie común en los distintos sitios, así como de asegurar su compatibilidad multidispositivo, la uniformidad visual y la accesibilidad, incluyendo además la compatibilidad entre diferentes navegadores.

**Este alineamiento directo con el requisito constituye uno de los principales puntos fuertes de la propuesta, ya que demuestra una comprensión adecuada del carácter transversal de estos elementos y de su impacto en la experiencia de usuario y en la identidad institucional de la plataforma.** La propuesta no introduce desviaciones ni interpretaciones erróneas, sino que se ajusta con precisión al alcance solicitado.

**Sin embargo, al analizar con mayor profundidad el contenido técnico, se observa que la respuesta permanece en un nivel eminentemente descriptivo, sin desarrollar de forma suficiente los aspectos arquitectónicos ni los procedimientos necesarios para llevar a cabo la integración.** En particular, no se detalla cómo se gestionará la integración en los distintos tipos de sitios existentes, ni se describen mecanismos para evitar conflictos con personalizaciones previas, ni se abordan posibles problemas derivados de la coexistencia de versiones o temas distintos dentro del entorno Liferay.

Asimismo, la propuesta no contempla una estrategia de despliegue estructurada, ni se identifican fases de implantación, mecanismos de validación funcional o procedimientos de rollback en caso de incidencias, lo que limita la capacidad de evaluar la viabilidad operativa de la solución en escenarios reales.

La ausencia de métricas de validación, criterios objetivos de aceptación o indicadores de calidad refuerza la percepción de que la propuesta, aun siendo correcta en su planteamiento, no alcanza un nivel de desarrollo técnico suficiente para garantizar una ejecución completamente controlada y verificable.

En consecuencia, se trata de una respuesta que cumple adecuadamente el requisito desde el punto de vista funcional, pero que adolece de falta de profundidad en su desarrollo técnico.

**MEDIA**

### ELIF3 – Mejoras de presentación

El subproyecto relativo a las mejoras de presentación tiene como objetivo la evolución del frontend de los sitios web, no sólo desde un punto de vista visual, sino también en términos de rendimiento, eficiencia y adaptación a distintos dispositivos, incorporando prácticas modernas de desarrollo web.

La propuesta presentada por empresa_s desarrolla este apartado con un nivel de detalle superior al observado en otros subproyectos del bloque, describiendo de manera relativamente amplia la adopción de estándares HTML5 semántico, el uso de CSS y JavaScript para la estructuración y dinamización de las interfaces, así como la optimización de recursos mediante técnicas como la minificación de archivos, el uso de caché y la compresión de imágenes. **Se incorporan también referencias explícitas a la mejora de tiempos de carga, la adaptación responsive y la optimización del comportamiento multidispositivo, lo que evidencia una comprensión adecuada de los retos asociados al rendimiento y a la experiencia de usuario.**

**Desde un punto de vista técnico, resulta particularmente relevante que la propuesta vincule la mejora de la presentación con la optimización de recursos, lo que permite interpretar que no se trata únicamente de un rediseño superficial, sino de una actuación orientada a la eficiencia global del sistema.** Este enfoque es coherente con las necesidades actuales de plataformas web complejas, en las que la experiencia de usuario está directamente condicionada por el rendimiento de carga y la capacidad de adaptación a distintos entornos de ejecución.

**No obstante, a pesar de estos aspectos positivos, el análisis detallado revela que la propuesta carece de elementos fundamentales que permitan garantizar la verificabilidad de las mejoras planteadas.** Aunque no se definen métricas concretas de rendimiento, la naturaleza del subproyecto permite inferir adecuadamente los objetivos perseguidos a partir de las actuaciones descritas. No obstante, la incorporación de indicadores cuantitativos habría facilitado una validación más objetiva de los resultados obtenidos. Asimismo, no se describen herramientas específicas de análisis o validación, ni se establecen procedimientos de medición antes y después de las intervenciones, lo que limita la capacidad de evaluar el éxito de las mejoras implementadas.

Adicionalmente, no se identifican criterios de aceptación formal ni mecanismos de validación funcional que permitan verificar la correcta aplicación de los estándares definidos, ni se contemplan posibles problemas derivados de la compatibilidad con desarrollos previos o personalizaciones existentes en el entorno Liferay.

En consecuencia, aunque la propuesta presenta un desarrollo razonablemente completo desde el punto de vista conceptual y demuestra un conocimiento adecuado de las técnicas de optimización frontend, la falta de métricas, indicadores y procedimientos de validación impide situarla en un nivel de excelencia, quedando en una posición intermedia-alta dentro de la escala cualitativa.

**MEDIA-ALTA**

### ELIF4 – Mejoras de usabilidad y accesibilidad

El subproyecto relativo a la mejora de la usabilidad y la accesibilidad constituye uno de los elementos más relevantes del bloque, dado que afecta directamente tanto a la experiencia de usuario como al cumplimiento normativo aplicable en entornos públicos.

La propuesta presentada por empresa_s responde de forma clara y estructurada a este requisito, incorporando referencias explícitas a aspectos clave como la navegación mediante teclado, la compatibilidad con lectores de pantalla, la mejora del contraste, el uso de atributos ARIA y la alineación con estándares como WCAG 2.1 en nivel AA y la norma EN 301 549. **Asimismo, se contemplan elementos adicionales como la accesibilidad de newsletters y la realización de auditorías periódicas, lo que sugiere una aproximación que va más allá del cumplimiento inicial y se orienta hacia una mejora continua.**

**Desde un punto de vista técnico, esta respuesta evidencia un conocimiento adecuado de los criterios de accesibilidad y de su aplicación en entornos web complejos, lo que constituye uno de los puntos fuertes de la propuesta dentro del bloque Liferay.** La inclusión de auditorías y seguimiento evolutivo refuerza esta percepción, al plantear un modelo en el que la accesibilidad no se considera un requisito puntual, sino un proceso continuo.

**No obstante, el análisis detallado pone de manifiesto que, al igual que en otros subproyectos, la propuesta presenta carencias relevantes en términos de concreción técnica.** En particular, no se identifican herramientas específicas para la validación de accesibilidad, tales como validadores automáticos, plataformas de testing o herramientas de auditoría reconocidas, lo que limita la capacidad de verificar la viabilidad real de las actuaciones propuestas. La propuesta podría reforzarse mediante la incorporación de indicadores de seguimiento y resultados de accesibilidad, si bien la referencia expresa a WCAG 2.1 AA y EN 301 549 proporciona ya un marco objetivo de validación.

Asimismo, la metodología de auditoría no se describe con suficiente nivel de detalle, sin especificar fases, procedimientos ni entregables asociados, lo que introduce incertidumbre sobre la forma en que se llevaría a cabo la validación de los requisitos normativos.

En consecuencia, aunque la propuesta presenta una alineación clara con los requisitos del pliego y demuestra un conocimiento adecuado de la normativa y de las buenas prácticas en accesibilidad, la falta de concreción metodológica y de métricas verificables impide alcanzar una valoración de excelencia.

**MEDIA-ALTA**

### CONCLUSIÓN DEL BLOQUE ELIF

El análisis conjunto de los subproyectos que componen el bloque de Proyectos Web Liferay permite identificar una propuesta que, en términos generales, presenta un buen grado de alineación con los requisitos establecidos en el pliego, incorporando actuaciones específicas para cada uno de los ámbitos solicitados y demostrando un conocimiento técnico adecuado de las tecnologías implicadas.

En particular, la memoria destaca por su capacidad para identificar correctamente las necesidades asociadas a la adaptación de páginas, la integración de elementos corporativos, la mejora de la presentación y la optimización de la usabilidad y accesibilidad, evitando en la mayoría de los casos una simple reformulación de los requisitos y aportando una cierta capa adicional de valor mediante referencias a prácticas de mantenibilidad, optimización y cumplimiento normativo.

Asimismo, la propuesta introduce elementos complementarios relacionados con la operación técnica, tales como aspectos de administración, monitorización o hardening, que, si bien no forman parte directa del alcance de los subproyectos analizados, contribuyen a reforzar la percepción de conocimiento global del entorno tecnológico y de los requisitos operativos asociados.

**No obstante, este conjunto de fortalezas se ve claramente limitado por la presencia de una serie de debilidades recurrentes a lo largo de todos los subproyectos del bloque.** Entre ellas destaca de manera especialmente significativa la ausencia de metodologías detalladas que describan con precisión cómo se llevarán a cabo las actuaciones propuestas, así como la falta de definición de entregables concretos y de criterios de validación que permitan verificar de forma objetiva el grado de cumplimiento de los requisitos.

**Del mismo modo, se observa una carencia generalizada de métricas cuantificables, indicadores de rendimiento o criterios objetivos de aceptación, lo que dificulta la evaluación de la eficacia real de las soluciones planteadas y limita su trazabilidad en fases posteriores del servicio.** Asimismo, la arquitectura se describe en un nivel relativamente alto, sin llegar a detallar los mecanismos concretos de integración, despliegue o validación en entornos reales.

En consecuencia, el bloque puede calificarse como una propuesta técnica correctamente orientada, con un nivel de desarrollo superior a una cobertura meramente formal, pero que no alcanza el nivel de profundidad, concreción y verificabilidad exigible para situarse en el rango de excelencia.

**Valoración global del bloque ELIF: MEDIA-ALTA**

### MEJORAS Y MANTENIMIENTO DE LA WEB DE INNOVACIÓN Y FORMACIÓN DEL PROFESORADO (IFP)

### IFP1 – Mejoras y mantenimiento de la web de Innovación y Formación del Profesorado

El subproyecto IFP1 constituye uno de los elementos de mayor complejidad y relevancia dentro del conjunto de requisitos del pliego, al implicar no sólo la evolución de un sistema existente, sino una transformación significativa de su arquitectura, su modelo de integración y su operación global.

**La propuesta presentada por empresa_s aborda este subproyecto mediante el desarrollo de una arquitectura global que contempla la migración a Drupal 11, la integración progresiva de aplicaciones externas, la generación de APIs para el desacoplamiento de sistemas, la creación de una intranet administrativa, la migración de inscripciones a nuevas entidades, la utilización de LDAP como origen de datos y la adaptación de la infraestructura subyacente.** Esta amplitud de cobertura permite afirmar que existe una correspondencia directa con la práctica totalidad de los requisitos definidos en el pliego, evitando en gran medida interpretaciones parciales o incompletas.

**Uno de los aspectos más destacados de la propuesta radica en su capacidad para demostrar una comprensión sólida del escenario actual, identificando correctamente la coexistencia de múltiples aplicaciones, las dependencias existentes sobre bases de datos, la interacción con sistemas externos como GIFP o Ponentes y la necesidad de abordar un proceso de desacoplamiento progresivo.** Esta capacidad de diagnóstico constituye un elemento diferencial relevante, ya que permite fundamentar la solución en una base realista y alineada con el contexto operativo.

En lo que respecta a la migración a Drupal 11, la propuesta describe una metodología estructurada basada en la migración por capas, la revisión de módulos, la actualización de dependencias, el uso de entornos de preproducción y la realización de validaciones funcionales previas al paso a producción. **Este enfoque resulta coherente con las buenas prácticas en procesos de migración de plataformas y aporta un nivel de control adecuado sobre los riesgos asociados.**

**Asimismo, la estrategia de integración de aplicaciones externas introduce un elemento de valor significativo mediante la definición de un modelo diferenciado basado en la clasificación de aplicaciones según su nivel de acoplamiento, contemplando escenarios de integración directa, adaptación mediante APIs o convivencia temporal.** La inclusión de una matriz de decisión en este ámbito contribuye a reforzar la percepción de madurez de la propuesta, al proporcionar un mecanismo estructurado para la toma de decisiones.

En el ámbito de las APIs, la propuesta desarrolla de forma específica aspectos relacionados con el diseño de interfaces, la autenticación y autorización, el versionado y la documentación, lo que constituye una respuesta directa al requisito de desacoplamiento de sistemas y facilita la evolución independiente de los distintos componentes de la arquitectura.

Igualmente, la integración con LDAP plano se describe mediante la definición de procesos de sincronización incremental, normalización de datos, creación y actualización de usuarios y registro de operaciones, lo que evidencia una respuesta explícita y alineada con el requisito planteado.

Otro de los elementos particularmente relevantes es el tratamiento de la migración de inscripciones, en el que se contemplan fases de análisis, diseño de nuevas entidades, optimización de índices, validación y pruebas, abordando uno de los puntos críticos en términos de rendimiento y modelo de datos.

Desde el punto de vista metodológico, la propuesta define un plan de migración estructurado en múltiples fases, incluyendo inventario, diseño, preproducción, migración, integración, pruebas y paso a producción, lo que aporta un marco de ejecución ordenado y verificable.

**No obstante, a pesar de este elevado nivel de desarrollo, el análisis detallado permite identificar una serie de carencias que limitan el grado de excelencia de la solución.** En primer lugar, dada la relevancia estructural del proyecto y su impacto sobre la arquitectura futura del servicio, la ausencia de métricas cuantificadas de rendimiento, escalabilidad y capacidad constituye una limitación significativa para valorar objetivamente los beneficios esperados de la solución. La validación se plantea fundamentalmente en términos cualitativos, sin definir indicadores objetivos de éxito.

En segundo lugar, en determinados apartados se detecta una escasa concreción tecnológica, especialmente en lo relativo a herramientas específicas de integración, mecanismos concretos de autenticación, herramientas de migración o soluciones de monitorización, lo que introduce cierta incertidumbre sobre la implementación real de algunos componentes de la solución.

**Asimismo, la propuesta presenta una dependencia significativa de análisis posteriores en varias decisiones críticas, utilizando formulaciones abiertas que dejan determinados aspectos sujetos a evaluación futura.** Aunque este enfoque puede ser razonable en ciertos contextos, reduce la capacidad de valorar de forma precisa la solidez de la solución en fase de licitación.

Finalmente, aunque el rendimiento se aborda desde un punto de vista conceptual, no se aportan estimaciones cuantificadas ni comparativas que permitan justificar de manera objetiva las mejoras esperadas, lo que limita la capacidad de evaluar el impacto real de las actuaciones propuestas.

En conjunto, la propuesta presentada para el subproyecto IFP1 puede considerarse técnicamente consistente, con un alto grado de cobertura de los requisitos y una arquitectura claramente definida, pero con carencias en términos de métricas, concreción tecnológica y justificación cuantitativa que impiden situarla en el nivel máximo de valoración.

**MEDIA***-ALTA**

### PROYECTOS MOODLE MISC (EMOM)

**El bloque relativo a MoodleMisc presenta una complejidad técnica particularmente elevada debido a la combinación de actuaciones de distinta naturaleza, que abarcan desde actualizaciones de plataforma y mantenimiento evolutivo hasta integración con servicios corporativos, automatización operativa, ciberseguridad y resolución de incidencias funcionales.** Esta amplitud de alcance exige una propuesta que no solo cubra los requisitos de forma exhaustiva, sino que incorpore un modelo operativo coherente y adaptado a entornos distribuidos con múltiples instancias y dependencias.

La propuesta presentada por empresa_s aborda este bloque mediante una respuesta amplia y estructurada, en la que se identifican tecnologías específicas del ecosistema Moodle, procesos operativos propios de este tipo de plataformas y mecanismos de gestión orientados a garantizar la estabilidad y evolución del servicio. **No obstante, como se detallará a continuación en el análisis subproyecto a subproyecto, esta cobertura general se ve acompañada de determinadas carencias recurrentes relacionadas con la ausencia de métricas cuantificables, la falta de herramientas concretas y un cierto predominio de descripciones metodológicas frente a definiciones plenamente operativas.**

### EMOM1 – Actualización de la plataforma MoodleMisc

El subproyecto relativo a la actualización de la plataforma MoodleMisc tiene como finalidad garantizar la evolución continua del entorno mediante la actualización a versiones estables, la revisión de dependencias y la incorporación de mejoras de seguridad y compatibilidad.

**La propuesta presentada por empresa_s desarrolla este requisito mediante la definición de una metodología estructurada que contempla la realización de un inventario previo de instancias, la creación de matrices de compatibilidad, la actualización escalonada de versiones, la revisión de plugins, la validación funcional y la automatización de despliegues.** Este conjunto de actuaciones permite identificar un enfoque ordenado y coherente con las buenas prácticas en procesos de actualización de plataformas complejas.

**Resulta especialmente destacable la inclusión de elementos como la identificación de dependencias y la consideración específica del tema EducaMadrid, lo que refleja una comprensión adecuada de la necesidad de preservar la coherencia visual y funcional del entorno durante el proceso de actualización.** Asimismo, la incorporación de mecanismos de despliegue automatizado introduce un componente relevante de control operativo, reduciendo el riesgo de errores manuales y mejorando la repetibilidad de las intervenciones.

**Sin embargo, el análisis en profundidad revela una serie de limitaciones que afectan al grado de concreción de la solución.** En particular, no se identifica la versión objetivo concreta a la que se pretende evolucionar la plataforma, lo que introduce incertidumbre sobre el alcance real de las actuaciones. Del mismo modo, no se describen procedimientos detallados de rollback que permitan revertir los cambios en caso de fallo, elemento crítico en entornos con múltiples instancias y elevada criticidad operativa.

Asimismo, se observa la ausencia de métricas de aceptación que permitan validar de manera objetiva el éxito del proceso de actualización, tales como indicadores de compatibilidad, tiempos de ejecución o criterios de validación funcional.

En conjunto, la propuesta presenta una metodología adecuada y coherente, pero con un nivel de detalle insuficiente en aspectos clave de control y validación.

**MEDIA-ALTA**

### EMOM2 – Adaptación de la plataforma MoodleMisc

El subproyecto de adaptación de la plataforma MoodleMisc implica la incorporación y mantenimiento de múltiples integraciones con servicios internos y externos, así como la adaptación del sistema a nuevas funcionalidades y requerimientos operativos.

**La propuesta presentada cubre de manera explícita la mayoría de los elementos solicitados en el pliego, incluyendo integraciones con SAML, WebAuth, Nextcloud, BigBlueButton, herramientas de inteligencia artificial, Kuet, CodeRunner, así como aspectos relacionados con el escalado horizontal, la adaptación de copias de seguridad y la gestión de calendarios y estadísticas.** Esta amplitud de cobertura constituye uno de los principales puntos fuertes de la propuesta, evidenciando una comprensión completa del alcance funcional del subproyecto.

Asimismo, se incorpora un procedimiento para la incorporación de nuevos nodos, lo que contribuye a reforzar la capacidad de escalabilidad de la solución, y se contempla la adaptación de las copias de seguridad a entornos distribuidos, elemento crítico en arquitecturas de este tipo.

**No obstante, al igual que en otros subproyectos, se detecta una falta de concreción en la implementación técnica de determinadas integraciones, especialmente en el caso de funcionalidades futuras o en evolución.** La propuesta no detalla los mecanismos específicos de integración, ni define arquitecturas concretas para cada uno de los servicios mencionados, lo que limita la capacidad de evaluar la viabilidad real de estas actuaciones.

Asimismo, no se establecen criterios objetivos de escalabilidad, tales como el número máximo de usuarios concurrentes, umbrales de carga o mecanismos de balanceo específicos, lo que impide cuantificar el rendimiento esperado del sistema.

En consecuencia, la propuesta presenta una cobertura funcional muy amplia y una comprensión clara del requisito, pero carece de la profundidad técnica necesaria para alcanzar una valoración de excelencia.

**ALTA**

### EMOM3 – Mantenimiento de la plataforma MoodleMisc

El subproyecto de mantenimiento se centra en la gestión continua del entorno Moodle, incluyendo la resolución de incidencias, la administración de plugins, la gestión de integraciones y la optimización del rendimiento.

La propuesta presentada por empresa_s desarrolla este apartado mediante la definición de un modelo de mantenimiento que abarca tanto aspectos correctivos como evolutivos y adaptativos, incluyendo la gestión de incidencias, la administración de plugins, el uso de herramientas como Moosh, la gestión de antivirus, la recuperación de contraseñas y la realización de copias de seguridad.

Uno de los elementos más relevantes de la propuesta es la incorporación de Redis clusterizado como mejora técnica, lo que introduce un componente de optimización del rendimiento que va más allá de los requisitos mínimos exigidos y evidencia una orientación hacia la mejora de la eficiencia del sistema.

Asimismo, la propuesta cubre de manera explícita una amplia gama de funcionalidades solicitadas en el pliego, lo que refuerza la percepción de adecuación al requisito.

**No obstante, el análisis detallado permite identificar ciertas limitaciones, especialmente en lo relativo al agrupamiento de desarrollos solicitados sin un tratamiento individualizado, lo que dificulta evaluar la profundidad de la solución para cada uno de ellos.** Asimismo, no se aportan métricas que permitan cuantificar el impacto de las mejoras introducidas, ni se establecen indicadores de rendimiento asociados al uso de Redis.

En consecuencia, aunque la propuesta presenta una cobertura sólida y una mejora técnica relevante, la falta de métricas y de detalle individualizado limita su valoración.

**ALTA**

### EMOM4 – Mejora de la ciberseguridad en Moodle Misc

El subproyecto de ciberseguridad tiene como objetivo reforzar la protección del entorno Moodle mediante la implementación de medidas de endurecimiento y control de acceso.

**La propuesta responde directamente a los requisitos del pliego, abordando aspectos como la autenticación mediante correo electrónico, la configuración segura de PHP, la ocultación de información sensible y el uso de cabeceras de seguridad.** Asimismo, incorpora elementos adicionales como la utilización de ClamAV y la consideración de la seguridad en integraciones.

Esta cobertura directa del requisito constituye un aspecto positivo, ya que demuestra una comprensión clara de las necesidades de seguridad del entorno.

Sin embargo, el nivel de detalle técnico resulta limitado, ya que no se concretan configuraciones específicas ni se hace referencia a mecanismos avanzados de seguridad como políticas CSP, HSTS o controles adicionales de endurecimiento, lo que reduce la profundidad de la solución.

Del mismo modo, la propuesta no incorpora indicadores de seguridad, umbrales de cumplimiento ni mecanismos de seguimiento que permitan evaluar de forma continuada la eficacia de las medidas implantadas, aspecto especialmente relevante en un ámbito de naturaleza preventiva como la ciberseguridad.

En consecuencia, la propuesta puede considerarse correcta en su planteamiento, pero con un nivel de desarrollo moderado.

**MEDIA-ALTA**

### EMOM5 – Solución de problemas conocidos en Moodle Misc

El subproyecto destinado a la resolución de problemas conocidos aborda la corrección de incidencias específicas identificadas en el entorno, tales como problemas con Wiris, H5P, calendarios, LaTeX o competencias.

La propuesta responde de forma directa a este requisito, describiendo una metodología estructurada basada en la reproducción de la incidencia, su análisis, la aplicación de la corrección, la validación y el despliegue, lo que constituye un enfoque coherente con las buenas prácticas en gestión de incidencias.

Este planteamiento aporta un nivel adecuado de organización y control del proceso de resolución, permitiendo garantizar la trazabilidad de las actuaciones.

No obstante, la propuesta no profundiza en el tratamiento específico de cada uno de los problemas identificados, ni proporciona ejemplos concretos de resolución, lo que limita la capacidad de evaluar la eficacia real de la solución.

Asimismo, no se establecen métricas de resolución, tiempos de respuesta ni indicadores de calidad del servicio.

En consecuencia, se trata de una propuesta correcta desde el punto de vista metodológico, pero con un nivel de detalle técnico limitado.

**MEDIA**

### EMOM6 – Tareas sobre configuraciones para conexiones externas

El subproyecto relativo a las configuraciones para conexiones externas aborda la integración con servicios como Marsupial, LTI y plataformas editoriales, así como la gestión de glosarios.

La propuesta contempla de forma explícita la mayoría de estos elementos, incluyendo la integración con Marsupial, LTI y servicios editoriales, lo que evidencia una cobertura adecuada del requisito.

Sin embargo, el análisis detallado pone de manifiesto que la propuesta no describe escenarios concretos de integración ni define arquitecturas específicas para cada caso, manteniéndose en un nivel genérico que limita su aplicabilidad práctica.

El tratamiento del análisis de glosarios resulta igualmente superficial, sin desarrollar procedimientos ni objetivos claros.

En consecuencia, la propuesta presenta una cobertura funcional correcta, pero con un nivel de desarrollo técnico insuficiente.

**MEDIA**

### EMOM7 – Otras tareas específicas de actualización y procedimiento

El subproyecto EMOM7 engloba un conjunto amplio de actuaciones adicionales relacionadas con la evolución de la plataforma, incluyendo la gestión de nuevos frontales, LDAP, bases de datos, almacenamiento, herramientas auxiliares y automatización.

La propuesta responde de manera completa a este conjunto de requisitos, abordando explícitamente todos los elementos solicitados y añadiendo mejoras adicionales como la integración selectiva del SSO corporativo, lo que aporta un valor técnico adicional relevante.

Asimismo, la automatización aparece claramente identificada como uno de los pilares de la solución, reforzando la capacidad operativa del sistema.

No obstante, aunque la cobertura es amplia, la propuesta mantiene las carencias habituales en términos de métricas, indicadores y herramientas concretas, lo que limita la capacidad de evaluar la eficacia real de las actuaciones.

**ALTA**

### CONCLUSIÓN DEL BLOQUE MOODLEMISC

El análisis global del bloque MoodleMisc permite identificar una propuesta con un elevado grado de cobertura de los requisitos, que demuestra un conocimiento técnico claro del ecosistema Moodle y de las necesidades operativas asociadas a este tipo de plataformas.

Se aprecia una arquitectura coherente, la incorporación de mejoras técnicas relevantes y una metodología de trabajo estructurada, lo que sitúa la propuesta en un nivel superior al de una mera respuesta formal.

No obstante, la ausencia sistemática de métricas cuantificables, indicadores de rendimiento y herramientas específicas introduce una limitación significativa en términos de verificabilidad y control, impidiendo alcanzar un nivel de excelencia.

**Valoración global del bloque EMOM: MEDIA-ALTA**

### PROYECTOS DE DINÁMICAS (EDIN)

El bloque de Dinámicas presenta unas características significativamente diferenciadas respecto a otros ámbitos del contrato, al tratarse de un entorno compuesto fundamentalmente por aplicaciones heredadas, con arquitecturas heterogéneas, dependencias históricas y niveles de mantenimiento dispares. **Esta naturaleza introduce un nivel de riesgo técnico elevado, especialmente en lo relativo a compatibilidad, seguridad y control operativo, lo que exige una propuesta capaz de abordar de forma específica este tipo de escenarios.**

La propuesta presentada por empresa_s destaca en este bloque por una adaptación más evidente al contexto real del entorno, alejándose en mayor medida de planteamientos genéricos y aproximándose a una visión técnica concreta basada en el análisis de sistemas legacy, lo que supone un elemento diferencial relevante respecto a otros apartados.

### EDIN1 – Mantenimiento, actualización y adecuación ENS del entorno Dinámicas

El subproyecto EDIN1 tiene como objetivo el mantenimiento y evolución del entorno de Dinámicas, así como su adecuación a requisitos de seguridad alineados con el Esquema Nacional de Seguridad, en un contexto caracterizado por la presencia de aplicaciones PHP/MySQL heredadas y configuraciones individuales por proyecto.

**La propuesta presentada por empresa_s parte de una caracterización detallada del entorno, identificando correctamente elementos clave como la existencia de aplicativos independientes, bases de datos segregadas, dominios diferenciados, integración con LDAP y uso de espacios FTP asociados.** Esta capacidad de diagnóstico constituye uno de los principales puntos fuertes de la propuesta, al reflejar una comprensión realista y contextualizada del servicio.

**A partir de esta base, la solución plantea un conjunto de actuaciones técnicas estructuradas que incluyen la elaboración de un inventario completo, la definición de una matriz de criticidad y riesgo, la clasificación de aplicaciones y la actualización progresiva de tecnologías, especialmente en lo relativo a versiones de PHP y motores de bases de datos.** Asimismo, se contemplan tareas específicas de adaptación de código heredado, revisión de dependencias y validación funcional, lo que evidencia un enfoque práctico orientado a la modernización de sistemas legacy.

**Desde el punto de vista de la seguridad, la propuesta incorpora medidas concretas de endurecimiento, tales como la segregación mediante Virtual Hosts, la configuración de logs independientes, la limitación de permisos, el control de directorios de subida y la mitigación de vulnerabilidades comunes como SQL Injection o XSS.** Este nivel de detalle en medidas técnicas supone uno de los desarrollos más consistentes dentro del bloque, al proporcionar actuaciones verificables y directamente aplicables.

En lo relativo a la adecuación al ENS, la propuesta introduce elementos como inventariado, gestión de cambios, trazabilidad, control de accesos y gestión de vulnerabilidades, alineados con los principios básicos del esquema. **Sin embargo, este aspecto presenta una limitación relevante, ya que no se desarrollan referencias explícitas a medidas concretas del ENS, categorías de seguridad o procedimientos formales de auditoría, lo que reduce el nivel de formalización de la adecuación planteada.**

**La ausencia de indicadores objetivos de evolución del riesgo y de grado de cumplimiento ENS dificulta la trazabilidad de las mejoras propuestas y limita la capacidad de demostrar de forma continuada la efectividad de las actuaciones, la evolución de las vulnerabilidades o el grado de cumplimiento alcanzado, lo que limita la trazabilidad de las actuaciones en términos cuantificables.** La monitorización, aunque presente, se describe de forma genérica, sin detallar herramientas, mecanismos de alerta o procedimientos de correlación de eventos.

En consecuencia, la propuesta presenta un alto nivel de adecuación técnica y una clara orientación práctica, especialmente en el tratamiento de entornos heredados, pero con carencias en la formalización del ENS y en la definición de métricas de control.

**ALTA**

### EDIN2 – Mantenimiento, actualización y mejora del espacio FTP

El subproyecto EDIN2 aborda la gestión del servicio FTP asociado al entorno de Dinámicas, incluyendo su mantenimiento, mejora y adecuación a requisitos de seguridad.

La propuesta presentada por empresa_s integra el servicio FTP dentro del modelo global de gestión del entorno, contemplando actuaciones específicas relacionadas con la administración de usuarios, la gestión de directorios, la definición de permisos, la segregación de espacios y el control de escritura. **Asimismo, se mencionan acciones relacionadas con la revisión de rutas, la limitación de accesos y la integración con sistemas de identidad como LDAP.**

Este tratamiento integrado constituye un aspecto positivo, ya que permite considerar el FTP no como un elemento aislado, sino como parte de un ecosistema más amplio de gestión de servicios, reforzando su control operativo y su alineación con las políticas generales de seguridad.

**No obstante, el nivel de detalle técnico resulta sensiblemente inferior al mostrado en EDIN1, especialmente en lo relativo a aspectos críticos de seguridad.** En particular, no se especifica el uso de protocolos seguros como SFTP o FTPS, ni se describen mecanismos de cifrado, autenticación reforzada o protección de credenciales, lo que introduce incertidumbre sobre el nivel real de seguridad del servicio.

**Asimismo, la adecuación al ENS se menciona de forma indirecta, sin desarrollar medidas específicas aplicables al entorno FTP, lo que refuerza la percepción de falta de formalización en este ámbito.** Tampoco se identifican métricas de control ni indicadores de uso o seguridad, lo que dificulta la evaluación del desempeño del servicio.

En consecuencia, la propuesta responde adecuadamente al requisito desde el punto de vista funcional, pero presenta un nivel de desarrollo técnico limitado en aspectos clave de seguridad y cumplimiento.

**MEDIA**

### CONCLUSIÓN DEL BLOQUE DINÁMICAS

El análisis conjunto del bloque de Dinámicas permite identificar una propuesta que presenta una buena adaptación al contexto específico del entorno, especialmente en lo relativo al tratamiento de aplicaciones heredadas y a la identificación de riesgos asociados.

Se aprecia una comprensión clara de la problemática técnica, así como la definición de actuaciones concretas orientadas a la modernización y securización de sistemas legacy, lo que sitúa este bloque en un nivel de desarrollo superior al observado en otros apartados de la propuesta.

No obstante, las carencias detectadas en la formalización del ENS, la ausencia de métricas objetivas y la falta de detalle en determinados componentes, como el servicio FTP, limitan el grado de excelencia alcanzable.

**Valoración global del bloque EDIN: MEDIA-ALTA**

### PROYECTOS DE INTEGRACIÓN CON LA PLATAFORMA DE EDUCAMADRID (EIPE)

El bloque de integración con la plataforma EducaMadrid tiene como finalidad garantizar la correcta incorporación de aplicaciones externas dentro del ecosistema corporativo, incluyendo tanto modificaciones de aplicaciones existentes como adaptaciones front-end y desarrollo de mecanismos de integración.

La propuesta presentada por empresa_s desarrolla este bloque mediante un enfoque metodológico estructurado, orientado al control del ciclo de vida del software y a la integración coherente de sistemas heterogéneos, lo que constituye uno de los aspectos más sólidos del documento.

### EIPE1 – Modificación de aplicaciones, plugins y scripts de integración

El subproyecto EIPE1 aborda la modificación de aplicaciones y el desarrollo de plugins y scripts necesarios para su integración con la plataforma EducaMadrid, incluyendo tecnologías diversas como PHP, Python, Java o Shell Script.

La propuesta presentada define un modelo de integración basado en un proceso estructurado que incluye la recepción técnica del desarrollo, el análisis de código, la identificación de dependencias, la revisión de arquitectura y la integración con servicios corporativos. **Este enfoque metodológico resulta coherente con las buenas prácticas en integración de sistemas y aporta un nivel de control adecuado sobre las actuaciones.**

**Asimismo, la propuesta identifica distintos patrones de integración, como plugins, módulos, scripts de sincronización, conectores API o modificaciones de core, lo que permite adaptar la solución a distintos escenarios tecnológicos.** La cobertura explícita de múltiples lenguajes refuerza la percepción de capacidad para abordar entornos heterogéneos.

Desde el punto de vista arquitectónico, se contemplan elementos como la separación entre código y configuración, la gestión de credenciales, la integración con LDAP y SSO, y la conexión con APIs y bases de datos, lo que configura una arquitectura coherente y alineada con el entorno EducaMadrid.

**No obstante, el análisis detallado revela la ausencia de herramientas concretas para la implementación de estos procesos, tales como sistemas de control de versiones, plataformas de integración continua o herramientas de despliegue, lo que limita la concreción de la solución.** La propuesta podría reforzarse mediante la definición de indicadores de integración y calidad del software, aunque esta ausencia no compromete la comprensión ni la viabilidad general del enfoque planteado.

En consecuencia, la propuesta presenta una buena base metodológica y una arquitectura coherente, pero con un nivel de detalle insuficiente en aspectos operativos concretos.

**ALTA**

### EIPE2 – Modificaciones Front-End (HTML, CSS y JavaScript)

El subproyecto EIPE2 se centra en la adaptación visual y funcional de aplicaciones mediante tecnologías frontend, incluyendo HTML, CSS y JavaScript.

La propuesta presentada contempla de forma específica la adaptación de interfaces, la integración con la imagen corporativa, la compatibilidad entre navegadores y el diseño responsive, incorporando además consideraciones de accesibilidad y revisión de dependencias JavaScript heredadas.

**Este planteamiento evidencia una comprensión adecuada del requisito, abordando tanto la dimensión estética como la funcional de las aplicaciones.** Asimismo, la referencia a la integración de elementos comunes, como cabeceras y pies corporativos, refuerza la coherencia con el resto del ecosistema.

**No obstante, el nivel de detalle técnico resulta inferior al observado en el subproyecto de integración backend, especialmente en lo relativo a la definición de estándares concretos, frameworks a utilizar o herramientas de validación.** Tampoco se incluyen métricas de experiencia de usuario ni criterios objetivos de validación visual.

En consecuencia, se trata de una propuesta correcta y alineada con el requisito, pero con un desarrollo técnico moderado.

**MEDIA-ALTA**

### CONCLUSIÓN DEL BLOQUE INTEGRACIÓN (EIPE)

El análisis global del bloque de integración permite identificar una propuesta técnicamente consistente, con una metodología clara y una arquitectura coherente, orientada a la integración controlada de aplicaciones heterogéneas dentro del entorno EducaMadrid.

Se aprecia una buena comprensión del ecosistema y de las necesidades de gobernanza del software, lo que constituye uno de los puntos fuertes de este bloque.

No obstante, la ausencia de herramientas concretas, métricas y criterios de aceptación limita la capacidad de evaluar la eficacia real de las soluciones planteadas.

**Valoración global del bloque EIPE: ALTA**

### PROYECTOS DE SISTEMAS EXTERNOS (ESIS)

El bloque de Sistemas Externos constituye el núcleo más extenso y técnicamente exigente del contrato, al agrupar un conjunto muy amplio de actuaciones que abarcan desde la actualización de infraestructuras base y bases de datos hasta la integración de servicios, la gestión de identidades, el despliegue de aplicaciones, la ciberseguridad, la monitorización y la operación global de los proyectos externos dentro del ecosistema EducaMadrid.

La propuesta presentada por empresa_s se caracteriza por una cobertura exhaustiva de los requisitos, con una orientación clara hacia la definición de metodologías operativas estructuradas, la consideración de aspectos de seguridad y la integración con servicios corporativos. **Sin embargo, como se observará en el análisis detallado, se mantiene un patrón recurrente de carencias relacionadas con la escasa concreción de herramientas y la ausencia de métricas cuantificables.**

### ESIS1 – Servicio de actualización del software base

El subproyecto relativo a la actualización del software base tiene como finalidad garantizar la evolución tecnológica de los entornos mediante la actualización controlada de componentes como PHP, Apache, WordPress o Moodle, asegurando simultáneamente la compatibilidad de los aplicativos y la continuidad del servicio.

La propuesta presentada por empresa_s desarrolla este requisito mediante la definición de una metodología estructurada que incluye el inventario de componentes, la detección de software obsoleto, el análisis de vulnerabilidades, la validación funcional en entornos segregados y la utilización de procedimientos de rollback. **Este planteamiento evidencia una comprensión adecuada del proceso de actualización en entornos críticos, incorporando prácticas que permiten reducir el riesgo asociado a cambios de versión.**

**Asimismo, resulta especialmente relevante la orientación a seguridad de la propuesta, en la que se incluyen referencias a la gestión de vulnerabilidades mediante CVEs, la identificación de software en estado de fin de vida y la aplicación de medidas de hardening alineadas con el cumplimiento normativo.** Este enfoque aporta un valor adicional al integrar la actualización tecnológica dentro de un marco más amplio de gestión de riesgos.

**No obstante, el análisis detallado pone de manifiesto la ausencia de herramientas concretas para la ejecución de estas tareas, tales como gestores de configuración, sistemas de inventario automatizado o plataformas de despliegue, lo que limita la concreción operativa de la solución.** Asimismo, la ausencia de indicadores operativos limita la capacidad de seguimiento de los resultados, especialmente en actuaciones de infraestructura cuya eficacia debería poder medirse mediante parámetros objetivos de disponibilidad, rendimiento o capacidad.

En consecuencia, la propuesta puede considerarse sólida desde el punto de vista metodológico y de cobertura funcional, pero insuficientemente desarrollada en términos de concreción técnica.

**ALTA**

### ESIS2 – Servicio de actualización de bases de datos

El subproyecto ESIS2 aborda la actualización de motores de bases de datos, incluyendo tecnologías como MariaDB, PostgreSQL o MongoDB, garantizando la compatibilidad de los sistemas y minimizando el riesgo asociado a cambios de versión.

La propuesta contempla un conjunto de actuaciones coherentes, incluyendo inventario de instancias, detección de obsolescencia, validaciones de compatibilidad, migraciones controladas y procedimientos de rollback, lo que configura un modelo de actuación alineado con las buenas prácticas en gestión de plataformas de datos.

Asimismo, se incorporan aspectos relevantes como la optimización de consultas, la validación de replicaciones y el refuerzo de la monitorización durante el proceso de migración, lo que contribuye a garantizar la continuidad del servicio y la estabilidad del entorno.

**Sin embargo, al igual que en otros subproyectos, se observa una escasa concreción en aspectos técnicos clave, tales como la identificación de versiones objetivo, las herramientas específicas de migración o los procedimientos diferenciados por tipo de motor de base de datos.** Del mismo modo, la ausencia de indicadores operativos y de rendimiento limita la capacidad de seguimiento de los resultados, especialmente en actuaciones de infraestructura cuya eficacia debería poder medirse mediante parámetros objetivos de disponibilidad, rendimiento o capacidad.

En consecuencia, la propuesta presenta una base metodológica adecuada, pero con un nivel de detalle técnico insuficiente para alcanzar la excelencia.

**MEDIA-ALTA**

### ESIS3 – Consultoría de integración

El subproyecto ESIS3 tiene como objetivo proporcionar servicios de asesoramiento técnico en materia de integración de sistemas, garantizando la interoperabilidad y la correcta utilización de servicios corporativos.

**La propuesta desarrolla este requisito de manera consistente, incluyendo el análisis funcional y técnico de integraciones, la evaluación de interoperabilidad, el diseño de arquitecturas desacopladas y el desarrollo de conectores específicos.** Asimismo, se incorporan conceptos avanzados como APIs REST, gRPC, middleware y arquitecturas orientadas a eventos, lo que evidencia un conocimiento técnico elevado.

Desde el punto de vista del rendimiento, la propuesta contempla el análisis de concurrencia, la identificación de cuellos de botella y la simulación de cargas, lo que refuerza la solidez de la solución en escenarios de alta demanda.

No obstante, se detecta la ausencia de referencias a herramientas concretas de integración, como plataformas de API Gateway o ESB, así como la falta de métricas que permitan evaluar el rendimiento de las integraciones.

En conjunto, se trata de una propuesta técnicamente sólida, con un buen nivel conceptual, pero con carencias en la concreción operativa.

**ALTA**

### ESIS4 – Consultoría de ciberseguridad

El subproyecto ESIS4 se centra en la prestación de servicios de asesoramiento en ciberseguridad, incluyendo el endurecimiento de sistemas, la validación de accesos y el desarrollo de conectores seguros.

**La propuesta responde de forma adecuada a este requisito, incluyendo análisis de seguridad, validación de mecanismos de autenticación, revisión de controles de acceso y aplicación de medidas de hardening.** Asimismo, se contemplan elementos relevantes como el uso de TLS, la gestión de vulnerabilidades y el cumplimiento del ENS.

Adicionalmente, se prevé la elaboración de documentación técnica, incluyendo políticas de seguridad y guías de buenas prácticas, lo que contribuye a reforzar la gobernanza del entorno.

**Sin embargo, la propuesta carece de referencias explícitas a marcos metodológicos reconocidos, como OWASP, NIST o ISO 27001, lo que limita la formalización del enfoque de seguridad.** Asimismo, no se incluyen métricas de riesgo ni indicadores de cumplimiento, lo que dificulta la evaluación objetiva del nivel de seguridad alcanzado.

En consecuencia, la propuesta presenta una cobertura adecuada, pero con un nivel de formalización insuficiente.

**MEDIA-ALTA**

### ESIS5 – Actualización de la autenticación centralizada de usuarios

El subproyecto ESIS5 aborda uno de los aspectos más críticos del sistema, al centrarse en la evolución de los mecanismos de autenticación e identidad.

**La propuesta presenta un desarrollo especialmente sólido en este ámbito, contemplando tecnologías como LDAP, SSO, SAML2, OAuth2, OpenID Connect y mecanismos de autenticación multifactor.** Esta amplitud tecnológica constituye uno de los puntos más fuertes de la propuesta, al incorporar estándares actuales de gestión de identidad.

Asimismo, se incluyen procedimientos de validación en entornos de laboratorio, pruebas de carga y validaciones de resiliencia, lo que refuerza la viabilidad de la solución.

No obstante, se detecta una falta de concreción en la identificación de plataformas IAM concretas, así como la ausencia de métricas de rendimiento o disponibilidad.

En conjunto, se trata de uno de los subproyectos mejor desarrollados del bloque.

**ALTA**

### ESIS6 – Mantenimiento de la autenticación centralizada de usuarios

El subproyecto ESIS6 complementa el anterior, centrándose en el mantenimiento evolutivo de la plataforma de autenticación.

**La propuesta aborda de forma completa este requisito, incluyendo la actualización de componentes, la gestión de dependencias, la adaptación normativa y la validación de compatibilidad.** Asimismo, se incorporan elementos de gobierno de identidad, como auditoría, trazabilidad y observabilidad.

El enfoque metodológico, basado en entornos de validación, despliegues progresivos y procedimientos de rollback, refuerza la robustez operativa de la solución.

Sin embargo, persiste la ausencia de indicadores cuantificables, así como la falta de herramientas concretas para la gestión IAM.

**ALTA**

### ESIS7 – Gestión de servicios para la sincronización de usuarios

El subproyecto ESIS7 se centra en la sincronización de identidades entre diferentes sistemas.

La propuesta contempla una solución basada en una plataforma web segura integrada con LDAP y SSO, incorporando funcionalidades de validación, sincronización bajo demanda y auditoría de operaciones, lo que constituye una respuesta adecuada al requisito.

Asimismo, se incluyen elementos de seguridad como MFA y control de permisos, así como mecanismos de trazabilidad y gestión de incidencias.

No obstante, la propuesta carece de concreción tecnológica en la arquitectura de sincronización y no define métricas de rendimiento o consistencia de datos.

**MEDIA-ALTA**

### ESIS8 – Supervisión de usuarios de aplicaciones externas

El subproyecto ESIS8 aborda la supervisión de usuarios en aplicaciones externas integradas en la plataforma.

La propuesta responde adecuadamente mediante el desarrollo de un aplicativo web seguro integrado con sistemas de identidad corporativa, incluyendo funcionalidades de consulta segura, sincronización bajo demanda y gestión de permisos basada en roles.

Se incorporan asimismo mecanismos de auditoría, trazabilidad y autenticación robusta, lo que refuerza la seguridad del sistema.

No obstante, la propuesta presenta carencias en la definición de herramientas concretas y en la inclusión de indicadores de uso o rendimiento.

**MEDIA-ALTA**

### ESIS9 – Soporte técnico en entornos de preproducción

El subproyecto ESIS9 tiene como finalidad garantizar la correcta preparación y validación de aplicaciones externas en entornos de preproducción antes de su paso a producción, constituyendo un elemento clave para asegurar la estabilidad del servicio y minimizar el impacto de cambios en entornos críticos.

La propuesta presentada por empresa_s aborda este requisito mediante la definición de un modelo estructurado de preparación de entornos, en el que se contempla la instalación de aplicaciones, la configuración de dependencias, la integración con servicios corporativos y la realización de validaciones funcionales y técnicas. **Este planteamiento evidencia una comprensión adecuada del papel que desempeñan los entornos de preproducción en el ciclo de vida del software, especialmente en contextos donde la continuidad del servicio resulta crítica.**

**Asimismo, se describe una metodología basada en entornos segregados, validaciones previas, control de cambios y procedimientos de rollback, lo que aporta un grado razonable de control sobre las actuaciones realizadas.** La inclusión de fases de validación antes del despliegue definitivo permite reducir la probabilidad de incidencias en producción y garantizar un nivel mínimo de calidad en los desarrollos.

**No obstante, el análisis detallado pone de manifiesto que la propuesta carece de concreción en lo relativo a herramientas específicas de despliegue, automatización o integración continua, no identificándose plataformas concretas que permitan implementar de forma efectiva los procesos descritos.** Del mismo modo, no se establecen métricas asociadas a los tiempos de despliegue, indicadores de validación o criterios cuantificables de aceptación, lo que limita la capacidad de evaluar la eficiencia y eficacia del proceso.

En consecuencia, la propuesta puede considerarse coherente desde el punto de vista metodológico, pero con un nivel de concreción operativa limitado.

**MEDIA-ALTA**

### ESIS10 – Despliegue de aplicaciones externas en producción

El subproyecto ESIS10 se centra en la puesta en producción de aplicaciones externas, incluyendo la validación funcional, la evaluación de impacto y la garantía de continuidad del servicio.

La propuesta presentada desarrolla este requisito mediante un modelo de despliegue controlado que incluye validaciones previas, integración con servicios corporativos, pruebas funcionales y de rendimiento, procedimientos de rollback y monitorización posterior al despliegue. **Este enfoque resulta coherente con prácticas DevSecOps y aporta un nivel adecuado de control sobre el proceso.**

Asimismo, se contempla la realización de despliegues progresivos y la gestión de incidencias posteriores, lo que contribuye a garantizar la estabilidad del servicio durante la transición a entornos productivos.

**No obstante, se detecta una ausencia de definición de compromisos operativos claros, como ventanas de despliegue, tiempos máximos de recuperación o niveles de disponibilidad exigidos, lo que introduce incertidumbre sobre la gestión real del servicio.** Del mismo modo, no se incluyen métricas de despliegue ni indicadores de éxito.

En consecuencia, la propuesta presenta una base técnica sólida, pero carece de elementos cuantificables que permitan evaluar su rendimiento operativo.

**ALTA**

### ESIS11 – Integración en el gestor de servidores de bases de datos

Este subproyecto tiene como objetivo la integración de bases de datos externas dentro del sistema corporativo de gestión, garantizando su supervisión y mantenimiento.

La propuesta contempla la integración de instancias, la gestión de accesos, la monitorización y la observabilidad, así como la documentación e inventariado de los sistemas, lo que constituye una respuesta alineada con el requisito.

Desde el punto de vista técnico, se incluyen motores como MariaDB, PostgreSQL o MongoDB, lo que evidencia una cobertura adecuada de los entornos habituales.

**No obstante, se detecta la ausencia de referencia al gestor corporativo concreto utilizado por EducaMadrid, lo que limita la adecuación específica de la propuesta.** Asimismo, no se incluyen métricas de disponibilidad ni indicadores de rendimiento.

**MEDIA-ALTA**

### ESIS12 – Estudio de los recursos solicitados

El subproyecto ESIS12 se centra en el análisis previo de necesidades de infraestructura, incluyendo sistemas operativos, bases de datos, red, almacenamiento y dependencias.

**La propuesta presentada desarrolla este ámbito de forma amplia, contemplando análisis de arquitectura, dimensionamiento, evaluación de impacto y planificación de capacidad.** Este enfoque estructurado constituye uno de los puntos fuertes del subproyecto, al incorporar una visión global de los recursos necesarios.

Asimismo, se introduce el concepto de capacity planning, contemplando el crecimiento futuro y la evolución del sistema, lo que aporta un componente estratégico adicional.

No obstante, la propuesta no identifica herramientas específicas de análisis ni establece criterios cuantificables de dimensionamiento, lo que limita la precisión del estudio.

**ALTA**

### ESIS13 – Solicitud de los recursos necesarios

Este subproyecto aborda la provisión de recursos de infraestructura, incluyendo máquinas virtuales, comunicaciones y almacenamiento.

La propuesta contempla la coordinación con equipos de sistemas, redes y seguridad, así como la gestión de recursos y la planificación de capacidad, lo que demuestra una comprensión adecuada del proceso.

Sin embargo, la ausencia de procedimientos concretos de solicitud, circuitos de aprobación o herramientas de provisión reduce la concreción operativa de la solución.

Asimismo, no se definen métricas de dimensionamiento ni indicadores de capacidad.

**MEDIA-ALTA**

### ESIS14 – Bastionado de los recursos solicitados

El subproyecto ESIS14 constituye uno de los desarrollos más sólidos dentro del bloque, al centrarse en el endurecimiento de sistemas y la aplicación de medidas de ciberseguridad avanzadas.

La propuesta incorpora referencias a guías STIC, CIS Benchmark y ENS, así como la aplicación de hardening en sistemas operativos y entornos dockerizados, lo que supone una alineación directa con los requisitos del pliego.

Asimismo, se contemplan procesos de validación, escaneo de vulnerabilidades y auditoría, lo que refuerza la robustez de la solución.

No obstante, se observa una falta de identificación de herramientas concretas para la gestión de vulnerabilidades o el control de cumplimiento, así como la ausencia de métricas de seguridad.

**ALTA**

### ESIS15 – Instalación de paquetería y gestión de dependencias

El subproyecto ESIS15 aborda la instalación de software base, aplicaciones, librerías y dependencias.

La propuesta presenta un desarrollo muy amplio, cubriendo sistemas operativos, repositorios, bases de datos, aplicaciones y almacenamiento, e incorporando además prácticas DevSecOps como IaC, Ansible y CI/CD.

Este nivel de detalle constituye uno de los puntos más fuertes del bloque, al proporcionar una visión completa del proceso de despliegue.

No obstante, se detecta cierta redundancia respecto a otros subproyectos y la ausencia de métricas objetivas que permitan evaluar la calidad del proceso.

**ALTA**

### ESIS16 – Configuración del entorno

El subproyecto ESIS16 se centra en la configuración de sistemas, servicios y medidas de seguridad.

La propuesta cubre adecuadamente todos los elementos solicitados, incluyendo almacenamiento, servicios web, seguridad, monitorización y rendimiento, e incorporando tecnologías como TLS, WAF o SIEM.

Sin embargo, al igual que en otros subproyectos, no se definen indicadores cuantificables ni métricas de rendimiento, lo que limita la evaluación objetiva de la solución.

**ALTA**

### ESIS17 – Integración con LDAP

La propuesta aborda correctamente la integración con sistemas LDAP, incluyendo replicación, sincronización e integración segura, lo que constituye una respuesta adecuada al requisito.

No obstante, se detecta la ausencia de herramientas concretas y métricas de autenticación o disponibilidad.

**MEDIA-ALTA**

### ESIS18 – Integración con el sistema de correo

La propuesta contempla la integración con sistemas de correo mediante la configuración de SMTP, uso de SPF, DKIM y DMARC, así como la monitorización del servicio, lo que evidencia una cobertura adecuada.

Sin embargo, no se describe la integración específica con la plataforma existente ni se incluyen métricas de servicio.

**MEDIA-ALTA**

### ESIS19 – Integración con bases de datos

Este subproyecto presenta uno de los desarrollos más completos, incorporando integración entre motores heterogéneos, seguridad avanzada, control de cambios y monitorización.

La propuesta destaca por su enfoque en gobierno del dato, observabilidad y rendimiento, lo que constituye un punto fuerte relevante.

No obstante, persiste la ausencia de herramientas concretas y métricas cuantificables.

**ALTA**

### ESIS20 – Integración con CMDB

La propuesta desarrolla de forma muy completa el concepto de CMDB, incluyendo inventariado, gestión de dependencias, automatización y trazabilidad, lo que constituye un desarrollo especialmente maduro.

Sin embargo, no se identifican herramientas concretas ni métricas de calidad del inventario.

**ALTA**

### ESIS21 – Documentación del proyecto externo

El subproyecto ESIS21 tiene como finalidad garantizar la correcta documentación de los proyectos externos, abarcando tanto aspectos funcionales como técnicos, de infraestructura y de accesos.

La propuesta presentada por empresa_s desarrolla este requisito mediante la definición de un modelo de documentación que incluye inventarios de accesos, descripción de arquitecturas, diagramas de red, documentación de sistemas y procedimientos operativos, lo que configura una respuesta claramente alineada con el alcance solicitado en el pliego. **Este enfoque evidencia una comprensión adecuada del papel crítico que desempeña la documentación en entornos complejos, no solo como soporte de operación, sino también como elemento esencial para la continuidad del servicio y la transferencia de conocimiento.**

Desde un punto de vista técnico, resulta positivo que la propuesta contemple la documentación de dependencias, accesos y configuraciones, así como la inclusión de procedimientos de explotación, recuperación y rollback, lo que contribuye a reforzar la mantenibilidad de los sistemas.

**No obstante, el análisis detallado revela una limitación significativa en la falta de definición de estándares documentales concretos, plantillas estructuradas o herramientas específicas de gestión documental, lo que introduce incertidumbre sobre la homogeneidad y calidad de la documentación generada.** Del mismo modo, no se establecen procedimientos de validación documental ni mecanismos de control de versiones.

En consecuencia, la propuesta cubre adecuadamente el requisito, pero con un nivel de formalización insuficiente.

**MEDIA-ALTA**

### ESIS22 – Gestión del riesgo del proyecto externo

El subproyecto ESIS22 aborda la identificación y gestión de riesgos asociados a proyectos externos, incluyendo aspectos de seguridad, redes, interconexiones y control de accesos.

La propuesta presenta un desarrollo especialmente sólido en este ámbito, incorporando una metodología formal basada en MAGERIT, lo que supone un alineamiento directo con marcos de referencia reconocidos en la administración pública. **Asimismo, se contemplan inventarios de accesos, análisis de interconexiones, gestión de VPN, cortafuegos y entornos DMZ, configurando una visión integral del riesgo.**

Este enfoque permite estructurar la gestión de riesgos de manera ordenada, identificando activos, amenazas, vulnerabilidades y medidas de mitigación, lo que constituye uno de los puntos más fuertes del bloque.

No obstante, se observa la ausencia de métricas cuantificables de riesgo y de indicadores que permitan evaluar la evolución del nivel de exposición, lo que limita la trazabilidad cuantitativa del modelo.

**ALTA**

### ESIS23 – Implementación de backups y Disaster Recovery

El subproyecto ESIS23 tiene como objetivo garantizar la resiliencia del sistema mediante la implementación de mecanismos de copia de seguridad y recuperación ante desastres.

La propuesta contempla la realización de backups verificados, la definición de procedimientos de recuperación y la validación periódica de los sistemas, lo que evidencia una comprensión adecuada del requisito.

Sin embargo, no se detallan aspectos clave como RPO, RTO, tecnologías utilizadas, estrategias de replicación o pruebas de recuperación automatizadas, lo que limita significativamente la profundidad técnica.

**MEDIA-ALTA**

### ESIS24 – Implementación de monitorización básica

La propuesta incluye la monitorización básica del sistema mediante la recogida de logs, métricas y alertas, lo que constituye una respuesta adecuada al requisito.

No obstante, la falta de herramientas concretas, definición de umbrales y modelos de alerta reduce la capacidad de evaluar la eficacia del sistema de monitorización.

**MEDIA**

### ESIS25 – Implementación de monitorización avanzada

En este subproyecto se amplía la monitorización a un nivel más avanzado, incluyendo análisis más detallados de rendimiento, comportamiento y correlación de eventos.

La propuesta mantiene un enfoque coherente con el subproyecto anterior, pero no introduce un salto significativo en detalle técnico, permaneciendo en un nivel descriptivo sin identificación de herramientas como APM, observabilidad distribuida o correlación avanzada.

**MEDIA-ALTA**

### ESIS26 – Servicios de ciberseguridad básicos

La propuesta contempla medidas básicas de seguridad, incluyendo control de accesos, protección perimetral y validaciones de seguridad.

Sin embargo, la falta de concreción técnica y de indicadores de seguridad limita la profundidad de la solución.

**MEDIA-ALTA**

### ESIS27 – Servicios de ciberseguridad avanzados

El subproyecto introduce un mayor nivel de sofisticación en seguridad, contemplando análisis avanzados, detección de amenazas y refuerzo de controles.

La propuesta responde adecuadamente, pero sin llegar a detallar herramientas SIEM, SOC o mecanismos avanzados de detección, manteniendo un enfoque conceptual.

**MEDIA-ALTA**

### ESIS28 – Actualización de sistemas operativos

La propuesta contempla la actualización controlada de sistemas operativos, incluyendo validaciones previas y control de compatibilidad.

No obstante, no se definen herramientas ni métricas de éxito, ni políticas concretas de actualización.

**MEDIA-ALTA**

### ESIS29 – Gestión y seguimiento del proyecto

La gestión del proyecto se plantea mediante mecanismos de seguimiento, control de actividades y reporting.

La propuesta es coherente metodológicamente, pero carece de indicadores de rendimiento del servicio, KPIs o cuadros de mando definidos.

**MEDIA-ALTA**

### ESIS30 – Segmentación de la red de servidores

La propuesta contempla la segmentación de la red como medida de seguridad, incluyendo separación de entornos y control de accesos.

Sin embargo, el nivel de detalle técnico es limitado, sin definir arquitecturas concretas de red ni tecnologías específicas.

**MEDIA**

### ESIS31 – Optimización de la infraestructura de virtualización

El subproyecto final aborda la optimización de entornos virtualizados, incluyendo mejora de rendimiento y eficiencia.

La propuesta introduce conceptos relevantes, pero sin profundizar en herramientas ni métricas de optimización.

**MEDIA-ALTA**

## CONCLUSIÓN GLOBAL DEL BLOQUE ESIS

El análisis completo del bloque ESIS permite identificar una propuesta con un elevado grado de cobertura de los requisitos, en la que se aprecia una clara orientación metodológica, una comprensión adecuada del ecosistema EducaMadrid y una capacidad para abordar entornos complejos y heterogéneos.

Se trata de un bloque bien desarrollado en términos globales, con especial fortaleza en:

- identidad y autenticación (ESIS5-6)

- bastionado (ESIS14)

- instalación y configuración (ESIS15-16)

- integración de datos y CMDB (ESIS19-20)

No obstante, se mantiene de manera sistemática una serie de debilidades transversales:

- ausencia de herramientas concretas

- escasez de métricas y KPIs

- falta de cuantificación del rendimiento

- insuficiente formalización en algunos ámbitos

Estas carencias limitan la capacidad de verificar objetivamente la eficacia de la solución y reducen su nivel de excelencia.

**Valoración global del bloque ESIS: ALTA**

### SEGURIDAD DE APLICACIONES WEB (ESEG)

El bloque de Seguridad de Aplicaciones Web tiene como finalidad reforzar la protección de los sistemas expuestos, mediante la identificación de vulnerabilidades, la gestión de logs y el control de la superficie de ataque. **Se trata de un ámbito transversal que impacta directamente sobre la seguridad global de la plataforma EducaMadrid y, por tanto, requiere un enfoque técnico sólido y formalizado.**

### ESEG1 – Realización de auditorías / Pentesting web

El subproyecto ESEG1 tiene como objetivo la identificación de vulnerabilidades mediante auditorías de seguridad y pruebas de intrusión, tanto desde una perspectiva externa como interna.

**La propuesta presentada por empresa_s contempla la realización de auditorías de seguridad y pruebas de pentesting, incluyendo análisis de vulnerabilidades y evaluación de aplicaciones web expuestas, lo que constituye una respuesta adecuada al requisito en términos de alcance funcional.** La inclusión de estos procesos permite considerar que la propuesta aborda adecuadamente la necesidad de identificar riesgos en aplicaciones web y de evaluar su resistencia frente a posibles ataques.

**No obstante, al analizar en profundidad el contenido técnico, se observa que la propuesta carece de un nivel de formalización suficiente en la definición de metodologías de auditoría.** En particular, no se hace referencia explícita a marcos de referencia reconocidos en el ámbito del pentesting y auditoría web, tales como OWASP Testing Guide o metodologías similares, lo que limita la claridad sobre el enfoque que se seguiría en la ejecución de las pruebas.

Asimismo, no se describen herramientas específicas de análisis ni se definen procedimientos detallados para la ejecución de las auditorías, la priorización de vulnerabilidades o la elaboración de informes. **La ausencia de métricas asociadas, como número de vulnerabilidades detectadas, niveles de criticidad o tiempos de remediación, limita la capacidad de evaluar el impacto de las actuaciones propuestas.**

En consecuencia, la propuesta cubre adecuadamente el requisito desde el punto de vista funcional, pero presenta un nivel de desarrollo técnico moderado en cuanto a formalización y verificabilidad.

**MEDIA-ALTA**

### ESEG2 – Gestión de logs de las aplicaciones web

El subproyecto ESEG2 aborda la gestión, análisis y explotación de logs generados por las aplicaciones web, como mecanismo de detección de incidentes y auditoría del sistema.

**La propuesta presentada contempla la recogida de logs, su almacenamiento y su utilización para la monitorización y análisis de eventos, lo que constituye una respuesta alineada con el requisito.** La inclusión de logs como elemento de observabilidad permite mejorar la trazabilidad de las operaciones y facilitar la detección de incidencias.

**Sin embargo, el nivel de detalle técnico es limitado, ya que no se especifican herramientas concretas de gestión de logs, tales como plataformas SIEM, sistemas de agregación o herramientas de análisis centralizado.** Tampoco se describen mecanismos de correlación de eventos, definición de alertas o procedimientos de análisis avanzado, lo que reduce significativamente la profundidad de la solución.

Asimismo, no se establecen indicadores ni métricas de gestión de logs, como tiempos de retención, volumen de eventos procesados o tasas de detección de incidencias.

En consecuencia, la propuesta responde de forma correcta al requisito, pero con un nivel de desarrollo insuficiente para garantizar una gestión avanzada de la información.

**MEDIA**

### ESEG3 – Análisis y protección de la superficie de ataque

El subproyecto ESEG3 tiene como finalidad identificar y proteger los puntos de exposición del sistema, reduciendo la superficie de ataque y mejorando la seguridad global.

La propuesta presentada contempla el análisis de servicios expuestos, la revisión de configuraciones y la aplicación de medidas de protección, lo que constituye un planteamiento adecuado en términos generales.

**No obstante, al igual que en otros subproyectos del bloque, la propuesta carece de concreción en la identificación de herramientas, técnicas avanzadas de análisis o metodologías específicas para la evaluación de la superficie de ataque.** Tampoco se describen mecanismos de priorización de riesgos ni se establecen métricas de reducción de exposición.

En consecuencia, la propuesta presenta una cobertura funcional correcta, pero con un nivel de madurez técnica limitado.

**MEDIA-ALTA**

### CONCLUSIÓN DEL BLOQUE ESEG

El análisis conjunto del bloque de seguridad de aplicaciones web permite identificar una propuesta que cubre los requisitos fundamentales, pero que se mantiene en un nivel predominantemente conceptual, sin alcanzar un grado elevado de detalle técnico ni de formalización metodológica.

Se trata de un bloque correctamente enfocado desde el punto de vista funcional, pero con limitaciones claras en cuanto a herramientas, métricas y procedimientos de ejecución.

**Valoración global del bloque ESEG: MEDIA-ALTA**

### DESARROLLO SEGURO DE APLICACIONES WEB (EDSA)

### EDSA1 – Análisis de código web

El subproyecto EDSA1 aborda el análisis del código fuente de aplicaciones web con el objetivo de identificar vulnerabilidades y mejorar la calidad del software desde una perspectiva de seguridad.

La propuesta presentada contempla la revisión de código, la identificación de vulnerabilidades y la aplicación de buenas prácticas de desarrollo seguro, lo que constituye una respuesta alineada con el requisito. **Se aprecia una comprensión adecuada de la necesidad de integrar la seguridad en el ciclo de desarrollo.**

**No obstante, la propuesta no identifica herramientas específicas de análisis estático o dinámico, ni hace referencia a estándares de desarrollo seguro reconocidos, lo que limita la concreción del enfoque.** Asimismo, no se establecen métricas de calidad del código ni indicadores de mejora.

**MEDIA-ALTA**

### EDSA2 – Ayuda al desarrollo seguro de código web

Este subproyecto complementa el anterior mediante la asistencia al desarrollo seguro, incluyendo recomendaciones, buenas prácticas y soporte a desarrolladores.

**La propuesta contempla la formación, la transferencia de conocimiento y la asistencia técnica, lo que constituye una respuesta adecuada al requisito.** Se aprecia una orientación hacia la mejora continua del proceso de desarrollo.

Sin embargo, al igual que en EDSA1, no se concretan metodologías, herramientas ni indicadores, lo que limita la profundidad de la solución.

**MEDIA***-ALTA**

### CONCLUSIÓN DEL BLOQUE EDSA

El bloque de desarrollo seguro presenta una propuesta correcta desde el punto de vista conceptual, pero con un nivel de desarrollo limitado en aspectos técnicos específicos.

**Valoración global del bloque EDSA: MEDIA-ALTA**

### GESTIÓN DEL PROGRAMA DE BUG BOUNTY (EBBO)

### EBBO1 – Mantenimiento y gestión del programa de Bug Bounty

El subproyecto EBBO1 tiene como objetivo la gestión de un programa de recompensa de vulnerabilidades, fomentando la detección proactiva de fallos de seguridad por parte de terceros.

La propuesta presentada contempla la gestión del programa, la recepción de reportes, su análisis y la coordinación de la resolución de vulnerabilidades, lo que constituye una respuesta alineada con el requisito.

No obstante, el nivel de detalle técnico es reducido, ya que no se definen plataformas de gestión, procesos de validación de reportes ni métricas asociadas al funcionamiento del programa, lo que limita la capacidad de evaluar su eficacia.

**MEDIA**

### CONCLUSIÓN DEL BLOQUE EBBO

El subproyecto relativo al programa de Bug Bounty presenta una cobertura funcional básica, pero con un desarrollo técnico muy limitado.

**Valoración global del bloque EBBO: MEDIA**

## CIERRE DEL CAPÍTULO 2

El análisis detallado de todos los bloques y subproyectos permite afirmar que la propuesta presentada por empresa_s:

- cubre prácticamente la totalidad de los requisitos del Anexo II

- presenta una arquitectura coherente

- demuestra un conocimiento técnico adecuado del entorno

Sin embargo, de forma sistemática, se identifican limitaciones relevantes en:

- métricas y KPIs

- herramientas concretas

- cuantificación del rendimiento

- formalización metodológica en algunos ámbitos

Este patrón será clave en la valoración final del apartado 7.2.2.

## EVALUACIÓN DE LA SOLUCIÓN TÉCNICA (APARTADO 7.2.2 DEL Documento de Invitación)

La presente sección tiene como finalidad realizar la valoración global de la **solución técnica ofertada por la empresa empresa_s**, conforme a los criterios establecidos en el apartado 7.2.2 del Documento de Invitación, en el que se define un sistema de evaluación basado en juicio de valor, estructurado en distintos subcriterios cualitativos y asociado a una puntuación máxima en función del grado de cumplimiento.

A diferencia del análisis realizado en el capítulo anterior, que se ha orientado a la evaluación detallada de cada subproyecto del Anexo II, el presente apartado realiza una **síntesis integradora**, agrupando las valoraciones parciales en torno a los ejes definidos en el pliego, con el objetivo de determinar el nivel de calidad global de la solución ofrecida.

Dado que el baremo no establece correspondencias directas con puntuaciones concretas, sino que define franjas de valoración cualitativa en función del grado de cumplimiento, el enfoque adoptado se basa en la identificación del posicionamiento de la propuesta dentro de dichas franjas, justificando en cada caso la asignación correspondiente en función de evidencias técnicas, coherencia global y nivel de desarrollo.

### Arquitectura de la solución técnica

Uno de los elementos más relevantes en la evaluación de la solución técnica es el grado de coherencia, adecuación y desarrollo de la arquitectura propuesta, entendida como el conjunto de decisiones que articulan la organización de los sistemas, su integración, su escalabilidad y su capacidad de evolución en el entorno EducaMadrid.

La propuesta presentada por empresa_s desarrolla una arquitectura con una estructura claramente identificable, basada en principios de modularidad, desacoplamiento, integración mediante APIs y adaptación al nivel de criticidad de cada subproyecto. En este sentido, se aprecia un esfuerzo significativo por definir una **arquitectura proporcional**, en la que no todos los sistemas reciben el mismo tratamiento, sino que se adaptan en función de su impacto y complejidad, lo que constituye un enfoque técnicamente adecuado y alineado con buenas prácticas.

Asimismo, la memoria describe de forma extensa un modelo transversal que incorpora elementos de seguridad, operación, observabilidad y continuidad, así como una segmentación por tipos de subproyecto (Moodle, Liferay, sistemas externos, Dinámicas, etc.), lo que permite estructurar el ecosistema de manera ordenada y coherente.

**Sin embargo, a pesar de este nivel de desarrollo conceptual, se identifican determinadas limitaciones relevantes que afectan a la valoración global de la arquitectura.** En particular, se observa que, en muchos casos, la descripción arquitectónica se mantiene en un nivel alto, sin descender al detalle de implementaciones concretas, herramientas específicas o mecanismos operativos que permitan evaluar con precisión la viabilidad real de las soluciones planteadas.

**Del mismo modo, la arquitectura no se acompaña de métricas de comportamiento, dimensionamiento cuantificado ni indicadores objetivos de rendimiento, lo que limita su verificabilidad en términos de ejecución real.** Esta ausencia es especialmente relevante en entornos de alta criticidad, donde la capacidad de medir y controlar el comportamiento del sistema resulta fundamental.

En consecuencia, la arquitectura propuesta puede considerarse **coherente, bien estructurada y alineada con el entorno**, pero con un grado de abstracción elevado que impide situarla en el nivel máximo del baremo.

**Valoración: ALTA (sin alcanzar excelencia)**

Puntuación asignada: 1,5 / 2

### Grado de comprensión de los requisitos

El grado de comprensión del pliego constituye uno de los factores más determinantes en la valoración de la solución técnica, al evaluar no sólo la capacidad de identificar lo que se solicita, sino también la capacidad de interpretarlo, contextualizarlo y traducirlo en soluciones ejecutables.

En este ámbito, la propuesta presentada por empresa_s destaca de manera significativa, mostrando una comprensión profunda del alcance del contrato y del entorno tecnológico en el que se inscribe. Esta comprensión se manifiesta en varios elementos clave:

- una interpretación global del servicio como una operación continua y no como un conjunto de actuaciones aisladas

- la identificación de interdependencias entre sistemas

- la contextualización de los requisitos dentro del ecosistema EducaMadrid

- la traducción de necesidades en soluciones técnicas estructuradas

Asimismo, se aprecia una capacidad destacada para abordar aspectos complejos como la migración a Drupal 11, el desacoplamiento mediante APIs, la gestión de identidades o la integración de múltiples plataformas, lo que evidencia una comprensión que va más allá de la mera reformulación del pliego.

No obstante, esta comprensión se ve parcialmente limitada por el hecho de que, en determinados casos, la propuesta no se acompaña de un nivel equivalente de concreción técnica, lo que genera un cierto desequilibrio entre la capacidad de interpretación y la capacidad de definición detallada de soluciones.

En consecuencia, el grado de comprensión puede considerarse claramente superior al estándar medio, situándose en un nivel alto dentro del baremo.

**Valoración: ALTA (próxima al nivel excelente)**

Puntuación asignada: 1,75 / 2

### Viabilidad técnica y operativa de la solución

La viabilidad constituye un criterio fundamental, al evaluar la capacidad real de implantar la solución propuesta en el entorno existente, garantizando su funcionamiento, su sostenibilidad y su adaptación a condiciones reales de operación.

La propuesta presentada por empresa_s se caracteriza por un enfoque claramente orientado a la viabilidad, incorporando elementos como:

- uso de tecnologías alineadas con el entorno actual

- evolución progresiva en lugar de sustituciones disruptivas

- separación de entornos

- validación previa de cambios

- incorporación de planes de transición

- coexistencia temporal de sistemas

Este conjunto de elementos permite afirmar que la solución está concebida con un alto grado de realismo, evitando planteamientos teóricos difícilmente aplicables en entornos productivos complejos.

Asimismo, la incorporación de metodologías estructuradas, fases de ejecución y mecanismos de rollback contribuye a reforzar la robustez operativa de la propuesta, especialmente en ámbitos críticos como migraciones o integraciones.

No obstante, la viabilidad se ve parcialmente condicionada por la ausencia de métricas cuantificables, dimensionamiento explícito y definición de capacidades, lo que dificulta evaluar de forma objetiva el comportamiento esperado de la solución en escenarios de carga real.

Adicionalmente, la presencia recurrente de formulaciones abiertas del tipo “se analizará” o “se decidirá posteriormente” introduce cierta incertidumbre en aspectos clave, trasladando decisiones relevantes a fases posteriores.

En consecuencia, la solución puede considerarse claramente viable, desde un punto de vista técnico y operativo, pero con márgenes de mejora en su nivel de concreción.

**Valoración: ALTA**

Puntuación asignada: 0,75 / 1

### Metodología de trabajo

El análisis de la metodología de trabajo pone de manifiesto que la propuesta incorpora un modelo estructurado basado en buenas prácticas reconocidas, incluyendo referencias a marcos como ITIL, DevOps y Agile.

Se identifican elementos relevantes como:

- gestión de incidencias y cambios

- automatización de despliegues

- control de versiones

- validación continua

- separación de entornos

- trazabilidad de actuaciones

Este conjunto de prácticas permite configurar un modelo operativo coherente con las necesidades del servicio, especialmente en entornos de operación continua.

Sin embargo, a pesar de esta base metodológica, se detecta una limitación clara en la **formalización operativa**, ya que en muchos casos no se describen procedimientos detallados, flujos de trabajo específicos, herramientas utilizadas ni entregables concretos, lo que reduce la capacidad de evaluar la aplicabilidad real del modelo.

En consecuencia, la metodología puede considerarse adecuada y alineada con buenas prácticas, pero con un nivel de desarrollo insuficiente para alcanzar la excelencia.

**Valoración: MEDIA-ALTA**

Puntuación asignada: 0,60 / 1

### Rendimiento previsible de la solución

El rendimiento constituye uno de los aspectos donde la propuesta presenta mayores debilidades relativas.

Aunque la memoria incluye múltiples referencias a la optimización de rendimiento, el uso de caché, la mejora de tiempos de respuesta o la reducción de carga, estas afirmaciones se mantienen en un plano conceptual, sin acompañarse de:

- métricas cuantificables

- estimaciones de capacidad

- indicadores técnicos

- comparativas de mejora

- objetivos de rendimiento

Esta ausencia de cuantificación limita de manera significativa la capacidad de evaluar el impacto real de la solución, ya que no permite establecer una base objetiva de comprobación ni definir criterios de aceptación medibles.

En consecuencia, a pesar de que la intención de mejora del rendimiento está claramente presente, su materialización técnica no alcanza el nivel requerido para las franjas superiores del baremo.

**Valoración: MEDIA**

Puntuación asignada: 0,50 / 1

### Grado de satisfacción de los requisitos

El grado de satisfacción de los requisitos constituye la síntesis final del análisis, al evaluar la cobertura global del Anexo II y la adecuación de la propuesta a las necesidades definidas.

En este ámbito, la propuesta presentada por empresa_s destaca por una cobertura prácticamente completa de los requisitos, sin identificarse omisiones significativas ni apartados sin respuesta.

Se aprecia una correspondencia clara entre los requisitos del pliego y las soluciones propuestas, lo que permite afirmar que la propuesta responde de manera adecuada al alcance solicitado.

No obstante, tal y como se ha puesto de manifiesto a lo largo del análisis, esta cobertura se produce en muchos casos con un nivel de detalle limitado, especialmente en términos de métricas, herramientas y procedimientos, lo que reduce el grado de satisfacción efectiva frente al esperado en los niveles más altos del baremo.

En consecuencia, el grado de satisfacción de los requisitos puede considerarse alto, aunque no excelente.

**Valoración: ALTA**

Puntuación asignada: 5,75 / 8

## CONCLUSIÓN DEL CAPÍTULO 3

### Resumen cuantitativo

| **Criterio** | **Puntos máx.** | **Puntuación** |
| --- | --- | --- |
| Arquitectura | 2 | 1,50 |
| Comprensión | 2 | 1,75 |
| Viabilidad | 1 | 0,75 |
| Metodología | 1 | 0,60 |
| Rendimiento | 1 | 0,50 |
| Satisfacción requisitos | 8 | 5,75 |
| **TOTAL** | **15** | **10,85** |

La evaluación global de la solución técnica permite posicionar la propuesta de empresa_s en un **nivel ALTO dentro del baremo del apartado 7.2.2**, caracterizado por:

### Fortalezas principales

- elevada cobertura de requisitos

- buena comprensión del entorno

- arquitectura coherente

- viabilidad técnica sólida

- enfoque metodológico correcto

### Debilidades estructurales

- ausencia sistemática de métricas

- escasa identificación de herramientas

- falta de cuantificación del rendimiento

- nivel de abstracción elevado en algunos apartados

- planificación técnica parcialmente abstracta

La puntuación obtenida:

**10,85 / 15 puntos**

representa de forma equilibrada:

- una propuesta sólida y bien desarrollada

- pero sin el nivel de detalle, precisión y cuantificación requerido 
  para alcanzar las franjas más altas del baremo

## EVALUACIÓN DE LA PLANIFICACIÓN (APARTADO 7.2.3 DEL Documento de Invitación)

La presente sección tiene como finalidad analizar la planificación propuesta por la empresa empresa_s desde una perspectiva técnica y operativa, de acuerdo con los criterios definidos en el apartado 7.2.3 del Documento de Invitación. **Este análisis no se limita a verificar la existencia de un plan de trabajo, sino que evalúa en profundidad su nivel de detalle, su coherencia interna, su alineación con la complejidad del servicio y su capacidad para garantizar una ejecución controlada, trazable y verificable de las actuaciones previstas.**

En este contexto, la planificación debe ser entendida como un elemento estructural fundamental de la propuesta, que permite transformar la solución técnica en una realidad operativa, articulando temporalmente las actividades, identificando dependencias, estableciendo hitos y definiendo mecanismos de control que aseguren el cumplimiento de los objetivos del contrato.

A continuación, se desarrolla el análisis individualizado de los distintos subcriterios definidos en el Documento de Invitación.

### Calendario y planificación del servicio

El análisis del calendario y planificación constituye el elemento central del bloque, dado que representa la mayor ponderación dentro del apartado 7.2.3, siendo determinante en la valoración global de la capacidad del licitador para ejecutar el servicio en condiciones reales.

**La propuesta presentada por empresa_s plantea una planificación estructurada en fases, en la que se identifican etapas diferenciadas correspondientes al arranque del servicio, la transición inicial, la fase de ejecución ordinaria y la mejora continua.** Esta organización responde a un esquema conceptual habitual en servicios de mantenimiento y evolución tecnológica, y permite establecer una secuencia lógica de actuaciones que facilita la comprensión global del modelo de ejecución.

Desde esta perspectiva, se aprecia un esfuerzo por construir una visión unificada del servicio, evitando la fragmentación por subproyectos y proponiendo una planificación transversal que integra los distintos ámbitos del contrato dentro de un marco común. **Este enfoque resulta adecuado en entornos complejos como el analizado, en los que la interdependencia entre sistemas requiere una coordinación global de las actuaciones.**

**No obstante, el análisis detallado pone de manifiesto que dicha planificación se mantiene en un nivel claramente conceptual, sin descender al grado de detalle necesario para su implementación operativa.** En particular, no se presenta un cronograma detallado que permita identificar la duración de las actividades, su secuencia temporal o su interrelación. Tampoco se incluye un diagrama tipo Gantt o equivalente que facilite la visualización del calendario de ejecución.

**Asimismo, no se realiza un desglose por subproyecto o tipo de actuación, lo que impide evaluar la adecuación de los tiempos propuestos en función de la complejidad de cada uno de los ámbitos incluidos en el contrato.** Esta ausencia resulta especialmente relevante en un escenario que incluye 53 subproyectos con niveles de criticidad y carga de trabajo muy heterogéneos.

De igual modo, no se identifican hitos intermedios claramente definidos que permitan verificar el avance del servicio, ni se establecen entregables asociados a dichos hitos, lo que limita de forma significativa la capacidad de seguimiento y control del proyecto.

Adicionalmente, la propuesta no contempla una asignación explícita de recursos temporales ni una estimación del esfuerzo requerido para las distintas actividades, lo que introduce incertidumbre en la evaluación de la viabilidad temporal del conjunto.

En consecuencia, aunque la planificación presenta una estructura coherente a nivel global y una orientación adecuada desde el punto de vista conceptual, carece del nivel de detalle operativo exigible para garantizar una ejecución plenamente controlada y verificable.

**MEDIA**

**Puntuación asignada: 5,50 / 11**

### Análisis de riesgos

El análisis de riesgos constituye un elemento esencial en la planificación de servicios complejos, permitiendo anticipar posibles incidencias, evaluar su impacto y establecer mecanismos de mitigación que reduzcan la probabilidad de materialización o sus consecuencias sobre el servicio.

**La propuesta presentada por empresa_s incorpora referencias explícitas a la existencia de riesgos asociados a la ejecución del contrato, especialmente en relación con la criticidad de los sistemas, la complejidad de las integraciones y la coexistencia de entornos heterogéneos.** Este reconocimiento constituye un aspecto positivo, ya que demuestra una cierta sensibilidad hacia la incertidumbre inherente a este tipo de servicios.

Asimismo, en distintos apartados de la memoria técnica se identifican elementos que pueden interpretarse como una gestión implícita de riesgos, tales como la validación previa de cambios, el uso de entornos de preproducción o la implementación de mecanismos de rollback, lo que contribuye a reducir el impacto de posibles incidencias.

No obstante, el análisis detallado pone de manifiesto la ausencia de un modelo formal de gestión de riesgos, entendida como un proceso estructurado que incluya la identificación sistemática de riesgos, su clasificación, la evaluación de su probabilidad e impacto, y la definición de medidas de mitigación asociadas.

**En particular, no se presenta una matriz de riesgos que permita visualizar de forma estructurada los distintos escenarios de riesgo, ni se establecen criterios de priorización que permitan focalizar los esfuerzos de mitigación en aquellos riesgos de mayor criticidad.** Tampoco se definen indicadores que permitan monitorizar la evolución del riesgo a lo largo del tiempo.

Asimismo, no se identifican responsables de la gestión de riesgos ni se establecen mecanismos de seguimiento y revisión periódica, lo que limita la capacidad de integrar este proceso dentro del ciclo de vida del servicio.

En consecuencia, la propuesta presenta un reconocimiento adecuado de la existencia de riesgos y una gestión implícita en determinados procesos, pero carece de la formalización y estructuración necesarias para considerarse un modelo robusto de gestión de riesgos.

**MEDIA-ALTA**

**Puntuación asignada: 0,60 / 1**

### Plan de contingencias

El análisis del plan de contingencias tiene como objetivo evaluar la capacidad de la propuesta para anticipar situaciones anómalas o críticas durante la ejecución del servicio, así como para definir mecanismos de respuesta que permitan minimizar el impacto de dichas situaciones sobre la continuidad operativa.

En la propuesta presentada por empresa_s se identifican distintos elementos que, aunque no estructurados formalmente como un plan de contingencias independiente, contribuyen a configurar un modelo implícito de gestión de incidencias. **Entre estos elementos destacan de manera significativa la incorporación de procedimientos de rollback en numerosos subproyectos, la utilización sistemática de entornos de preproducción para la validación previa de cambios, así como la separación de entornos y la ejecución progresiva de actuaciones críticas.**

**Este conjunto de prácticas permite inferir la existencia de un enfoque orientado a la mitigación de riesgos operativos, especialmente en aquellos ámbitos donde la introducción de cambios puede tener un impacto elevado sobre la disponibilidad del servicio.** Asimismo, la presencia de validaciones previas y pruebas funcionales refuerza la capacidad del sistema para detectar errores antes de su paso a producción.

**No obstante, el análisis en profundidad pone de manifiesto que estos elementos no se articulan dentro de un marco formal de contingencias, en el que se definan de manera explícita los distintos escenarios de fallo, las acciones a realizar en cada caso, los responsables de su ejecución y los tiempos estimados de recuperación.** En particular, no se identifican parámetros clave como los tiempos objetivo de recuperación (RTO) o los niveles de pérdida de datos aceptables (RPO), ni se establecen protocolos estructurados para la actuación ante incidentes críticos.

Asimismo, no se describe la existencia de procedimientos documentados que permitan garantizar la repetibilidad de las actuaciones ante situaciones similares, ni se contemplan mecanismos de simulación o pruebas periódicas de contingencias que permitan validar la eficacia del modelo en condiciones reales.

En consecuencia, la propuesta presenta un conjunto de buenas prácticas que contribuyen a la resiliencia del sistema, pero carece de la formalización necesaria para configurar un plan de contingencias robusto, estructurado y plenamente verificable.

**MEDIA-ALTA**

**Puntuación asignada: 0,60 / 1**

### Plan de calidad

El análisis del plan de calidad tiene como finalidad evaluar la capacidad de la propuesta para garantizar que las actuaciones realizadas cumplen con los niveles de calidad esperados, incorporando mecanismos de control, validación y mejora continua del servicio.

La propuesta presentada por empresa_s incorpora distintos elementos que permiten identificar una orientación clara hacia la calidad, incluyendo la definición de procesos de validación funcional, la realización de pruebas técnicas, la verificación de integraciones y la incorporación de prácticas propias de entornos DevOps, como la automatización de despliegues y la integración continua.

**Este conjunto de prácticas contribuye a establecer un modelo operativo en el que la calidad se incorpora de manera transversal a lo largo del ciclo de vida del software, evitando su tratamiento como una fase aislada y favoreciendo una validación continua de las actuaciones realizadas.** Asimismo, la referencia a procesos de revisión y validación previos al paso a producción refuerza la percepción de control sobre la ejecución del servicio.

**Sin embargo, el análisis detallado revela que estos elementos no se desarrollan dentro de un plan de calidad formalmente estructurado, en el que se definan objetivos claros, indicadores de rendimiento, métricas de calidad y procedimientos específicos de seguimiento.** En particular, no se identifican indicadores clave de desempeño (KPIs) asociados a la calidad del servicio, tales como tiempos de respuesta, niveles de disponibilidad, tasas de error o métricas de satisfacción.

**Asimismo, no se describen mecanismos específicos de mejora continua, ni se establece un sistema de evaluación periódica que permita medir la evolución de la calidad a lo largo del tiempo.** De igual modo, no se identifican herramientas concretas para la gestión de calidad ni se definen roles responsables de su seguimiento.

En consecuencia, la propuesta incorpora buenas prácticas orientadas a la calidad, pero carece de un modelo formal que permita medir, controlar y mejorar de manera sistemática el nivel de servicio.

**MEDIA-ALTA**

**Puntuación asignada: 0,65 / 1**

### Trazabilidad

La trazabilidad constituye un elemento fundamental para el control del servicio, al permitir registrar, seguir y auditar todas las actuaciones realizadas, facilitando la identificación de responsabilidades, la reconstrucción de eventos y la evaluación del cumplimiento de los objetivos.

**La propuesta presentada por empresa_s incorpora referencias a distintos mecanismos que contribuyen a la trazabilidad, tales como la gestión de logs, el control de cambios, la auditoría de accesos y el seguimiento de determinadas actuaciones técnicas.** Estos elementos permiten inferir la existencia de un modelo básico de registro de actividad, orientado a garantizar un cierto nivel de visibilidad sobre el funcionamiento del sistema.

Asimismo, la integración de sistemas de autenticación centralizada, así como la incorporación de elementos de auditoría en distintos subproyectos, contribuyen a reforzar la capacidad de seguimiento de las operaciones realizadas por usuarios y sistemas.

No obstante, el análisis detallado pone de manifiesto que estos elementos no se integran dentro de un sistema estructurado de trazabilidad, en el que se definan de manera explícita los flujos de información, los sistemas implicados, los mecanismos de correlación de eventos y los procedimientos de explotación de la información generada.

**En particular, no se identifican herramientas específicas para la gestión centralizada de logs, ni se describen sistemas de correlación que permitan analizar de forma conjunta eventos procedentes de distintas fuentes.** Tampoco se establecen criterios de retención de información, niveles de detalle en el registro de eventos o mecanismos de explotación analítica de los datos.

Asimismo, no se define un modelo de trazabilidad end-to-end que permita seguir de forma completa el ciclo de vida de una actuación, desde su solicitud inicial hasta su resolución final, incluyendo validaciones, aprobaciones y despliegues.

En consecuencia, la propuesta presenta elementos parciales de trazabilidad, pero carece de un modelo completo, integrado y estructurado que permita garantizar un control exhaustivo del servicio.

**MEDIA**

**Puntuación asignada: 0,50 / 1**

### RESUMEN GLOBAL DE LA PLANIFICACIÓN

El análisis conjunto de los distintos subcriterios de planificación permite identificar una propuesta que presenta una estructura general coherente y una comprensión adecuada de los elementos básicos de gestión de servicios, pero que adolece de una falta significativa de detalle operativo en aspectos clave para su ejecución.

En particular, la planificación se caracteriza por una adecuada organización conceptual en fases, una incorporación implícita de mecanismos de control y una orientación a la calidad y a la mitigación de riesgos, lo que permite afirmar que existe una base metodológica suficientemente sólida para abordar el servicio desde un punto de vista global.

No obstante, estas fortalezas se ven claramente limitadas por la ausencia de un desarrollo detallado en los elementos más críticos para la evaluación del apartado 7.2.3, especialmente en lo relativo al calendario de ejecución, la definición de hitos, la formalización del análisis de riesgos, la estructuración del plan de contingencias y la implantación de un modelo completo de calidad y trazabilidad.

Esta falta de detalle no implica una inviabilidad de la propuesta, pero sí limita de manera significativa su capacidad de ser evaluada como una planificación plenamente controlada, medible y verificable, requisitos que resultan fundamentales para alcanzar las franjas superiores del baremo.

A partir del análisis realizado, se obtiene la siguiente distribución de puntuaciones:

### Resumen cuantitativo de la planificación (7.2.3)

| **Criterio** | **Puntos máximos** | **Puntuación** |
| --- | --- | --- |
| Calendario y planificación | 11 | 5,50 |
| Análisis de riesgos | 1 | 0,60 |
| Plan de contingencias | 1 | 0,60 |
| Plan de calidad | 1 | 0,65 |
| Trazabilidad | 1 | 0,50 |
| **TOTAL** | **15** | **7,85** |

En consecuencia, la planificación presentada por empresa_s se sitúa de forma coherente en una valoración **ALTA (aunque muy cerca del límite con la franja MEDIA**) según el baremo incluido en el capítulo 7.2.2 del PPT. Esta valoración refleja una propuesta estructurada y viable, pero insuficientemente desarrollada en términos de precisión, control y cuantificación.

## PUNTUACIÓN GLOBAL JUSTIFICADA

A partir del análisis detallado desarrollado en los capítulos anteriores, tanto en lo relativo a la solución técnica ofertada como a la planificación del servicio, se procede a establecer una valoración global integrada de la propuesta presentada por la empresa empresa_s, conforme al modelo de juicio de valor definido en el apartado 7.2 del Documento de Invitación.

**La evaluación realizada pone de manifiesto que la oferta presenta un nivel de desarrollo técnico global elevado, caracterizado por una amplia cobertura de los requisitos del Anexo II, una comprensión clara del entorno tecnológico y una arquitectura coherente y adecuadamente estructurada.** Este posicionamiento se ha visto reflejado de manera consistente en el análisis del capítulo 3, donde la propuesta se sitúa de forma estable en la franja de valoración alta, sin alcanzar el nivel máximo exigido para obtener la puntuación plena.

**De forma complementaria, el análisis de la planificación desarrollado en el capítulo 4 evidencia la existencia de un enfoque organizado y coherente a nivel conceptual, aunque con un nivel de detalle insuficiente en aspectos clave como la temporalización, la definición de hitos, la gestión formal de riesgos o la estructuración de los mecanismos de control y seguimiento.** Esta circunstancia ha determinado una valoración intermedia de este bloque, situándolo en una franja media con tendencia a media-alta, claramente inferior a la obtenida en la solución técnica.

**La combinación de ambos bloques permite identificar una propuesta sólida, técnicamente consistente y viable desde el punto de vista operativo, pero con limitaciones estructurales en su nivel de concreción, especialmente en aquellos aspectos que afectan a la verificabilidad, medición y control del servicio.** Estas limitaciones resultan especialmente relevantes en un procedimiento de este tipo, en el que la capacidad de justificar de manera objetiva el cumplimiento de los requisitos constituye un elemento fundamental.

En consecuencia, la valoración global se sitúa de forma coherente en una posición intermedia dentro de las franjas superiores del baremo, reflejando tanto la calidad de la propuesta como las carencias detectadas.

### Principales elementos destacados de la oferta

Del análisis realizado se derivan una serie de elementos positivos que contribuyen de manera significativa a la valoración obtenida y que caracterizan la propuesta como una oferta técnicamente consistente y alineada con los requisitos del pliego:

- Destaca de manera significativa el elevado grado de cobertura de los requisitos del Anexo II, no identificándose omisiones relevantes y existiendo una correspondencia clara entre los subproyectos solicitados y las soluciones planteadas en la memoria técnica.

- Se aprecia una comprensión profunda del entorno EducaMadrid y de las interrelaciones entre sus distintos componentes, evidenciada en la forma en que se abordan aspectos complejos como la integración de sistemas, la gestión de identidades o la evolución de plataformas como Drupal o Moodle.

- La arquitectura propuesta presenta una estructura coherente, basada en principios de modularidad, desacoplamiento e integración mediante APIs, lo que permite articular de forma consistente los distintos ámbitos del servicio.

- La viabilidad técnica de la solución es elevada, apoyándose en tecnologías alineadas con el contexto real del entorno y evitando planteamientos disruptivos que pudieran comprometer la continuidad del servicio.

- La propuesta incorpora buenas prácticas metodológicas, incluyendo referencias a modelos de gestión reconocidos y a procesos de validación, despliegue controlado y gestión de cambios, lo que contribuye a reforzar la robustez operativa del conjunto.

### Principales limitaciones y carencias detectadas

Junto a los elementos positivos anteriormente descritos, el análisis ha permitido identificar una serie de debilidades recurrentes que limitan la valoración obtenida y que justifican la no inclusión de la propuesta en las franjas superiores del baremo:

- Se detecta de forma sistemática la ausencia de métricas cuantificables, indicadores de rendimiento o KPIs que permitan evaluar objetivamente el impacto de las soluciones propuestas, especialmente en lo relativo al rendimiento del sistema.

- La propuesta presenta una escasa identificación de herramientas concretas en numerosos ámbitos, lo que introduce incertidumbre sobre la implementación efectiva de determinados procesos.

- Se observa un nivel de abstracción elevado en la descripción de algunos componentes, especialmente en arquitectura y metodología, sin llegar al grado de detalle operativo necesario para garantizar una ejecución completamente controlada.

- La planificación del servicio constituye uno de los elementos más limitantes, debido a la falta de un calendario detallado, la ausencia de hitos verificables y la inexistencia de un modelo temporal claramente definido.

- La gestión de riesgos, contingencias, calidad y trazabilidad se presenta de forma parcialmente desarrollada y no estructurada, sin alcanzar un nivel de formalización suficiente para garantizar su aplicación sistemática a lo largo del servicio.

### Resumen cuantitativo de la valoración

A partir de las valoraciones cuantitativas establecidas en los capítulos 3 y 4, se obtiene la siguiente síntesis global de puntuación para los criterios sujetos a juicio de valor:

<table>
  <tr>
    <th><strong>BLOQUE</strong></th>
    <th><strong>Criterio</strong></th>
    <th><strong>Puntos máximos</strong></th>
    <th><strong>Puntuación</strong></th>
  </tr>
  <tr>
    <td rowspan="7"><strong>Solución técnica</strong></td>
    <td>Arquitectura</td>
    <td>2</td>
    <td>1,50</td>
  </tr>
  <tr>
    <td>Comprensión requisitos</td>
    <td>2</td>
    <td>1,75</td>
  </tr>
  <tr>
    <td>Viabilidad</td>
    <td>1</td>
    <td>0,75</td>
  </tr>
  <tr>
    <td>Metodología</td>
    <td>1</td>
    <td>0,60</td>
  </tr>
  <tr>
    <td>Rendimiento</td>
    <td>1</td>
    <td>0,50</td>
  </tr>
  <tr>
    <td>Satisfacción requisitos</td>
    <td>8</td>
    <td>5,75</td>
  </tr>
  <tr>
    <td><strong>Subtotal solución técnica</strong></td>
    <td><strong>15</strong></td>
    <td><strong>10,85</strong></td>
  </tr>
  <tr>
    <td rowspan="6"><strong>Planificación</strong></td>
    <td>Calendario</td>
    <td>11</td>
    <td>5,50</td>
  </tr>
  <tr>
    <td>Riesgos</td>
    <td>1</td>
    <td>0,60</td>
  </tr>
  <tr>
    <td>Contingencias</td>
    <td>1</td>
    <td>0,60</td>
  </tr>
  <tr>
    <td>Calidad</td>
    <td>1</td>
    <td>0,65</td>
  </tr>
  <tr>
    <td>Trazabilidad</td>
    <td>1</td>
    <td>0,50</td>
  </tr>
  <tr>
    <td><strong>Subtotal planificación</strong></td>
    <td><strong>15</strong></td>
    <td><strong>7,85</strong></td>
  </tr>
  <tr>
    <td><strong>TOTAL</strong> <br><strong>(<strong><em><em>J</em></strong></em>uicios de valor)</strong></td>
    <td></td>
    <td><strong>30</strong></td>
    <td><strong>18,70</strong></td>
  </tr>
</table>

### Conclusión final

En base al análisis realizado, la propuesta presentada por empresa_s obtiene una puntuación total de **18,70 puntos sobre 30**, y por tanto una valoración **ALTA***,** posicionándose de forma justificada como una oferta técnicamente sólida, viable y ampliamente alineada con los requisitos del pliego, pero limitada por un **déficit de concreción técnica, cuantificación y detalle en la planificación**, que impide alcanzar niveles de excelencia en la valoración por juicios de valor.

<!-- salto de página -->

## ANEXO CLASIFICACIÓN DE LA PROPUESTA TÉCNICA POR SUBPROYECTO

## Criterios de clasificación

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

El análisis realizado sobre la memoria técnica evidencia que empresa_s incorpora, en muchos subproyectos, propuestas de mejora y aportación de valor añadido, estructuradas explícitamente en el documento.

## Tablas de proyectos y grado de desarrollo

## Proyectos Web Liferay (ELIF)

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| ELIF1 | Propuesta técnica con mejoras (sin valor añadido) | PM (reutilización componentes y mantenibilidad) |
| ELIF2 | Propuesta técnica incluida (desarrollo deficiente) | No |
| ELIF3 | Propuesta técnica incluida (desarrollo suficiente) | No |
| ELIF4 | Propuesta técnica con mejoras (sin valor añadido) | PM (auditorías, revisiones, entornos no productivos, automatización de releases) |

## Innovación y Formación del Profesorado (IFP)

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| IFP1 | Propuesta técnica incluida (desarrollo suficiente) | No |

## Proyectos Moodle Misc (EMOM)

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| EMOM1 | Propuesta técnica incluida (desarrollo suficiente) | No |
| EMOM2 | Propuesta técnica incluida (desarrollo suficiente) | No |
| EMOM3 | Propuesta técnica con valor añadido | VA (uso Redis para rendimiento) |
| EMOM4 | Propuesta técnica incluida (desarrollo suficiente) | No |
| EMOM5 | Propuesta técnica incluida (desarrollo deficiente) | No |
| EMOM6 | Propuesta técnica incluida (desarrollo deficiente) | No |
| EMOM7 | Propuesta técnica con valor añadido | VA (integración selectiva SSO) |

## Proyectos de Dinámicas (EDIN)

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| EDIN1 | Propuesta técnica con valor añadido | VA (inventario y matriz de riesgo) |
| EDIN2 | Propuesta técnica incluida (desarrollo deficiente) | No |

## Integración EducaMadrid (EIPE)

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| EIPE1 | Propuesta técnica incluida (desarrollo suficiente) | No |
| EIPE2 | Propuesta técnica incluida (desarrollo suficiente) | No |

## Sistemas Externos (ESIS)

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| ESIS1 | Propuesta técnica con mejoras (sin valor añadido) | PM (automatización y gobierno del ciclo de vida software) |
| ESIS2 | Propuesta técnica con mejoras (sin valor añadido) | PM (automatización y gobierno de plataformas de datos) |
| ESIS3 | Propuesta técnica con valor añadido | VA (gobierno e integración de servicios avanzada) |
| ESIS4 | Propuesta técnica con mejoras (sin valor añadido) | PM (modelo centralizado y<br>gobernado de integración segura) |
| ESIS5 | Propuesta técnica con mejoras (sin valor añadido) | PM (evolucionar la autenticación centralizada hacia una plataforma moderna) |
| ESIS6 | Propuesta técnica con valor añadido | VA (modernización y gobierno IAM) |
| ESIS7 | Propuesta técnica con valor añadido | VA (plataforma avanzada de gobierno y<br>observabilidad de identidades) |
| ESIS8 | Propuesta técnica con valor añadido | VA (control IAM) |
| ESIS9 | Propuesta técnica con valor añadido | VA (modelo automatizado y<br>gobernado de validación de aplicativos) |
| ESIS10 | Propuesta técnica con valor añadido | VA (modelo DevSecOps) |
| ESIS11 | Propuesta técnica con valor añadido | VA (plataforma avanzada de administración centralizada y automatizada de BBDD) |
| ESIS12 | Propuesta técnica con valor añadido | VA (capacity planning) |
| ESIS13 | Propuesta técnica con valor añadido | VA (plataforma automatizada y<br>gobernada de aprovisionamiento) |
| ESIS14 | Propuesta técnica con valor añadido | VA (hardening con CIS/ENS) |
| ESIS15 | Propuesta técnica con valor añadido | VA (DevSecOps e IaC) |
| ESIS16 | Propuesta técnica con valor añadido | VA (automatización de configuraciones – IaC y auditoría automática de configs.) |
| ESIS17 | Propuesta técnica con valor añadido | VA (Evolucionar LDAP a Identity Governance) |
| ESIS18 | Propuesta técnica con mejoras (sin valor añadido) | PM (seguridad SPF/DKIM) |
| ESIS19 | Propuesta técnica con valor añadido | VA (gobierno y observabilidad de datos) |
| ESIS20 | Propuesta técnica con valor añadido | VA (gestión avanzada CMDB) |
| ESIS21 | Propuesta técnica con mejoras (sin valor añadido) | PM (gobierno del conocimiento) |
| ESIS22 | Propuesta técnica con valor añadido | VA (metodología MAGERIT) |
| ESIS23 | Propuesta técnica con valor añadido | VA (repositorios WORM y replicación entre CPDs) |
| ESIS24 | Propuesta técnica incluida (desarrollo deficiente) | No (lo que incluye no supone una mejora o un valor añadido) |
| ESIS25 | Propuesta técnica con valor añadido | VA (Inteligencia operacional e integración con SOC) |
| ESIS26 | Propuesta técnica con valor añadido | VA (MFA unificado, hardening con pantillas STIC y reporting ENS) |
| ESIS27 | Propuesta técnica con valor añadido | VA (modelo continuo de defensa activa y<br>observabilidad inteligente) |
| ESIS28 | Propuesta técnica con valor añadido | VA (gestión<br>proactiva del ciclo de vida tecnológico:) |
| ESIS29 | Propuesta técnica con valor añadido | VA (modelo integral de gobierno técnico) |
| ESIS30 | Propuesta técnica incluida (desarrollo deficiente) | PM (microsegmentación y seguridad adaptativa) |
| ESIS31 | Propuesta técnica incluida (desarrollo suficiente) | PM (evolucionar virtualización a modelos preparados para la IA) |

## Seguridad de Aplicaciones Web (ESEG)

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| ESEG1 | Propuesta técnica con mejoras (sin valor añadido) | PM (sistema continuo de validación ofensiva) |
| ESEG2 | Propuesta técnica incluida (desarrollo deficiente) | PM (evolución a SIEM) |
| ESEG3 | Propuesta técnica con mejoras (sin valor añadido) | PM (modelo ASM - Attack Surface<br>Management) |

## Desarrollo Seguro Web (EDSA)

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| EDSA1 | Propuesta técnica con valor añadido | VA (Implantar DevSecOps) |
| EDSA2 | Propuesta técnica con valor añadido | VA (Seguridad integrada en desarrollo) |

## Bug Bounty (EBBO)

| **Proyecto** | **Clasificación** | **Valor añadido** |
| --- | --- | --- |
| EBBO1 | Propuesta técnica incluida (desarrollo deficiente) | No |

## Conclusión global del análisis del grado de desarrollo

El análisis conjunto realizado sobre los distintos proyectos y subproyectos incluidos en el Anexo II del Documento de Invitación permite extraer una serie de conclusiones globales respecto al grado de desarrollo de la propuesta técnica presentada por empresa_s.

En primer lugar, debe destacarse que la propuesta técnica **cubre la totalidad de los subproyectos definidos en el pliego**, no habiéndose identificado casos en los que no exista respuesta técnica. Este hecho evidencia un adecuado nivel de comprensión del alcance del contrato y una correspondencia directa entre los requisitos establecidos y las soluciones planteadas.

No obstante, el grado de desarrollo de dichas propuestas presenta un comportamiento heterogéneo. La mayoría de los subproyectos se sitúan en el nivel de **propuesta técnica incluida con desarrollo suficiente**, **Propuesta técnica con mejoras (sin valor añadido)** o **Propuesta técnica con valor añadido**, lo que implica la existencia de planteamientos técnicos concretos y una definición razonable de arquitectura o procesos. Sin embargo, de forma recurrente, dichas propuestas adolecen de carencias en aspectos clave como la definición de herramientas específicas, la formalización de procedimientos de implementación, la identificación de entregables y la incorporación de métricas o indicadores de validación.

Asimismo, se observa la presencia de un conjunto no despreciable de subproyectos clasificados como **propuesta técnica incluida con desarrollo deficiente**, especialmente en aquellos ámbitos de menor complejidad o carácter más transversal, en los que la respuesta se mantiene en un nivel descriptivo sin alcanzar un grado suficiente de concreción técnica.

Por otro lado, el **valor añadido** se manifiesta de forma selectiva y no homogénea a lo largo de los distintos proyectos. Este se concentra principalmente en determinados ámbitos técnicos de mayor complejidad o criticidad. En estos casos, la propuesta incorpora mejoras claras respecto a los requisitos del pliego, introduciendo enfoques metodológicos, arquitecturas o tecnologías adicionales que aportan un valor diferencial.

En términos globales, puede concluirse que la propuesta técnica presenta un nivel **sólido y consistente**, con una cobertura completa de requisitos y múltiples áreas correctamente desarrolladas, si bien el valor añadido no se distribuye de forma uniforme y el grado de desarrollo técnico presenta ciertas carencias en lo relativo a concreción, cuantificación y formalización operativa. Estas circunstancias limitan la posibilidad de alcanzar niveles de excelencia, situando la propuesta en una posición intermedia dentro de la franja de valoración ALTA.
