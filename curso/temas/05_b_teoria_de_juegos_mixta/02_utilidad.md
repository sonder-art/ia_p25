
# 1. Matching Pennies (Repaso Rápido)

Ya se discutió antes de forma detallada, así que haremos un repaso para contextualizar:

**Descripción:**  
- Dos jugadores (1 y 2) eligen simultáneamente mostrar “Cara” (C) o “Cruz” (X) de una moneda.  
- Si coinciden (C-C o X-X), Jugador 1 gana 1 (y Jugador 2 pierde 1).  
- Si difieren (C-X o X-C), Jugador 2 gana 1 (y Jugador 1 pierde 1).

**Matriz de pagos** (para Jugador 1, Jugador 2):

\[
\begin{array}{c|cc}
 & \text{Cara (C) 2} & \text{Cruz (X) 2} \\
\hline
\text{Cara (C) 1} & ( +1,\,-1 ) & ( -1,\,+1 ) \\
\text{Cruz (X) 1} & ( -1,\,+1 ) & ( +1,\,-1 )
\end{array}
\]

**No hay equilibrio en puras.** El **equilibrio mixto**:  
- Jugador 1 juega Cara con probabilidad \(p^* = 1/2\).  
- Jugador 2 juega Cara con probabilidad \(q^* = 1/2\).  

**Interpretaciones no clásicas**:  
- Podríamos ver a dos emprendedores que compiten por sacar un producto al mercado (ej. un *gadget* innovador). Cada uno decide si se centra en “características de software” (Cara) o “características de hardware” (Cruz). Si ambos eligen lo mismo, uno gana la delantera y el otro pierde. Al final, la estrategia es “mezclar” (innovar un poco en ambos campos) para no ser predecible y así no dejar vía libre al competidor.  
- También se puede imaginar una coreografía de danza (Cara/Cruz como dos estilos opuestos). Los bailarines se turnan intentando coincidir o no coincidir en el momento del espectáculo; la “mezcla” en sus movimientos crea un equilibrio que mantiene el interés escénico.

---

# 2. Piedra, Papel o Tijeras

## 2.1. Descripción y Matriz de Pagos

Uno de los ejemplos más famosos de juego en el que **no hay** equilibrio en estrategias puras y, en cambio, hay un **equilibrio mixto**:

- Cada jugador elige simultáneamente “Piedra” (P), “Papel” (A) o “Tijeras” (T).  
- Piedra gana a Tijeras, Tijeras gana a Papel y Papel gana a Piedra.  
- Cuando un jugador gana, el otro pierde (juego de suma cero); en caso de empate (mismo símbolo), la recompensa es cero para ambos.

Podemos representar la matriz de pagos para Jugador 1 en forma resumida (aunque para 3x3 es un poco más grande). Por ejemplo:

|           | Papel (A)           | Piedra (P)           | Tijeras (T)          |
|-----------|----------------------|-----------------------|-----------------------|
| **Papel (A)**   | \(0,\,0\)              | \(+1,\,-1\)            | \(-1,\,+1\)            |
| **Piedra (P)**  | \(-1,\,+1\)            | \(0,\,0\)              | \(+1,\,-1\)            |
| **Tijeras (T)** | \(+1,\,-1\)            | \(-1,\,+1\)            | \(0,\,0\)              |

(El primer valor es la utilidad de Jugador 1, el segundo la de Jugador 2.)

## 2.2. Equilibrio de Nash en Estrategias Mixtas

Por **simetría**, en muchos de estos juegos de “ciclo” (P-A-T) la mezcla de equilibrio es la misma para ambos jugadores:

\[
p^*(\text{Piedra}) = p^*(\text{Papel}) = p^*(\text{Tijeras}) = \tfrac{1}{3}.
\]

Es decir, cada jugador elige **cada opción con probabilidad 1/3**. Esta mezcla hace a cualquier oponente **indiferente** entre jugar P, A o T, ya que todas dan la misma utilidad esperada.

## 2.3. Interpretaciones no clásicas

