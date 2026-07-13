# REVISIÓN DE CONGRUENCIA — DESARROLLO

Fecha de revisión: 13 de julio de 2026.

## Alcance

Se han contrastado los siguientes archivos:

- `informe_conjunto_y_normalizado_desarrollo.md`
- `informe_individual_normalizado_desarrollo_empresa_s.md`
- `informe_individual_normalizado_desarrollo_empresa_n.md`
- `informe_individual_normalizado_desarrollo_empresa_u.md`
- `tareas_anexoii_desarrollo.csv`

En las opciones de resolución, `[x]` señala la opción recomendada. Este documento no aplica todavía ninguna corrección a los cinco archivos revisados.

## Resumen ejecutivo

Se han localizado los siguientes grupos de incongruencias o ambigüedades:

1. El universo de tareas no coincide: los tres informes individuales evalúan 85 proyectos, mientras que el CSV contiene 82 y omite `AV12`, `COR3` y `COR4`.
2. Siete identificadores del CSV no coinciden con los códigos utilizados de forma unánime en los tres informes individuales.
3. Siete niveles cualitativos del informe conjunto no coinciden con los de los informes individuales, aunque sus puntuaciones numéricas sí coinciden.
4. En 49 tareas de empresa_s, la consideración de «valor añadido» del CSV y la del anexo individual apuntan en direcciones opuestas.
5. La escala de `val_empresa_*` no está definida y no puede derivarse de forma unívoca de los grados e indicadores de los informes normalizados.
6. El informe conjunto utiliza afirmaciones de cobertura imprecisas o incompatibles con los recuentos de los anexos individuales para empresa_s y empresa_n.
7. Hay tres variantes terminológicas erróneas en una misma frase del informe individual de empresa_n.

Además, se considerará incongruencia transversal cualquiera de estas situaciones:

- utilizar un nivel distinto de los cinco definidos por los propios informes: `EXCELENTE`, `ALTA`, `MEDIA`, `BAJA` y `MUY BAJA`;
- asignar un nivel que no corresponda a estos umbrales: `EXCELENTE`, del 76 % al 100 %; `ALTA`, del 51 % al 75 %; `MEDIA`, del 26 % al 50 %; `BAJA`, del 0 % al 25 %; y `MUY BAJA`, exactamente el 0 % de la puntuación de la sección correspondiente;
- convertir un nivel a un valor CSV distinto de `EXCELENTE=10`, `ALTA=8`, `MEDIA=5`, `BAJA=2` y `MUY BAJA=0`.

Cuando el 0 % pudiera encajar nominalmente tanto en `BAJA` como en `MUY BAJA`, prevalecerá la regla específica de `MUY BAJA`.

No se han encontrado diferencias en las puntuaciones numéricas, las sumas de los bloques, los totales sobre 30, la aplicación del umbral de 15 puntos ni la propuesta de continuación o exclusión.

## INC-01. El CSV contiene 82 tareas y los informes individuales evalúan 85

- **Evidencia**

Los tres anexos individuales contienen los mismos 85 identificadores únicos. Sus resúmenes cuantitativos también declaran 85 proyectos y sus recuentos internos cuadran:

| Licitador | Suficiente | Insuficiente | No incluida | Total |
| --- | ---: | ---: | ---: | ---: |
| empresa_s | 81 | 4 | 0 | 85 |
| empresa_n | 12 | 73 | 0 | 85 |
| empresa_u | 22 | 37 | 26 | 85 |

El CSV contiene 82 filas de datos. Faltan exactamente estas tres tareas:

| ID ausente | Denominación del Anexo II | Grupo | empresa_n | empresa_s | empresa_u |
| --- | --- | --- | --- | --- | --- |
| `AV12` | Generador de textos | Aulas Virtuales | INSUFICIENTE; sin VA; sin error | SUFICIENTE; VA; sin error | INSUFICIENTE; sin VA; sin error |
| `COR3` | Redacción de correos | Correo Web | INSUFICIENTE; sin VA; con error | SUFICIENTE; VA; sin error | INSUFICIENTE; sin VA; sin error |
| `COR4` | Reescritura de correos | Correo Web | INSUFICIENTE; sin VA; con error | SUFICIENTE; VA; sin error | INSUFICIENTE; sin VA; sin error |

