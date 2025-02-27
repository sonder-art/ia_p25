# Teorema de Existencia de Equilibrio de Nash en Estrategias Puras

## 1. Introducción

En la discusión anterior (sobre equilibrios mixtos), vimos que el **Teorema de Nash** garantiza la existencia de (al menos) un **equilibrio de Nash en estrategias mixtas** en cualquier juego finito (suma de jugadores finita, con un número finito de estrategias puras por jugador). Sin embargo, **no** todo juego finito tiene equilibrios en estrategias puras (ejemplo: "Matching Pennies").

Aun así, en muchos problemas económicos, de ingeniería o de coordinación, existe un **interés particular** en la existencia (y cálculo) de **equilibrios en estrategias puras**, pues pueden representar "decisiones deterministas" o "posiciones estables" sin necesidad de mezclar probabilidades. 

La buena noticia es que **sí** hay un **Teorema de Existencia de Equilibrio de Nash en Estrategias Puras**, pero **bajo ciertas condiciones** de continuidad y concavidad (o monotonicidad, etc.). Dichas condiciones se suelen cumplir en muchos modelos de la teoría económica (por ejemplo, en juegos con estrategias continuas y preferencias cuasi-concavas), así como en **juegos potenciales** o **juegos supermodulares**.

En este documento, presentaremos:

1. **Planteamiento y supuesto**: qué condiciones hacen posible garantizar al menos un equilibrio de Nash puro.
2. **Enunciado formal** del teorema.
3. **Intuición** de la demostración y vínculos con el teorema estándar de punto fijo.
4. **Ejemplo ilustrativo**.
5. **Componente computacional y algorítmico**: ideas generales para encontrar (o aproximar) un equilibrio en estrategias puras.

---

## 2. Planteamiento: Juegos con Estrategias Continuas y Payoffs Bien Comportados

El **Teorema de Existencia de Nash en Estrategias Puras** se suele enunciar para:

- Juegos con un número finito de jugadores, $N$.
- Cada jugador $i$ tiene un conjunto de estrategias $S_i \subset \mathbb{R}^k$ (para algún $k$), **no vacío**, **convexo** y **compacto**.
- La función de utilidad (payoff) $u_i : S_1 \times \cdots \times S_N \to \mathbb{R}$ de cada jugador $i$ es:
  1. **Continua** en los vectores de estrategia de **todos** los jugadores.
  2. **Cuasi-concava** (o estrictamente concava) en la estrategia propia $s_i$, manteniendo fijas las estrategias de los demás jugadores.

Bajo estas condiciones (y algunas variantes técnicas), **existe** un equilibrio de Nash **en estrategias puras**. En este contexto, una **estrategia pura** es un vector $s_i$ escogido dentro del conjunto continuo $S_i$.

> **Comentario**:  
> - El teorema clásico de Nash (1950, 1951) asume juegos finitos y prueba la existencia de **equilibrio en mezclas** (estrategias mixtas).  
> - Para **estrategias puras**, hace falta que el juego cumpla propiedades "más suaves" (continuidad, convexidad, cuasi-concavidad, etc.).  
> - En **juegos potenciales** (Monderer & Shapley, 1996) o **juegos supermodulares** (Topkis, 1998), también se garantiza la existencia de un equilibrio puro, incluso si los conjuntos de estrategia no son finitos, siempre que se cumplan ciertas condiciones de isotonicidad o de potencial bien definido.

---

## 3. Enunciado Formal (Versión Simplificada)

**Teorema (Existencia de Equilibrio de Nash en Estrategias Puras, versión cuasi-concava):**  
Sea $G = \bigl(N, \{S_i\}_{i=1}^N, \{u_i\}_{i=1}^N\bigr)$ un juego con:
1. $N$ jugadores.
2. Para cada jugador $i$, $S_i$ es un conjunto **no vacío**, **convexo** y **compacto** en $\mathbb{R}^k$.
3. La función de pago (utilidad) $u_i(s_i, s_{-i})$ es **continua** en $(s_i, s_{-i})$ para cada $i$.
4. Para cada $i$, $u_i$ es cuasi-concava (o estrictamente concava) en $s_i$, manteniendo fijos $s_{-i}$.

Entonces, **existe** al menos un **perfil de estrategias puras** $(s_1^*, \dots, s_N^*)$ tal que, para cada jugador $i$,
$s_i^* \in \arg\max_{s_i \in S_i} \; u_i\bigl(s_i, s_{-i}^*\bigr).$

