# Revisión de posibles motivos de recurso de empresa_n

## 1. Objeto, alcance y criterio de la revisión

Este documento revisa, desde la perspectiva de una eventual reclamación o recurso de **empresa_n**, los siguientes informes:

- `desarrollo/informes/informe_conjunto_y_normalizado_desarrollo.md`;
- `exteriores/informes/informe_conjunto_y_normalizado_exteriores.md`;
- `sistemas/informes/informe_conjunto_y_normalizado_sistemas.md`.

El objetivo no es sustituir el juicio técnico ni afirmar que un recurso vaya a prosperar, sino localizar puntos de exposición y proponer formas de motivar los informes con mayor seguridad. **Una redacción más extensa no subsana una regla de valoración introducida después de presentarse las ofertas, un dato técnicamente incorrecto ni una puntuación carente de soporte**. En esos casos, la opción recomendada incluye verificar el expediente y, si procede, volver a valorar.

La revisión se ha realizado sobre los archivos disponibles en el repositorio. Antes de aprobar una versión definitiva debe contrastarse cuál fue la documentación contractual **firmada, publicada y puesta a disposición de los licitadores antes de presentar sus ofertas**. Los archivos locales llamados `_bis.md` no se consideran por sí solos documentación contractual vigente.

### Escala de prioridad

- **Crítica**: puede afectar a las reglas aplicadas o a errores materiales determinantes de la puntuación.
- **Alta**: puede comprometer la motivación, la trazabilidad o la igualdad de trato.
- **Media**: normalmente es subsanable mediante una redacción más precisa si existe evidencia previa suficiente.

### Cómo se presentan las alternativas

Cada punto contiene varias opciones. La opción marcada con **[x]** es la recomendada. La selección presupone que todavía es posible revisar el informe antes de su aprobación o notificación. Si el acto ya hubiera sido aprobado o notificado, debe validarse con asesoría jurídica qué vía de rectificación o retroacción resulta procedente.

## 2. Marco mínimo de contraste

Las recomendaciones se apoyan en estas reglas generales:

- Los órganos de contratación deben respetar la **igualdad, la transparencia y la proporcionalidad** ([artículo 132 de la LCSP](https://www.boe.es/buscar/act.php?id=BOE-A-2017-12902#a132)).
- Los criterios deben estar vinculados al objeto y permitir una valoración conforme a las reglas anunciadas ([artículo 145](https://www.boe.es/buscar/act.php?id=BOE-A-2017-12902#a145) y [artículo 146 de la LCSP](https://www.boe.es/buscar/act.php?id=BOE-A-2017-12902#a146)). El umbral del 50 % en una fase de criterios cualitativos es compatible, en principio, con el artículo 146.3; el riesgo principal no está en la existencia del umbral, sino en cómo se obtienen y motivan las puntuaciones que conducen a él.
- La decisión debe estar **motivada** y permitir conocer las razones del rechazo y las características o ventajas de la oferta seleccionada ([artículo 151 de la LCSP](https://www.boe.es/buscar/act.php?id=BOE-A-2017-12902#a151)).
- La doctrina del TACRC admite la concreción técnica de aspectos generales, pero no la creación posterior de criterios, subcriterios o ponderaciones capaces de haber influido en la preparación de las ofertas. También exige que la motivación permita descartar arbitrariedad, discriminación o error material manifiesto ([Resolución 300/2025 del TACRC](https://www.hacienda.gob.es/TACRC/Resoluciones/A%C3%B1o%202025/Recurso%201796-2024%20AST%2088-2024%20%28Res%20300%29%2005-03-2025.pdf)).
- La utilización de niveles o porcentajes puede ser válida cuando está prevista de antemano; lo relevante es que la regla aplicada y la razón de la nota sean reconstruibles y no se inventen después de conocer las ofertas ([Resolución 1220/2019 del TACRC](https://www.hacienda.gob.es/tacrc/resoluciones/a%C3%B1o%202019/recurso%200969-2019%20mu%2074-2019%20%28res%201220%29%2028-10-2019.pdf)).

## 3. Resumen ejecutivo

| Código | Informe | Posible motivo de recurso | Prioridad | Recomendación resumida |
| --- | --- | --- | --- | --- |
| C-01 | Los tres | Apariencia de normalización o cambio metodológico posterior | Crítica | Acreditar la regla ex ante; si no existía, revalorar con la regla publicada |
| C-02 | Los tres | Falta de motivación del porcentaje exacto dentro de cada nivel | Alta | Explicar por qué se elige ese punto de la banda sin crear una fórmula nueva |
| C-03 | Los tres | Conversión no publicada de recuentos de subproyectos en notas | Alta | Usar el recuento solo como apoyo y motivar cualitativamente el criterio |
| C-04 | Los tres | Trazabilidad insuficiente hasta páginas concretas de la oferta | Alta | Incorporar una matriz de evidencia accesible en el expediente |
| C-05 | Los tres | Uso de elementos no exigidos como requisitos autónomos | Alta | Vincular cada carencia al descriptor publicado o eliminarla como penalización |
| C-06 | Los tres | Doble penalización por una misma carencia | Media-Alta | Identificar el efecto distinto en cada subcriterio o imputarla solo una vez |
| C-07 | Los tres | Confusión entre calidad, cumplimiento, solvencia y umbral | Media-Alta | Separar esas cuatro categorías y moderar afirmaciones absolutas |
| D-01 | Desarrollo | Error aparente en la acusación «CalDAV frente a ICS» | Crítica | Eliminarla y revisar si influyó en niveles o puntos |
| D-02 | Desarrollo | Cero en satisfacción pese a 12 desarrollos suficientes | Alta | Revalorar o justificar de forma reforzada por qué el descriptor es MUY BAJA |
| D-03 | Desarrollo | Tensión entre cronograma interpretable y nota MEDIA de 3,74 | Media-Alta | Mantener solo lo que realmente puede verificarse y explicar el 34 % |
| E-01 | Exteriores | Premisas técnicas discutibles sobre LDAP Plano y Drupal | Crítica | Verificar en fuentes contractuales; retirar y recalcular si no se acreditan |
| E-02 | Exteriores | Caída de satisfacción a 2,00/8,00 con cobertura parcial relevante | Alta | Motivar por importancia de requisitos, no por simple conteo |
| E-03 | Exteriores | Calendario 1,76/11 por cubrir solo un año de dos | Media | Mantener la nota si se acredita el periodo; reforzar cita y descriptor |
| S-01 | Sistemas | Ambigüedad entre versiones de la metodología y error «2 puntos» en `_bis` | Crítica | Identificar y citar exclusivamente la versión contractual vigente |
| S-02 | Sistemas | Cero en satisfacción pese a tres subproyectos suficientes | Alta | Revalorar o explicar por qué esos contenidos no apartan el conjunto de MUY BAJA |
| S-03 | Sistemas | «Ausencia» de MAX e IA cuando existen epígrafes que reproducen requisitos | Alta | Distinguir ausencia formal de falta de propuesta propia evaluable |
| S-04 | Sistemas | Escala auxiliar del CSV dentro del informe de valoración | Media-Alta | Retirarla del cuerpo del informe o declarar y demostrar que no puntúa |
| S-05 | Sistemas | Penalización del Gantt por recursos y búferes no expresos | Alta | Basar la nota en detalle, duración, relaciones e hitos publicados |

## 4. Puntos comunes a los tres informes

### C-01. Apariencia de normalización o modificación metodológica posterior

**Prioridad: crítica.**

**Posible alegación de empresa_n.** Los tres informes dicen que, «para normalizar puntuaciones previas», se adopta el entero más próximo y que el porcentaje exacto se fija atendiendo a alcance, concreción, coherencia, verificabilidad y peso de fortalezas y carencias. Esta frase puede interpretarse como reconocimiento de que, después de valorar o incluso después de conocer las ofertas, se introdujo una nueva regla de conversión. Además, el estado del repositorio muestra variaciones relevantes respecto de la versión base: empresa_n pasa de 11,30 a 8,29 en Desarrollo, de 10,05 a 7,66 en Exteriores y de 11,45 a 6,80 en Sistemas. El repositorio no demuestra que esas versiones fueran aprobadas o notificadas, pero obliga a documentar el historial real.

**Riesgo.** Si la regla no estaba fijada antes de las ofertas, la frase puede sostener una alegación de subcriterios o ponderaciones ex post. Si solo se corrigieron borradores internos, el riesgo disminuye, pero el expediente debe dejarlo claro.

**Opciones de redacción o actuación:**

- [ ] **Opción A — No cambiar el informe.** Solo sería aconsejable si existe un documento anterior a las ofertas, aprobado y accesible, que contenga exactamente esta regla y si se incorpora su referencia, fecha y versión al expediente.
- [ ] **Opción B — Eliminar únicamente «para normalizar puntuaciones previas».** Reduce la apariencia de revisión retrospectiva, pero no soluciona una eventual falta de regla previa ni explica los cambios de puntuación.
- [x] **Opción C — Verificar el historial y rehacer la explicación metodológica.** Si la regla era previa, citar literalmente el documento, su fecha y su ubicación en el expediente, y describir los cambios como correcciones motivadas de borradores no aprobados. Si no era previa, no aplicarla: revalorar conforme a los descriptores y porcentajes publicados, dejando acta del motivo y de la incidencia en cada puntuación.

**Redacción recomendada si la regla sí era previa:**

> La valoración se ha realizado aplicando exclusivamente los criterios, niveles y porcentajes recogidos en el Documento de Invitación [versión, fecha y apartado]. Las cifras reflejadas en este informe sustituyen a cálculos de trabajo no aprobados ni notificados y responden a las correcciones individualizadas que se detallan en la matriz de motivación, sin incorporar criterios, subcriterios ni ponderaciones nuevos.

### C-02. Falta de motivación del porcentaje exacto dentro de cada nivel

**Prioridad: alta.**

**Posible alegación de empresa_n.** Los informes asignan, por ejemplo, 16 %, 25 %, 34 %, 40 %, 50 % o 55 % del máximo, pero la frase genérica sobre «alcance, concreción, coherencia, verificabilidad y peso» no permite siempre reconstruir por qué se eligió exactamente ese porcentaje y no otro dentro del mismo nivel. También se utilizan rangos cerrados —76-100, 51-75, 26-50 y 1-25— donde los documentos normales de invitación expresan «hasta» determinados porcentajes.

**Opciones:**

- [ ] **Opción A — Conservar solo el nivel cualitativo y asignar siempre el límite publicado.** Es sencilla, pero puede alterar sustancialmente las puntuaciones y no debe adoptarse si la documentación no establece ese automatismo.
- [x] **Opción B — Mantener la nota exacta con motivación individualizada.** Para cada subcriterio, explicar qué rasgos positivos justifican superar la parte inferior del nivel y qué carencias impiden llegar al siguiente, sin convertir esos rasgos en una fórmula nueva.
- [ ] **Opción C — No cambiar.** Solo sería defendible si la matriz completa ya incorporada al expediente permite reconstruir cada porcentaje; los informes conjuntos actuales no lo hacen por sí solos en todos los casos.

**Plantilla recomendada:**

> **Nivel BAJA — 0,50/2,00 (25 %).** La oferta aporta [evidencia positiva concreta], por lo que existe contenido valorable. No alcanza MEDIA porque [carencia vinculada al descriptor publicado y referencia exacta]. Se sitúa en el límite superior de BAJA por [razón comparativa dentro del propio descriptor, no por comparación con otro licitador].

### C-03. Recuentos de subproyectos como posible regla de puntuación no publicada

**Prioridad: alta.**

**Posible alegación de empresa_n.** Las categorías «desarrollo suficiente», «desarrollo insuficiente» y «sin solución concreta» facilitan la trazabilidad, pero no aparecen como fórmula de conversión en la invitación. Al justificar niveles como MUY BAJA o BAJA mediante recuentos, puede parecer que se aplicó una regla cuantitativa oculta. El riesgo aumenta cuando una oferta con varios desarrollos considerados suficientes recibe cero puntos.

**Opciones:**

- [ ] **Opción A — Convertir expresamente el recuento en porcentaje.** No se recomienda salvo que esa fórmula estuviera publicada antes de las ofertas.
- [x] **Opción B — Mantener el recuento solo como dato auxiliar.** Aclarar que no genera automáticamente la nota; motivar el nivel atendiendo a la importancia, profundidad y adecuación de los requisitos afectados, conforme al descriptor publicado.
- [ ] **Opción C — Suprimir todos los recuentos.** Evita la apariencia de fórmula, pero pierde trazabilidad útil y puede debilitar la motivación.

**Redacción recomendada:**

> La clasificación del anexo es una herramienta de localización de evidencias y no una fórmula matemática de puntuación. El nivel se determina aplicando el descriptor publicado al contenido global del subcriterio, ponderando cualitativamente la relevancia de los requisitos afectados. El número de epígrafes suficiente o insuficientemente desarrollados se ofrece únicamente como elemento de apoyo.

### C-04. Trazabilidad insuficiente hasta la oferta y la exigencia contractual

**Prioridad: alta.**

**Posible alegación de empresa_n.** Las motivaciones breves remiten a informes individuales y anexos, pero numerosas afirmaciones técnicas no indican a la vez: código del requisito, página de la invitación, página de la oferta, fragmento evaluado, criterio afectado y efecto sobre el nivel. La mera afirmación de que existe «plena trazabilidad» no sustituye esa cadena probatoria.

**Opciones:**

- [ ] **Opción A — Copiar todo el análisis individual al informe conjunto.** Sería autosuficiente, pero muy extenso y propenso a contradicciones.
- [x] **Opción B — Incorporar una matriz de evidencia al expediente y referenciarla.** El informe conjunto debe contener la razón esencial de cada puntuación; la matriz puede aportar el detalle si queda incorporada al expediente y se facilita o se permite su acceso al licitador.
- [ ] **Opción C — Mantener la remisión genérica actual.** Presenta riesgo si el documento remitido no es identificable, estable o accesible.

**Campos mínimos de la matriz:** `subcriterio`, `código`, `exigencia`, `documento y página de la invitación`, `documento y página de la oferta`, `hallazgo`, `incidencia concreta en el nivel/puntuación` y `revisor`.

### C-05. Elementos no publicados tratados como requisitos autónomos

**Prioridad: alta.**

**Posible alegación de empresa_n.** Los informes penalizan con frecuencia la ausencia de herramientas, métricas, responsables, recursos, búferes, diagramas, criterios de aceptación o determinados mecanismos. Algunos pueden ser indicios razonables de detalle, viabilidad, rendimiento o trazabilidad; no obstante, si la invitación no los exige expresamente, no deben convertirse en requisitos independientes cuya ausencia produzca por sí sola una penalización.

**Opciones:**

- [ ] **Opción A — Mantener la formulación «debía incluir».** Solo cuando pueda citarse la cláusula que impone exactamente el elemento.
- [x] **Opción B — Presentarlos como evidencia ligada al descriptor.** Redactar que la oferta no permite verificar determinado aspecto y explicar por qué esa falta de verificabilidad incide en el criterio publicado, sin afirmar que existía una obligación documental autónoma.
- [ ] **Opción C — Eliminar cualquier referencia a esos elementos.** Es excesiva cuando el elemento sí es una manifestación técnica razonable del criterio y no altera la preparación de las ofertas.

**Ejemplo recomendado:**

> La memoria no concreta cómo se verificará el rendimiento mediante valores, escenarios o comprobaciones reproducibles. Esta ausencia no se valora como incumplimiento de un formato documental autónomo, sino como falta de justificación convincente del rendimiento previsible exigido por el subcriterio.

### C-06. Doble penalización de una misma carencia

**Prioridad: media-alta.**

**Posible alegación de empresa_n.** La falta de detalle o los mismos supuestos errores se invocan en arquitectura, comprensión, viabilidad, metodología, rendimiento y satisfacción. Una misma evidencia puede tener efectos distintos, pero la repetición sin explicar esos efectos permite alegar doble castigo.

**Opciones:**

- [ ] **Opción A — Prohibir toda reutilización de evidencia.** Resulta artificial: un error arquitectónico puede afectar también a la viabilidad.
- [x] **Opción B — Asignar un efecto primario y justificar cualquier efecto secundario.** La matriz debe indicar por qué el mismo hecho mide dimensiones distintas y evitar que una carencia genérica rebaje automáticamente todos los subcriterios.
- [ ] **Opción C — No cambiar.** Solo si la motivación actual ya diferencia con precisión los efectos, circunstancia que no se aprecia de forma uniforme.

**Redacción recomendada:**

> La ausencia de un flujo de integración se valora principalmente en Arquitectura. Solo incide también en Viabilidad porque impide comprobar [operación concreta]. No se utiliza para reducir Metodología, Rendimiento o Satisfacción salvo en los requisitos específicamente identificados en la matriz.

### C-07. Confusión entre calidad de la oferta, incumplimiento, solvencia y umbral

**Prioridad: media-alta.**

**Posible alegación de empresa_n.** Expresiones como «mínimos de solvencia técnica», «no acredita el cumplimiento de requisitos», «no permite garantizar la ejecución», «exclusión automática y sin margen de discrecionalidad» o «evaluación plenamente objetiva» mezclan categorías diferentes. La solvencia pertenece a la aptitud del licitador; un requisito obligatorio puede justificar exclusión por incumplimiento; un desarrollo cualitativamente débil conduce a menor puntuación; y el umbral opera después de sumar esa puntuación. La valoración técnica mediante juicio de valor contiene discrecionalidad técnica, aunque esté sujeta a control.

**Opciones:**

- [ ] **Opción A — No cambiar.** No se recomienda por el riesgo de sobreactuación y confusión jurídica.
- [x] **Opción B — Separar las cuatro categorías y emplear lenguaje neutro.** Reservar «incumplimiento» para obligaciones obligatorias identificadas; usar «no alcanza el nivel/puntuación» para la valoración cualitativa; no llamar solvencia al umbral; reconocer que existe juicio técnico motivado.
- [ ] **Opción C — Suprimir toda conclusión de exclusión.** No es necesario si el umbral y el cálculo están correctamente establecidos.

**Redacción recomendada:**

> La oferta obtiene **[x] puntos sobre 30** en los criterios cualitativos y, por tanto, no alcanza el umbral de **15 puntos** previsto en el apartado [referencia]. La consecuencia deriva del resultado de la valoración motivada de esos criterios. Esta conclusión no constituye una apreciación sobre la solvencia del licitador ni añade un incumplimiento técnico distinto de los expresamente identificados en la documentación contractual.

## 5. Informe de Desarrollo

Resultado actual de empresa_n: **8,29/30**, por debajo del umbral de 15 puntos.

### D-01. Error aparente en «CalDAV frente a ICS» y necesidad de auditar los errores técnicos

**Prioridad: crítica.**

**Posible alegación de empresa_n.** El informe individual utilizado como soporte y la síntesis del informe conjunto presentan como error una «confusión entre CalDAV e ICS». Sin embargo, el requisito de calendario de EMPieza del anexo de la invitación pide conexión con **CalDAV**, y la propuesta de empresa_n para **TRA8 — Calendario escolar** también emplea CalDAV. Además, TRA2 se refiere a cambios de nombre de centro, no al calendario. Esta acusación aparece, por tanto, mal atribuida o materialmente incorrecta con la documentación local revisada.

No todos los ejemplos técnicos son erróneos: en **AV11**, la invitación exige generación asíncrona y la oferta dice expresamente que se ejecutará de forma síncrona. Precisamente por ello, no conviene agrupar todos los hallazgos bajo una afirmación global sin verificar cada código.

**Opciones:**

- [ ] **Opción A — Mantener todos los ejemplos y añadir páginas.** Solo sería viable si otra cláusula contractual demuestra la supuesta exigencia de ICS y su relación con el código correcto.
- [ ] **Opción B — Eliminar los ejemplos y conservar la afirmación genérica de errores.** Reduce la posibilidad de refutar un ejemplo, pero debilita la motivación y no corrige el posible efecto en la nota.
- [x] **Opción C — Auditar cada error, retirar el de CalDAV y recalcular si influyó.** Mantener únicamente errores acreditados, como la oposición síncrono/asíncrono de AV11, con código y páginas exactas. Si el supuesto error de CalDAV se utilizó para bajar Comprensión, Viabilidad, Satisfacción u otro subcriterio, revisar esos niveles y puntos.

**Redacción recomendada para AV11:**

> En AV11, el requisito [documento y página] dispone que la generación se realice de forma asíncrona, mientras que la propuesta [página] afirma que «se ejecutará de forma síncrona». Esta contradicción concreta reduce la adecuación de ese subproyecto y se imputa a [subcriterio], con el efecto indicado en la matriz. No se extiende automáticamente a otros proyectos de IA que sí plantean procesamiento asíncrono.

### D-02. Satisfacción de requisitos: 0,00/8,00 pese a 12 desarrollos suficientes

**Prioridad: alta.**

**Posible alegación de empresa_n.** El informe reconoce 12 de 85 proyectos con desarrollo suficiente y cobertura nominal completa, pero asigna nivel MUY BAJA y cero puntos. La versión base del repositorio contenía 2,50/8,00 y nivel MEDIA. Aunque esa versión puede ser un borrador sin eficacia jurídica, una bajada hasta cero exige una explicación particularmente sólida. El simple número de insuficientes no demuestra por sí solo que el descriptor global aplicable sea MUY BAJA.

**Opciones:**

- [ ] **Opción A — Mantener 0,00 sin más cambios.** Presenta un riesgo alto de falta de proporcionalidad y de motivación.
- [ ] **Opción B — Asignar automáticamente una nota proporcional a 12/85.** Introduciría una fórmula no publicada y tampoco ponderaría la importancia de los requisitos.
- [x] **Opción C — Revalorar cualitativamente y motivar el resultado.** Determinar qué peso funcional tienen los 12 proyectos suficientes y si permiten apartar el conjunto de MUY BAJA. Si se mantiene cero, explicar por qué esos contenidos no alteran el descriptor global; si no puede explicarse sin una fórmula nueva, asignar el nivel que resulte de los descriptores publicados.

**Redacción recomendada si, tras revisar, se mantiene cero:**

> Los 12 desarrollos identificados como suficientes se concentran en [bloques/códigos] y aportan [contenido]. No compensan las carencias que afectan a [requisitos esenciales concretos], por las razones y evidencias de la matriz. Aplicado el descriptor publicado —sin conversión automática del recuento—, el contenido global del subcriterio permanece en MUY BAJA.

### D-03. Coherencia de la valoración del calendario: MEDIA — 3,74/11,00

**Prioridad: media-alta.**

**Posible alegación de empresa_n.** Se asigna nivel MEDIA y 34 % del máximo, lo que presupone una planificación básica evaluable. Sin embargo, algunos pasajes afirman que la ausencia de leyenda impide la correcta interpretación o afecta «enormemente», y se penaliza también la falta de recursos, aunque los descriptores publicados se centran en detalle de tareas, fechas, duración, relaciones, hitos y objetivos. Debe distinguirse lo que sí se lee del cronograma de lo que no puede verificarse.

**Opciones:**

- [ ] **Opción A — Bajar a MUY BAJA porque el cronograma no puede interpretarse.** Solo si realmente no existe contenido temporal evaluable; contradice la actual clasificación MEDIA y exigiría revalorar.
- [x] **Opción B — Mantener MEDIA — 3,74/11,00 con una motivación coherente.** Describir el contenido básico legible, indicar qué relaciones o fechas no se verifican, explicar por qué se asigna 34 % y no usar la falta de recursos como obligación autónoma salvo cláusula expresa.
- [ ] **Opción C — No cambiar.** Mantiene la tensión entre «interpretable como nivel medio» y «no interpretable».

**Redacción recomendada:**

> El cronograma permite identificar [fases/periodos concretos], por lo que existe una planificación básica y el nivel es MEDIA. No obstante, la ausencia de una leyenda inequívoca y de relaciones verificables entre tareas impide reconstruir [aspectos concretos] y aleja la oferta del siguiente nivel. La nota de 3,74/11 se sitúa en [posición] de la banda por [fortaleza y carencia concretas].

## 6. Informe de Exteriores

Resultado actual de empresa_n: **7,66/30**, por debajo del umbral de 15 puntos.

### E-01. Premisas técnicas discutibles sobre LDAP Plano y Drupal

**Prioridad: crítica.**

**Posible alegación de empresa_n.** El informe sostiene que empresa_n interpreta LDAP Plano como un LDAP convencional cuando el sistema real sería PostgreSQL, y que propone Drupal sobre PostgreSQL cuando el entorno real sería MySQL. En la documentación local revisada, el anexo de la invitación denomina el elemento «BBDD LDAP plano» y exige usar su API; la oferta de empresa_n para IFP1 propone precisamente usar la API disponible. Tampoco se ha localizado en la documentación contractual revisada una cláusula que establezca, para el punto criticado, el motor MySQL de Drupal como premisa de valoración. Estas afirmaciones pueden apoyarse en conocimiento técnico interno, pero ese conocimiento debe quedar probado y vinculado al requisito.

**Opciones:**

- [ ] **Opción A — Mantener las dos afirmaciones sin nuevas referencias.** Presenta riesgo de error material manifiesto.
- [ ] **Opción B — Sustituirlas por una crítica genérica de falta de detalle.** Evita el dato discutible, pero no permite conservar una penalización basada en ese supuesto error.
- [x] **Opción C — Verificar las premisas en fuentes contractuales, retirar las no acreditadas y recalcular.** Si existe una fuente del expediente que prueba la arquitectura real y era cognoscible para los licitadores, citarla y confrontarla con la página exacta de la oferta. Si no, eliminar la acusación. Revisar Arquitectura, Comprensión, Viabilidad y Satisfacción si recibieron el impacto del mismo hecho.

**Redacción recomendada si solo se acredita falta de concreción:**

> Para IFP1 la oferta identifica el uso de la API de LDAP Plano, por lo que no se aprecia una incompatibilidad en ese extremo. La valoración desfavorable se limita, en su caso, a la falta de detalle sobre [autenticación, flujo, validación u otro aspecto exigido], conforme a la evidencia de la página [x].

### E-02. Satisfacción de requisitos: BAJA — 2,00/8,00

**Prioridad: alta.**

**Posible alegación de empresa_n.** El informe identifica 26 desarrollos insuficientes y dos sin solución entre 53 subproyectos, lo que implica que 25 se consideran suficientes, pero asigna exactamente el límite superior de BAJA. La versión base del repositorio contenía 4,20/8,00 y nivel ALTA. La modificación puede ser correcta, pero necesita una explicación por relevancia y profundidad de requisitos, no una mera cifra agregada.

**Opciones:**

- [ ] **Opción A — Mantener 2,00/8,00 con la motivación actual.** La referencia a los recuentos no explica por sí sola el salto de nivel ni el límite exacto.
- [ ] **Opción B — Calcular la nota en proporción a 25/53.** Sería una fórmula nueva no prevista.
- [x] **Opción C — Revalorar y motivar por bloques y requisitos relevantes.** Identificar qué 25 desarrollos son suficientes, qué importancia tienen y cuáles son las deficiencias determinantes. Mantener 2,00 solo si esa aplicación del descriptor puede explicarse sin automatismo numérico; documentar la razón de cualquier corrección del borrador previo.

**Redacción recomendada si se mantiene 2,00:**

> Aunque existe contenido suficiente en [códigos/bloques], las carencias acreditadas afectan a [funciones de especial relevancia] y limitan la satisfacción global en los términos del descriptor BAJA. Se asigna el límite superior de ese nivel porque [fortalezas concretas], sin alcanzar MEDIA debido a [carencias concretas y referencias]. El recuento del anexo no opera como fórmula de puntuación.

### E-03. Calendario: BAJA — 1,76/11,00 por cobertura temporal incompleta

**Prioridad: media.**

**Posible alegación de empresa_n.** La oferta incorpora cronograma, pero el informe sostiene que cubre aproximadamente un año cuando el servicio abarca dos, además de carecer de leyenda y detalle suficiente. Este es un fundamento potencialmente sólido si las fechas y la duración contractual están correctamente citadas. El riesgo proviene de añadir recursos o perfiles como exigencias autónomas y de no explicar por qué se elige 16 % dentro de BAJA.

**Opciones:**

- [x] **Opción A — Mantener nivel y puntuación, reforzando la motivación.** Citar las páginas del plazo contractual y del cronograma, describir el periodo omitido y vincular la nota a detalle, duración, relaciones e hitos de los descriptores publicados. Explicar el 16 %.
- [ ] **Opción B — Elevar al 25 % por existir Gantt.** La mera existencia formal del gráfico no obliga al límite superior si la cobertura temporal es incompleta.
- [ ] **Opción C — No cambiar ni añadir referencias.** Deja sin cerrar una prueba objetiva que puede reforzar mucho la defensa.

**Redacción recomendada:**

> El cronograma de la página [x] abarca de [fecha] a [fecha], mientras que el plazo contractual indicado en [documento y página] comprende [periodo]. La omisión de [periodo] impide verificar la secuencia completa del servicio. El contenido existente permite superar la parte inferior de BAJA, pero la cobertura parcial, junto con [relaciones/hitos no verificables], justifica el 16 % y no el límite superior del nivel.

## 7. Informe de Sistemas

Resultado actual de empresa_n: **6,80/30**, por debajo del umbral de 15 puntos.

### S-01. Versión aplicable de la metodología y error interno en `_valoracion_bis.md`

**Prioridad: crítica.**

**Posible alegación de empresa_n.** El archivo normal de valoración asigna 8 puntos a Satisfacción y presenta descriptores agrupados; el archivo `_bis.md` separa los descriptores por subcriterio y convierte los porcentajes «hasta» en intervalos cerrados, pero encabeza Satisfacción como **«2 puntos»**, pese a que el total del bloque exige 8. El informe conjunto aplica 8 puntos y los intervalos cerrados. Si no se identifica la versión contractual, puede alegarse una composición selectiva de dos documentos o una metodología ambigua.

**Opciones:**

- [ ] **Opción A — Citar el archivo `_bis.md` como metodología.** No se recomienda mientras contenga la contradicción 2/8 y no se pruebe que fue la versión publicada antes de las ofertas.
- [ ] **Opción B — Corregir ahora `_bis.md` y usarlo.** Una corrección posterior no puede convertir por sí sola un borrador en regla ex ante ni sanar una ambigüedad conocida después de las ofertas.
- [x] **Opción C — Determinar la versión contractual y aplicar solo esa.** Citar documento firmado, fecha, apartado y huella/versionado. Si el documento vigente es el normal con 8 puntos, explicar la aplicación de sus descriptores sin importar reglas nuevas del `_bis`. Si la versión vigente fuera `_bis`, solicitar análisis jurídico específico sobre la contradicción antes de cerrar la valoración.

**Redacción recomendada si rige la versión normal:**

> Se aplica el Documento de Invitación BAC06/2026, versión [identificación], publicado en fecha [x], que asigna 8 puntos a Satisfacción. El archivo de trabajo denominado `_bis` no forma parte de la documentación contractual utilizada y no fundamenta niveles, intervalos ni puntuaciones.

### S-02. Satisfacción de requisitos: MUY BAJA — 0,00/8,00

**Prioridad: alta.**

**Posible alegación de empresa_n.** El informe clasifica 65 de 89 subproyectos como insuficientes, 21 sin solución concreta y tres suficientes, y asigna cero puntos. La versión base del repositorio contenía 2,00/8,00. Aunque tres proyectos sean una parte reducida, el informe debe explicar por qué ese contenido no aparta el conjunto del descriptor MUY BAJA y por qué el cambio no deriva de una conversión matemática no publicada.

**Opciones:**

- [ ] **Opción A — Mantener cero apoyándose solo en 65+21.** Insuficiente: el recuento no es la regla publicada.
- [ ] **Opción B — Asignar un porcentaje por los tres proyectos.** Introduciría una fórmula nueva.
- [x] **Opción C — Revalorar el contenido material de los tres proyectos y de las carencias esenciales.** Si se mantiene cero, razonar su escasa relevancia o profundidad frente a los requisitos determinantes; si esa conclusión no resulta del descriptor publicado, corregir el nivel y recalcular el total.

### S-03. MAX e inteligencia artificial: no confundir ausencia formal con falta de propuesta propia

**Prioridad: alta.**

**Posible alegación de empresa_n.** El informe habla de «ausencia de contenido técnico evaluable» y llega a presentar MAX e IA como bloques sin contenido. La oferta contiene epígrafes relativos a esos ámbitos, aunque el análisis sostiene que reproducen requisitos y no añaden una solución propia. Empresa_n puede rebatir con facilidad una afirmación literal de ausencia mostrando esas páginas; la cuestión defendible es si el texto de la licitadora aporta desarrollo evaluable más allá de reproducir antecedentes.

**Opciones:**

- [ ] **Opción A — Mantener «ausencia» sin matices.** Presenta riesgo de error material por contradicción con la propia estructura de la oferta.
- [x] **Opción B — Reconocer el contenido formal y explicar por qué no es propuesta evaluable.** Separar texto del requisito, texto propio del licitador y análisis. Citar las páginas y describir qué elementos exigibles para el subcriterio no pueden verificarse.
- [ ] **Opción C — Considerar suficiente cualquier epígrafe existente.** La mera reproducción del pliego no obliga a una valoración positiva.

**Redacción recomendada:**

> La oferta incluye los epígrafes MAX e inteligencia artificial en las páginas [x-y]. No se afirma, por tanto, su ausencia formal. No obstante, el contenido identificado como propio del licitador [descripción precisa] no desarrolla [aspecto vinculado al descriptor], mientras que [fragmentos] reproducen los antecedentes o requisitos. Por ello, el contenido no permite asignar una valoración superior en [subcriterio], con el efecto concreto reflejado en la matriz.

### S-04. Escala auxiliar de «datos derivados» del CSV

**Prioridad: media-alta.**

**Posible alegación de empresa_n.** El informe incluye una escala auxiliar de datos derivados —0, 2, 5, 8 y 10— que no coincide con las puntuaciones de los subcriterios. Aunque se indique que corresponde a un CSV, su presencia dentro del apartado metodológico puede sugerir una segunda escala no publicada o dificultar la reconstrucción de la nota.

**Opciones:**

- [x] **Opción A — Retirar la escala del informe de valoración.** Mantenerla, si es necesaria, en un documento de trabajo separado, con declaración de que no intervino en la puntuación y con trazabilidad de su uso.
- [ ] **Opción B — Conservarla con una advertencia destacada.** Es posible si se acredita que solo codifica datos, pero añade complejidad sin mejorar la motivación del acto.
- [ ] **Opción C — No cambiar.** Mantiene una fuente evitable de confusión metodológica.

**Redacción sustitutiva:**

> Los anexos de trabajo se utilizan únicamente para localizar y ordenar evidencias. Ninguna codificación auxiliar del CSV se convierte en puntos ni sustituye los niveles, máximos y descriptores del Documento de Invitación.

### S-05. Calendario: BAJA — 2,75/11,00 y aspectos no expresos

**Prioridad: alta.**

**Posible alegación de empresa_n.** El informe utiliza ausencia de leyenda, duraciones, dependencias, recursos, hitos y secuencia. Los descriptores publicados se refieren expresamente al Gantt o similar, detalle, duración, relaciones, hitos y objetivos. Los recursos y los búferes pueden ser útiles, pero no deben operar como obligaciones autónomas si no se localizaron en la invitación. La versión base asignaba 5,00/11,00 y nivel MEDIA; la bajada a 2,75 requiere una motivación verificable.

**Opciones:**

- [ ] **Opción A — Mantener todos los motivos con igual peso.** Presenta riesgo de introducir exigencias no publicadas.
- [x] **Opción B — Revalorar con los rasgos expresos del descriptor y motivar el 25 %.** Basar BAJA en el carácter genérico, el detalle, la duración, las relaciones, los hitos y los objetivos. Mencionar recursos o búferes solo como contexto no decisivo. Explicar por qué se alcanza el límite superior de BAJA y no MEDIA.
- [ ] **Opción C — Volver automáticamente a 5,00/11,00.** La nota anterior no es fuente jurídica y no debe restaurarse sin análisis técnico.

**Redacción recomendada si se mantiene 2,75:**

> La matriz mensual permite identificar una secuencia temporal básica, por lo que la oferta alcanza el límite superior de BAJA. No llega a MEDIA porque [páginas] no permiten verificar la duración individual de [tareas], las relaciones entre [tareas] ni su conexión con [hitos/objetivos], aspectos expresamente contemplados por el descriptor. La eventual falta de asignación de recursos no se utiliza como criterio autónomo.

## 8. Redacciones transversales que conviene sustituir

| Formulación de riesgo | Sustitución recomendada |
| --- | --- |
| «La oferta carece de contenido» cuando hay epígrafe | «Existe el epígrafe, pero el texto propio identificado no permite verificar…» |
| «No cumple los requisitos» usado para una baja calidad | «El desarrollo no alcanza el nivel [x] del subcriterio por…» |
| «No acredita solvencia técnica» | «No alcanza el umbral de puntuación cualitativa» |
| «No permite garantizar la ejecución» | «No aporta evidencia suficiente para considerar acreditada [dimensión evaluada]» |
| «Exclusión automática y sin discrecionalidad» | «Una vez motivada la puntuación mediante juicio técnico, la aplicación aritmética del umbral determina…» |
| «Evaluación plenamente objetiva» | «Juicio técnico motivado, homogéneo y trazable, sujeto a las reglas publicadas» |
| «Errores tecnológicos» sin identificación | «En [código y página], la oferta afirma [hecho], que se opone a [requisito y página]» |
| «Faltan recursos/métricas/herramientas» | «La oferta no permite verificar [aspecto del descriptor]; [elemento] se cita como evidencia, no como requisito autónomo» |

## 9. Orden recomendado de actuación antes de cerrar los informes

1. **Congelar e identificar la documentación contractual vigente** de cada expediente: versión, fecha, firma/publicación y apartados de valoración.
2. **Reconstruir el historial de puntuaciones** y distinguir borradores internos de actos aprobados o comunicados. Documentar cada cambio.
3. **Auditar los posibles errores materiales** —con prioridad para CalDAV/ICS en Desarrollo y LDAP Plano/Drupal en Exteriores— frente a código, invitación y oferta.
4. **Revalorar cuando sea necesario**. No limitar la corrección a cambiar palabras si desaparece una premisa que influyó en la nota.
5. **Completar una matriz de motivación** por subcriterio y por licitador, con referencias exactas y explicación del porcentaje dentro del nivel.
6. **Comprobar simetría**: aplicar el mismo estándar probatorio y de detalle a todas las empresas, sin que la comparación sustituya la valoración individual.
7. **Reescribir conclusiones y propuesta de exclusión** con la terminología de C-07.
8. **Verificar el resultado aritmético y el umbral** después de cualquier cambio.
9. **Someter el expediente completo a revisión jurídica** si ya hubo aprobación, notificación o apertura de la siguiente fase.

## 10. Conclusión

La existencia del umbral de 15 puntos no parece, por sí sola, el principal foco de riesgo. Los puntos más sensibles son:

1. la posible apariencia de una **metodología de normalización introducida ex post**;
2. la falta de una explicación reproducible del **porcentaje exacto** dentro de cada nivel;
3. la conversión aparente de recuentos de subproyectos en una regla de puntuación;
4. los **errores o premisas técnicas discutibles** identificados en Desarrollo y Exteriores;
5. la ambigüedad de versiones de valoración en Sistemas; y
6. los cambios intensos de puntuación hasta llegar a cero en Satisfacción sin una motivación reforzada.

La mejor defensa no consiste en hacer más categóricas las conclusiones, sino en asegurar que cada nota provenga de la regla publicada, se apoye en hechos exactos, explique su efecto una sola vez y permita a empresa_n reconstruir el razonamiento. Donde esa cadena no pueda acreditarse, debe corregirse la valoración antes de corregir la redacción.