Los tres IDs aparecen en las líneas 772, 805 y 806 de cada informe individual. Las denominaciones se han comprobado en el Anexo II disponible en el repositorio; no se han inferido a partir de las ofertas.

- **Opciones de resolución**

- [x] **Opción A — recomendada:** incorporar las tres filas al CSV, en sus posiciones lógicas (`AV12` entre `AV11` y `AV13`, y `COR3`/`COR4` después de `COR2`), usando las denominaciones oficiales y las valoraciones que resulten de la regla acordada en INC-04 e INC-05. Mantener los informes individuales en 85 proyectos.
- [ ] **Opción B:** declarar expresamente que el CSV es un listado parcial de 82 tareas y documentar sus tres exclusiones. No es recomendable porque su nombre y estructura indican que pretende representar el Anexo II completo.
- [ ] **Opción C:** eliminar `AV12`, `COR3` y `COR4` de los tres informes y recalcular todos sus recuentos. No es recomendable: los tres informes coinciden entre sí y los códigos existen en el Anexo II.

## INC-02. Identificadores no canónicos o ambiguos en el CSV

- **Evidencia**

Para poder cruzar las 82 filas presentes ha sido necesario aplicar estas equivalencias:

| ID actual en el CSV | ID en los tres informes | Tarea |
| --- | --- | --- |
| `EMP` | `EMP1` | EMPieza |
| `BUS` | `BUS1` | Buscador de AV y cursos |
| `ANI` | `ANI1` | Animalandia |
| `FOR` | `FOR1` | Formularios |
| `FOROS` | `FOR` | Foros |
| `MAD` | `MAM` | Mamood |
| `EducaSAAC (EDU)` | `EDU` | EducaSAAC |

El caso `FOR`/`FOROS` es especialmente propenso a errores: `FOR` significa Formularios en el CSV, pero significa Foros en los informes; Formularios se identifica como `FOR1` en los informes.

- **Opciones de resolución**

- [x] **Opción A — recomendada:** usar en la columna `ID` del CSV exactamente los códigos de los informes (`EMP1`, `BUS1`, `ANI1`, `FOR1`, `FOR`, `MAM` y `EDU`). Mantener los nombres legibles únicamente en `NOMBRE DEL SUBPROYECTO` y `PROYECTO (GRUPO)`. La sustitución `FOR`/`FOROS` debe hacerse de forma simultánea para evitar una colisión temporal.
- [ ] **Opción B:** conservar los IDs actuales y añadir una columna `ID_CANONICO`.
- [ ] **Opción C:** conservar el CSV sin cambios y mantener una tabla de alias externa. Es la opción más frágil para futuros cruces automáticos.

## INC-03. Siete niveles cualitativos distintos entre el informe conjunto y los individuales

- **Evidencia**

Las puntuaciones numéricas coinciden en todos los casos, pero no estas etiquetas:

| Licitador | Subcriterio | Puntuación | Informe individual | Informe conjunto | Etiqueta propuesta |
| --- | --- | ---: | --- | --- | --- |
| empresa_n | Arquitectura | 1,00/2,00 | MEDIA | Media-Alta | MEDIA |
| empresa_n | Comprensión de requisitos | 1,00/2,00 | MEDIA | Media-Alta | MEDIA |
| empresa_n | Plan de calidad | 0,60/1,00 | ALTA | Media | ALTA |
| empresa_u | Arquitectura | 0,30/2,00 | BAJA | Media | BAJA |
| empresa_u | Comprensión de requisitos | 0,30/2,00 | BAJA | Media | BAJA |
| empresa_u | Análisis de riesgos | 0,30/1,00 | MEDIA | Baja | MEDIA |
| empresa_u | Plan de calidad | 0,30/1,00 | MEDIA | Baja | MEDIA |