Es decir, $(s_1^*, \ldots, s_N^*)$ es un **equilibrio de Nash en estrategias puras**.

---

## 4. Intuición de la Demostración

La **idea conceptual** detrás de la prueba se basa en la extensión de los **argumentos de punto fijo** (como el de **Kakutani** o el de **Brouwer**) usados en el teorema de Nash para estrategias mixtas.

- En la versión original para **juegos finitos**, cada jugador elige una **mezcla** (un punto en un **simplejo** de dimensión finita). Luego se define la "correspondencia de mejores respuestas" de cada jugador y se usa el teorema de Kakutani para probar que existe un **punto fijo** de esa correspondencia. Ese punto fijo corresponde a un perfil de estrategias mixtas en equilibrio.
- En la versión para **juegos continuos** con **cuasi-concavidad**:
  1. El conjunto de estrategias ya no es un simplejo finito, sino un conjunto convexo y compacto en $\mathbb{R}^k$.  
  2. Las mejores respuestas en estrategias puras (dado $s_{-i}$) están **bien definidas** (por ejemplo, la maximización de una función cuasi-cóncava sobre un conjunto convexo y compacto tiene soluciones).  
  3. Se define la **correspondencia de mejores respuestas puras** $BR_i$, que asocia a cada perfil de estrategias $(s_1, \dots, s_N)$ la mejor respuesta $s_i^*$ de cada jugador.
  4. Se muestra que esta correspondencia cumple las condiciones (no vacía, convexa, grafo cerrado, etc.) para aplicar de nuevo el **Teorema de Kakutani** y obtener un punto fijo.  
  5. Ese punto fijo $(s_1^*, \dots, s_N^*)$ es, por construcción, un equilibrio de Nash en **estrategias puras**.

En resumen, la **cuasi-concavidad** (o concavidad) y la **compacidad** del conjunto de estrategias permiten garantizar que cada jugador **tiene** al menos una mejor respuesta pura para cada posible configuración del juego, y la aplicación del teorema de punto fijo prueba que existe un "punto" (o perfil) donde todos juegan sus mejores respuestas simultáneamente.

---

## 5. Ejemplo Ilustrativo

### 5.1. Juego de Duopolio de Cournot (con Funciones de Costos y Demanda Simples)

Consideremos un juego económico de **duopolio** (2 jugadores, "empresa 1" y "empresa 2"), donde cada empresa elige **su cantidad de producción** $q_1, q_2 \in [0, \infty)$. Para simplificar, supongamos que:
- $S_1 = S_2 = [0, K]$ para algún $K$ grande (por ejemplo, la capacidad máxima). Este intervalo es **compacto** y **convexo**.  
- La función de demanda de mercado es lineal: $p(Q) = a - b\,Q$, donde $Q = q_1 + q_2$, con $a > 0$ y $b > 0$.
- El costo de producción es $C_i(q_i) = c \, q_i$, constante marginal.

La utilidad (beneficio) para la empresa $i$ es:
$u_i(q_i, q_j) = \bigl[a - b\,(q_i + q_j)\bigr] \cdot q_i \;-\; c\, q_i.$

Si fijamos $q_j$, la empresa $i$ resuelve:
$\max_{q_i \in [0, K]} \;\; (a - b(q_i + q_j))\,q_i \;-\; c\,q_i.$

Esta es una función **cóncava** en $q_i$ (fácil de verificar, ya que es cuadrática con coeficiente negativo en el término $q_i^2$). El conjunto de estrategias es convexo y compacto. Además, la función es continua.

Cumplidas las condiciones, existe un **equilibrio de Nash en estrategias puras** (las cantidades $(q_1^*, q_2^*)$ que satisfacen que cada $q_i^*$ sea la mejor respuesta a $q_j^*$).

De hecho, se puede calcular explícitamente (en la versión sin restricción $K$ grande, y asumiendo no-negatividad) y se obtienen las **cantidades de Cournot**. Eso corresponde a la intersección de las **curvas de reacción** de cada empresa, que son las ecuaciones donde cada una maximiza su utilidad dada la cantidad de la otra.

### 5.2. Verificación de las Condiciones

1. $S_i = [0, K]$ es no vacío, convexo (un intervalo) y compacto (cerrado y acotado).
2. $u_i(q_i, q_j)$ es continua en $(q_i, q_j)$.
3. Dada $q_j$, la función $q_i \mapsto u_i(q_i, q_j)$ es una cuasi-cóncava (de hecho, estrictamente cóncava en un rango) en $q_i$.

