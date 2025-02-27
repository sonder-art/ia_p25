# Equilibrios Mixtos de Nash

## 1. Introducción General

En la teoría de juegos, particularmente en la modalidad **estática** o de **forma normal**, un "juego" se describe principalmente por:
1. Un conjunto de **jugadores** (por ejemplo, Jugador 1 y Jugador 2).
2. El conjunto de **estrategias** de cada jugador (las "acciones" posibles).
3. Una **función de pago** (o utilidad) para cada jugador, que depende de la combinación de estrategias elegidas por todos los jugadores.

Hasta ahora, si has revisado teoría de juegos básica, habrás estudiado:
- **Estrategias puras**: cuando el jugador elige determinísticamente una sola estrategia.
- **Equilibrio de Nash** en estrategias puras: un perfil de estrategias donde ningún jugador tiene incentivos a desviarse de su estrategia dada la estrategia del otro.

Sin embargo, hay situaciones en las que **no** existen equilibrios en estrategias puras. Para abordar estos casos surge el concepto de **estrategias mixtas**, donde cada jugador asigna probabilidades a sus estrategias puras.

El objetivo de este documento es describir de forma detallada qué es un **equilibrio de Nash en estrategias mixtas** ("equilibrio mixto"), cómo se define, la intuición detrás de él y cómo se calcula. Para ello, introduciremos primero las definiciones formales y luego desarrollaremos un **ejemplo concreto** (un juego sencillo) para ilustrar todos los pasos.

---

## 2. Estrategias Puras vs. Estrategias Mixtas

### 2.1. Estrategia Pura

Una **estrategia pura** es la elección directa de una de las opciones disponibles. Por ejemplo, si un jugador tiene dos acciones $A$ y $B$, escoger una estrategia pura es elegir $A$ con probabilidad 1 (y 0 para $B$), o viceversa.

### 2.2. Estrategia Mixta

Una **estrategia mixta** consiste en asignar una probabilidad a cada estrategia pura, de forma que la suma de todas las probabilidades sea 1. Si un jugador tiene dos acciones $A$ y $B$, una estrategia mixta podría ser, por ejemplo:
$p(A) = p \quad\text{y}\quad p(B) = 1 - p$,
donde $0 \leq p \leq 1$. En la práctica, el jugador "lanza una moneda" (metafóricamente) para decidir qué acción elegir, siguiendo las probabilidades definidas.

### 2.3. Beneficio o Pago Esperado

Para combinar probabilidades y recompensas (pagos), se utiliza el **valor esperado**. La utilidad (o pago) esperada de un jugador se calcula ponderando los pagos que resultan de cada combinación de acciones, según las probabilidades de elección de esas acciones (tanto las propias como las de los demás jugadores).

---

## 3. Definición de Equilibrio de Nash en Estrategias Mixtas

Un **equilibrio de Nash en estrategias mixtas** es un perfil de estrategias (una para cada jugador) en las que cada jugador está usando la mejor respuesta **dada** la estrategia mixta del o de los demás jugadores. Dicho más intuitivamente:

> **En un equilibrio mixto, cuando un jugador escoge una distribución de probabilidad sobre sus acciones, esa distribución hace que el otro jugador sea indiferente entre las acciones que aparecen con probabilidad positiva** (es decir, no gana más al cambiar sus propias probabilidades). De la misma forma, dado lo que hace el otro, el primer jugador tampoco puede mejorar su pago ajustando su propia mezcla.

Formalmente, el perfil de estrategias mixtas $(\sigma_1^*, \sigma_2^*, \dots, \sigma_n^*)$ es un equilibrio de Nash si para cada jugador $i$,
$\sigma_i^* \in \arg\max_{\sigma_i} \; U_i(\sigma_i, \sigma_{-i}^*)$,
donde $U_i(\sigma_i, \sigma_{-i}^*)$ es la utilidad esperada del jugador $i$ cuando él juega $\sigma_i$ y los demás juegan $\sigma_{-i}^*$.

---

## 4. Ejemplo para Ilustrar: "Cara o Cruz" (Matching Pennies)

A lo largo de este documento usaremos **el juego de "Matching Pennies"** (Cara o Cruz) como ejemplo. Este juego es muy conocido porque **no** tiene equilibrio de Nash en estrategias puras, pero sí en **estrategias mixtas**.

### 4.1. Descripción del Juego