La metodología solo admite cinco niveles: `EXCELENTE`, `ALTA`, `MEDIA`, `BAJA` y `MUY BAJA`. `Media-Alta`, utilizada dos veces en el informe conjunto, no está definida. Además, en el informe conjunto los dos valores de 0,30/1,00 de empresa_u se califican como `BAJA`, aunque el 30 % corresponde a `MEDIA`.

La escala que deberá aplicarse siempre es:

| Nivel | Porcentaje de la puntuación de la sección |
| --- | ---: |
| EXCELENTE | Del 76 % al 100 % |
| ALTA | Del 51 % al 75 % |
| MEDIA | Del 26 % al 50 % |
| BAJA | Del 0 % al 25 % |
| MUY BAJA | 0 % |

En el 0 % prevalece la categoría específica `MUY BAJA`.

Referencias principales: tablas comparativas del informe conjunto, líneas 278-297; evaluaciones individuales, líneas 571-675 de cada informe.

- **Opciones de resolución**

- [x] **Opción A — recomendada:** considerar el informe conjunto como fuente de verdad de la valoración, conservar sus puntuaciones y normalizar sus etiquetas mediante los cinco niveles y los umbrales anteriores. Después, hacer que los informes individuales reproduzcan esas valoraciones normalizadas. En los siete casos de la tabla, las etiquetas resultantes son las de la última columna.
- [ ] **Opción B:** considerar los informes individuales como fuente de verdad y trasladar sus etiquetas al conjunto. Aunque conduce a las mismas siete etiquetas en estos casos, invierte el origen documental acordado.
- [ ] **Opción C:** volver a valorar los siete subcriterios y permitir cambios tanto de nivel como de puntuación. Solo procede si se decide reabrir la valoración técnica de fondo.

## INC-04. Empresa_s: 49 discrepancias sobre «valor añadido» entre CSV y anexo individual

- **Evidencia**

El anexo normalizado de empresa_s separa el grado de desarrollo (`SUFICIENTE`/`INSUFICIENTE`) del indicador independiente de valor añadido (`VA`/`NO`). El CSV, en cambio, mezcla ambos conceptos en una descripción y una valoración numérica.

Hay dos discrepancias opuestas:

### A. El CSV afirma valor añadido y asigna 10, pero el anexo marca `NO` — 6 tareas

`TRA2`, `TRA3`, `AV13`, `CLO1`, `CLO2` y `EML`.

En estas seis filas el CSV usa la descripción «Propuesta técnica con valor añadido» y `val_empresa_s = 10`, mientras que el anexo de empresa_s las clasifica como `SUFICIENTE | NO | NO` y no identifica una mejora concreta.

### B. El anexo marca `VA`, pero el CSV las deja en desarrollo suficiente con valor 8 — 43 tareas

- TRA: `TRA5`, `TRA7`, `TRA8`.
- AV: `AV2`, `AV3`, `AV6`, `AV8`, `AV9`, `AV10`, `AV14`, `AV15`, `AV16`, `AV17`, `AV18`, `AV19`, `AV21`.
- MED: `MED3` a `MED11`.
- WPM: `WPM2`, `WPM4`, `WPM5`.
- VID: `VID3`, `VID4`.
- Resto de servicios, con los IDs actuales del CSV: `FOR` (Formularios), `ANI`, `CAU`, `EducaSAAC (EDU)`, `BAN`, `DTIC`, `ALB`, `AVI`, `FOROS` (Foros), `BOL`, `WES`, `GES` y `MAD`.

En estas 43 filas el CSV asigna `val_empresa_s = 8` y las describe como desarrollo suficiente, aunque suele conservar en el texto la mejora concreta; el anexo marca expresamente `VA` para todas ellas.

Los tres proyectos ausentes del CSV (`AV12`, `COR3` y `COR4`) también están marcados como `VA` en el anexo de empresa_s, pero se tratan en INC-01 y no se incluyen en el recuento de 49.

- **Opciones de resolución**