- En ecología, puede modelar **competencia de especies** que se especializan en diferentes nichos (un sistema “roca-papel-tijeras” se ha observado, por ejemplo, en ciertos lagartos de distintas coloraciones y comportamientos). La mezcla de estrategias evolutiva podría ser la proporción de individuos con cada “comportamiento”.
- En una liga deportiva con tres tipos de tácticas (por ejemplo, un equipo de fútbol que alterna ataque por bandas, ataque por el centro o contraataque), cada táctica “vence” a una y “pierde” con otra. El entrenador puede, en equilibrio, mezclar sus tácticas al 33% para sorprender al rival.

---

# 3. Chicken (El “Juego de la Gallina”)

El famoso “Juego de la Gallina” (o “Chicken”) consiste en que **dos conductores** avanzan en dirección de choque frontal. Cada uno elige “Desviarse” (D) o “No Desviarse” (N). Si ambos no se desvían, ocurre un desastre (gran castigo para ambos). Si uno se desvía y el otro no, el que se desvió queda como “cobarde” y el otro obtiene un beneficio simbólico (por ejemplo, prestigio).  
Una posible **matriz de pagos** (para Jugador 1, Jugador 2) es:

\[
\begin{array}{c|cc}
 & \text{No Desviarse (N) 2} & \text{Desviarse (D) 2} \\
\hline
\text{No Desviarse (N) 1} & (-10,\,-10) & ( +2,\,-2 ) \\
\text{Desviarse (D) 1} & ( -2,\,+2 ) & ( 0,\,0 )
\end{array}
\]

- \((-10, -10)\): choque frontal; ambos pierden mucho.  
- \((+2, -2)\): Jugador 1 “gana prestigio” mientras Jugador 2 “cede”.  
- \((-2, +2)\): Jugador 1 “cede” mientras Jugador 2 “gana prestigio”.  
- \((0, 0)\): ambos se desvían, todos seguros, sin prestigio adicional.

### 3.1. Equilibrios de Nash en Puras

- (N, D): Jugador 1 no se desvía, Jugador 2 se desvía.  
- (D, N): Jugador 1 se desvía, Jugador 2 no se desvía.  

Ambas combinaciones son equilibrios puros.

### 3.2. Equilibrio en Estrategias Mixtas

Existe también un **equilibrio mixto** donde cada jugador elige “No Desviarse” con cierta probabilidad que llamaremos \(p\), y “Desviarse” con \(1 - p\). Por **simetría**, ambos jugadores usarán la misma \(p^*\).

Para encontrar \(p^*\), hacemos que cualquiera de los dos jugadores sea indiferente entre N y D. Por ejemplo, la **utilidad esperada** para Jugador 1 si juega N contra la mezcla \((p, 1-p)\) de Jugador 2:

\[
U_1(\text{N} \mid p) = p \cdot (-10) + (1 - p) \cdot 2 \;=\; -10p + 2 - 2p = 2 - 12p.
\]

La **utilidad esperada** si Jugador 1 juega D:

\[
U_1(\text{D} \mid p) = p \cdot (-2) + (1 - p) \cdot 0 = -2p.
\]

La condición de indiferencia:

\[
2 - 12p = -2p 
\quad\Longrightarrow\quad
2 = 10p 
\quad\Longrightarrow\quad
p^* = \frac{2}{10} = 0.2.
\]

Así, en el **equilibrio mixto**:
- Cada jugador no se desvía (N) con prob \(0.2\).  
- Cada jugador se desvía (D) con prob \(0.8\).  

### 3.3. Interpretaciones no clásicas

- Dos artistas en una competición (o dos orquestas) deciden si van a tocar una pieza extremadamente difícil (no desviarse) o una más sencilla (desviarse). Si ambos tocan la difícil y fallan, es catastrófico (pérdida de prestigio). Si uno toca la difícil y el otro la sencilla, el primero destaca más. Mezclar probabilidades (a veces arriesgar, a veces ser más cauto) puede ser un equilibrio.
- Ocurren ejemplos en mercados financieros: dos traders pueden “arriesgar” mucho en inversiones (N) o ser más conservadores (D). Si ambos arriesgan y el mercado cae, la pérdida es grande. El equilibrio mixto representa la proporción de veces que uno arriesga vs. se retira.

---

# 4. Battle of the Sexes (Batalla de los Sexos)