- Hay dos jugadores: Jugador 1 y Jugador 2.
- Cada uno elige mostrar "Cara" (C) o "Cruz" (X) en una moneda.
- Si ambos coinciden (Cara-Cara o Cruz-Cruz), Jugador 1 gana 1 y Jugador 2 pierde 1.  
- Si no coinciden (Cara-Cruz o Cruz-Cara), Jugador 2 gana 1 y Jugador 1 pierde 1.

Podemos representar la **matriz de pagos** desde el punto de vista de Jugador 1 (arriba) y Jugador 2 (abajo) de la siguiente forma:

$\begin{array}{c|cc}
 & \text{Cara (C) Jugador 2} & \text{Cruz (X) Jugador 2} \\
\hline
\text{Cara (C) Jugador 1} & ( +1,\,-1 ) & ( -1,\,+1 ) \\
\text{Cruz (X) Jugador 1} & ( -1,\,+1 ) & ( +1,\,-1 )
\end{array}$

- La primera coordenada de cada pareja es el pago para Jugador 1.
- La segunda coordenada es el pago para Jugador 2.

### 4.2. Observación: No existe Equilibrio en Estrategias Puras

Comprobemos rápidamente:
- Si Jugador 1 elige Cara, entonces Jugador 2 preferiría elegir Cruz (para ganar 1).  
- Si Jugador 2 elige Cruz, entonces Jugador 1 prefiere elegir Cruz (para ganar 1).  
- Pero si Jugador 1 elige Cruz, Jugador 2 preferiría elegir Cara (para ganar 1).  
- Y así sucesivamente…

No hay un punto donde ambos estén contentos sin desviarse. Así que no hay equilibrio puro.

---

## 5. Encontrando el Equilibrio en Estrategias Mixtas

Ahora veremos cómo encontrar el equilibrio mixto en este juego.

### 5.1. Planteamiento de las Probabilidades

- Sea $p$ la probabilidad con que **Jugador 1** juega Cara (C). Entonces juega Cruz (X) con probabilidad $1-p$.
- Sea $q$ la probabilidad con que **Jugador 2** juega Cara (C). Entonces juega Cruz (X) con probabilidad $1-q$.

El perfil de estrategias mixtas será $(p, q)$, y nos interesa encontrar $(p^*, q^*)$ que forme un equilibrio de Nash.

### 5.2. Cálculo de la Utilidad Esperada

Calculemos la utilidad esperada de Jugador 1, $U_1$, dado $(p,q)$:

1. **Cara-Cara** ocurre con probabilidad $p \cdot q$ y paga $+1$ a Jugador 1.
2. **Cara-Cruz** ocurre con probabilidad $p \cdot (1-q)$ y paga $-1$ a Jugador 1.
3. **Cruz-Cara** ocurre con probabilidad $(1-p) \cdot q$ y paga $-1$ a Jugador 1.
4. **Cruz-Cruz** ocurre con probabilidad $(1-p) \cdot (1-q)$ y paga $+1$ a Jugador 1.

Entonces:
$U_1(p,q) = (+1)\,p\,q \;+\; (-1)\,p\,(1-q) \;+\; (-1)\,(1-p)\,q \;+\; (+1)\,(1-p)\,(1-q)$.

Agrupando términos:

$\begin{aligned}
U_1(p,q) &= p\,q - p\,(1-q) - (1-p)\,q + (1-p)\,(1-q) \\
         &= p\,q - p + p\,q - q + p\,q + 1 - p - q + pq \quad (\text{revisar con cuidado}) \\
         &\text{(Para simplificar, combinemos con método más sistemático.)}
\end{aligned}$

Es más rápido reagrupar "por los términos p y q":

$\begin{aligned}
U_1(p,q) &= p\,q \;-\; p(1-q) \;-\; (1-p)\,q \;+\; (1-p)(1-q) \\
&= p\,q - p + p\,q - q + p\,q + 1 \quad(\text{ver si hay error al expandir}) \\
&\quad - p - q + pq \quad \text{(cuidado, es fácil equivocarse con tantos términos).}
\end{aligned}$

Para evitar confusión, vamos a simplificar directo desde la definición caso por caso:

- $p\,q$ aporta $+1$.
- $p(1-q)$ aporta $-1$.
- $(1-p)q$ aporta $-1$.
- $(1-p)(1-q)$ aporta $+1$.

Sumémoslo de manera ordenada:

$U_1 = p\,q + (-1)\cdot p(1-q) + (-1)\cdot (1-p)q + (1-p)(1-q)$.

