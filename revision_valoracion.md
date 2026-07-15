# Revisión de cobertura y motivación de las valoraciones

## 1. Objeto y alcance

Se ha comprobado `valoracion_plantilla.md` frente a los diez informes indicados, limitando la revisión a dos preguntas:

1. Si cada informe valora los once subcriterios de la plantilla.
2. Si cada nivel cualitativo y cada puntuación dispone de una motivación suficiente y coherente con el árbol de valoración.

La revisión es documental. No sustituye la comprobación de las memorias técnicas originales ni propone modificar automáticamente una puntuación sin volver a contrastar la evidencia de la oferta.

## 2. Conclusión ejecutiva

**No faltan subcriterios.** Los diez informes incluyen Arquitectura, Comprensión, Viabilidad, Metodología, Rendimiento, Satisfacción de requisitos, Calendario, Riesgos, Contingencias, Calidad y Trazabilidad.

La comprobación estructural arroja el siguiente resultado:

- Los siete informes individuales contienen **77 de 77 valoraciones esperadas**: 7 informes × 11 subcriterios.
- Las 77 valoraciones incluyen un texto justificativo, un nivel cualitativo y una puntuación.
- Las 77 puntuaciones están dentro de la banda porcentual declarada para el nivel asignado.
- Los tres informes conjuntos reproducen esas mismas 77 combinaciones de nivel y puntuación sin diferencias respecto de los informes individuales.
- Los subtotales y totales publicados son aritméticamente coherentes con las puntuaciones de los subcriterios.

Por tanto, la respuesta estricta a la pregunta de cobertura es **sí**. Sin embargo, la respuesta a la pregunta de motivación es **parcial**:

- Los siete informes individuales sí contienen una motivación diferenciada para cada subcriterio.
- Los tres informes conjuntos muestran todos los niveles y notas, pero no justifican de forma individual cada celda de sus tablas comparativas.
- En el conjunto de los informes no existe una regla que explique por qué, dentro de una misma banda, se elige una cifra exacta y no otra.
- Se han localizado varios casos en los que la motivación escrita no encaja con el descriptor literal del nivel asignado.

## 3. Matriz de comprobación por informe

| Informe                                                  | Motivación por subcriterio | Resultado                                                        |
|----------------------------------------------------------|---------------------------:|------------------------------------------------------------------|
| `informe_conjunto_y_normalizado_desarrollo.md`           |     No; global por empresa | Revisión necesaria                                               |
| `informe_individual_normalizado_desarrollo_empresa_n.md` |                         Sí | Cobertura correcta; revisar correspondencia semántica            |
| `informe_individual_normalizado_desarrollo_empresa_s.md` |                         Sí | Correcto en el alcance comprobado                                |
| `informe_individual_normalizado_desarrollo_empresa_u.md` |                         Sí | Cobertura correcta; revisar Gantt y satisfacción                 |
| `informe_conjunto_y_normalizado_exteriores.md`           | Parcial; varios se agrupan | Revisión necesaria                                               |
| `informe_individual_normalizado_exteriores_empresa_n.md` |                         Sí | Cobertura correcta; revisar arquitectura, satisfacción y riesgos |
| `informe_individual_normalizado_exteriores_empresa_s.md` |                         Sí | Cobertura correcta; revisar calendario/Gantt                     |
| `informe_conjunto_y_normalizado_sistemas.md`             |     No; global por bloques | Revisión necesaria                                               |
| `informe_individual_normalizado_sistemas_empresa_n.md`   |                         Sí | Cobertura correcta; revisar arquitectura y calendario            |
| `informe_individual_normalizado_sistemas_empresa_s.md`   |                         Sí | Correcto en el alcance comprobado                                |

## 4. Incongruencias detectadas y opciones de solución

### RV-01 — La plantilla asigna dos máximos distintos a Satisfacción de los requisitos

**Prioridad:** crítica.

**Evidencia:**

