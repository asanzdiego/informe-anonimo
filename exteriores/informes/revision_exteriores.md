# REVISIÓN DE INCONGRUENCIAS — EXTERIORES

Fecha de revisión: 13 de julio de 2026.

## 1. Alcance y criterio de revisión

Se han cruzado exclusivamente estos cuatro archivos:

- `informe_conjunto_y_normalizado_exteriores.md`;
- `informe_individual_normalizado_exteriores_empresa_s.md`;
- `informe_individual_normalizado_exteriores_empresa_n.md`;
- `tareas_anexo_ii_exteriores.csv`.

La revisión comprende puntuaciones y sumas, niveles cualitativos, umbral y propuesta final, inventario de tareas, correspondencia entre ID y contenido, descripciones y valores del CSV, anexos de los informes y terminología común.

Las opciones marcadas con `[x]` son las recomendadas. Este documento no modifica todavía ninguno de los cuatro archivos auditados.

## 2. Resultado general

La cobertura estructural es correcta: los 53 ID del CSV aparecen una vez en el análisis detallado y una vez en el anexo de cada informe individual, sin duplicados ni códigos ausentes.

No obstante, se han encontrado incongruencias materiales que impiden considerar coherentes los cuatro archivos:

1. El informe conjunto cambia diez valoraciones parciales de empresa_n respecto a su informe individual, muestra `2,80` puntos de planificación en lugar de `2,65` y conserva un total de `9,90` que no suma con el `2,80` mostrado.
2. El informe conjunto cambia cuatro niveles cualitativos de empresa_s, aunque mantiene sus puntos.
3. El conjunto declara tres licitadores —incluida empresa_u—, pero solo valora a empresa_s y empresa_n y el CSV solo contiene columnas para esas dos empresas.
4. En empresa_n, cuatro contenidos están asignados a tareas `ESIS` cuyo título no corresponde a lo analizado; además, cinco filas relacionadas permanecen vacías en el CSV pese a existir secciones y valoraciones en el informe actual.
5. El informe de empresa_n afirma que `EDSA2` no tiene respuesta, pero su análisis detallado sí contiene respuesta, el anexo la clasifica como suficiente y el CSV la describe y puntúa.
6. Los 45 subproyectos de empresa_s clasificados como `ALTA` se convierten en el CSV de dos formas distintas: 28 reciben `7` y 17 reciben `8`.
7. En varios subproyectos, el anexo y el CSV atribuyen mejoras o tecnologías que no son trazables en el análisis detallado y, en algunos casos, contradicen carencias expresas de ese análisis.

Además, se considerará incongruencia transversal cualquiera de estas situaciones:

- utilizar un nivel distinto de los cinco definidos por los propios informes: `EXCELENTE`, `ALTA`, `MEDIA`, `BAJA` y `MUY BAJA`;
- asignar un nivel que no corresponda a estos umbrales: `EXCELENTE`, del 76 % al 100 %; `ALTA`, del 51 % al 75 %; `MEDIA`, del 26 % al 50 %; `BAJA`, del 0 % al 25 %; y `MUY BAJA`, exactamente el 0 % de la puntuación de la sección correspondiente;
- convertir un nivel a un valor CSV distinto de `EXCELENTE=10`, `ALTA=8`, `MEDIA=5`, `BAJA=2` y `MUY BAJA=0`.

Cuando el 0 % pudiera encajar nominalmente tanto en `BAJA` como en `MUY BAJA`, prevalecerá la regla específica de `MUY BAJA`.

Las propuestas finales de continuación de empresa_s y exclusión de empresa_n no cambian con ninguna de las dos cifras globales actualmente visibles para empresa_n (`9,90` o `10,05`), porque ambas quedan por debajo del umbral de 15 puntos. Esto no elimina la obligación de corregir las puntuaciones y su motivación.

## 3. Incongruencias críticas de puntuación

### 3.1. Empresa_n: el conjunto no reproduce el informe individual

Fuentes principales: tabla individual de solución técnica, líneas 2265-2273; tabla individual de planificación, líneas 2373-2380; tablas conjuntas, líneas 250-269.

#### Solución técnica

