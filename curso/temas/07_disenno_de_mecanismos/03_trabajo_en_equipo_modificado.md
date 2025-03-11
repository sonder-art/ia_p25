
A continuación ampliamos el análisis del **juego repetido** introducido antes, centrándonos en **qué sucede cuando los jugadores no cooperan** y contrastando ese resultado con la optimización cooperativa. Asimismo, consideramos **escenarios** que modifican distintos aspectos del modelo original: desde la forma en que valoran el ocio o la calificación, hasta la eficiencia del esfuerzo invertido.

---

## 1. El dilema de la (no) cooperación

En el modelo básico, cada estudiante $e \in \{1, \dots, E\}$ elige cuántas horas $h_{e,t}$ dedicar a un proyecto en cada periodo $t \in \{1, \dots, T\}$. La **calificación** resultante en el periodo $t$ es $G_t = f\!\bigl(\sum_{e=1}^E h_{e,t}\bigr)$, y la **utilidad** de cada estudiante combina el promedio de dichas calificaciones (compartidas) con su ocio total:
$
  U_e 
  \;=\; \frac{1}{T}\sum_{t=1}^T f\Bigl(\sum_{i=1}^E h_{i,t}\Bigr) 
       \;+\; \sum_{t=1}^T \bigl(W - h_{e,t}\bigr).
$

### 1.1. Incentivos de free-rider ("carreado")

Un problema típico en este juego es que la calificación $f(H_t)$ depende **del esfuerzo total** $H_t = \sum_{i=1}^E h_{i,t}$, **no** de quién específicamente pone ese esfuerzo. Por tanto:
- Si un jugador **anticipa** que los demás se esforzarán "lo suficiente" para obtener una calificación alta, él podría bajar su esfuerzo $h_{e,t}$ para maximizar su ocio sin dañar "demasiado" la calificación total.  
- **Resultado**: El jugador que reduce su esfuerzo se beneficia de más horas de ocio **a costa** del esfuerzo extra que tengan que poner los demás (o de la calificación ligeramente menor, si nadie compensa su reducción).

### 1.2. Contraste con la solución cooperativa

En la **cooperación perfecta**, los jugadores maximizan la **suma de utilidades** o algún criterio social que promueva la eficiencia global. Esto generalmente lleva a un **nivel de esfuerzo colectivo** mayor que en el equilibrio individual de no-cooperación, logrando (posiblemente) una calificación $f(H_t)$ más alta y una distribución equilibrada del esfuerzo.

Sin embargo, sostener dicho nivel cooperativo en un juego repetido requiere:
- **Amenazas creíbles** de castigo a quien reduzca esfuerzo.  
- **Coordinación** para asignar de modo estable quién trabaja cuánto en cada periodo.  

En la realidad, la falta de mecanismos de sanción o vigilancia favorece el **problema del free-rider** ("me van a carrear"), que lleva a resultados subóptimos.

---

## 2. Escenario 1: Ocio lineal y saturación de la calificación

En el escenario básico, si el **ocio** se valora de manera lineal ($\sum_{t=1}^T (W - h_{e,t})$) y la calificación $f(H_t)$ alcanza rápidamente un nivel de "saturación", podría surgir la estrategia en la que un solo estudiante (o un subgrupo) concentra la mayor parte del esfuerzo en un periodo para "asegurar" la calificación suficiente, **permitiendo** que los demás descansen (tengan más ocio).

1. **Función de calificación saturada**  
   - Supongamos que $f(H_t)$ crece con $H_t$ hasta cierto punto, luego se **aplana** (rendimientos decrecientes muy marcados). Una cantidad moderada de horas basta para alcanzar una calificación decente (cerca del máximo posible).  

2. **Reparto del esfuerzo**  
   - Si una persona está dispuesta a poner la mayor parte de las horas, el total $H_t$ puede ser suficientemente alto para alcanzar la zona de saturación de $f$.  
   - Los demás tienen menos incentivo a cooperar en ese periodo, pues "ganan" la misma calificación pero disfrutan de más horas de ocio.

3. **Alternancia de quién hace el esfuerzo**  
   - Si la repetición es finita y no hay castigos, la alternancia coordinada (un jugador "se sacrifica" en un periodo, otro lo hace en el siguiente) puede ser **difícil de sostener** sin acuerdos explícitos.  
   - Cada uno podría pensar: "Si yo no me esfuerzo, quizás otro suba su esfuerzo para no perder calificación global".  