- `valoracion_plantilla.md:29-34` distribuye la solución técnica como 2 + 2 + 1 + 1 + 1 + **8**, total 15.
- `valoracion_plantilla.md:78` titula después «Satisfacción de los requisitos - **2 puntos**».
- Todos los informes emplean un máximo de **8 puntos**, que es el único que permite que el bloque sume 15.

**Impacto:** la plantilla contiene una contradicción material sobre la ponderación del subcriterio de mayor peso.

**Opciones:**

- [ ] Opción A — Mantener el título de 2 puntos y redistribuir los seis puntos restantes del bloque. Exigiría una modificación sustancial de toda la valoración.
- [x] **Opción B — Corregir el título de la plantilla a «Satisfacción de los requisitos - 8 puntos».** Es coherente con el desglose, con el total de 15 y con los diez informes.

### RV-02 — Las bandas porcentuales dejan intervalos sin clasificar

**Prioridad:** alta.

**Evidencia:** `valoracion_plantilla.md:86-92` y `valoracion_plantilla.md:143-149` definen 76-100, 51-75, 26-50, 1-25 y 0. Con puntuaciones decimales quedan sin nivel porcentajes como 75,5 %, 50,5 % o 25,5 %.

**Impacto:** una nota decimal podría ser válida aritméticamente y no pertenecer a ninguna categoría. Ninguna nota actual cae en esos huecos, pero la regla no es completa.

**Opciones:**

- [x] **Opción A — Restringir todas las notas a porcentajes enteros.
- [ ] Opción B — Redactar las bandas como intervalos continuos: EXCELENTE ≥ 76 %; ALTA ≥ 51 % y < 76 %; MEDIA ≥ 26 % y < 51 %; BAJA > 0 % y < 26 %; MUY BAJA = 0 %.

### RV-03 — Los informes conjuntos no motivan cada nivel y nota de sus tablas

**Prioridad:** alta.

**Evidencia:**

- Desarrollo publica las 33 valoraciones en `informe_conjunto_y_normalizado_desarrollo.md:278-297`, pero las justifica después con tres párrafos globales por empresa en las líneas 311-319. No explica individualmente Arquitectura, Comprensión, Viabilidad, Metodología, Rendimiento, Satisfacción, Calendario, Riesgos, Contingencias, Calidad y Trazabilidad.
- Exteriores publica las 22 valoraciones en `informe_conjunto_y_normalizado_exteriores.md:250-269`. La motivación de las líneas 282-294 distingue Arquitectura, Comprensión, Viabilidad y Satisfacción, pero no trata separadamente Metodología y Rendimiento; los cinco subcriterios de planificación se justifican como un único bloque.
- Sistemas publica las 22 valoraciones en `informe_conjunto_y_normalizado_sistemas.md:296-315`, pero las líneas 328-338 justifican globalmente la solución técnica y la planificación. Solo Satisfacción recibe una referencia diferenciada.

**Impacto:** el lector puede conocer la nota, pero no reconstruir dentro del propio informe conjunto qué evidencia conduce a cada nivel y a cada puntuación. La existencia del informe individual no corrige por sí sola esa falta si se exige que todos los informes sean autosuficientes.

**Opciones:**

- [ ] Opción A — Añadir únicamente referencias al apartado exacto de cada informe individual.
- [x] **Opción B — Añadir en cada informe conjunto una motivación breve por empresa y subcriterio**, reutilizando de manera fiel la evidencia del informe individual y manteniendo una referencia a este para el desarrollo completo.
- [ ] Opción C — Suprimir niveles y notas desglosados de los informes conjuntos y dejar únicamente totales. Reduciría la utilidad y la transparencia del documento.

### RV-04 — No hay una regla para elegir la puntuación exacta dentro de cada banda

**Prioridad:** alta.

**Evidencia:** la plantilla define intervalos amplios, pero no establece anclajes ni una fórmula interna. Los informes justifican generalmente la categoría, pero no explican por qué se asigna, por ejemplo, 0,55 en vez de 0,60 dentro de ALTA, 0,40 en vez de 0,50 dentro de MEDIA o 1,80 en vez de otra cifra dentro de BAJA.