| Subcriterio                | Informe individual |  Informe conjunto | Incongruencia                                                          |
| -------------------------- | -----------------: | ----------------: | ---------------------------------------------------------------------- |
| Comprensión de requisitos  |        ALTA — 1,30 |      Media — 1,00 | Cambian nivel y puntos.                                                |
| Viabilidad                 |       MEDIA — 0,55 | Media-Baja — 0,40 | Cambian nivel y puntos; `Media-Baja` no existe en el baremo declarado. |
| Metodología                |        BAJA — 0,30 |      Media — 0,50 | Cambian nivel y puntos.                                                |
| Rendimiento                |        BAJA — 0,20 |       Baja — 0,25 | Cambian los puntos.                                                    |
| Satisfacción de requisitos |       MEDIA — 4,00 |       Baja — 4,20 | Cambian nivel y puntos.                                                |
| **Total**                  |           **7,25** |          **7,25** | El mismo total resulta de repartos incompatibles.                      |

Arquitectura es el único subcriterio técnico coincidente: `MEDIA — 0,90`.

#### Planificación

| Subcriterio   | Informe individual |  Informe conjunto | Incongruencia                              |
| ------------- | -----------------: | ----------------: | ------------------------------------------ |
| Calendario    |        BAJA — 1,10 |       Baja — 1,80 | Cambian los puntos.                        |
| Riesgos       |       MEDIA — 0,45 |      Media — 0,25 | Cambian los puntos.                        |
| Contingencias |       MEDIA — 0,45 |      Media — 0,25 | Cambian los puntos.                        |
| Calidad       |       MEDIA — 0,35 |      Media — 0,25 | Cambian los puntos.                        |
| Trazabilidad  |        BAJA — 0,30 | Media-Baja — 0,25 | Cambian nivel y puntos; nivel no definido. |
| **Total**     |           **2,65** |          **2,80** | Los bloques no coinciden.                  |

Además, el resultado global conjunto muestra `7,25 + 2,80 = 9,90` (líneas 275-278 y 318-321), pero la suma correcta de esas dos cifras es `10,05`. El `9,90` sí coincide con `7,25 + 2,65`, que es el desglose del informe individual.

Opciones:

- [ ] Tomar el informe individual como fuente de verdad y trasladar al conjunto todos sus niveles y puntos: solución `7,25`, planificación `2,65`, total `9,90`.
- [x] **Tomar el informe conjunto como fuente de verdad, trasladar su reparto a la valoración individual y corregir el total global de empresa_n a `10,05` (`7,25 + 2,80`).** Los niveles deberán normalizarse con los cinco niveles y los umbrales del apartado 3.3.
- [ ] Mantener `9,90` pero conservar los parciales conjuntos actuales. No es admisible porque la suma seguiría siendo incorrecta y se mantendrían dos motivaciones distintas.

### 3.2. Empresa_s: los puntos coinciden, pero cuatro niveles cambian

Fuentes principales: tablas individuales, líneas 2049-2057 y 2165-2172; tablas conjuntas, líneas 250-269.

| Subcriterio   | Informe individual | Informe conjunto | Puntos |
| ------------- | ------------------ | ---------------- | -----: |
| Metodología   | ALTA               | Media-Alta       |   0,60 |
| Riesgos       | ALTA               | Media-Alta       |   0,60 |
| Contingencias | ALTA               | Media-Alta       |   0,60 |
| Calidad       | ALTA               | Media-Alta       |   0,65 |

`Media-Alta` no forma parte de los cinco niveles definidos por los propios informes (`EXCELENTE`, `ALTA`, `MEDIA`, `BAJA` y `MUY BAJA`).

Opciones:

- [x] **Tomar el informe conjunto como fuente de verdad, conservar sus puntos y normalizar `Media-Alta` como `ALTA` por corresponder al intervalo del 51 % al 75 %.** Después se reproducirán en el informe individual los niveles normalizados del conjunto.
- [ ] Tomar el informe individual como fuente de verdad y sustituir directamente `Media-Alta` por `ALTA` en el conjunto. Aunque produce la misma etiqueta en estos cuatro casos, invierte el origen documental acordado.

### 3.3. Los niveles y sus porcentajes no forman una escala aplicable sin contradicciones

Los tres informes declaran que `ALTA` llega hasta el 75 %, `MEDIA` hasta el 50 %, `BAJA` hasta el 25 % y `MUY BAJA` equivale al 0 %. Sin embargo:

- empresa_s recibe `ALTA — 1,75/2`, es decir, 87,5 %, en comprensión;
- empresa_n recibe `MEDIA — 0,55/1`, es decir, 55 %, en viabilidad;
- empresa_n recibe `BAJA — 0,30/1`, es decir, 30 %, en metodología;
- empresa_n recibe `BAJA — 0,30/1`, es decir, 30 %, en trazabilidad;
- el conjunto asigna `Baja — 4,20/8`, es decir, 52,5 %, a satisfacción de requisitos de empresa_n;
- el conjunto usa además `Media-Alta` y `Media-Baja`, niveles no definidos.

La palabra “hasta” también hace que los intervalos se solapen si no se establece un límite inferior. Se aplicará siempre esta escala cerrada:

| Nivel | Porcentaje de la puntuación de la sección |
| --- | ---: |
| EXCELENTE | Del 76 % al 100 % |
| ALTA | Del 51 % al 75 % |
| MEDIA | Del 26 % al 50 % |
| BAJA | Del 0 % al 25 % |
| MUY BAJA | 0 % |

En el 0 % prevalece la categoría específica `MUY BAJA`. No se admitirán categorías intermedias distintas de estos cinco niveles.

Opciones:

- [x] **Aplicar los cinco niveles y los umbrales anteriores a todas las valoraciones, recalculando o renombrando cualquier nivel que quede fuera de su banda y manteniendo la igualdad de criterio entre licitadores.**
- [ ] Mantener las puntuaciones discrecionales y eliminar de la metodología los topes porcentuales, dejando claro que el nivel es solo descriptivo.
- [ ] Mantener escala, niveles y puntos tal como están. Dejaría contradicciones objetivas en la metodología.

## 4. Licitadores y alcance

### 4.1. Empresa_u aparece como licitador, pero no se valora

El objeto del informe conjunto afirma que se comparan las propuestas de `empresa_s`, `empresa_n` y `empresa_u` (línea 9). El resto del documento, los dos informes individuales y las columnas del CSV solo contemplan empresa_s y empresa_n.

Opciones:

- [x] **Eliminar `empresa_u` de la introducción del conjunto**, salvo que exista realmente una tercera oferta que deba incorporarse con informe individual, columnas CSV, análisis, puntuación y propuesta final.
- [ ] Añadir la valoración completa de empresa_u en los cuatro artefactos. Solo procede si esa tercera oferta forma parte real del expediente.

## 5. Incongruencias por tarea e ID

### 5.1. Empresa_n: contenido asignado a tareas ESIS equivocadas

Los títulos actuales de los cinco apartados coinciden con el CSV, pero el contenido analizado no siempre corresponde a esos títulos.

| ID     | Tarea indicada por título y CSV | Contenido que realmente analiza empresa_n                    | Nivel del informe | CSV empresa_n          |
| ------ | ------------------------------- | ------------------------------------------------------------ | ----------------- | ---------------------- |
| ESIS25 | Monitorización avanzada         | Registro, análisis, resolución y seguimiento de incidencias  | BAJA              | descripción vacía; `-` |
| ESIS26 | Ciberseguridad básica           | Análisis de causa raíz y gestión de problemas recurrentes    | BAJA              | descripción vacía; `-` |
| ESIS27 | Ciberseguridad avanzada         | Detección y correlación de eventos mediante SIEM Open Source | ALTA              | descripción vacía; `-` |
| ESIS30 | Segmentación de red             | Zero Trust, control de acceso y MFA                          | ALTA              | descripción vacía; `-` |
| ESIS31 | Optimización de virtualización  | Soporte operativo y resolución de incidencias                | BAJA              | descripción vacía; `-` |

Referencias: informe de empresa_n, líneas 1663-1877; anexo, líneas 2509-2515; CSV, líneas 42-48.

ESIS27 es compatible en términos generales con ciberseguridad avanzada, aunque el CSV siga vacío. En ESIS25, ESIS26, ESIS30 y ESIS31 la discrepancia semántica es clara.

Opciones:

- [x] **Usar los ID y nombres del Anexo II oficial como inventario canónico y volver a la oferta original de empresa_n para decidir qué evidencia corresponde realmente a cada una de estas cinco tareas.** Después deben regenerarse de forma conjunta el análisis, la clasificación del anexo, la descripción y el valor CSV. Si no existe evidencia para una tarea canónica, debe figurar expresamente como no incluida; no debe reutilizarse contenido de otra tarea.
- [ ] Renombrar las tareas del CSV y de empresa_s para adaptarlas al contenido actual de empresa_n. No se recomienda porque rompería el inventario común y alteraría tareas que sí son coherentes en empresa_s.
- [ ] Rellenar las cinco celdas vacías usando sin más los niveles actuales de empresa_n. No se recomienda hasta corregir la asignación semántica.

### 5.2. Empresa_n: contradicción directa sobre EDSA2

El apartado de satisfacción afirma que no existe respuesta identificable para `ESIS11`, `ESIS14` y `EDSA2` (línea 2253). Sin embargo:

- `EDSA2` dispone de análisis detallado y se valora como `BAJA` (líneas 2039-2072);
- el anexo la clasifica como `SUFICIENTE` con mejora `PM` (línea 2530);
- el CSV incluye una descripción y el valor `3` (línea 53);
- el resumen del anexo solo cuenta dos tareas no incluidas, que son `ESIS11` y `ESIS14`.

Opciones:

- [x] **Eliminar `EDSA2` de la lista de tareas sin respuesta y mantener como no incluidas únicamente `ESIS11` y `ESIS14`.** Revisar después si la clasificación `SUFICIENTE` del anexo está suficientemente motivada frente al nivel `BAJA`, aunque ambas categorías describen dimensiones distintas.
- [ ] Reclasificar EDSA2 como no incluida y borrar su descripción/valor del CSV. Contradice el contenido evaluable ya escrito y requeriría justificar por qué ese contenido no procede de la oferta.

### 5.3. El CSV no aplica una conversión numérica única

En el informe de empresa_s hay 45 tareas con nivel `ALTA` y 8 con nivel `MEDIA`. En el CSV:

- las 8 tareas `MEDIA` reciben `5`;
- 17 tareas `ALTA` reciben `8`;
- otras 28 tareas igualmente `ALTA` reciben `7`.

Las 28 tareas `ALTA` valoradas con `7` son:

`ELIF1`, `ELIF3`, `ELIF4`, `IFP1`, `EMOM1`, `EMOM4`, `EIPE2`, `ESIS2`, `ESIS4`, `ESIS7`, `ESIS8`, `ESIS9`, `ESIS11`, `ESIS13`, `ESIS17`, `ESIS18`, `ESIS21`, `ESIS23`, `ESIS25`, `ESIS26`, `ESIS27`, `ESIS28`, `ESIS29`, `ESIS31`, `ESEG1`, `ESEG3`, `EDSA1` y `EDSA2`.

En empresa_n, todos los valores no vacíos siguen de hecho la equivalencia actual `MUY BAJA=1`, `BAJA=3`, `MEDIA=5` y `ALTA=8`; las únicas excepciones son las cinco filas vacías descritas en el apartado 5.1. Esa equivalencia también es incongruente con la escala obligatoria porque `MUY BAJA` debe valer `0` y `BAJA` debe valer `2`.

Opciones:

- [x] **Documentar y aplicar siempre la conversión `MUY BAJA=0`, `BAJA=2`, `MEDIA=5`, `ALTA=8` y `EXCELENTE=10`; convertir a `8` las 28 filas `ALTA` de empresa_s y completar empresa_n solo después de corregir ESIS25/26/27/30/31.** Todos los `1` asociados a `MUY BAJA` y los `3` asociados a `BAJA` deberán convertirse, respectivamente, en `0` y `2`.
- [ ] Recuperar en los informes un nivel intermedio distinto —por ejemplo, `MEDIA-ALTA=7`— para justificar los `7`. Exige incorporar ese nivel al baremo, definir su intervalo y revisar ambos licitadores.
- [ ] Mantener `7` y `8` como matices libres dentro de `ALTA`. Exigiría documentar una regla reproducible; en su estado actual no existe trazabilidad para distinguirlos.

### 5.4. El anexo y el CSV contienen afirmaciones no trazables en el análisis detallado

Las descripciones del CSV reproducen normalmente las observaciones del anexo. En los siguientes casos, la mejora o tecnología concreta no aparece en el análisis detallado, pertenece a otro ámbito o entra en tensión con una carencia expresamente indicada en ese análisis.