Un ejemplo clásico de **coordinación** con preferencias distintas: se suele contar como una pareja que quiere salir juntos, pero uno prefiere “Ópera” (O) y el otro “Boxeo” (B). Quieren coordinar para disfrutar juntos, pero cada quien tiene su propia actividad favorita.

Podemos denominar las estrategias de Jugador 1: {O, B} y las de Jugador 2: {O, B}. Una matriz de pagos posible:

\[
\begin{array}{c|cc}
 & \text{O 2} & \text{B 2} \\
\hline
\text{O 1} & (2,1) & (0,0) \\
\text{B 1} & (0,0) & (1,2)
\end{array}
\]

- (O, O): Jugador 1 gana 2, Jugador 2 gana 1.  
- (B, B): Jugador 1 gana 1, Jugador 2 gana 2.  
- (O, B) o (B, O): obtienen (0,0).

### 4.1. Equilibrios Puros

Hay **dos equilibrios** en estrategias puras:  
- (O, O)  
- (B, B)  

Los dos coordinan en un mismo lugar, aunque uno de los dos es “más feliz” que el otro en cada caso.

### 4.2. Equilibrio Mixto

También existe **un equilibrio en estrategias mixtas**:  
- Sea \(p\) la probabilidad con que Jugador 1 juega O (y \(1-p\) juega B).  
- Sea \(q\) la probabilidad con que Jugador 2 juega O (y \(1-q\) juega B).

Para que Jugador 1 sea indiferente entre O y B, se igualan sus utilidades esperadas:

- \(U_1(\text{O}) = 2 \times q + 0 \times (1-q) = 2q.\)  
- \(U_1(\text{B}) = 0 \times q + 1 \times (1-q) = 1 - q.\)

Indiferencia:  
\[
2q = 1 - q 
\quad\Longrightarrow\quad 
3q = 1 
\quad\Longrightarrow\quad 
q^* = \tfrac{1}{3}.
\]

Para que Jugador 2 sea indiferente:

- \(U_2(\text{O}) = 1 \times p + 0 \times (1-p) = p.\)  
- \(U_2(\text{B}) = 0 \times p + 2 \times (1-p) = 2(1-p) = 2 - 2p.\)

Indiferencia:  
\[
p = 2 - 2p 
\quad\Longrightarrow\quad 
3p = 2 
\quad\Longrightarrow\quad 
p^* = \tfrac{2}{3}.
\]

Así, el **equilibrio de Nash en mixtas** es:
- Jugador 1 elige O con \(p^* = \frac{2}{3}\).  
- Jugador 2 elige O con \(q^* = \frac{1}{3}\).

### 4.3. Interpretaciones no clásicas

- Dos compañías de software quieren acordar un **estándar** (por ejemplo, un lenguaje de programación para un proyecto conjunto). A cada una le conviene que las dos usen el mismo, pero cada una tiene una preferencia distinta por razones internas. Pueden terminar “coordinándose” en la preferencia de la compañía A o de la compañía B, pero a veces la negociación se resuelve con probabilidades.
- Dos grupos musicales quieren hacer un **álbum colaborativo** y decidir el género principal: uno prefiere pop y otro prefiere rock. Coordinar en un género genera ganancias (fama, dinero), pero cada grupo prefiere su propio estilo. Hay mezcla de ensayos en pop y rock hasta que se define la colaboración final (o se dan versiones en ambos estilos).

---

# 5. Hawk-Dove (o “Juego de Halcón-Paloma”)

También llamado “Snowdrift” o “Juego del Atizador de Fuego”. Modela conflictos donde hay un posible comportamiento agresivo (“Halcón”) y uno menos agresivo o más pacífico (“Paloma”). La idea principal:  
- Si ambos son agresivos (H-H), hay una confrontación costosa para ambos.  
- Si uno es agresivo y el otro pacífico, el agresivo gana más (se queda con el recurso).  
- Si ambos son pacíficos (P-P), se reparten el recurso y se obtiene un beneficio, aunque menor que si uno intimida al otro sin coste.

Una matriz de pagos típica es (para Jugador 1, Jugador 2):

