
## 1. Introducción

Hasta ahora hemos discutido:

1. **Qué son los juegos repetidos** y por qué el historial y las estrategias condicionadas son importantes.  
2. **Qué significa un equilibrio** en estrategias puras y mixtas para juegos repetidos, tanto en horizonte finito como infinito.

En este documento nos enfocaremos en:

- **Cómo "resolver"** (o caracterizar equilibria) en juegos repetidos de manera **formal** (matemática) en términos generales.  
- Aplicar dichos métodos a un **ejemplo concreto**: el *Dilema del Prisionero repetido*.  
- Distinguir las diferencias clave en la resolución cuando el horizonte es **finito** versus **infinito**.

---

## 2. Método de resolución (en términos generales)

### 2.1 Horizonte finito: Inducción hacia atrás

Para un **juego repetido finito** con $T$ etapas, uno de los métodos estándar para caracterizar los equilibrios es la **inducción hacia atrás** (*backward induction*). Este procedimiento se fundamenta en la idea de resolver primero la **última** etapa, luego la penúltima, etc., hasta llegar a la primera.

1. **Definir el juego base** $(N, \{A_i\}, \{u_i\})$.  
2. **Empezar en la etapa $T$** (la última).  
   - Como no hay consecuencias futuras (no hay más etapas luego de la $T$), cada jugador resuelve su **juego de una sola ronda** para la etapa final. 
   - Se determina el conjunto de **equilibrios de Nash** (puro o mixto) para esa ronda $T$.
3. **Retroceder a la etapa $T-1$**:  
   - Sabiendo cómo se comportarán los jugadores en la etapa $T$, cada jugador ajusta su decisión en la etapa $T-1$.  
   - Nuevamente se busca un equilibrio de Nash, pero esta vez incorporando las ganancias de la jugada $T-1$ *más* la utilidad en la etapa $T$. 
4. **Repetir el proceso hasta la primera etapa**.

Finalmente, lo que se obtiene es un **Equilibrio Perfecto en Subjuegos** (o al menos un Equilibrio de Nash) que cubre todas las etapas desde la 1 hasta la $T$. Formalmente, esto significa que en cada "subjuego" (cada etapa, dada la historia anterior) la estrategia constituye un equilibrio de Nash.

#### Representación matemática (simplificada)

Sea $\sigma = (\sigma_1,\dots,\sigma_n)$ un perfil de estrategias para las $T$ etapas. Definimos la utilidad total con (posible) factor de descuento $\delta$:

$U_i(\sigma) = \sum_{t=1}^{T} \delta^{t-1} \, \mathbb{E}[u_i(a_i^t, a_{-i}^t)]$

Donde $(a_i^t, a_{-i}^t)$ son las acciones (puras o mixtas) elegidas en la etapa $t$ según $\sigma$. Para que $\sigma$ sea un **equilibrio** (perfecto en subjuegos, en la versión más fuerte), debe no haber incentivos a desviarse *en ninguna* subetapa, dado lo que se anticipa suceder en las etapas posteriores.

El proceso de inducción hacia atrás hace que en la práctica sea frecuente (para ciertos juegos) que, en la última ronda, aparezca el **equilibrio de la etapa estática** "desconectado" de cualquier castigo o recompensa futuro, y ello "contamine" las rondas previas, imposibilitando la cooperación (como pasa en el Dilema del Prisionero finito).

---

### 2.2 Horizonte infinito: argumentos de amenazas y recompensas

Cuando el horizonte es **infinito** (o indefinido, con probabilidad de continuar en cada etapa), la inducción hacia atrás no aplica directamente porque no hay una "última" etapa. En este caso, la forma típica de análisis pasa por:

1. **Suponer o proponer** una *estructura* de estrategias (por ejemplo, "cooperar mientras el otro coopere, y castigar si el otro no coopera").  
2. Verificar formalmente la **condición de no desviación**: que, dado el comportamiento de los demás, un jugador *no ganaría* al desviarse en ningún punto. Esto se expresa matemáticamente revisando la **condición de incentivo**:

   $U_i(\sigma_i^*, \sigma_{-i}^*) \geq U_i(\sigma_i', \sigma_{-i}^*), \quad \forall i,\; \forall \sigma_i'$

3. Generalmente, se traduce en **desigualdades** que comparan la ganancia inmediata por desviarse frente a la pérdida futura debida a castigos o ruptura de cooperación.

#### Representación matemática (con factor de descuento)

Para horizontes infinitos, el pago de un jugador $i$ con factor de descuento $\delta \in (0,1)$ se expresa como:

$U_i(\sigma) = \sum_{t=1}^{\infty} \delta^{t-1} \, \mathbb{E}[u_i(a_i^t,a_{-i}^t)]$

En un **equilibrio** $\sigma^*$, ningún jugador puede encontrar una estrategia $\sigma_i'$ que le otorgue un mayor valor esperado *teniendo en cuenta* todas las futuras reacciones y pagos.

> El **Folk Theorem** (que no profundizamos en detalle) explica que, bajo ciertas condiciones, en un juego repetido con horizonte infinito pueden sostenerse en equilibrio multitud de resultados, incluyendo cooperar o no cooperar, siempre que la **amenaza** de castigo sea lo bastante dura y **los jugadores valoren** suficientemente el futuro (alto $\delta$).

---

## 3. Ejemplo: Dilema del Prisionero repetido

Recordemos la **matriz de pagos** (simplificada) para dos jugadores (A y B):

|                       | B coopera (C) | B defecta (D) |
|-----------------------|---------------|---------------|
| **A coopera (C)**     | (3, 3)        | (1, 4)        |
| **A  defecta (D)**    | (4, 1)        | (2, 2)        |

La estrategia dominante en una sola ronda es *Defectar (D)*. Esto conduce en equilibrio estático a $(D, D)$ con pagos $(2, 2)$.

### 3.1 Caso Finito

Sea $T$ el número de repeticiones. Utilizaremos **inducción hacia atrás**:

1. **Etapa $T$**:  
   - Al estar en la última ronda, no hay sanciones o recompensas futuras.  
   - Cada jugador razona como en el juego de una sola etapa: **defectar** es la estrategia dominante.  
   - Por tanto, el resultado en $t = T$ es $(D, D)$.

2. **Etapa $T-1$**:  
   - Cada jugador *sabe* que, independientemente de lo que haga en $T-1$, **la otra parte** defectará en $T$. Por ello, en $T-1$ no existe un "premio" a cooperar en la última ronda (porque no se va a "recibir" cooperación en $T$).  
   - Entonces, en $T-1$, la tentación inmediata a defection (D) también domina.  
   - Resultado en $t = T-1$: $(D, D)$.

3. **Repitiendo esta lógica** hacia atrás para cada etapa $t = T-2, T-3, \dots, 1$:  
   - Todos defectan en todas las etapas.  
   - El equilibrio (perfecto en subjuegos) es: $\sigma_A^*(t)=D, \sigma_B^*(t)=D$ para todo $t \in \{1,\dots,T\}$.

**Conclusión caso finito**:  
La **inducción hacia atrás** concluye que en todas las rondas se juega $(D,D)$. No hay lugar para que la cooperación surja en un **equilibrio perfecto en subjuegos** si el horizonte es conocido y finito.

---

### 3.2 Caso Infinito (o Indefinido)

Ahora consideremos que el juego se repite un número *infinito* de veces, o con probabilidad $p$ de continuar cada ronda y factor de descuento $\delta \approx p$.

#### 3.2.1 Ejemplo de estrategia: Grim Trigger (o castigo eterno)

**Definición**:  
- Cada jugador, en la primera ronda, **coopera**.  
- Mientras ninguno de los dos haya defectado en el pasado, siguen cooperando.  
- Si en algún momento uno de los jugadores defecta, el otro *responde* defectando **para siempre** en las rondas siguientes (castigo eterno).

**Cálculo de la condición de no desviación**:

- Si ambos cooperan cada ronda, el pago para un jugador $i$ es:  
  $U_i(\text{Coop forever}) = \sum_{t=1}^{\infty} \delta^{t-1} \times 3 = 3 \,\frac{1}{1-\delta}$
  (Pues en cada ronda obtiene 3, descontando con $\delta$.)

- Si el jugador $i$ se **desvía** en la ronda 1 (por ejemplo), obtiene:
  - **Ganancia inmediata** en la ronda 1 por defection (D) contra la cooperación (C) del otro: $4$.  
  - **Pero a partir de la ronda 2**, será castigado por el otro defectando, con lo cual ambos terminan en (D, D) con ganancia 2 por ronda. Sin embargo, *jugador $i$* también defecta, así que su pago por cada ronda posterior es 2.  
  - Descontado a partir de la ronda 2, su utilidad total es:
    $U_i(\text{Desvía en }t=1) = 4 + \sum_{t=2}^{\infty} \delta^{t-1}\times 2$
    Simplificando,
    $U_i(\text{Desvía en }t=1) = 4 + 2\delta \sum_{k=0}^{\infty} (\delta)^k = 4 + 2\delta \frac{1}{1-\delta} = 4 + \frac{2\delta}{1-\delta}$

- Para que **no** le convenga desviarse, necesitamos:
  $U_i(\text{Coop forever}) \geq U_i(\text{Desvía en }t=1)$
  Sustituyendo los valores:
  $3\,\frac{1}{1-\delta} \geq 4 + \frac{2\delta}{1-\delta}$
  Multiplicamos ambos lados por $1-\delta$:
  $3 \geq 4(1-\delta) + 2\delta$
  $3 \geq 4 - 4\delta + 2\delta$
  $3 \geq 4 - 2\delta$
  $2\delta \geq 1$
  $\delta \geq \frac{1}{2}$

**Interpretación**:  
Si el **factor de descuento** $\delta \geq 1/2$, es decir, si los jugadores valoran lo suficiente el futuro, la amenaza de castigo eterno es suficiente para que *ningún jugador quiera desviarse*.

> Este argumento puede extenderse a la posibilidad de desviar en rondas posteriores, pero la lógica es análoga; mientras $\delta$ sea grande, la **pérdida futura** por castigo supera la **ganancia inmediata** por desviar.

**Conclusión caso infinito**:  
- **Hay** estrategias (ej.: Grim Trigger, Tit-for-Tat, etc.) que pueden sostener la cooperación en equilibrio si $\delta$ es lo suficientemente alto.  
- La cooperación mutua $(C,C)$ puede ser parte de un **equilibrio** en estrategias puras (de castigo/recompensa) cuando se valora el futuro.  
- A diferencia del caso finito, **no** se fuerza lógicamente a $(D,D)$ en todas las rondas.  
- Además, existen **múltiples** equilibrios posibles, incluidos aquellos donde los jugadores pueden terminar defectando permanentemente o cooperar todo el tiempo, según las estrategias que se adopten.

---

## 4. Resumen y comentarios finales

1. **Resolución formal en finito**:  
   - Se basa en **inducción hacia atrás**.  
   - Para juegos como el Dilema del Prisionero, el resultado típico es **defectan siempre** (en equilibrio perfecto en subjuegos).

2. **Resolución formal en infinito**:  
   - Se basa en analizar condiciones de **no desviación** a largo plazo.  
   - Las *amenazas y recompensas* futuras son cruciales.  
   - Pueden existir múltiples equilibrios, incluyendo la cooperación sostenida, si el factor de descuento $\delta$ excede cierto umbral.  

3. **Dilema del Prisionero repetido**:  
   - Caso finito: la cooperación no se sostiene hasta el final; se llega a $(D,D)$ en todas las rondas (equilibrio perfecto en subjuegos).  
   - Caso infinito: es posible sostener la cooperación si $\delta$ es suficientemente alto, mediante estrategias de "castigo" (Grim Trigger, Tit-for-Tat, etc.).

4. **Importancia práctica**:  
   - Muchos fenómenos económicos y sociales (colusión en precios, acuerdos, alianzas, etc.) se analizan bajo un horizonte **(casi) infinito**, y se explica por qué se puede mantener la cooperación a pesar de que la "trampa" de desviar sea tentadora en una sola jugada.

---

### Conclusión

Hemos mostrado:

- **Cómo** se "resuelven" (o analizan) juegos repetidos formalmente, tanto en un **horizonte finito** (inducción hacia atrás) como en un **horizonte infinito** (condiciones de no desviación y sumas infinitas con descuento).  
- **Aplicación** al Dilema del Prisionero repetido, mostrando las diferencias drásticas de comportamiento en finito (todos defectan) versus infinito (es posible cooperar en equilibrio).  

Este análisis constituye la base de la teoría de juegos repetidos y nos permite comprender cómo la dependencia del **futuro** (capturada en $\delta$) puede cambiar radicalmente los resultados respecto a los de una sola jugada.