4. **Resultado posible**  
   - En un **equilibrio** no cooperativo, a veces se observa que un único jugador se *especializa* voluntaria o involuntariamente en mantener la calificación, mientras otros se aprovechan.  
   - Desde la perspectiva del jugador que "carga" con el trabajo, en teoría debería tener incentivos a no seguir haciéndolo, pero si todos lo dejan de hacer, la calificación baja notablemente, y quizás ese jugador la valora más (por reputación, urgencia, etc.).

> **Conclusión**:  
> Este escenario ilustra cómo la combinación de **calificación de respuesta rápida** (fácil de saturar) y **valoración lineal del ocio** puede llevar a conductas de "especialización extrema" en las horas de trabajo. En el mejor de los casos, se podrían turnar, pero sin sanciones creíbles ni acuerdos, suele desembocar en desequilibrios donde pocos hacen el grueso y los demás se benefician.

---

## 3. Escenario 2: Rendimientos decrecientes del ocio

Ahora **modificamos** la utilidad respecto al ocio: en lugar de ser lineal, suponemos que cada jugador valora el ocio con **rendimientos marginales decrecientes**. Por ejemplo, la utilidad por ocio en cada periodo $t$ podría modelarse como:
$
  u_{\text{ocio}}(h_{e,t}) \;=\; g\bigl(W - h_{e,t}\bigr),
$
donde $g(\cdot)$ es una función cóncava y creciente (e.g., $g(x) = \beta \sqrt{x}$, $g(x)=\ln(1+x)$, etc.). Así, las **primeras horas** de ocio son más valiosas que las últimas.

1. **Intuición**  
   - Con rendimientos decrecientes, un jugador que ya tiene "mucho ocio" en un periodo adicional no gana tanto extra por robar más horas libres.  
   - Por lo tanto, colaborar un poco más (poner algo de esfuerzo adicional) no sacrifica tanto bienestar, especialmente si se logra una calificación **(más alta)**.

2. **Efecto en la cooperación**  
   - Es más **fácil** sostener acuerdos cooperativos porque el **costo marginal** de perder algo de ocio no es tan alto cuando ya tienes un nivel moderado de ocio.  
   - Se reduce el incentivo a hacer "cero" esfuerzo, ya que las ganancias de ocio adicionales podrían ser relativamente pequeñas en valor marginal.

3. **Equilibrio no cooperativo**  
   - Aun así, puede existir comportamiento de free-riding, pero la aversión a perder la calificación (que también puede tener un rendimiento creciente al principio) y el hecho de que la utilidad del ocio no escala linealmente pueden acercar un poco más el resultado no cooperativo al cooperativo.

> **Conclusión**:  
> Las **preferencias no lineales** (en el ocio) modifican la estructura de incentivos, haciéndola **menos** propensa a desequilibrios extremos (una sola persona cargando) y acercándola más a un equilibrio con **repartición** del esfuerzo.

---

## 4. Escenario 3: Diferentes valoraciones de la calificación

En muchos equipos, no todos valoran igual la nota final. Por ejemplo, algunos estudiantes necesitan cierto promedio para mantener una beca. Podemos representarlo asignando un **peso** distinto $\alpha_e$ a la parte de la utilidad que proviene de la calificación:
$
  U_e 
  \;=\; \alpha_e \cdot \frac{1}{T} \sum_{t=1}^T f\Bigl(\sum_{i=1}^E h_{i,t}\Bigr) 
       + \sum_{t=1}^T g_e\bigl(W - h_{e,t}\bigr).
$
- Aquí $\alpha_e > 0$ indica cuán **sensible** es el jugador $e$ a la calificación.  
- La función $g_e(\cdot)$ modela la utilidad del ocio, que puede ser lineal o con rendimientos decrecientes. (Incluso podría variar entre jugadores).

### 4.1. Impacto en la decisión

- Un estudiante con $\alpha_e$ **grande** (por ejemplo, por necesitar beca) estará dispuesto a **sacrificar** más ocio para asegurar una calificación alta.  
- Otro con $\alpha_e$ **pequeño** (no le importa tanto la nota) tenderá a reducir su esfuerzo, confiando en que el primero "no querrá bajar la calificación".

### 4.2. Riesgo de explotación