Por ello, **el teorema** garantiza la existencia de un equilibrio en estrategias puras (aunque también sabemos que la versión lineal de Cournot se resuelve directamente hallando la intersección de mejores respuestas).

---

## 6. Componente Computacional y Algorítmico

En la **práctica**, aunque el teorema garantiza la **existencia** de un equilibrio puro, encontrarlo puede requerir métodos numéricos. Algunas aproximaciones:

1. **Algoritmos de mejor respuesta iterada (o sucesiva)**:
   - Se parte de un perfil inicial $(s_1^{(0)}, \dots, s_N^{(0)})$.
   - Iterativamente, cada jugador actualiza su estrategia a su **mejor respuesta** frente a la estrategia actual de los demás.
   - En ciertos juegos (por ejemplo, **juegos supermodulares**), este proceso converge a un **equilibrio en estrategias puras**.

2. **Métodos de optimización conjunta** en **juegos potenciales**:
   - Si el juego admite una **función de potencial** $P(s_1, \dots, s_N)$ tal que cada $u_i$ está alineada con $P$, la búsqueda de equilibrio en puras se reduce a encontrar los puntos que maximizan (o hacen estacionario) el potencial.
   - Ejemplo: en algunos juegos de enrutamiento, la minimización de la latencia agregada coincide con encontrar el equilibrio de Nash.

3. **Fictitious play**:
   - Cada jugador asume que los demás juegan estrategias estocásticas basadas en las frecuencias históricas de jugadas.  
   - Se puede demostrar convergencia en ciertos tipos de juegos (p.ej., juegos con una función de utilidad que es cuasi-concava y ciertos supuestos de unicidad de mejor respuesta, o juegos de dos jugadores con ciertas propiedades).

4. **Métodos de punto fijo (Kakutani / Brouwer) en versión computacional**:
   - Existen enfoques de "punto fijo computacional" (por ejemplo, algoritmos homotópicos o de recubrimiento) para aproximar los puntos fijos de la **correspondencia de mejores respuestas**.

En todos estos métodos, la **clave** es que, al cumplir las condiciones del teorema, la **mejor respuesta** de cada jugador siempre existe y es un **conjunto compacto** (a menudo un solo punto si la utilidad es estrictamente cóncava). Así, la iteración o el algoritmo de punto fijo está bien definido en todo momento.

---

## 7. Comentarios Finales

- El **Teorema de Nash** más **conocido** (1950) es el de **existencia de un equilibrio en estrategias mixtas** para juegos finitos.
- El **Teorema de existencia en estrategias puras** se basa en extensiones similares de punto fijo, pero requiere **hipótesis adicionales** de continuidad y cuasi-concavidad/convexidad en los conjuntos de estrategias.  
- En casos como "Matching Pennies", donde las estrategias puras son discretas, el teorema de pureza **no** aplica en su forma general (porque no hay concavidad ni conjuntos compactos en $\mathbb{R}^k$); por ello su equilibrio es **mixto**.
- En escenarios económicos (producción, subastas continuas, etc.) o de ingeniería (control de recursos, potencia, etc.), la existencia de equilibrio puro está muy ligada a la estructura de **maximización concava** de cada jugador.

En conclusión, **la existencia de un equilibrio puro** depende de condiciones que permitan garantizar una solución de maximización pura para cada jugador y la aplicabilidad de un argumento de **punto fijo** que fuerce la intersección de todas las mejores respuestas en un único perfil. Desde el punto de vista **computacional**, varios algoritmos explotan dichas propiedades de concavidad y continuidad para **encontrar** o **aproximar** el equilibrio en la práctica.

---

# Referencias Breves

- **Nash, J. F. (1950)**. *Equilibrium points in n-person games*. Proceedings of the National Academy of Sciences. (Versión clásica para juegos finitos, mezclas).
- **Debreu, G. (1952)** y **Glicksberg, I. (1952)**: extensión de juegos con conjuntos de estrategia compactos y convexos en $\mathbb{R}^n$.
- **Rosen, J. B. (1965)**: *Existence and Uniqueness of Equilibrium Points for Concave N-Person Games*.
- **Monderer, D., & Shapley, L. (1996)**: juegos potenciales y su existencia de equilibrio puro.  
- **Topkis, D. (1998)**: Juegos supermodulares.

Estos resultados complementan la teoría de **equilibrio de Nash** y, en conjunto, explican cuándo podemos asegurar equilibrios puros y cuándo sólo podemos asegurar (en general) equilibrios mixtos.