\[
\begin{array}{c|cc}
 & \text{Halcón (H) 2} & \text{Paloma (P) 2} \\
\hline
\text{Halcón (H) 1} & (\frac{B-C}{2}, \frac{B-C}{2}) & (B, 0) \\
\text{Paloma (P) 1} & (0, B) & (\frac{B}{2}, \frac{B}{2})
\end{array}
\]

Donde:
- \(B\) = beneficio del recurso.  
- \(C\) = coste de la confrontación (y se asume \(C > B\) para que sea peor pelear que no obtener el recurso).  
- \(\frac{B-C}{2}\) = si ambos pelean, a veces se parte el recurso tras un costo grande.

### 5.1. Equilibrios

- No suele haber un **equilibrio puro** único (dependiendo de los valores de \(B\) y \(C\) puede haber uno o dos). A menudo, el **juego tiene un equilibrio mixto**.
- Si llamamos \(p\) la probabilidad de Jugador 1 de jugar Halcón, y \(q\) la de Jugador 2, se obtiene un \(p^*\) donde cada jugador es indiferente entre H y P.

La **condición de indiferencia** para Jugador 1:
\[
U_1(\text{H}) = p^*\,(\tfrac{B-C}{2}) + (1-p^*)\,B,
\]
\[
U_1(\text{P}) = p^*\,0 + (1-p^*)\,\tfrac{B}{2}.
\]
Igualando:
\[
p^*\,\bigl(\tfrac{B-C}{2}\bigr) + (1-p^*)\,B \;=\; (1-p^*)\,\tfrac{B}{2}.
\]
Se resuelve y se obtiene:

\[
p^* = \frac{B}{C}.
\]
(Asumiendo que \(\frac{B}{C} < 1\), lo cual es habitual en este tipo de juego.)

Igualmente, por simetría, \(q^* = \frac{B}{C}\).

### 5.2. Interpretaciones no clásicas

- Modelar **discusiones creativas** en un equipo de diseño. “Halcón” es insistir agresivamente en tu idea, “Paloma” es ceder o discutir en tono más suave. Ambos comportamientos pueden llevar a ciertas ganancias y costos. A veces la mezcla natural en un equipo es que una parte de las discusiones alguien adopta la posición “firme” y otras veces “concede”.
- **Seguridad informática**: hay dos desarrolladores (o departamentos) que pueden “ser agresivos” (H) intentando imponer su sistema de seguridad, o “ser dóciles” (P) adoptando estándares compartidos. Si ambos son agresivos, se generan altos costos de incompatibilidad. Si uno impone y el otro cede, el primero gana mayor control. El equilibrio mixto indica la proporción con la que se “pelea” por una configuración vs. se colabora.

---

# Conclusiones Generales

Como se ve, **muchos juegos no tienen equilibrio en estrategias puras** (o tienen múltiples equilibrios puros), y las **estrategias mixtas** garantizan que exista (por el Teorema de Nash). La idea clave es siempre la misma:

1. **Asignar probabilidades** a cada estrategia.  
2. **Calcular utilidades esperadas** frente a la mezcla del oponente.  
3. **Exigir indiferencia** (para las estrategias que se van a usar con prob. positiva).  
4. **Resolver** para hallar las probabilidades en equilibrio.

Las **interpretaciones** pueden ir más allá de la política o la sociedad: se puede aplicar a fenómenos naturales, competiciones artísticas, ecología, economía digital, etc. Lo importante es identificar la estructura de recompensas y costos para entender cómo (y por qué) una mezcla de estrategias puede estabilizarse como un **equilibrio** donde ningún jugador mejora cambiando unilateralmente su estrategia.

---

## Referencias y Lecturas Sugeridas

- **Teoría de Juegos** de Roger Myerson (libro clásico).  
- **Juego, Estrategia y Razonamiento** de Avinash Dixit y Susan Skeath.  
- Artículos sobre **RPS dynamics** en ecología (p.ej., sobre lagartos Uta stansburiana con distintos comportamientos reproductivos).  
- Modelos de **suma cero** con múltiples estrategias, como **“Generalized Rock-Paper-Scissors”**.

Estos ejemplos demuestran la **amplitud de aplicaciones** de la Teoría de Juegos y, en particular, la **universalidad del concepto de equilibrio de Nash en estrategias mixtas** como una forma de entender decisiones interdependientes en multitud de ámbitos.