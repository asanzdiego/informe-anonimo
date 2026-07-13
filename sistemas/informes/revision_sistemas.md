# REVISIÓN DE INCONGRUENCIAS — SISTEMAS

Fecha de revisión: 13 de julio de 2026.

## 1. Alcance y criterio de revisión

Se han cruzado exclusivamente estos cuatro archivos en su estado actual:

- `informe_conjunto_y_normalizado_sistemas.md`;
- `informe_individual_normalizado_sistemas_empresa_s.md`;
- `informe_individual_normalizado_sistemas_empresa_n.md`;
- `tareas_anexo_ii_sistemas.csv`.

La revisión comprende metadatos del expediente, licitadores, puntuaciones y sumas, niveles cualitativos, baremo, umbral y propuesta final, inventario y orden de tareas, correspondencia entre ID y denominación, análisis detallado, anexos individuales, descripciones y valores del CSV y trazabilidad de las afirmaciones de valor añadido.

Las opciones marcadas con `[x]` son las recomendadas. Este documento no modifica todavía ninguno de los cuatro archivos auditados.

## 2. Resultado general

La cobertura estructural es correcta: los 89 ID del CSV aparecen una vez y en el mismo orden tanto en el análisis detallado como en el anexo de cada informe individual. No hay ID duplicados, filas incompletas ni valores vacíos. Las puntuaciones numéricas actuales de los dos informes individuales coinciden con el informe conjunto, todas sus sumas son correctas y la aplicación del umbral de 15 puntos es coherente.

No obstante, se han localizado las siguientes incongruencias materiales:

1. El informe conjunto conserva dos tipos de marcador de plantilla —cuatro apariciones en total— para el contrato y el expediente, mientras los individuales identifican el contrato y el expediente como `BAC06_2026`.
2. El conjunto afirma que compara tres licitadores —incluida `empresa_u`—, pero solo analiza y puntúa a `empresa_s` y `empresa_n`; el CSV tampoco contiene columnas para `empresa_u`.
3. Ocho etiquetas cualitativas del informe conjunto no coinciden con las de los individuales. El conjunto emplea además `Media-Alta` y `Media-Baja`, niveles no definidos por la metodología.
4. La trazabilidad de empresa_n se califica como `BAJA` y recibe `0,40/1,00`, aunque el baremo fija para `BAJA` un máximo del 25 %.
5. El CSV aplica una escala numérica no documentada. En empresa_s, el mismo nivel `ALTA` se convierte en `7`, `8` o `9`, y `BAJA` se convierte en `3` o `4`.
6. El anexo de empresa_s clasifica los 89 subproyectos como `SUFICIENTE` y los 89 como `VA`, pese a que el cuerpo y el CSV describen 21 con nivel `BAJA` y carencias que en varios casos equivalen a ausencia de solución concreta.
7. En empresa_s hay numerosas afirmaciones de valor añadido no trazables o asignadas a una tarea distinta; varios casos son contradicciones literales entre la fortaleza declarada y las carencias del mismo apartado.
8. Parte del análisis y de las carencias de `MIG4` está colocada dentro de `MIG3`, mientras `MIG4` declara que no hay carencias adicionales.
9. Los dos informes individuales coinciden entre sí en los nombres, pero 47 de las 89 denominaciones no son idénticas a las del CSV.
10. En empresa_n, `UPD5` y `OTR1` muestran combinaciones de grado del anexo, nivel cualitativo y valor CSV cuya relación no está definida y que siguen sentidos opuestos al patrón dominante.

Además, se considerará incongruencia transversal cualquiera de estas situaciones:

- utilizar un nivel distinto de los cinco definidos por los propios informes: `EXCELENTE`, `ALTA`, `MEDIA`, `BAJA` y `MUY BAJA`;
- asignar un nivel que no corresponda a estos umbrales: `EXCELENTE`, del 76 % al 100 %; `ALTA`, del 51 % al 75 %; `MEDIA`, del 26 % al 50 %; `BAJA`, del 0 % al 25 %; y `MUY BAJA`, exactamente el 0 % de la puntuación de la sección correspondiente;
- convertir un nivel a un valor CSV distinto de `EXCELENTE=10`, `ALTA=8`, `MEDIA=5`, `BAJA=2` y `MUY BAJA=0`.