Esto afecta a los diez informes. Algunos apartados convierten la nota ya aprobada a porcentaje, pero esa conversión solo demuestra que cae en la banda; no explica cómo se obtuvo la cifra.

**Impacto:** dos ofertas con una motivación equivalente podrían recibir notas distintas dentro de la misma categoría sin una regla documental que permita auditar la diferencia.

**Opciones:**

- [ ] Opción A — Utilizar un único valor fijo para cada nivel cualitativo.
- [x] **Opción B — Mantener la libertad de elegir cualquier cifra de la banda y añadir solo una frase genérica**.
- [ ] Opción C — Definir indicadores observables para cada subcriterio y una regla de cálculo intra-banda. Cada justificación deberá indicar los indicadores cumplidos, los no cumplidos, el nivel resultante y el cálculo de la nota exacta.

### RV-05 — Varias valoraciones de Arquitectura usan MEDIA pese a describir una arquitectura incompleta

**Prioridad:** alta.

**Regla de la plantilla:** `valoracion_plantilla.md:40-44` reserva MEDIA para una arquitectura descrita de forma completa y BAJA para una descripción incorrecta o incompleta.

**Casos detectados:**

1. `informe_individual_normalizado_desarrollo_empresa_n.md:571-576`: la motivación afirma que la definición no es completa, que la cobertura es parcial y que existen errores; asigna MEDIA y 1,00/2,00.
2. `informe_individual_normalizado_exteriores_empresa_n.md:2135-2151`: se indica que la mayor parte de los bloques no desarrolla arquitecturas completas, que faltan diagramas y arquitecturas específicas y que el desarrollo es insuficiente; asigna MEDIA y 0,90/2,00.
3. `informe_individual_normalizado_sistemas_empresa_n.md:2431-2448`: se afirma que no existe una arquitectura técnica definida, que faltan relaciones y arquitecturas por subproyecto y que aspectos esenciales no son evaluables; asigna MEDIA y 0,90/2,00.

Los tres informes conjuntos reproducen esas categorías y notas.

**Impacto:** la nota es compatible con la banda matemática de MEDIA, pero la motivación utiliza literalmente los rasgos que la plantilla asocia a BAJA.

**Opciones:**

- [ ] Opción A — Mantener MEDIA y reescribir la motivación para acreditar que la arquitectura sí es completa, aunque no sea correcta o excelente. Solo es admisible si la oferta original contiene esa evidencia.
- [x] **Opción B — Cambiar directamente los tres casos a BAJA y recalcular totales**.
- [ ] Opción C — Reabrir los tres casos contra la oferta original; si se mantiene la evidencia actualmente escrita, reclasificar Arquitectura como BAJA y recalcular los informes individual y conjunto. No debe maquillarse la motivación para conservar una nota predeterminada.

### RV-06 — Varias valoraciones de Satisfacción no encajan con el descriptor literal asignado

**Prioridad:** alta.

**Regla de la plantilla:** `valoracion_plantilla.md:80-84` describe ALTA y MEDIA como situaciones en las que la solución cumple los requisitos, con distinto grado de mejoras; BAJA presupone que los cumple de forma justa, y MUY BAJA contempla el incumplimiento.

**Casos detectados:**

1. Desarrollo, empresa_n (`informe_individual_normalizado_desarrollo_empresa_n.md:606-611`): 73 de 85 proyectos se califican como insuficientes o con errores, pero el resultado es MEDIA, 2,50/8,00.
2. Desarrollo, empresa_u (`informe_individual_normalizado_desarrollo_empresa_u.md:606-611`): 37 proyectos son menciones insuficientes y 26 no contienen solución concreta, pero el resultado es BAJA, 0,80/8,00; la propia motivación no acredita que se cumplan justamente todos los requisitos.
3. Exteriores, empresa_n (`informe_individual_normalizado_exteriores_empresa_n.md:2239-2259`): se reconocen cobertura incompleta, carencias técnicas y ausencia de respuesta evaluable para ESIS11 y ESIS14, pero se asigna ALTA, 4,20/8,00. La justificación demuestra que el 52,5 % está dentro de ALTA, pero no que se cumpla el descriptor cualitativo de ALTA.
4. Sistemas, empresa_n (`informe_individual_normalizado_sistemas_empresa_n.md:2512-2529`): se indica que la mayoría de las respuestas no alcanza una satisfacción técnica efectiva y que existen bloques completos sin contenido evaluable; se asigna BAJA, 2,00/8,00.