Agrupemos:
$U_1 = p\,q + (-p + p\,q) + (-q + p\,q) + (1 - p - q + p\,q)$.

Sumar cuidadosamente:
- Términos con $pq$: $p\,q + p\,q + p\,q + p\,q = 4p\,q$.
- Términos con $-p$: $-p$.
- Términos con $-q$: $-q$.
- Términos constantes: $+1$.

Entonces:
$U_1 = 4p\,q - p - q + 1$.

No obstante, **ojo**, en muchos textos, el valor final del Pago para Matching Pennies es más fácil de ver si se simplifica de otra manera. De hecho, a menudo se busca la **indiferencia**, que es lo realmente importante para encontrar $p$ y $q$. Veamos mejor la utilidad esperada de Jugador 1 **si** Jugador 1 elige Cara o Cruz, dado que Jugador 2 mezcla con $q$. Esto es más directo para la condición de indiferencia:

- **Si Jugador 1 juega Cara** (y Jugador 2 mezcla $q$ y $1-q$):
  - Cara-Cara con prob $q$, pago $+1$.
  - Cara-Cruz con prob $1-q$, pago $-1$.

  Entonces,
  $U_1(\text{Cara}, q) = (+1)\cdot q + (-1)\cdot (1-q) = q - (1-q) = 2q - 1$.

- **Si Jugador 1 juega Cruz** (y Jugador 2 mezcla $q$ y $1-q$):
  - Cruz-Cara con prob $q$, pago $-1$.
  - Cruz-Cruz con prob $1-q$, pago $+1$.

  Entonces,
  $U_1(\text{Cruz}, q) = (-1)\cdot q + (+1)\cdot (1-q) = -q + (1-q) = 1 - 2q$.

De este modo, la **utilidad esperada de Jugador 1** cuando mezcla con probabilidad $p$ (y Jugador 2 con $q$) será:
$U_1(p,q) = p\,U_1(\text{Cara}, q) + (1-p)\,U_1(\text{Cruz}, q)$.

Pero para encontrar el **equilibrio**, necesitamos que Jugador 1 sea **indiferente** entre jugar Cara y Cruz **si ambas se juegan con probabilidad positiva** en el equilibrio. Es decir, en un equilibrio mixto, Jugador 1 no preferirá exclusivamente Cara ni Cruz; las dos le dejan la misma utilidad esperada. Por tanto:

$U_1(\text{Cara}, q) = U_1(\text{Cruz}, q)$.

Sustituyendo:
$2q - 1 = 1 - 2q \quad \Longrightarrow \quad 2q - 1 = 1 - 2q$.

$\Longrightarrow 4q = 2 \quad \Longrightarrow \quad q = \tfrac{1}{2}$.

**Interpretación**: si Jugador 2 mezcla con $q = \frac{1}{2}$, Jugador 1 queda indiferente entre Cara y Cruz, y por tanto es razonable que Jugador 1 mezcle.

Simétricamente, calculemos la **utilidad esperada de Jugador 2** (o bien, la de Jugador 1 desde el punto de vista "qué hace Jugador 2 para dejar indiferente a Jugador 2"). Pero es más sencillo darse cuenta de que, por la estructura de este juego de suma cero, Jugador 2 hará a Jugador 1 indiferente y viceversa. 

Para ser sistemáticos, veamos la utilidad de Jugador 2 cuando él juega Cara vs. Cruz, dado que Jugador 1 mezcla con probabilidad $p$:

- Si Jugador 2 juega Cara:  
  - Coincide con Cara (Jugador 1) con prob $p$ y Jugador 2 recibe $-1$ (porque Jugador 1 gana +1).  
  - Coincide con Cruz (Jugador 1) con prob $1-p$ y Jugador 2 recibe $+1$.  

  Utilidad para Jugador 2:
  $U_2(\text{Cara}, p) = (-1) \cdot p + (+1) \cdot (1 - p) = -p + (1-p) = 1 - 2p$.

- Si Jugador 2 juega Cruz:
  - Coincide con Cara (Jugador 1) con prob $p$ y Jugador 2 recibe $+1$.  
  - Coincide con Cruz (Jugador 1) con prob $1-p$ y Jugador 2 recibe $-1$.  

  $U_2(\text{Cruz}, p) = (+1)\cdot p + (-1)\cdot (1-p) = p - (1-p) = 2p - 1$.

Para la indiferencia de Jugador 2 (suponiendo que en equilibrio también juega ambas estrategias con probabilidad positiva):
$U_2(\text{Cara}, p) = U_2(\text{Cruz}, p)$.