Cuando el 0 % pudiera encajar nominalmente tanto en `BAJA` como en `MUY BAJA`, prevalecerá la regla específica de `MUY BAJA`.

Las propuestas finales no cambian con las correcciones aritméticas o terminológicas recomendadas: empresa_s continúa por encima de 15 puntos y empresa_n permanece por debajo. Esto no elimina la necesidad de hacer coherentes la motivación, las categorías y los datos derivados.

## 3. Metadatos y licitadores

### 3.1. El conjunto conserva marcadores de plantilla

El informe conjunto muestra `[DENOMINACIÓN DEL CONTRATO O SERVICIO] ([NÚMERO DE EXPEDIENTE])` en las líneas 3 y 9. Los dos individuales usan de forma coincidente:

`DESARROLLO EVOLUTIVO Y CORRECTIVO DEL PORTAL EDUCATIVO, EL LDAP, EL CLOUD, MAX Y OTROS SISTEMAS DE EDUCAMADRID (BAC06_2026)`.

Opciones:

- [x] **Sustituir en el conjunto los dos marcadores por la denominación y el expediente que coinciden en ambos informes individuales.**
- [ ] Mantener los marcadores hasta contrastar el Documento de Invitación. No se recomienda porque el dato ya es unánime en los dos informes individuales.

### 3.2. Empresa_u figura como licitador, pero no se valora

La línea 9 del conjunto declara propuestas de `empresa_s`, `empresa_n` y `empresa_u`. Sin embargo, las secciones de análisis, las tablas comparativas, la propuesta final, los informes individuales y las columnas del CSV solo contemplan a las dos primeras. La frase de la línea 418 según la cual «únicamente» empresa_s supera el umbral tampoco puede sostenerse respecto de una tercera oferta no evaluada.

Opciones:

- [x] **Eliminar `empresa_u` de la introducción del conjunto**, salvo que exista realmente una tercera oferta que deba incorporarse con informe individual, dos campos CSV, puntuación y propuesta final.
- [ ] Añadir la valoración completa de empresa_u a todos los artefactos. Solo procede si esa oferta forma parte real del expediente.

## 4. Puntuaciones, niveles y baremo

### 4.1. Ocho niveles del conjunto no reproducen los individuales

Los puntos son idénticos; cambian únicamente estas etiquetas:

| Licitador | Subcriterio | Puntos | Informe individual | Informe conjunto |
| --- | --- | ---: | --- | --- |
| empresa_s | Viabilidad | 0,65/1,00 | ALTA | Media-Alta |
| empresa_s | Metodología | 0,65/1,00 | ALTA | Media-Alta |
| empresa_s | Calendario | 7,50/11,00 | ALTA | Media-Alta |
| empresa_s | Plan de calidad | 0,65/1,00 | ALTA | Media-Alta |
| empresa_s | Trazabilidad | 0,65/1,00 | ALTA | Media-Alta |
| empresa_n | Viabilidad | 0,40/1,00 | MEDIA | Media-Baja |
| empresa_n | Satisfacción de requisitos | 2,00/8,00 | BAJA | Muy baja |
| empresa_n | Trazabilidad | 0,40/1,00 | BAJA | Media-Baja |

Referencias principales: conjunto, líneas 302-320; empresa_n, tablas iniciadas en las líneas 2531 y 2632; empresa_s, tablas iniciadas en las líneas 2803 y 2892.

`Media-Alta` y `Media-Baja` no pertenecen a los cinco niveles que declaran los tres informes: `EXCELENTE`, `ALTA`, `MEDIA`, `BAJA` y `MUY BAJA`. Además, `Muy baja — 2,00/8,00` contradice la regla que asigna a `MUY BAJA` el 0 %.

Opciones:

- [x] **Tomar el informe conjunto como fuente de verdad de la valoración, conservar sus puntos y normalizar sus etiquetas mediante los cinco niveles y los umbrales del apartado 4.3.** Después, los informes individuales reproducirán las valoraciones normalizadas del conjunto: los cinco casos de empresa_s serán `ALTA`; viabilidad de empresa_n será `MEDIA`; satisfacción de empresa_n será `BAJA`; y trazabilidad de empresa_n será `MEDIA`.
- [ ] Introducir formalmente `Media-Alta` y `Media-Baja` en la metodología de los tres informes. Exigiría definir sus intervalos y revisar todas las valoraciones.
- [ ] Mantener las etiquetas actuales. Dejaría niveles distintos para los mismos puntos y categorías no definidas.

