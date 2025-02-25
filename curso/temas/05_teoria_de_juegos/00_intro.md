---
jupyter: python3
---


# Teoría de Juegos: Un Documento Introductorio para Estudiantes

## 1. Introducción

La teoría de juegos es una disciplina que combina elementos de la economía, la matemática, la psicología y las ciencias sociales para estudiar cómo toman decisiones individuos o grupos cuando sus elecciones se encuentran interdependientemente relacionadas. A grandes rasgos, analiza situaciones —a las que llamamos "juegos"— en las cuales el resultado que obtiene cada participante depende no solo de sus propias decisiones, sino también de las decisiones de los demás.

**Definición coloquial:** Imagina que estás jugando un juego de mesa con tus amigos. En cada turno, tú decides tu movimiento, pero no basta con saber cómo quieres jugar tú: también debes tener en cuenta lo que podrían hacer los demás y cómo eso afecta tu estrategia. Esa interacción estratégica es esencialmente lo que estudia la teoría de juegos.

**Intuición:** En la vida cotidiana, muchas situaciones son similares a jugar un "juego": negociar un contrato, competir en un mercado o coordinar con colegas en el trabajo. Incluso elegir dónde cenar con tu familia puede ser un "juego" si varios tienen preferencias distintas y no pueden ir a dos lugares al mismo tiempo. La teoría de juegos nos ayuda a razonar sobre estos escenarios de manera estructurada, a predecir comportamientos y a diseñar políticas o mecanismos (en economía, política pública, etc.) para obtener ciertos resultados deseados.

**Rigidez y formalidad:** Aunque el uso de la palabra "juego" suena informal, la teoría de juegos es muy rigurosa y matemática. Se nutre de conceptos de probabilidad, optimización y análisis de estrategias, y sus conclusiones suelen expresarse mediante conceptos formales como el Equilibrio de Nash, la dominancia de estrategias y mucho más.

## 2. Conceptos Fundamentales

### 2.1. Jugadores
Los jugadores son los agentes o tomadores de decisiones involucrados en el juego. Cada jugador puede ser una persona, una empresa, un país o incluso un algoritmo informático. Lo importante es que cada jugador tenga objetivos (sus preferencias o "utilidad") y pueda elegir entre varias acciones o estrategias.

### 2.2. Estrategias
Una **estrategia** es el plan de acción que un jugador sigue durante el juego. Dependiendo del tipo de juego, la estrategia puede ser:

* **Estrategia pura:** Donde el jugador elige una acción concreta sin elementos de azar (por ejemplo, "cooperar" o "traicionar").
* **Estrategia mixta:** Donde el jugador selecciona una acción con cierta probabilidad. Es decir, elige diferentes acciones en un porcentaje de ocasiones o según un sorteo planificado (por ejemplo, "cooperar con 60% de probabilidad, traicionar con 40%").

### 2.3. Pagos (payoffs o utilidades)
El **pago** (o utilidad) es la recompensa que obtiene un jugador al final del juego. Puede ser cualquier cosa que valore el jugador: dinero, puntos, bienestar, satisfacción, etc. La utilidad se asume cuantificable de alguna manera para poder modelar matemáticamente las preferencias del jugador.

### 2.4. Información
El tipo de información con que cuentan los jugadores puede diferenciar la clase de juego:

* **Juegos de información completa:** Todos los jugadores conocen las estrategias y pagos disponibles para los demás, aunque no necesariamente conozcan las acciones que escogieron en cada momento.
* **Juegos de información incompleta:** Hay alguna incertidumbre; por ejemplo, un jugador desconoce la "función de pagos" o el tipo de otro jugador.

### 2.5. Formas de Representación
Existen dos grandes formas de representar un juego:

1. **Forma normal o estratégica:** Se representa con una matriz (en juegos de dos jugadores) o con una función de pagos que muestra lo que gana cada jugador según las elecciones simultáneas de todos.
2. **Forma extensiva:** Se representa con un árbol de decisiones, útil para juegos secuenciales en los que el orden de jugadas influye en el resultado.


## 3. Ejemplo Central: El Dilema del Prisionero