#### Empresa_n

| ID    | Afirmación del anexo/CSV                | Problema de trazabilidad en el análisis detallado                                                          |
| ----- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| ELIF1 | Virtual hosts y despliegues controlados | El cuerpo solo acredita cobertura funcional general y falta de procedimientos; no menciona esos elementos. |
| ELIF3 | Arquitectura frontend desacoplada       | El cuerpo menciona tecnologías frontend, accesibilidad y responsive, pero no una arquitectura desacoplada. |
| EMOM1 | CI/CD y auditoría automatizada          | El cuerpo describe actualización y validación genéricas; no identifica CI/CD ni auditoría automatizada.    |

Referencias: cuerpo, líneas 311, 369 y 487; anexo, líneas 2444, 2446 y 2459; CSV, líneas 2, 4 y 7.

#### Empresa_s

| ID     | Afirmación del anexo/CSV                              | Problema de trazabilidad en el análisis detallado                                                                    |
| ------ | ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| ESIS4  | Modelo centralizado y gobernado de integración segura | El cuerpo trata consultoría de ciberseguridad, hardening y controles; no ese modelo de integración.                  |
| ESIS9  | Validación automatizada y gobernada                   | El cuerpo describe segregación, control y rollback, pero declara que no se concretan herramientas de automatización. |
| ESIS11 | Administración centralizada y automatizada de BBDD    | El cuerpo no identifica el gestor corporativo ni automatización.                                                     |
| ESIS13 | Aprovisionamiento automatizado y gobernado            | El cuerpo señala ausencia de procedimientos, circuitos y herramientas de provisión.                                  |
| ESIS16 | IaC y auditoría automática de configuraciones         | El cuerpo cita TLS, WAF o SIEM, pero no IaC ni auditoría automática.                                                 |
| ESIS17 | Evolución de LDAP a Identity Governance               | El cuerpo se limita a replicación, sincronización e integración LDAP.                                                |
| ESIS23 | Repositorios WORM y replicación entre CPD             | El cuerpo afirma que no se detallan tecnologías ni estrategias de replicación.                                       |
| ESIS25 | Inteligencia operacional e integración con SOC        | El cuerpo afirma que no se identifican APM, observabilidad distribuida ni correlación avanzada.                      |
| ESIS26 | MFA, hardening STIC y reporting ENS                   | El cuerpo solo contiene medidas básicas genéricas y destaca la falta de concreción.                                  |
| ESIS27 | Defensa activa y observabilidad inteligente           | El cuerpo indica que no se detallan SIEM, SOC ni mecanismos avanzados.                                               |
| ESIS28 | Gestión proactiva del ciclo de vida                   | El cuerpo describe actualización controlada, pero sin herramientas ni políticas concretas.                           |
| ESIS29 | Modelo integral de gobierno técnico                   | El cuerpo describe seguimiento general y señala la ausencia de KPI y cuadros de mando.                               |
| ESIS30 | Microsegmentación y seguridad adaptativa              | El cuerpo indica que no se definen arquitecturas de red ni tecnologías específicas.                                  |
| ESIS31 | Virtualización preparada para IA                      | El cuerpo solo alude a conceptos de optimización y declara que no hay herramientas ni métricas.                      |
| ESEG1  | Validación ofensiva continua                          | El cuerpo describe pentesting genérico y declara que faltan metodología, herramientas y procedimiento.               |
| ESEG3  | Attack Surface Management                             | El cuerpo declara que no hay herramientas ni técnicas avanzadas para la superficie de ataque.                        |
| EDSA1  | Implantación de DevSecOps                             | El cuerpo declara que no identifica herramientas ni estándares de desarrollo seguro.                                 |

Referencias: cuerpo, líneas 995-1829; anexo, líneas 2280-2321; CSV, líneas 21-52.

No se concluye aquí que esas mejoras sean falsas: se concluye que, dentro de los cuatro archivos revisados, no tienen una evidencia coherente y trazable.

Opciones:

- [x] **Contrastar cada afirmación con la oferta original. Si existe evidencia, incorporarla de forma concreta al análisis detallado y conservar el anexo/CSV; si no existe, retirar o rebajar la afirmación del anexo y del CSV y revisar su efecto en el nivel.**
- [ ] Tomar el anexo como verdad e insertar automáticamente sus afirmaciones en el cuerpo. No se recomienda porque podría convertir una síntesis no acreditada en motivación de la puntuación.
- [ ] Tomar el cuerpo como verdad y borrar automáticamente todas las mejoras. Es más prudente que inventarlas, pero podría eliminar evidencia real omitida durante la normalización.

## 6. Nombres de tareas y grupos

### 6.1. Veinte nombres de subproyecto no son idénticos

Ambos informes individuales coinciden entre sí. El CSV usa otra redacción en estos 20 ID:

| ID     | CSV                                                                               | Informes individuales                                                       |
| ------ | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| ELIF2  | Barra de herramientas y pie de EducaMadrid                                        | Barra de herramientas y pie común de EducaMadrid                            |
| IFP1   | Mejoras y mantenimiento de la web de Innovación y Formación del Profesorado (IFP) | Mejoras y mantenimiento de la web de Innovación y Formación del Profesorado |
| EMOM6  | Tareas sobre las configuraciones para las conexiones externas                     | Configuraciones para conexiones externas                                    |
| EMOM7  | Otras tareas específicas para la actualización y procedimiento en Moodle Misc     | Otras tareas específicas de actualización y procedimiento                   |
| ESIS2  | Servicio de actualización del bases de datos                                      | Servicio de actualización de bases de datos                                 |
| ESIS11 | Integración en el Gestor de Servidores de Bases de Datos                          | Integración con el gestor de servidores de bases de datos                   |
| ESIS15 | Instalación de la paquetería y gestión de dependencias                            | Instalación de paquetería y gestión de dependencias                         |
| ESIS17 | Soporte para la integración con el LDAP de la plataforma EducaMadrid              | Integración con LDAP                                                        |
| ESIS18 | Soporte para la integración con el sistema de correo de la plataforma EducaMadrid | Integración con el sistema de correo                                        |
| ESIS19 | Soporte para la integración con distintas BBDD de la plataforma EducaMadrid       | Integración con bases de datos                                              |
| ESIS20 | Soporte para la integración del CMDB de la plataforma EducaMadrid                 | Integración con la CMDB                                                     |
| ESIS21 | Documentación del proyecto externo                                                | Documentación del proyecto exterior                                         |
| ESIS22 | Gestión del riesgo del proyecto externo                                           | Gestión del riesgo del proyecto exterior                                    |
| ESIS23 | Implementación de sistemas de Backups y procedimiento de Disaster Recovery        | Implementación de copias de seguridad y recuperación ante desastres         |
| ESIS26 | Implementación de servicios de ciberseguridad básicos                             | Implantación de medidas de ciberseguridad básicas                           |
| ESIS27 | Implementación de servicios de ciberseguridad avanzados                           | Implantación de medidas de ciberseguridad avanzadas                         |
| ESIS28 | Actualización de los sistemas operativos                                          | Actualización de sistemas operativos                                        |
| ESIS30 | Segmentación de la actual red de servidores                                       | Segmentación de la red de servidores                                        |
| ESIS31 | Optimización de la infraestructura de virtualización del entorno                  | Optimización de la infraestructura de virtualización                        |
| ESEG1  | Realización de Auditorías/Pentesting Web                                          | Realización de auditorías y pentesting web                                  |

La mayoría son variantes editoriales. `ESIS2` contiene además el error gramatical `del bases de datos` en el CSV.

Opciones:

- [x] **Copiar literalmente para los cuatro archivos la denominación del Anexo II oficial.** Si no se dispone de él, usar provisionalmente la redacción común de los dos informes y corregir el error de ESIS2.
- [ ] Mantener títulos abreviados en los informes y completos en el CSV, añadiendo una nota expresa de equivalencia. Es válido, pero reduce la comparación automática.

### 6.2. Cuatro nombres de grupo tampoco coinciden