### 4.2. Trazabilidad de empresa_n: nivel bajo con una puntuación del 40 %

El individual motiva expresamente un «nivel bajo», lo etiqueta como `BAJA` y asigna `0,40/1,00` (líneas 2617-2629). Sin embargo, la metodología fija `BAJA` en hasta el 25 %. El conjunto intenta reflejar el 40 % mediante `Media-Baja`, pero esa categoría no existe.

Opciones:

- [ ] Conservar el nivel `BAJA`, respaldado por la motivación detallada del informe individual, y reducir la puntuación a `0,25/1,00`.
- [x] **Conservar la puntuación `0,40/1,00` del informe conjunto, cambiar el nivel normalizado a `MEDIA` y hacer que el informe individual reproduzca ambos datos y una motivación compatible con el 40 %.**
- [ ] Definir `MEDIA-BAJA` y usarla en ambos informes. No se recomienda porque ampliaría el baremo solo para justificar una nota ya incompatible con la escala declarada.

### 4.3. Las bandas porcentuales deben quedar cerradas y no solapadas

Los informes emplean «hasta» para todos los niveles, pero no definen límites inferiores. Esa redacción permite solapamientos y no explica cómo se elige un punto concreto dentro de cada nivel. Se aplicará siempre esta escala:

| Nivel | Porcentaje de la puntuación de la sección |
| --- | ---: |
| EXCELENTE | Del 76 % al 100 % |
| ALTA | Del 51 % al 75 % |
| MEDIA | Del 26 % al 50 % |
| BAJA | Del 0 % al 25 % |
| MUY BAJA | 0 % |

En el 0 % prevalece la categoría específica `MUY BAJA`. No se admitirán categorías intermedias distintas de estos cinco niveles.

Opciones:

- [x] **Aplicar los cinco niveles y los umbrales anteriores a todas las valoraciones, recalculando o renombrando cualquier nivel que quede fuera de su banda.**
- [ ] Eliminar los porcentajes y declarar que el nivel es descriptivo y la puntuación se motiva de forma independiente. Es viable, pero reduce la reproducibilidad.

## 5. Empresa_s: anexo, niveles por tarea y CSV

### 5.1. El anexo declara 89 desarrollos suficientes y 89 aportaciones de valor

El propio anexo define `SUFICIENTE` como existencia de una solución concreta y evaluable y `VA` como valor añadido verificable (líneas 2949-2953). Después clasifica los 89 proyectos como `SUFICIENTE`, los 89 como `VA` y ninguno como insuficiente o no incluido (líneas 3117-3130).

Eso no es compatible con el análisis detallado y el CSV en estos 21 subproyectos calificados como `BAJA`:

- `UPD4`, `UPD11`;
- `OTR5`;
- `COR9`, `COR10`;
- `MAX1` a `MAX14`;
- `POR2`;
- `CON3`.

En ellos el CSV usa valores `3` o `4` y describe, según el caso, una solución indirecta o genérica, ausencia de herramienta o procedimiento, cobertura insuficiente o ausencia de contenido específico. Los casos MAX son especialmente claros: el conjunto afirma que «no existe desarrollo técnico específico» (línea 216), el CSV dice que no se aporta contenido técnico específico en cada una de las 14 filas, el cuerpo asigna `BAJA`, pero el anexo marca las 14 como `SUFICIENTE | VA` (líneas 3036-3049).

Opciones:

- [x] **Revisar los 21 ID contra la oferta original y reconstruir una única matriz fuente con `grado`, `nivel`, `valor añadido`, `error`, `observación` y `val`. Si la resolución se limita a los cuatro archivos auditados, dar preferencia provisional al análisis detallado y al CSV frente al resumen del anexo, porque contienen la carencia concreta.** No debe convertirse automáticamente todo nivel `BAJA` en `NO INCLUIDA`: algunos casos tienen cobertura parcial y corresponderán a `INSUFICIENTE`.
- [ ] Tomar el anexo como fuente de verdad y reescribir cuerpo y CSV para sostener 89 soluciones suficientes y 89 mejoras verificables. No se recomienda porque exigiría añadir evidencias que no aparecen en los archivos revisados.
- [ ] Derivar el grado solo del nivel (`ALTA/MEDIA = SUFICIENTE`, `BAJA = INSUFICIENTE`). Es útil como control, pero no sustituye la revisión de evidencia ni distingue una respuesta insuficiente de una no incluida.