1. **Coloquialmente**, imagina que la policía arresta a dos sospechosos por un delito. Los separan y les ofrecen el mismo trato:
   * Si uno confiesa (traiciona) y el otro guarda silencio (coopera), el que confiesa sale libre y el otro recibe la pena máxima.
   * Si ambos confiesan, ambos reciben una pena moderada.
   * Si ambos guardan silencio, cada uno recibe una pena menor por no tenerse evidencia fuerte.

2. **Intuición:** A cada prisionero le conviene individualmente confesar, sin importar lo que haga el otro (porque confesar domina a callar). Sin embargo, si ambos confiesan, terminan con una condena peor que si ambos hubieran guardado silencio.

3. **Representación en forma normal (matriz de pagos):**

   Supongamos que los jugadores son $A$ y $B$. Cada uno tiene dos estrategias: **Cooperar** (guardar silencio) o **Traicionar** (confesar).

   |                | **B coopera** | **B traiciona** |
   |----------------|---------------|-----------------|
   | **A coopera**  | $(-1, -1)$   | $(-3, 0)$      |
   | **A traiciona**| $(0, -3)$    | $(-2, -2)$     |

* **Interpretación de los valores:**
  * Si ambos cooperan ($A$ coopera, $B$ coopera): cada uno recibe -1 (poca condena)
  * Si $A$ coopera y $B$ traiciona: $A$ obtiene -3 (condena larga), $B$ obtiene 0 (sale libre)
  * Si $A$ traiciona y $B$ coopera: $A$ obtiene 0, $B$ -3
  * Si ambos traicionan: ambos reciben -2 (condena moderada)

## 4. Definición Formal

Podemos formalizar un **juego en forma normal** con la siguiente notación:

1. Conjunto de jugadores: $N = \{1, 2, \dots, n\}$
2. Conjunto de estrategias para el jugador $i$: $S_i$
3. Función de utilidad o payoff: $u_i: S_1 \times S_2 \times \dots \times S_n \to \mathbb{R}$

Así, un juego en forma normal se describe por la terna:

$\Gamma = (N, \{S_i\}_{i \in N}, \{u_i\}_{i \in N})$


### 4.1 Estructura General de una Matriz de Pagos

Consideremos un juego de dos jugadores: Jugador A y Jugador B.

* **Filas**: Corresponden a las estrategias del Jugador A.
* **Columnas**: Corresponden a las estrategias del Jugador B.
* **Entradas de la matriz**: Cada celda muestra el pago (o utilidad) de ambos jugadores cuando se elige la combinación de estrategias asociada a esa fila y columna.

|     | B1                      | B2                      |
|-----|-------------------------|-------------------------|
| A1  | $(u_A(A_1,B_1), u_B(A_1,B_1))$ | $(u_A(A_1,B_2), u_B(A_1,B_2))$ |
| A2  | $(u_A(A_2,B_1), u_B(A_2,B_1))$ | $(u_A(A_2,B_2), u_B(A_2,B_2))$ |

* $A_1$ y $A_2$ son las estrategias disponibles de A.
* $B_1$ y $B_2$ son las estrategias disponibles de B.
* $u_A(\cdot)$ y $u_B(\cdot)$ denotan las utilidades (pagos) respectivas.

**Lectura**: Para encontrar qué obtiene cada jugador si A elige $A_1$ y B elige $B_2$, localizamos la fila $A_1$ y la columna $B_2$. Dentro de esa celda, vemos dos números $(x,y)$. El primero $(x)$ es la utilidad de A; el segundo $(y)$ es la de B.

### 4.2 Cómo leer y analizar la matriz paso a paso

#### Paso 1: Identifica las estrategias
* Observa el encabezado de filas y columnas para entender las posibles acciones de cada jugador.

#### Paso 2: Fíjate en los pagos (utilidades)
* Cada celda tiene un par ordenado (o tupla). En juegos de 2 jugadores se acostumbra a poner primero el pago de A y luego el de B.

#### Paso 3: Compara y busca "mejores respuestas"
* Para A: en cada columna (fijando la estrategia de B), observa qué fila le da mayor utilidad a A.
* Para B: en cada fila (fijando la estrategia de A), observa qué columna le da mayor utilidad a B.