$1 - 2p = 2p - 1 \quad \Longrightarrow \quad 4p = 2 \quad \Longrightarrow \quad p = \tfrac{1}{2}$.

### 5.3. Equilibrio Mixto

Concluimos que **en el equilibrio**, cada jugador asigna probabilidad $\frac{1}{2}$ a Cara y $\frac{1}{2}$ a Cruz. Es decir, el **equilibrio de Nash en estrategias mixtas** de "Matching Pennies" es:

$\bigl(p^*, q^*\bigr) = \Bigl(\tfrac{1}{2}, \tfrac{1}{2}\Bigr)$.

Ningún jugador puede mejorar su pago esperado modificando unilateralmente esa mezcla. Cada uno hace que el otro sea indiferente entre sus opciones.

---

## 6. Intuición Detrás del Equilibrio Mixto

- En juegos como "Matching Pennies" (suma cero), si uno de los jugadores revelara su acción con seguridad (p.e., "siempre Cara"), el otro se aprovecharía (jugando "Cruz"). Entonces, la **aleatoriedad** protege contra la explotación del otro jugador.
- En el equilibrio, ambos jugadores usan una mezcla que hace que el oponente quede **indiferente** entre sus estrategias puras. Si el oponente no puede ganar más cambiando su estrategia, entonces tampoco hay incentivo para cambiar la propia mezcla.

---

## 7. Resumen de Pasos para Hallar un Equilibrio Mixto

1. **Etiquetar probabilidades**: Denota con $p$ la probabilidad de Jugador 1 de jugar una acción y con $q$ la de Jugador 2 (en un juego de 2x2; con más estrategias se hace de forma análoga).
2. **Calcular utilidad esperada** para cada jugador cuando se juega una estrategia pura frente a la mezcla del oponente.
3. **Exigir indiferencia** en las estrategias que se juegan con probabilidad positiva. Esto genera ecuaciones (por ejemplo, $U_1(A) = U_1(B)$ si A y B son jugadas con prob. > 0).
4. **Resolver las ecuaciones** para encontrar las probabilidades $p$ y $q$.
5. **Verificar** que con esas probabilidades no hay incentivos a desviarse.

---

## 8. Conclusiones

- El **equilibrio de Nash en estrategias mixtas** existe incluso cuando no hay equilibrio en estrategias puras.  
- La base de la mezcla en estos juegos es la **indiferencia** que se logra en el oponente: al usar ciertas probabilidades, haces que la recompensa esperada de su acción sea la misma para cualquiera de sus opciones, impidiéndole así beneficiarse de un cambio unilateral.  
- En juegos de 2x2, el procedimiento es relativamente sencillo: se igualan las utilidades esperadas de cada acción pura, para encontrar la mezcla que hace al rival indiferente.

El ejemplo de "Matching Pennies" muestra de forma clara la necesidad de los equilibrios mixtos. Este mismo procedimiento se aplica a muchos otros juegos (por ejemplo, "Piedra, Papel o Tijera", "Duopolio de Cournot" en versiones simplificadas, "Batalla de los Sexos" con ligeras modificaciones, etcétera).

---

## 9. Apéndice: Forma Simplificada de "Matching Pennies"

A modo de confirmación rápida, muchos manuales usan las ecuaciones de indiferencia directamente:

- Para Jugador 1:  
  $\text{Pago esper. al jugar Cara} = \text{Pago esper. al jugar Cruz}$.
  Esto nos da la ecuación para $q$.

- Para Jugador 2:  
  $\text{Pago esper. al jugar Cara} = \text{Pago esper. al jugar Cruz}$.
  Esto nos da la ecuación para $p$.

En un **juego de suma cero 2x2**, el equilibrio mixto suele terminar con las probabilidades $p = q = \frac{1}{2}$ (cuando la estructura es simétrica, como en Matching Pennies). La idea de igualar utilidades esperadas de las acciones con probabilidad positiva en la mezcla es la clave central.

---

## Referencias y Comentarios Finales

- La existencia de equilibrios en estrategias mixtas está garantizada en cualquier juego finito (Teorema de Nash).
- En juegos sencillos (2x2), basta usar la condición de indiferencia para las estrategias que se utilizan con probabilidad positiva.
- Es esencial practicar con distintos ejemplos. "Matching Pennies" es uno de los más simples, pero otros juegos clásicos como "Piedra, Papel o Tijeras" ilustran el mismo concepto con más acciones.