### 5.2. Afirmaciones de valor añadido no trazables o asignadas a otra tarea

La columna `VA` no solo presenta un problema cuantitativo. En numerosos apartados la frase de «Fortalezas y valor añadido» no está sustentada por el análisis o es negada literalmente por las carencias. Los grupos afectados son:

| Bloque | ID afectados | Ejemplos de incongruencia |
| --- | --- | --- |
| UPD | `UPD4`, `UPD6`, `UPD9` a `UPD15` | Kanban recibe «optimización de servicios web»; Abies+ recibe «reducción de incidencias post-update» pese a que no hay procedimientos de prueba; Empieza y CMDB reciben afirmaciones de rollback o preproducción no desarrolladas en sus análisis. |
| CLO | `CLO3` | Se declara «autoescalado y balanceo dinámico», pero las carencias dicen expresamente que no se desarrollan escalabilidad ni balanceo. |
| OTR | `OTR5` | La herramienta de flujos recibe «portal CAU mejorado», contenido que corresponde a `OTR6`; el cuerpo dice que `OTR5` no se desarrolla de forma específica. |
| COR | `COR1` a `COR6`, `COR9`, `COR10` | `COR1` declara gestión inteligente de colas mientras el cuerpo dice que no se desarrolla gestión de colas; `COR2` recibe antispam y `COR4` automatización de listas, aparentemente intercambiados; `COR9` y `COR10` no tienen diseño o soporte específico. |
| MAX | `MAX1` a `MAX14` | Se atribuyen 14 mejoras concretas, pero el análisis remite de forma genérica al bloque, el CSV no encuentra contenido específico y el conjunto declara que no existe desarrollo técnico específico. |
| AV | `AV1`, `AV2`, `AV3` | Se atribuyen optimización de picos, balanceo inteligente y carga predictiva, mientras el cuerpo declara falta de desarrollo específico, de componentes Moodle y de procedimientos de despliegue. |
| POR | `POR1`, `POR2` | Se atribuyen identidad escalable y alta disponibilidad, aunque faltan procedimientos de replicación y un plan de migración LDAP. |
| SEG | `SEG1` a `SEG11` | Varias mejoras pertenecen a otro subproyecto: correlación de eventos en certificados, gestión de certificados en vulnerabilidades, SIEM en claves RSA o gestión de vulnerabilidades en logs. En otros casos se afirman automatización o respuesta avanzada mientras se declara que faltan herramientas, metodología o roles. |
| CON | `CON1`, `CON3` | `CON1` declara Kubernetes avanzado y después dice que no se identifica Kubernetes; `CON3` declara despliegue DevOps sin desarrollar el sistema auxiliar. |
| MIG | `MIG1` a `MIG5` | Se declaran migración sin impacto, validación completa y control total mientras faltan fases, dependencias, pruebas, criterios de aceptación y soporte posmigración específico. |
| IA | `IA1` a `IA5` | Las mejoras no corresponden con precisión a cada requisito: integración LLM para evaluación de rendimiento, optimización de inferencia para prompts, observabilidad para guardarraíles, seguridad para integración y «LLMOps completo» para límites por usuario; además faltan métricas, herramientas o mecanismos concretos. |

No se concluye que esas mejoras no existan en la oferta original. Se concluye que no son verificables de manera coherente dentro de los cuatro archivos revisados, pese a que el informe exige evaluabilidad y prohíbe suplir con inferencias una referencia no desarrollada.

Opciones:

- [x] **Contrastar cada afirmación con la oferta original. Si existe evidencia, incorporarla al análisis de la tarea correcta y conservar la mejora; si no existe, retirar o rebajar la afirmación del cuerpo y del anexo y revisar el grado, el nivel y el CSV.**
- [ ] Copiar las afirmaciones del anexo al resto del cuerpo. No se recomienda porque convertiría una síntesis no acreditada en motivación.
- [ ] Borrar todas las mejoras afectadas sin volver a la oferta. Es prudente frente a la invención, pero podría eliminar evidencia real omitida durante la normalización.