#### Paso 4: Identifica equilibrios (como el Equilibrio de Nash)
* En cada celda, pregúntate: si ya estoy en esta celda, ¿algún jugador quiere desviarse unilateralmente?


### 4.3. Estrategia Dominante
**Definición:** Una estrategia $s_i^*$ es dominante para el jugador $i$ si, para **cualquier** perfil de estrategias de los otros jugadores $(s_{-i})$, se cumple:

$u_i(s_i^*, s_{-i}) \ge u_i(s_i, s_{-i})$ para todo $s_i \in S_i$

### 4.4. Equilibrio de Nash
**Definición formal:** Un perfil de estrategias $(s_1^*, s_2^*, \dots, s_n^*)$ es un Equilibrio de Nash si, para cada jugador $i$, dado que los otros jugadores siguen sus estrategias de equilibrio $s_{-i}^*$, la estrategia $s_i^*$ maximiza la utilidad de $i$. Es decir:

$u_i(s_i^*, s_{-i}^*) \ge u_i(s_i, s_{-i}^*)$ para todo $s_i \in S_i$

## 5. Tipos de Juegos

### 5.1. Juegos Simultáneos vs. Secuenciales
* **Juegos simultáneos:** Los jugadores eligen sus estrategias sin saber lo que han elegido los demás.
* **Juegos secuenciales:** El orden de decisiones importa. Los jugadores pueden observar las acciones previas.

### 5.2. Juegos Cooperativos vs. No Cooperativos
* **Juegos no cooperativos:** Cada jugador busca su propio beneficio sin acuerdos vinculantes.
* **Juegos cooperativos:** Se permiten coaliciones o acuerdos vinculantes entre jugadores.

### 5.3. Juegos de Suma Cero vs. Suma No Cero
* **Juegos de suma cero:** Lo que uno gana es exactamente lo que pierde el otro.
* **Juegos de suma no cero:** Los pagos no necesariamente se compensan.

## 6. Ejemplo Ampliado: Dilema del Prisionero en Distintas Variantes

1. **Dilema del Prisionero Repetido Finitamente:**
   * Si conocen cuántas rondas van a jugar, se puede analizar por inducción hacia atrás.
   * La traición sistemática se convierte en la única estrategia racional.

2. **Dilema del Prisionero Repetido Infinita o Indefinidamente:**
   * La posibilidad de "castigar" al otro en rondas futuras puede incentivar la cooperación.
   * La estrategia "Tit-for-Tat" puede generar altos niveles de cooperación.

## 7. Aplicaciones en el Mundo Real

**7.1. Economía y Negocios**
* Competencia de mercado
* Subastas  

**7.2. Política y Relaciones Internacionales**
* Negociaciones diplomáticas
* Formación de coaliciones  

**7.3. Biología y Teoría Evolutiva**
* Estrategias evolutivamente estables  

**7.4. Informática e Inteligencia Artificial**
* Diseño de algoritmos de negociación
* Aprendizaje por refuerzo

## 8. Más Allá de la Forma Normal: El Juego en Forma Extensiva

1. **Nodos de decisión:** Momentos en que un jugador elige su acción
2. **Ramas:** Acciones posibles desde cada nodo
3. **Hojas del árbol:** Pagos finales
4. **Subjuegos:** Partes del árbol que pueden considerarse como juegos independientes

## 9. Herramientas Matemáticas Avanzadas

* Teoría de juegos combinatorios
* Teoría de incentivos y diseño de mecanismos
* Equilibrios refinados

## 10. Conclusiones

La teoría de juegos proporciona un marco poderoso para entender las interacciones estratégicas, permitiendo:

* **Predecir** comportamientos en situaciones interactivas
* **Diseñar** mecanismos o sistemas de incentivos
* **Evaluar** la eficiencia y equidad de distintos resultados

## Lecturas Recomendadas

1. "Theory of Games and Economic Behavior" de John von Neumann y Oskar Morgenstern
2. "An Introduction to Game Theory" de Martin J. Osborne
3. "The Evolution of Cooperation" de Robert Axelrod
4. "Game Theory: Analysis of Conflict" de Roger B. Myerson