- [x] **Opción A — recomendada:** considerar definitivo el anexo normalizado y modificar directamente las 49 filas del CSV: retirar la afirmación de VA de los 6 falsos positivos y reflejarla en los 43 casos marcados `VA`. La cifra numérica debe decidirse después de fijar la regla de INC-05.
- [ ] **Opción B:** contrastar estos 49 IDs con la oferta original de empresa_s y el requisito correspondiente del Anexo II, fijar el resultado en una única matriz fuente y regenerar desde ella tanto el anexo como el CSV. Si se decide resolver usando solo los cinco archivos revisados, dar preferencia provisional al anexo normalizado, porque identifica la mejora concreta, separa grado e indicador y su recuento de 72 VA es internamente consistente.
- [ ] **Opción C:** considerar definitivo el CSV y modificar los 49 indicadores del anexo, sus resúmenes y cualquier narrativa que mencione 72 aportaciones de valor añadido. Es menos recomendable porque eliminaría numerosos indicadores acompañados de una mejora técnica concreta.

## INC-05. La escala `val_empresa_*` no tiene una semántica común ni una regla de cálculo documentada

- **Evidencia**

En las 82 filas actuales se observan estas distribuciones:

| Licitador | Valores usados | Distribución |
| --- | --- | --- |
| empresa_n | 1, 3, 5 | 11 con 1; 59 con 3; 12 con 5 |
| empresa_s | 5, 8, 10 | 4 con 5; 50 con 8; 28 con 10 |
| empresa_u | 1, 3, 4, 8 | 26 con 1; 34 con 3; 16 con 4; 6 con 8 |

La correspondencia observada no es uniforme:

- En empresa_n sí es determinista: error técnico e insuficiente = 1; insuficiente sin error = 3; suficiente = 5.
- En empresa_s, `SUFICIENTE + VA` puede valer 8 o 10 y `SUFICIENTE + NO` también puede valer 8 o 10. Los cuatro `WEK` combinan `INSUFICIENTE + VA` en el anexo con valor 5 en el CSV.
- En empresa_u, `SUFICIENTE + NO` puede valer 4 u 8.

Ninguno de los cinco archivos define la escala 0-10, su relación con el grado de desarrollo, el peso separado de VA/error ni la fórmula que conecta las valoraciones por tarea con los 8 puntos del subcriterio «Satisfacción de los requisitos». Por ello, la coherencia de los `val_empresa_*` no puede auditarse de forma concluyente solo a partir de estos archivos.

Se fija como conversión obligatoria de los niveles cualitativos al CSV: `EXCELENTE=10`, `ALTA=8`, `MEDIA=5`, `BAJA=2` y `MUY BAJA=0`. Cualquier valor distinto para uno de esos niveles constituirá una incongruencia.

- **Opciones de resolución**

- [x] **Opción A — recomendada:** crear una matriz fuente con campos independientes por licitador (`grado`, `nivel`, `valor_añadido`, `error`, `observación`) y derivar siempre `val` mediante `EXCELENTE=10`, `ALTA=8`, `MEDIA=5`, `BAJA=2` y `MUY BAJA=0`. Mantener `desc_empresa_*` y `val_empresa_*` como columnas derivadas si son necesarias por compatibilidad.
- [ ] **Opción B:** conservar el esquema actual y documentar reglas de valoración distintas por empresa. Es menos defendible frente al principio declarado de igualdad de trato.
- [ ] **Opción C:** eliminar las columnas `val_empresa_*` y conservar solo la clasificación textual. Evita falsas precisiones, pero pierde una parte del uso actual del CSV.

## INC-06. Afirmaciones de cobertura imprecisas en el informe conjunto

- **Evidencia**

Para empresa_s, el informe individual declara 81 proyectos suficientes y 4 insuficientes (`WEK1` a `WEK4`). Sin embargo, el informe conjunto afirma que desarrolla «de forma efectiva la totalidad de los sistemas» (línea 210). «Cobertura completa» puede ser correcto si significa que todos aparecen, pero no si significa que todos tienen desarrollo suficiente.

