

## 1. Introducción

En el documento previo, hablamos de los **juegos repetidos** y vimos cómo la repetición de un juego base (o *stage game*) puede cambiar radicalmente la forma en que los jugadores se comportan a lo largo del tiempo. También introdujimos la idea de que una estrategia en un juego repetido está definida en función del **historial**.

En este nuevo documento profundizaremos en cómo se definen los **equilibrios** (tanto en estrategias **puras** como **mixtas**) cuando el juego se repite, ya sea de manera **finita** o **indefinida**. El objetivo es entender, con un enfoque matemático, qué significa que un perfil de estrategias sea un **equilibrio de Nash** en un juego repetido y, en particular, qué lo distingue de un equilibrio en un juego de una sola etapa.

---

## 2. Definiciones básicas

### 2.1 Juego repetido

Recordemos que partimos de un **juego base**:
$G = \bigl(N,\{A_i\}_{i\in N}, \{u_i\}_{i\in N}\bigr),$
- $N$: conjunto de jugadores, $N = \{1,2,\dots,n\}$.
- $A_i$: conjunto de acciones (puras) del jugador $i$.
- $u_i: A_1 \times \cdots \times A_n \to \mathbb{R}$: función de utilidad (o pago) de cada jugador.

El **juego repetido** $G^T$ se define cuando este juego base se juega en cada una de las $T$ etapas (rondas) de forma secuencial. Cuando $T$ tiende a infinito o la repetición es indefinida, hablamos de $G^\infty$.

### 2.2 Historias y estrategias en un juego repetido

- La **historia** en la etapa $t$ (denotada $h^{t-1}$) especifica las acciones jugadas por todos los jugadores en las rondas anteriores $1,2,\dots, t-1$.
- Una **estrategia** para el jugador $i$ en el juego repetido es una regla que, dada la historia, asigna a cada historia un **conjunto de probabilidades** (en el caso de estrategia mixta) o una **acción específica** (en el caso de estrategia pura) que el jugador elige en la ronda presente.

Formalmente, si definimos el espacio de historias posibles hasta la ronda $t$ como $H^{t-1}$, entonces:
- Una **estrategia pura** de jugador $i$, $\sigma_i$, es una función:
  $\sigma_i : \bigcup_{t=1}^{T} H^{t-1} \; \to \; A_i,$
  que indica qué acción (determinística) tomar dada la historia.
- Una **estrategia mixta** de jugador $i$, $\sigma_i$, es una función:
  $\sigma_i : \bigcup_{t=1}^{T} H^{t-1} \; \to \; \Delta(A_i),$
  donde $\Delta(A_i)$ es el conjunto de **distribuciones de probabilidad** sobre $A_i$. Esto indica qué **probabilidad** asigna a cada acción en $A_i$ dada la historia.

> Nótese que la distinción entre puras y mixtas en un juego repetido es simplemente que en puras se elige una sola acción (sin aleatoriedad en cada historia), mientras que en mixtas se elige un *vector de probabilidades* sobre acciones.

### 2.3 Pago total con factor de descuento

Como vimos, el **pago total** del jugador $i$ se suele modelar con un factor de descuento $\delta \in (0,1]$. Si denotamos la acción del jugador $i$ en la ronda $t$ por $a_i^t$, su utilidad en la ronda $t$ por $u_i(a_i^t, a_{-i}^t)$ y si el juego tiene un horizonte infinito, el pago esperado de la estrategia de equilibrio $\Sigma = (\sigma_1, \dots, \sigma_n)$ para $i$ es:
$U_i(\Sigma) \;=\; \sum_{t=1}^{\infty} \delta^{\,t-1} \,\mathbb{E}\bigl[u_i(a_i^t, a_{-i}^t)\bigr].$
Para el caso finito $T$, se reemplaza el $\infty$ por $T$.

---

## 3. Equilibrio de Nash en el juego repetido