## 6. Empresa_s: contenido de MIG4 colocado dentro de MIG3

En `MIG3` aparecen el requisito, el análisis y las carencias propios de `MIG4` (líneas 2465-2469 y 2481-2485). A continuación, el apartado real de `MIG4` indica que no tiene análisis diferenciado y que no se identifican carencias adicionales (líneas 2491-2507). El CSV, en cambio, separa correctamente ambas ideas:

- `MIG3`: faltan checklists y formatos documentales;
- `MIG4`: faltan plan de pruebas y criterios de aceptación.

Opciones:

- [x] **Mover de `MIG3` a `MIG4` los párrafos relativos a verificación, integridad, pruebas y criterios de aceptación, eliminar en `MIG4` las frases que afirman que no hay análisis o carencias diferenciadas y conservar en `MIG3` solo preparación y documentación.** Revisar después los dos niveles y, si se mantienen como `ALTA`, asignarles el valor CSV `8`.
- [ ] Mantener el cuerpo y cambiar los títulos/ID. No se recomienda porque rompería el inventario común y el CSV ya demuestra la separación correcta.

## 7. Escala de valores del CSV

Ninguno de los cuatro archivos define la semántica de `val_empresa_n` y `val_empresa_s` ni su relación con los cinco niveles de los informes.

En empresa_n la correspondencia es completamente determinista:

| Nivel del informe | Valor CSV | Número de tareas |
| --- | ---: | ---: |
| MUY BAJA | 1 | 38 |
| BAJA | 3 | 49 |
| MEDIA | 5 | 1 |
| ALTA | 8 | 1 |

En empresa_s se usan varias cifras para un mismo nivel:

| Nivel del informe | Valor CSV | Número de tareas |
| --- | ---: | ---: |
| BAJA | 3 | 18 |
| BAJA | 4 | 3 |
| MEDIA | 5 | 28 |
| ALTA | 7 | 24 |
| ALTA | 8 | 15 |
| ALTA | 9 | 1 |

Las 28 excepciones a la equivalencia que aplica actualmente empresa_n (`MUY BAJA=1`, `BAJA=3`, `MEDIA=5`, `ALTA=8`) son:

- `BAJA=4`: `UPD4`, `UPD11`, `CON3`;
- `ALTA=7`: `UPD3`, `UPD7`, `UPD12`, `UPD13`, `CLO1`, `CLO3`, `OTR1`, `OTR3`, `OTR7`, `COR5`, `COR6`, `AV1`, `AV4`, `SEG2`, `SEG5`, `MIG2`, `MIG3`, `MIG4`, `MIG5`, `IA1`, `IA2`, `IA3`, `IA4`, `IA5`;
- `ALTA=9`: `MON2`.

Esto parece conservar matices intermedios —por ejemplo, media-baja, media-alta o muy alta— que los informes normalizados ya no definen. Además, incluso la equivalencia determinista de empresa_n es incongruente con la escala obligatoria porque `MUY BAJA` debe valer `0` y `BAJA` debe valer `2`.

Opciones:

- [x] **Aplicar y documentar siempre la escala `MUY BAJA=0`, `BAJA=2`, `MEDIA=5`, `ALTA=8` y `EXCELENTE=10`.** Esto llevará a `0` las 38 filas `MUY BAJA` de empresa_n; a `2` todas las filas `BAJA` actualmente valoradas con `3` o `4`; a `8` las 24 filas `ALTA` valoradas con `7` y `MON2`, actualmente valorada con `9`, después de resolver las incongruencias de evidencia de los apartados 5 y 6.
- [ ] Recuperar en los informes una escala ampliada (`MEDIA-BAJA=4`, `MEDIA-ALTA=7`, `MUY ALTA=9`) y definirla formalmente. Exigiría revisar metodología, niveles por tarea y tablas comparativas.
- [ ] Mantener valores distintos como matices libres dentro de cada nivel. No es recomendable sin una regla reproducible que explique cada diferencia.

## 8. Empresa_n: relación ambigua entre grado, nivel y valor

El patrón general de empresa_n es coherente entre nivel cualitativo y CSV, pero hay dos combinaciones llamativas en el anexo:

| ID | Nivel detallado | Valor CSV | Grado del anexo | Observación del anexo |
| --- | --- | ---: | --- | --- |
| `UPD5` | BAJA | 3 | SUFICIENTE | mantenimiento convencional sin pipelines |
| `OTR1` | MEDIA | 5 | INSUFICIENTE | SSO genérico sin federación técnica |

El informe no define si `grado de desarrollo` y `nivel cualitativo` son dimensiones independientes ni cómo se relacionan. `UPD5` resulta especialmente difícil de conciliar con la definición de `SUFICIENTE`, porque el análisis y el CSV destacan la ausencia de repositorios, pipelines y seguridad específica. `OTR1` sigue el sentido contrario: nivel medio, pero desarrollo insuficiente.

Opciones:

- [x] **Mantener ambos campos separados, definir expresamente su relación y revalidar `UPD5` y `OTR1` contra la oferta.** Si `SUFICIENTE` exige una solución concreta y evaluable, `UPD5` debe justificarse mejor o pasar a `INSUFICIENTE`.
- [ ] Forzar una equivalencia automática entre nivel y grado. Es más simple, pero puede eliminar matices legítimos si las dos columnas miden aspectos distintos.

## 9. Denominaciones de tareas

Los dos informes individuales usan exactamente los mismos 89 títulos. El CSV usa una redacción distinta en 47 ID:

| ID | CSV | Informes individuales |
| --- | --- | --- |
| `BD1` | Mantenimiento y mejora de entornos de Bases de Datos MariaDB y Proxy SQL avanzado | Mantenimiento y mejora de entornos de Bases de Datos MariaDB y ProxySQL avanzado |
| `BD3` | Mantenimiento de las diferentes Bases de Datos de gestión de la configuración de EducaMadrid | Mantenimiento de las bases de datos de gestión de la configuración de EducaMadrid |
| `BD5` | Mantenimiento de disparadores y Foreign Data Wrappers en los entornos “Portal” y “LDAP Plano” | Mantenimiento de disparadores y Foreign Data Wrappers en los entornos Portal y LDAP Plano |
| `BD6` | Implementación y Mantenimiento de las Bases de Datos necesarias en entornos de Microservicios | Implementación y mantenimiento de bases de datos en entornos de microservicios |
| `MON3` | Mantener actualizado el sistema de monitorización y estadísticas de uso | Mantenimiento del sistema de monitorización y estadísticas de uso |
| `MON4` | Mantener actualizado el sistema de monitorización y estadísticas de servicios basados en IA | Monitorización y estadísticas de servicios basados en IA |
| `UPD2` | Mantenimiento y mejora del sistema secundario de Videoconferencias con opción de grabación | Mantenimiento y mejora del sistema secundario de videoconferencias con opción de grabación |
| `UPD3` | Mantenimiento y mejora de la herramienta Mattermost | Mantenimiento y mejora de Mattermost |
| `UPD5` | Mantenimiento y mejora de la solución GitLab | Mantenimiento y mejora de GitLab |
| `UPD6` | Mantenimiento y mejora de la solución LimeSurvey | Mantenimiento y mejora de LimeSurvey |
| `UPD9` | Mantenimiento y configuración de Wowza Streaming Engine. | Mantenimiento y configuración de Wowza Streaming Engine |
| `UPD11` | Actualización, Mantenimiento y gestión de contenidos de Abies+ | Actualización, mantenimiento y gestión de contenidos de Abies+ |
| `UPD13` | mantenimiento y mejora del sistema de gestión de la configuración | Mantenimiento y mejora del sistema de gestión de la configuración |
| `UPD14` | Mantenimiento, Actualización y mejora de la solución de contenedores | Mantenimiento, actualización y mejora de la solución de contenedores |
| `UPD15` | Mantenimiento de gestión y decomisionado de servidores | Mantenimiento, gestión y decomisionado de servidores |
| `OTR1` | Mantenimiento y mejora del sistema de autentificación centralizada Single Sign On (SSO) | Mantenimiento y mejora del sistema de autenticación centralizada Single Sign-On (SSO) |
| `OTR2` | Mantenimiento, configuración y gestión 2FA en el servicio de Single Sign On (SSO) | Mantenimiento, configuración y gestión de 2FA en el servicio de Single Sign-On |
| `OTR4` | Mantenimiento y mejora de un sistema de gestión y análisis de datos mediante el stack de Elastic | Mantenimiento y mejora del sistema de gestión y análisis de datos mediante Elastic |
| `OTR7` | Mantenimiento y evolución de servicios de Inteligencia Artificial para la plataforma EducaMadrid | Mantenimiento y evolución de servicios de Inteligencia Artificial |
| `COR4` | Mantenimiento y mejora de las herramientas relacionadas con el control del spam | Mantenimiento y mejora de las herramientas de control del spam |
| `COR6` | Mantenimiento y mejora continua de la seguridad del sistema de correo | Mantenimiento y mejora de la seguridad del sistema de correo |
| `COR7` | Actualización y mejora continua de la infraestructura en la que se basa el sistema de correo | Actualización y mejora continua de la infraestructura de correo |
| `COR9` | Implementación y mejora de un módulo receptor de inyección directa para la infraestructura de transporte de correo | Implementación de un módulo receptor de inyección directa de correo |
| `MAX4` | Lanzamiento de distribuciones de MAX “Full Equip” anualmente | Lanzamiento anual de distribuciones de MAX «Full Equip» |
| `MAX5` | Lanzamiento de distribuciones de “MAX lite” y/o “max gestión” anualmente | Lanzamiento anual de distribuciones «MAX lite» y/o «MAX gestión» |
| `MAX6` | Integración de aplicaciones externas a los repositorios oficiales | Integración de aplicaciones externas en los repositorios oficiales |
| `MAX7` | Mantenimiento y mejora del servidor de gestión accesos remotos | Mantenimiento y mejora del servidor de gestión de accesos remotos |
| `MAX10` | Soporte presencial en eventos especiales (MAX Install Party) | Soporte presencial en eventos especiales MAX Install Party |
| `MAX12` | Instalación y configuración de dispositivos solicitadas por los centros educativos | Instalación y configuración de dispositivos solicitados por los centros educativos |
| `AV1` | Actualización y comprobación periódicas de servidores físicos y virtuales de BBDD de los entornos de aulas virtuales | Actualización y comprobación periódicas de servidores de bases de datos de aulas virtuales |
| `AV2` | Mantenimiento de los servidores virtuales FrontEnd de los entornos de aulas virtuales | Mantenimiento de los servidores FrontEnd de aulas virtuales |
| `AV3` | Despliegue periódico de nuevos grupos de aulas virtuales y ampliación de los actuales | Despliegue de nuevos grupos de aulas virtuales |
| `AV4` | Redistribución periódica de los NFS de datos de las aulas virtuales | Redistribución periódica de NFS de aulas virtuales |
| `SEG2` | Mantenimiento y mejora de un LDAP Máster independiente para usuarios privilegiados | LDAP Máster independiente para usuarios privilegiados |
| `SEG3` | Gestión, mantenimiento e implantación anual de los certificados de EducaMadrid | Gestión, mantenimiento e implantación de certificados |
| `SEG4` | Gestión y mantenimiento periódico de dominios DNS | Gestión y mantenimiento de dominios DNS |
| `SEG6` | Gestión, mantenimiento y ajuste de la herramienta para la detección de intrusiones, monitorización de la integridad, análisis de logs y respuesta ante incidentes. | Detección de intrusiones y análisis de logs |
| `SEG7` | Realización de auditorías internas de aplicaciones | Auditorías internas de aplicaciones |
| `SEG8` | Realización de auditorías internas continuas de los sistemas | Auditorías internas continuas de sistemas |
| `SEG11` | Asistencia y soporte presencial en los diferentes eventos de Ciberseguridad de EducaMadrid | Asistencia en eventos de ciberseguridad |
| `CON2` | Mantenimiento y mejora de los scripts y sistemas de automatización de tareas | Mantenimiento y mejora de scripts y automatización de tareas |
| `CON3` | Mantenimiento y mejora del sistema auxiliar de automatización | Mantenimiento del sistema auxiliar de automatización |
| `MIG4` | verificación de la migración | Verificación de la migración |
| `IA1` | EVALUAR el rendimiento de los modelos seleccionados | Evaluación del rendimiento de los modelos seleccionados |
| `IA2` | Ingeniería de Prompts adaptados para cada servicio | Ingeniería de prompts adaptados para cada servicio |
| `IA4` | Evaluar Posibilidades de Integración en Distintos Aplicativos | Evaluación de posibilidades de integración en distintos aplicativos |
| `IA5` | Evaluación de Capacidades de Respuesta y Límites por Usuario | Evaluación de capacidades de respuesta y límites por usuario |