**Impacto:** se está usando primero el porcentaje para nombrar el nivel, aunque la narración pueda contradecir la definición cualitativa de ese nivel. Esto convierte el árbol descriptivo en una consecuencia de la nota, no en su fundamento.

**Opciones:**

- [ ] Opción A — Mantener las notas y eliminar del árbol las descripciones de cumplimiento, dejando solo bandas porcentuales.
- [ ] Opción B — Reescribir las motivaciones para afirmar cumplimiento suficiente. Solo sería válido si lo acredita la oferta original.
- [x] **Opción C — Revalorar estos cuatro casos contra la oferta original aplicando primero el descriptor cualitativo y después la banda.** Si se mantienen las carencias documentadas, deberán ajustarse nivel, nota, subtotales, total y umbral en los informes individual y conjunto.

### RV-07 — La valoración del Calendario no aplica de forma uniforme el requisito de Gantt o equivalente

**Prioridad:** alta.

**Regla de la plantilla:** `valoracion_plantilla.md:94-109` exige un diagrama de Gantt o similar y lo incorpora a todos los descriptores del subcriterio.

**Casos detectados:**

1. Desarrollo, empresa_u (`informe_individual_normalizado_desarrollo_empresa_u.md:631-636`): declara que no existe Gantt ni planificación operativa, pero asigna BAJA y 0,50/11,00.
2. Sistemas, empresa_n (`informe_individual_normalizado_sistemas_empresa_n.md:2549-2574`): sí existe cronograma, pero se describe como no interpretable, no operativo, sin secuencia, continuidad, dependencias, recursos, trazabilidad ni hitos; aun así recibe MEDIA y 5,00/11,00. La descripción se aproxima más a los rasgos de BAJA de la plantilla.

**Impacto:** la ausencia total del instrumento recibe puntuaciones no nulas muy diferentes y un cronograma descrito como no operativo se sitúa cerca del máximo de MEDIA.

**Opciones:**

- [ ] Opción A — Considerar el Gantt un elemento orientativo y retirar su exigencia de los descriptores.
- [x] **Opción B — Definir expresamente «ausencia de Gantt o equivalente = MUY BAJA / 0 puntos» y revalorar los dos casos.** Para sistemas empresa_n, donde sí existe cronograma, debe decidirse entre MEDIA y BAJA contrastando su coherencia real con el descriptor, no solo el porcentaje deseado.
- [ ] Opción C — Mantener las notas actuales y añadir una excepción distinta para cada expediente. Reduciría la homogeneidad.

### RV-08 — La motivación de Riesgos de exteriores empresa_n contradice su nivel y nota

**Prioridad:** media-alta.

**Evidencia:** `informe_individual_normalizado_exteriores_empresa_n.md:2303-2319` afirma que el apartado tiene un desarrollo relativamente superior, una comprensión razonable, un análisis identificable y razonablemente alineado, y que merece una valoración superior a otros apartados. Sin embargo, asigna exactamente el mismo resultado que Contingencias, Calidad y Trazabilidad: BAJA y 0,25/1,00.

**Impacto:** las frases positivas no justifican el descriptor «mal análisis» de BAJA ni la afirmación de superioridad se refleja en la nota.

**Opciones:**

- [ ] Opción A — Elevar nivel y nota de Riesgos.
- [ ] Opción B — Mantener 0,25 y eliminar las afirmaciones de superioridad y adecuación razonable.
- [x] **Opción C — Revalorar el apartado contra la oferta y hacer coincidir conclusión y nota.** Si se conserva 0,25, la motivación deberá concluir inequívocamente que el análisis es deficiente; si se conserva la conclusión positiva, deberá asignarse una banda superior.