Para empresa_n, el informe individual declara que los 85 proyectos están incluidos, con 12 suficientes, 73 insuficientes y 0 no incluidos. El conjunto indica que identifica «la mayoría de los sistemas» (líneas 222 y 232), lo que oculta que la cobertura nominal es total y que el problema real es el desarrollo insuficiente.

- **Opciones de resolución**

- [ ] **Opción A:** sustituir en el informe conjunto las expresiones aproximadas por los recuentos exactos de los anexos: empresa_s, 85 incluidos, 81 suficientes y 4 insuficientes; empresa_n, 85 incluidos, 12 suficientes y 73 insuficientes; empresa_u, 22 suficientes, 37 insuficientes y 26 no incluidos. Esta opción tomaría los informes individuales como origen.
- [ ] **Opción B:** conservar la redacción actual y añadir una nota que defina qué significa «cobertura completa» o «mayoría» en cada pasaje.
- [x] **Opción C — recomendada:** considerar el informe conjunto como fuente de verdad y adaptar a él los recuentos y la narrativa de los informes individuales, dejando explícita en todos los documentos la diferencia entre «presencia/cobertura nominal» y «desarrollo suficiente».

## INC-07. Terminología inconsistente en el informe individual de empresa_n

- **Evidencia**

La línea 289 del informe individual de empresa_n usa `Word Press Multisite`, `Weekans` y `Videoconferenca`, mientras que los encabezados del propio informe, los otros informes y el CSV usan `WordPress Multisite`, `Wekan` y `Videoconferencia`.

- **Opciones de resolución**

- [x] **Opción A — recomendada:** normalizar las tres denominaciones en esa línea a `WordPress Multisite`, `Wekan` y `Videoconferencia`.
- [ ] **Opción B:** mantenerlas por no afectar a las puntuaciones. No es recomendable en documentos que declaran trazabilidad terminológica.

## Comprobaciones que no han detectado incongruencias

- Los tres anexos individuales contienen 85 IDs únicos y el mismo universo de IDs y bloques.
- Los recuentos y porcentajes de suficiente, insuficiente, no incluida, error y VA de cada informe individual coinciden con sus tablas de 85 filas.
- Las puntuaciones de los 11 subcriterios de cada licitador son numéricamente idénticas en el informe individual y el conjunto.
- Todas las sumas son correctas: empresa_s, 13,60 + 13,10 = 26,70; empresa_n, 5,70 + 5,60 = 11,30; empresa_u, 2,20 + 1,50 = 3,70.
- La aplicación del umbral es consistente: empresa_s supera 15 puntos; empresa_n y empresa_u no lo superan.
- Tras normalizar los alias de INC-02, no hay IDs duplicados en el CSV y las 82 filas presentes encuentran correspondencia en los tres anexos.
- En empresa_n y empresa_u no se han encontrado contradicciones entre el grado/error del anexo y el valor de las 82 tareas presentes, conforme a la correspondencia observable en el propio CSV.
- Las observaciones técnicas concretas del CSV concuerdan, en general, con las observaciones de los anexos; la discrepancia material se concentra en la clasificación de VA de empresa_s descrita en INC-04.

## Orden recomendado para una futura corrección

1. Fijar el universo canónico de 85 IDs y normalizar los alias (INC-01 e INC-02).
2. Definir la matriz fuente y aplicar la escala cualitativa y la conversión CSV obligatorias (INC-05).
3. Resolver mediante evidencia los 49 casos de empresa_s (INC-04).
4. Regenerar o actualizar el CSV desde la matriz acordada.
5. Regenerar las etiquetas, recuentos y afirmaciones de cobertura de los informes individuales a partir del informe conjunto, aplicando los cinco niveles y sus umbrales (INC-03 e INC-06).
6. Corregir las tres variantes terminológicas (INC-07).
7. Recalcular recuentos, puntuaciones y umbral; comprobar que solo cambian si la revisión de evidencia obliga a reabrir la valoración de fondo.