| Código | CSV                                                                               | Informes individuales                            |
| ------ | --------------------------------------------------------------------------------- | ------------------------------------------------ |
| IFP    | Mejoras y mantenimiento de la web de Innovación y Formación del Profesorado (IFP) | Innovación y Formación del Profesorado (IFP)     |
| EMOM   | Proyectos Moodle Misc (EMOM)                                                      | Proyectos MoodleMisc (EMOM)                      |
| EIPE   | Proyectos de Integración con la Plataforma de EducaMadrid (EIPE)                  | Integración con la plataforma EducaMadrid (EIPE) |
| EDSA   | Realización de pruebas de desarrollo seguro de aplicaciones web (EDSA)            | Desarrollo Seguro de Aplicaciones Web (EDSA)     |

Opciones:

- [x] **Aplicar la misma denominación oficial de grupo en todos los archivos**, conservando el código como clave estable.
- [ ] Admitir nombres descriptivos diferentes y comparar solo por ID. Es técnicamente posible, pero mantiene ruido y dificulta revisiones manuales.

## 7. Referencias y terminología editorial

### 7.1. Nombre del contrato y espaciado

El conjunto escribe `EEDUCAMADRID (BAC01_2026)`; los individuales escriben `EEDUCAMADRID(BAC01_2026)`. Además, conviene confirmar si `EEDUCAMADRID` es el literal oficial o una errata de `EducaMadrid`.

Opciones:

- [x] **Copiar en los tres informes el literal oficial exacto del contrato y normalizar el espacio antes de `(BAC01_2026)`.**
- [ ] Corregir solo el espacio, manteniendo `EEDUCAMADRID` sin comprobar el título oficial.

### 7.3. Comas adheridas a los identificadores de empresa

El conjunto contiene once apariciones de `empresa_s,` o `empresa_n,` en tablas o frases donde la coma queda integrada en el identificador; son especialmente visibles en las líneas 238, 298, 320-321, 335-336, 346 y 348.

Opciones:

- [x] **Eliminar las comas que no correspondan sintácticamente y usar siempre los identificadores exactos `empresa_s` y `empresa_n`.**
- [ ] Mantenerlas como puntuación contextual. No se recomienda dentro de celdas de tabla ni texto en negrita porque parecen formar parte del nombre.

## 8. Orden recomendado de corrección posterior

Cuando se autorice la actualización de los archivos, el orden recomendado es:

1. Confirmar el inventario y las denominaciones oficiales del Anexo II.
2. Resolver contra la oferta original la asignación de `ESIS25`, `ESIS26`, `ESIS27`, `ESIS30` y `ESIS31` de empresa_n y las afirmaciones sin trazabilidad del apartado 5.4.
3. Corregir la contradicción de `EDSA2` y las referencias ambiguas a `Anexo I`.
4. Aplicar los cinco niveles, sus umbrales y la conversión CSV `10/8/5/2/0`.
5. Tomar las tablas del informe conjunto como origen para regenerar las tablas de los informes individuales.
6. Recalcular automáticamente subtotales, totales y umbral.
7. Regenerar las cuatro columnas `desc_empresa_n`, `val_empresa_n`, `desc_empresa_s` y `val_empresa_s` del CSV desde los informes corregidos.
8. Uniformar nombres de tareas, grupos, contrato y empresas.
9. Validar de nuevo: 53 ID únicos, correspondencia semántica por ID, sumas, niveles, valores CSV, anexos y propuesta final.

## 9. Decisiones preseleccionadas

- [x] El informe conjunto será la fuente de verdad de las puntuaciones y valoraciones que deberán reproducir los informes individuales.
- [x] Empresa_n adoptará el reparto del conjunto y su total se corregirá a `7,25 + 2,80 = 10,05`.
- [x] Empresa_s conservará `10,85 + 7,85 = 18,70`; su informe individual reproducirá los niveles del conjunto una vez normalizados.
- [x] Se eliminará empresa_u del alcance, salvo que se aporte su expediente completo.
- [x] El Anexo II oficial será la fuente de nombres e ID.
- [x] No se rellenarán automáticamente las cinco filas vacías de empresa_n antes de resolver la asignación de contenido.
- [x] Toda mejora no trazable se contrastará con la oferta original antes de conservarla o eliminarla.
- [x] Solo se usarán `EXCELENTE`, `ALTA`, `MEDIA`, `BAJA` y `MUY BAJA`, con los umbrales del apartado 3.3.
- [x] El CSV aplicará siempre `EXCELENTE=10`, `ALTA=8`, `MEDIA=5`, `BAJA=2` y `MUY BAJA=0`.