### RV-09 — Rendimiento se penaliza por falta de métricas sin justificar el rendimiento previsible concreto

**Prioridad:** media.

**Evidencia:** el árbol de `valoracion_plantilla.md:70-76` distingue rendimiento excelente, bueno, normal, malo o muy malo. En varios informes, por ejemplo desarrollo empresa_n (`líneas 599-604`), desarrollo empresa_u (`líneas 599-604`) y sistemas empresa_n (`líneas 2497-2510`), la motivación se centra en la falta de métricas, pruebas o criterios de aceptación. Eso justifica una baja verificabilidad, pero no identifica de forma directa si el rendimiento previsible es normal, malo o muy malo.

**Impacto:** se mezclan dos dimensiones distintas: calidad del rendimiento esperado y suficiencia de la evidencia aportada para estimarlo.

**Opciones:**

- [ ] Opción A — Valorar únicamente si existen métricas, sin cambiar el texto de la plantilla.
- [ ] Opción B — Mantener la exigencia de evidencia, pero hacer explícito el razonamiento: indicar qué rendimiento puede inferirse, qué evidencia lo sustenta y por qué la ausencia de prueba impide alcanzar el nivel superior. Si no puede inferirse ningún rendimiento, revalorar conforme al nivel que el órgano considere aplicable.
- [ ] Opción C — Separar Rendimiento y Verificabilidad en dos subcriterios, lo que alteraría la estructura oficial.
- [x] **Opción D - Dejarlo como está, no hacer nada con esta revisión**.

### RV-10 — BAJA y MUY BAJA tienen el mismo descriptor en Trazabilidad

**Prioridad:** media.

**Evidencia:** `valoracion_plantilla.md:135-141` define tanto BAJA como MUY BAJA mediante la misma frase: «Se presenta una mala descripción de cómo se va a fiscalizar la trazabilidad del servicio».

**Impacto:** no existe una diferencia cualitativa que permita decidir entre una puntuación del 1-25 % y 0 %.

**Opciones:**

- [ ] Opción A — Mantener ambos textos y distinguir los niveles solo por porcentaje.
- [ ] Opción B — Reservar MUY BAJA para ausencia de descripción o descripción no evaluable, y BAJA para una descripción existente pero claramente deficiente.
- [x] **Opción C - Dejarlo como está, no hacer nada con esta revisión**.

## 5. Orden recomendado de corrección

1. Corregir y cerrar la plantilla: máximo de Satisfacción, intervalos continuos, regla para ausencia de Gantt, diferencia entre BAJA y MUY BAJA y método intra-banda.
2. Revalorar contra las ofertas originales los casos RV-05, RV-06, RV-07, RV-08 y RV-09. La revisión debe decidir primero el descriptor cualitativo y después la puntuación dentro de su banda.
3. Actualizar simultáneamente cada informe individual y su informe conjunto, recalculando subtotales, totales y umbral cuando cambie una nota.
4. Añadir en los tres informes conjuntos una justificación breve por empresa y subcriterio.
5. Ejecutar una comprobación final automática de cobertura, bandas, sumas y coincidencia conjunto/individual.

## 6. Decisión recomendada global

- [x] **No modificar todavía de forma automática las puntuaciones.** Primero debe aprobarse una versión inequívoca de la regla de valoración y contrastarse cada caso semánticamente dudoso con la memoria técnica original.
- [x] **Sí considerar confirmada la cobertura estructural:** ninguno de los diez informes omite un punto de valoración.
- [x] **Sí considerar pendiente la suficiencia de motivación de los tres informes conjuntos y la justificación de la nota exacta en los diez informes.**

Esta opción preserva la trazabilidad del proceso: evita cambiar notas para hacerlas encajar retrospectivamente y obliga a que cualquier ajuste posterior quede sustentado en la oferta, el descriptor aplicable y una regla numérica explícita.
