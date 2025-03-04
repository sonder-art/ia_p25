
## 1\. Breve definición del juego

Antes de hablar de *juegos repetidos*, recordemos qué es un *juego* en términos de teoría de juegos. Un juego, en este contexto, es una situación de decisión estratégica donde varios jugadores (o agentes) toman acciones, y la combinación de estas acciones determina un resultado, el cual típicamente otorga una utilidad (ganancia, costo, preferencia, etc.) a cada jugador. Como ya sabes, cada jugador escoge su estrategia (pura o mixta) para maximizar su beneficio esperado.

En un **juego repetido**, la misma situación de decisión (el mismo juego base o *stage game*) se juega múltiples veces de manera secuencial o indefinida. Esto significa que cada jugador puede tener en cuenta lo que sucedió en rondas (o etapas) anteriores para decidir su estrategia en la ronda presente o futura.

---

## 2\. ¿Qué son los juegos repetidos? (Explicación platicada)

Imagina que tienes un juego sencillo, por ejemplo, el famoso *Dilema del Prisionero*. Normalmente, se plantea como un juego de una sola ronda: ambos prisioneros deciden **confesar (defectar)** o **guardar silencio (cooperar)** sin posibilidad de comunicarse. En esa versión de "una sola jugada", sabemos que *confesar* suele ser la estrategia dominante para ambos, y por lo tanto terminan en un resultado no tan deseable.

Ahora bien, en la vida real, a veces estos encuentros no ocurren solo una vez, sino que pueden repetirse varias veces. Por ejemplo, dos competidores en un mercado se enfrentan a la decisión de fijar precios altos o bajar el precio (para ganar clientes) ¡todos los días! Este comportamiento repetido cambia por completo el panorama, ya que ahora cada competidor (o prisionero, en el caso de la versión clásica) **puede "premiar o castigar"** a su rival dependiendo de las decisiones pasadas.

Así que cuando repetimos el mismo juego varias veces, de forma finita o incluso de forma indefinida, las estrategias posibles se vuelven mucho más ricas. El historial de jugadas pasadas influye en las decisiones futuras, y eso permite que los jugadores puedan cooperar o darse mutuamente incentivos para salirse de la estrategia dominante "egoísta".

---

## 3\. Una visión intuitiva de los juegos repetidos

Desde un punto de vista **intuitivo**, la repetición del juego introduce **confianza y reputación**. Si sabes que vas a ver a la misma persona (o empresa, o rival) muchas veces más, probablemente no quieras "quemar puentes" a la primera oportunidad. Preferirías, por ejemplo, *cooperar* en vez de *defectar*, siempre que veas que la otra parte también coopera y "se porta bien".

Algunos comportamientos que se pueden observar intuitivamente en juegos repetidos son:

1. **Estrategias de disparo ("trigger strategies")**: Donde el jugador castiga a otro si *detecta* que éste le traiciona en alguna ronda. Ese castigo puede durar una sola ronda o mantenerse en el tiempo.
2. **Estrategias de perdón ("tit-for-tat")**: Donde el jugador imita en la siguiente ronda la acción del otro en la ronda previa; por ejemplo, colaboro si colaboraste, y te castigo (no colaboro) si me traicionaste.
3. **Estabilización de la cooperación**: Dado que hay repetición, puede que a ambos jugadores les convenga cooperar (aunque no sea lo que la estrategia dominante sugeriría en una sola jugada) para obtener mayores beneficios a lo largo de todas las etapas.

Estas situaciones surgen porque la "repetición" crea una **dependencia temporal** en la que el comportamiento presente de cada jugador afecta las expectativas del comportamiento futuro del otro.

---

## 4\. Descripción formal de un juego repetido

Veámoslo **un poco** más formalmente (aunque sin entrar a los teoremas avanzados):

1. **Juego base o stage game**:  
   - Se especifica como $(N, \{A_i\}_{i \in N}, \{u_i\}_{i \in N})$,  
     donde $N$ es el conjunto de jugadores, $A_i$ es el conjunto de acciones del jugador $i$, y $u_i$ es la función de utilidad de $i$.

2. **Horizonte de tiempo**:  
   - El juego se repite a lo largo de $T$ etapas (rondas).  
   - Si $T$ es finito, significa que habrá una última ronda.  
   - Si $T$ es infinito (o incierto, con probabilidad de continuar en cada ronda), hablamos de juegos repetidos con horizonte infinito.