- El escenario se presta a que los de $\alpha_e$ alto se **sobre-esfuercen**, mientras que los de $\alpha_e$ bajo se **aprovechen** de ello.  
- En un **juego repetido**, el estudiante que valora mucho la calificación puede intentar amenazar con reducir su esfuerzo si los demás se aprovechan; pero si su propia necesidad de calificación es tan alta, esa amenaza puede no ser creíble.

> **Conclusión**:  
> Con diferentes valoraciones de la calificación, surge un **desequilibrio** interno: quienes más necesitan la nota suelen trabajar más. Ello hace que la cooperación "justa" sea difícil de sostener a menos que existan mecanismos que fuercen a los demás a poner un mínimo esfuerzo.

---

## 5. Escenario 4: Diferentes rendimientos del esfuerzo en la calificación

Por último, consideremos el caso en el que el **esfuerzo de cada persona no contribuye de la misma manera** a la calificación grupal. Esto puede deberse a:
- Diferencias de conocimiento o habilidad.  
- Diferente calidad del tiempo invertido (cansancio, concentración).  
- Asignación de tareas específicas (alguien se ocupa de la parte "dura" y otro de la parte "menor").  

Una manera de modelarlo es redefinir la calificación en cada periodo $t$ como:
$
  G_t = f\Bigl(\sum_{e=1}^E \omega_e \, h_{e,t}\Bigr),
$
donde $\omega_e$ es la **productividad** o el factor de contribución de cada jugador $e$. Así, **una hora** de la persona $e$ puede equivaler a varias horas de otra (si $\omega_e$ es grande).

### 5.1. Efecto en la cooperación

- Si un jugador tiene $\omega_e$ **muy alto**, su esfuerzo aumenta la calificación más que el de los otros.  
- Los demás podrían volverse dependientes de su aporte, quedándose en la parte baja de esfuerzo (free-riding).  
- A su vez, si ese jugador de alta productividad no valora tanto la calificación (o está cansado), también puede negarse a poner más esfuerzo.

### 5.2. Combinado con valoración distinta

- Si la persona con $\omega_e$ grande **además** valora la nota ($\alpha_e$ alto), es probable que tome casi todo el trabajo.  
- Si la persona con $\omega_e$ grande valora poco la nota ($\alpha_e$ bajo), entonces no hay incentivos a que se "sacrifique", y la calificación grupal puede descender notablemente a menos que otros compensen (aunque su $\omega$ sea menor).

> **Conclusión**:  
> Cuando el **esfuerzo** de cada uno no produce el mismo impacto, se acentúa el problema de free-riding y la complejidad de sostener acuerdos cooperativos. El jugador con alta $\omega_e$ se vuelve un objetivo de presión por parte de los demás para que "lidere" el trabajo, lo que a menudo no es estable sin un mecanismo de compensación o sanción.

---

## 6. Reflexiones finales

- **No cooperación vs. cooperación**:  
  En todos los escenarios (linealidad, rendimientos decrecientes del ocio, distintas valoraciones de la calificación y productividades diferenciadas), la tendencia a la no cooperación **empeora** los resultados colectivos respecto a una asignación cooperativa **óptima**.

- **Repetición y credibilidad**:  
  En un **juego repetido**, la posibilidad de "premiar" esfuerzos pasados o "castigar" conductas de free-rider en periodos futuros puede sostener niveles más altos de cooperación (especialmente si hay muchos periodos $T$ o si hay factores de reputación). Sin embargo, cada escenario introduce fricciones y desequilibrios nuevos.

- **Diseño institucional**:  
  En la práctica, las **instituciones** (por ejemplo, evaluación individual, seguimiento, control de aportes) pueden modificar drásticamente los incentivos. Si el profesor "penaliza" a quienes no trabajan o si la calificación final depende parcialmente de la contribución individual, el free-riding puede reducirse.

- **Heterogeneidad**:  
  La heterogeneidad en la valoración de la nota ($\alpha_e$) o en la productividad ($\omega_e$) puede hacer que ciertos jugadores asuman desproporcionadamente la carga de trabajo, lo cual **no** siempre es socialmente eficiente o justo, y además puede desembocar en tensiones y rupturas en la cooperación.

En suma, estos **cuatro escenarios** ilustran cómo pequeñas modificaciones en el modelo original generan respuestas e incentivos distintos, destacando la complejidad real de la toma de decisiones en equipos. El objetivo de esta construcción formal es **comprender** mejor por qué surgen comportamientos de "carreo" o free-rider, así como proponer mecanismos que fomenten la cooperación y eviten los conflictos de reparto de esfuerzo.