La mayoría son abreviaciones, diferencias de mayúsculas o variantes editoriales. Algunas sí cambian alcance o contienen errores claros: `UPD15` usa «Mantenimiento de gestión» frente a «Mantenimiento, gestión»; `MAX12` usa «dispositivos solicitadas»; `SEG6`, `COR9`, `AV1`, `AV2` y `AV3` son sensiblemente más detalladas en el CSV.

Los nombres de los 13 grupos también difieren formalmente porque el CSV incorpora el código entre paréntesis; en `BD` añade además «Mantenimiento y mejora de entornos de». Los prefijos y la agrupación de las 89 filas sí coinciden.

Opciones:

- [x] **Usar literalmente la denominación del Anexo II oficial como catálogo canónico en los tres artefactos.** Si no se consulta todavía el Anexo II, conservar provisionalmente los ID —que sí son unánimes— y no elegir en bloque entre CSV e informes: el CSV parece más completo en varios casos, pero contiene errores editoriales evidentes.
- [ ] Mantener títulos completos en el CSV y abreviados en los informes, añadiendo una nota expresa de equivalencia. Es válido, pero dificulta los cruces automáticos y la trazabilidad literal.

## 10. Comprobaciones que no han detectado incongruencias

- El CSV contiene 89 filas, 7 columnas, 89 ID únicos y ningún campo vacío.
- Los dos análisis detallados y los dos anexos contienen los mismos 89 ID, una vez cada uno y en el mismo orden que el CSV.
- Los dos informes individuales tienen la misma secuencia de 200 encabezados.
- Los recuentos del anexo de empresa_n cuadran: 66 insuficientes, 21 no incluidos y 2 suficientes; 67 `PM`, 21 sin mejora y 1 `VA`; 1 error técnico.
- Los recuentos declarados por bloques de empresa_n coinciden con su anexo.
- Los valores CSV de empresa_n siguen sin excepciones la equivalencia observada `1/3/5/8`, que deberá sustituirse por la escala obligatoria `0/2/5/8/10`.
- En empresa_s, las 28 tareas `MEDIA` reciben siempre `5`; la incongruencia de escala se concentra en `BAJA` y `ALTA`.
- Las puntuaciones numéricas actuales de los 11 subcriterios de cada licitador son idénticas entre individual y conjunto.
- Las sumas actuales son correctas: empresa_s, `11,05 + 9,80 = 20,85`; empresa_n, `5,05 + 6,40 = 11,45`.
- La aplicación actual del umbral es coherente: empresa_s supera 15 puntos y empresa_n no los supera.
- No se han encontrado marcadores de plantilla en los informes individuales; los dos tipos detectados (`DENOMINACIÓN` y `NÚMERO DE EXPEDIENTE`), con dos apariciones cada uno, están en el conjunto.

## 11. Orden recomendado para una futura corrección

1. Confirmar contrato, expediente y número real de licitadores.
2. Aplicar los cinco niveles y sus umbrales, tomando el informe conjunto como fuente de verdad, y resolver la trazabilidad de empresa_n antes de tocar totales.
3. Crear la matriz fuente de 89 tareas y separar grado, nivel, valor añadido, error, observación y valor numérico.
4. Revalidar los 21 casos `BAJA | SUFICIENTE | VA` de empresa_s y las afirmaciones de valor añadido no trazables.
5. Separar correctamente `MIG3` y `MIG4`.
6. Aplicar a `val_empresa_*` la escala `EXCELENTE=10`, `ALTA=8`, `MEDIA=5`, `BAJA=2` y `MUY BAJA=0`.
7. Copiar las denominaciones oficiales del Anexo II a los tres artefactos.
8. Regenerar anexos y CSV desde la matriz acordada.
9. Regenerar los informes individuales desde el informe conjunto, recalcular sumas y volver a comprobar el umbral y la propuesta final.