Un **perfil de estrategias** $\Sigma^* = (\sigma_1^*, \dots, \sigma_n^*)$ es un **Equilibrio de Nash** en el juego repetido si para cada jugador $i$, dada la estrategia de los demás jugadores $\sigma_{-i}^*$, no existe una estrategia $\sigma_i'$ tal que el jugador $i$ obtenga un **pago total** mayor. En notación:
$U_i(\sigma_i^*, \sigma_{-i}^*) \;\ge\; U_i(\sigma_i', \sigma_{-i}^*), 
\quad \text{para todo } i \in N \text{ y para toda estrategia } \sigma_i'.$

### 3.1 Equilibrio en estrategias puras

Cuando el perfil $\Sigma^*$ es tal que **cada** $\sigma_i^*$ escoge acciones determinísticas (puras) en cada etapa (dependiendo de la historia), hablamos de un **equilibrio en estrategias puras**.

**Ejemplo**:  
- En el *Dilema del Prisionero* repetido (con horizonte infinito y factor de descuento $\delta$), la *Estrategia de Castigo Eterno* ("Disparo" o "Grim Trigger") que indica:
  - *Coopera* mientras todos hayan cooperado en el pasado.
  - *Defecta* para siempre en cuanto el oponente *defecte* una vez.
  
  puede formar parte de un **equilibrio** *siempre y cuando* $\delta$ sea suficientemente grande para que la amenaza del castigo sea creíble. Esto se explora formalmente con la condición de que el costo de ser castigado en el futuro sea mayor que el beneficio inmediato de desviarse (defectar). Aunque este tipo de estrategia se suele analizar en el marco de Equilibrio Perfecto en Subjuegos, es un buen ejemplo intuitivo para mostrar la lógica de un equilibrio puro en juegos repetidos.

### 3.2 Equilibrio en estrategias mixtas

Análogamente, hay perfiles de estrategias donde $\sigma_i^*$ asigna *probabilidades* a las acciones en cada historia. Para que esto sea un **Equilibrio de Nash en estrategias mixtas**:
- Dado que los demás jugadores usan $\sigma_{-i}^*$, el jugador $i$ no puede aumentar su **pago total** cambiando la distribución de probabilidades que asigna a sus acciones en ninguna etapa, ni en ninguna historia.

En otras palabras, si uno de los jugadores, observando lo que ha pasado, decide cambiar su regla de elección de acciones futuras (sus distribuciones de probabilidad), esto no debería reportarle **mayor** utilidad total esperada, *dado* que el resto no cambia sus estrategias.

> **Recordatorio**: Este concepto generaliza la idea de "no tener incentivos a desviar" del Equilibrio de Nash de una sola ronda, pero aquí se aplica sobre secuencias de acciones (o distribuciones de acciones) que dependen de la historia.

---

## 4. Formulación matemática del problema de optimización

Para profundizar en el aspecto matemático, veamos cómo se formula el problema de optimización de un jugador $i$ que considera cambiar su estrategia:

1. **Perfil de estrategias**: $\Sigma = (\sigma_1, \ldots, \sigma_n)$.  
2. **Pago esperado** para $i$: 
   $U_i(\Sigma) \;=\; \sum_{t=1}^{T}\delta^{t-1}\;\mathbb{E}\!\Bigl[u_i(a_i^t,\,a_{-i}^t)\Bigr],$
   donde la expectativa $\mathbb{E}[\cdot]$ se toma sobre la aleatoriedad (si la hubiera) de las estrategias mixtas y, en caso de horizonte infinito, $T\to\infty$.

3. **Desviación unilateral**: sea $\sigma_i'$ una estrategia (pura o mixta) diferente a $\sigma_i$. La utilidad para $i$ al usar $\sigma_i'$ mientras los demás usan $\sigma_{-i}$ es:
   $U_i(\sigma_i', \sigma_{-i}).$

4. **Condición de equilibrio de Nash**: $\Sigma^*$ es equilibrio si para todo $i\in N$,
   $U_i(\sigma_i^*, \sigma_{-i}^*) \;\ge\; U_i(\sigma_i', \sigma_{-i}^*) 
     \quad \forall \sigma_i'.$

El **desafío** con los juegos repetidos es que cada $\sigma_i$ es mucho más complejo que en los juegos de una sola etapa, pues depende de *todas* las historias posibles.

---

## 5. Caso especial: horizonte finito vs. horizonte infinito

### 5.1 Horizonte finito

Cuando $T$ es **finito**, existe la noción de **análisis hacia atrás** ("backward induction"). En la última etapa $T$, los jugadores no tienen castigos o recompensas futuros, así que su comportamiento en la etapa final es como el de un juego de una sola jugada. Luego, retrocediendo a la etapa $T-1$, sabiendo cómo actuarán en $T$, etc., uno resuelve el juego completamente por inducción hacia atrás.

- En muchos casos (como en el Dilema del Prisionero finito), esto lleva a la predicción de que **todos defectan** en todas las etapas, porque la cooperación en la última etapa no se sostiene, y sabiendo que la última etapa no habrá cooperación, la penúltima tampoco, y así sucesivamente.

### 5.2 Horizonte infinito o indefinido

Cuando $T \to \infty$ (o la terminación del juego en cada ronda sigue una probabilidad $p$), la lógica de backward induction no aplica, y surgen múltiples equilibrios. Por ejemplo, en el Dilema del Prisionero repetido **indefinidamente**, la estrategia de **cooperar** mientras el otro coopere (y castigar si el otro falla) puede sostener la cooperación mutua, dependiendo de la magnitud de $\delta$. Este es el fundamento de muchos resultados (por ejemplo, el conocido "Folk Theorem" para juegos repetidos, que no abordaremos en detalle aquí).

---

## 6. Ejemplo matemático sencillo: Perfil de estrategias mixtas en un Dilema del Prisionero repetido

Imaginemos que en cada ronda los jugadores **pueden** escoger probabilísticamente entre *cooperar (C)* o *defectar (D)*, pero condicionan su probabilidad de cooperar a lo que ocurrió en rondas pasadas.

**Estrategia mixta ejemplo**:  
- Jugador $i$ cooperará con probabilidad $p^t$ en la ronda $t$, donde
  $p^t = 
    \begin{cases}
      \alpha & \text{si todos han cooperado en las últimas \(k\) rondas},\\
      \beta  & \text{en caso contrario}.
    \end{cases}$
  con $0 \le \beta \le \alpha \le 1$.

En este caso, la utilidad esperada del jugador $i$ se calcula considerando la probabilidad con que el otro (u otros) cooperan o defectan en cada ronda, y se acumula a través de $\delta^{t-1}$. Para ver si es **equilibrio**, se verifica si un jugador al modificar $\alpha$ o $\beta$ unilateralmente (o su regla de transición) incrementa su utilidad esperada.

Este tipo de análisis puede llegar a ser complejo, pero la idea es la misma:  
$\max_{\sigma_i'} \quad U_i(\sigma_i', \sigma_{-i}^*) 
\quad \text{sujeto a } \sigma_i' \in \Delta(A_i \times \dots \times A_i),$
y $\sigma_i'(\cdot \mid h^{t-1})$ describe la asignación de probabilidades según la historia.

---

## 7. Conclusiones y puntos clave

1. **Los equilibrios en juegos repetidos** (puras o mixtas) se definen análogamente a como se define un Equilibrio de Nash en un juego estático de una sola etapa; pero ahora las estrategias dependen de **todo el historial** y el pago es la **suma (descontada o no) de utilidades** a lo largo de varias rondas.
   
2. **Horizonte finito vs. infinito**:
   - En finito, usualmente la predicción (mediante backward induction) lleva a comportamientos "miopes" en la última etapa, influyendo a las anteriores.
   - En infinito o indefinido, surgen **múltiples** equilibrios y la posibilidad de sostener la cooperación (como en el Dilema del Prisionero repetido) siempre que $\delta$ sea suficientemente alto.
   
3. **Estrategias puras vs. mixtas**:
   - Puras: asignan una **acción única** dada la historia.
   - Mixtas: asignan una **distribución de probabilidad** sobre acciones dada la historia.
   - En ambos casos, la condición de equilibrio implica que ningún jugador se puede desviar unilateralmente para mejorar su **pago total esperado**.

4. **Aspecto técnico**: Para verificar un equilibrio en un juego repetido, se necesitan:
   - Describir formalmente las estrategias como funciones de historia.
   - Calcular (o estimar) la utilidad total esperada.
   - Demostrar (por un argumento de optimización) que ningún jugador gana al desviarse unilateralmente.

5. **Ejemplos clásicos**: Dilema del Prisionero repetido, juegos de coordinación repetidos, competencia de precios repetida (modelos tipo Bertrand/ Cournot repetidos), etc.

---

## Referencias para profundizar

- *Friedman, J.* (1971). "A Non-cooperative Equilibrium for Supergames." *The Review of Economic Studies*.
- *Osborne, M. J., & Rubinstein, A.* (1994). *A Course in Game Theory* (Cap. 8, "Repeated Games").
- *Tirole, J.* (1988). *The Theory of Industrial Organization* (capítulos sobre colusión en mercados repetidos).

---