3. **Historia e información**:  
   - En la ronda $t$, cada jugador $i$ observa (total o parcialmente) las acciones elegidas en las rondas anteriores y decide su acción $a_i^t$.  
   - La historia hasta la ronda $t$ puede denotarse como $h^{t-1} = ( (a_1^1, \dots, a_n^1), (a_1^2, \dots, a_n^2), \dots, (a_1^{t-1}, \dots, a_n^{t-1}) )$.

4. **Estrategia de un jugador**:
   - Una estrategia en un juego repetido no es solo escoger una acción en cada ronda de manera aislada; sino que es una *regla* que indica qué acción escoger dado el historial.  
   - Formalmente, $\sigma_i$ es una función de las historias pasadas a las acciones presentes y futuras: $\sigma_i: H \to A_i$, donde $H$ es el conjunto de todas las posibles historias.

5. **Pago total o payoff acumulado**:  
   - Se suele definir como la suma (o el valor presente descontado) de las utilidades obtenidas en cada ronda:  
     $U_i(\sigma_1, \ldots, \sigma_n) \;=\; \sum_{t=1}^{T} \delta^{t-1} u_i(a_i^t, a_{-i}^t)$,
     donde $0 < \delta \le 1$ es un factor de descuento (representa la paciencia o preferencia por el presente vs. el futuro).

En resumen, lo importante aquí es que la **estrategia** en un juego repetido depende del *historial*, y el **pago** se acumula (o se descuenta) a lo largo de todas las rondas.

---

## 5\. Ejemplo: Dilema del Prisionero repetido

Para ilustrarlo, tomemos el **Dilema del Prisionero (DP)**, que ustedes ya conocen. Recordemos la matriz de pagos simplificada (en una única jugada) para dos jugadores, $A$ y $B$, donde cada uno puede **Cooperar (C)** o **Defectar (D)**:

|                  | B coopera (C)  | B defecta (D)   |
|------------------|----------------|-----------------|
| **A coopera (C)** | (3,3)          | (1,4)           |
| **A defeca (D)**  | (4,1)          | (2,2)           |

En la versión de *juego de una sola jugada*, la estrategia dominante para ambos es *Defectar (D)*, lo que lleva al resultado $(2,2)$.

### 5.1 Dilema del Prisionero repetido en múltiples rondas

Supongamos que este juego se repite, por ejemplo, un número indeterminado de veces (con alguna probabilidad de terminar en cada ronda). Ahora ambos jugadores pueden idear estrategias que premien la cooperación mutua y castiguen la traición.

- **Estrategia Tit-for-Tat (TFT)**  
  Una de las estrategias más famosas y simples. Consiste en:
  1. En la **primera** ronda, **coopera**.  
  2. En cada ronda siguiente, **haz lo que tu oponente hizo en la ronda anterior**:  
     - Si tu oponente cooperó, tú cooperas.  
     - Si tu oponente defectó, tú defectas en la siguiente ronda.

Esta estrategia promueve la cooperación siempre y cuando el oponente coopere, pero también "castiga" inmediatamente si detecta una traición. En muchos experimentos y simulaciones, se ha visto que Tit-for-Tat fomenta y estabiliza la cooperación, al menos mientras los jugadores valoren lo suficiente el futuro (es decir, $\delta$ es suficientemente grande).

### 5.2 Por qué cambia la situación

En el Dilema del Prisionero de una sola jugada, cada uno quiere traicionar para maximizar su utilidad individual inmediata. Pero en la versión repetida, **traicionar** puede tener consecuencias negativas en rondas futuras (el oponente puede responder defendiéndose o dejando de cooperar), por lo que la amenaza de perder futuros pagos hace más atractivo cooperar.

**En otras palabras**, gracias a la repetición, se abren posibilidades de castigo y recompensa, lo que puede mantener la cooperación como una estrategia posible y *a veces* deseable desde un punto de vista de beneficio global y hasta individual (cuando el factor de descuento, la probabilidad de continuidad y otras condiciones lo permiten).

---

## 6\. Reflexión final

Los juegos repetidos son fundamentales para entender muchos fenómenos en la realidad: desde la fijación de precios en mercados, la formación de alianzas políticas, hasta la manera en que colaboramos en la vida cotidiana. A diferencia de un juego de una sola jugada, un juego repetido introduce la dinámica de la memoria y la reputación, lo que hace que el concepto de *equilibrio* sea más amplio e interesante (por ejemplo, en términos de *Equilibrio Perfecto en Subjuegos*, aunque no profundicemos en eso todavía).

Así, el aspecto clave para "resolver" (o comprender) juegos repetidos es ver cómo el historial de decisiones afecta las estrategias en el futuro, y cómo la posibilidad de castigo o recompensa puede llevar a resultados diferentes a los que se observarían en un solo encuentro.
