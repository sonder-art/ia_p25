# **Ejemplos Famosos de Juegos en Teoría de Juegos**

Exploraremos **varios ejemplos de juegos** (más allá del Dilema del Prisionero) que son **famosos** o ilustran situaciones habituales en la vida cotidiana. A cada uno le daremos alguna interpretación sencilla y **analizaremos** sus equilibrios de Nash (si los tienen) o remarcaremos la **ausencia** de los mismos en estrategia pura, cuando sea el caso.

Los ejemplos aquí presentados son **juegos estáticos** y de **información completa**, con un **número reducido de estrategias** para cada jugador (generalmente 2 o 3). Veremos cómo cada uno **puede interpretarse** de maneras variadas que conectan con la vida diaria.

---

# **1. El Juego de la Gallina (Chicken)**

## **Matriz de Pagos (Versión Clásica)**
Dos conductores se dirigen de frente, cada uno en su carril, y **ninguno** quiere ser el que "se aparte" (por orgullo). Cada uno elige entre:
- **Desviarse** (D): girar el volante y ceder.
- **Mantenerse** (M): continuar su trayecto sin desviarse.

|                   | **Conductor B: D** | **Conductor B: M** |
|-------------------|-------------------|-------------------|
| **Conductor A: D**| $(0, 0)$         | $(-1, +1)$       |
| **Conductor A: M**| $(+1, -1)$       | $(-10, -10)$     |

**Interpretación de pagos**:
- Si ambos se desvían (D, D), nadie "gana orgullo", pero ninguno sufre el choque, por lo que el pago es intermedio $(0,0)$.
- Si A se desvía y B no, B "gana" (1) su orgullo, A "pierde" (–1) algo de orgullo. Viceversa si A no se desvía y B sí.
- Si ambos se mantienen (M, M), ocurre un **choque** catastrófico $(-10, -10)$.

## **Análisis y Equilibrios**
- **Estrategias dominantes**: No hay.
- **Equilibrios de Nash en estrategias puras**:
  - (M, D) → A no se desvía, B se desvía.
  - (D, M) → A se desvía, B no se desvía.
  Ambos son equilibrios porque ningún jugador querría cambiar su estrategia unilateralmente dadas las acciones del otro.
- **Interpretación cotidiana**:
  - **Invitar a salir** vs. **esperar a que te inviten**. Si ambos esperan, nadie se mueve $(-10, -10)$, "fracaso total". Si uno toma la iniciativa y el otro no, el que "empuja" la situación se arriesga un poco (pago -1), el otro se beneficia de la invitación (+1), pero es mejor que nadie haga nada.

---

# **2. Matching Pennies (Sin Equilibrio Puro)**

## **Matriz de Pagos**
Dos jugadores (A y B) eligen simultáneamente si mostrar "cara" (C) o "cruz" (X). Si coinciden (ambos muestran C o ambos X), A gana 1 y B pierde 1 (o viceversa, según la convención). Si difieren (uno C, otro X), gana B y pierde A.

|               | **B elige C**  | **B elige X**  |
|---------------|----------------|----------------|
| **A elige C** | $(+1, -1)$    | $(-1, +1)$    |
| **A elige X** | $(-1, +1)$    | $(+1, -1)$    |

## **Análisis y Equilibrios**
- **Estrategias dominantes**: No hay.
- **Equilibrio de Nash en estrategias puras**: **No existe**. Cualquier celda que elijas, el otro jugador puede cambiar su estrategia y obtener un mejor pago.
- **Equilibrio de Nash en estrategias mixtas**: Cada uno elige C o X con **probabilidad 1/2**. Ese es el único equilibrio, pero no está en estrategias puras.
- **Interpretación cotidiana**:
  - **Juego de adivinar** el "verdadero interés" del otro: si la otra persona cree que vas a "cooperar", ella puede cambiar su jugada para aprovecharse, etc.
  - **Salir a beber vs. quedarse en casa**: si uno cree que su compañero se queda en casa, tal vez prefiera salir y viceversa, lo que genera un vaivén de decisiones.
  - Este juego suele modelar la idea de "ocultar o descubrir", donde cada jugador trata de anticipar la acción del otro.

---

# **3. Stag Hunt (Caza del Ciervo)**

## **Matriz de Pagos (Versión 2x2)**
Dos cazadores salen a cazar. Pueden **colaborar** (C) para cazar un ciervo grande (requiere ambos) o **ir solos** (S) y cazar un conejo (menos valioso, pero seguro).

|                       | **B elige C (colaborar)** | **B elige S (solo)** |
|-----------------------|---------------------------|---------------------|
| **A elige C (colaborar)** | $(3, 3)$              | $(0, 2)$           |
| **A elige S (solo)**      | $(2, 0)$              | $(2, 2)$           |

**Interpretación de pagos** (ejemplo numérico):
- Si ambos colaboran (C, C): cada uno obtiene 3 (ciervo grande compartido).
- Si uno colabora y el otro no, el que va solo atrapa un conejo (2), y el que colaboró no consigue nada (0).
- Si ambos van solos (S, S), cada uno se lleva un conejo (2).

## **Análisis y Equilibrios**
- **Equilibrios de Nash en puras**:
  1. (C, C) → ambos colaboran y nadie gana desviándose (desviarte te da 2, que es menos que 3).
  2. (S, S) → ambos van solos, y si uno se desvía a colaborar mientras el otro sigue solo, sale perdiendo (pasa de 2 a 0).
- **Interpretación cotidiana**:
  - **Hacer tareas en equipo** vs. **hacerlas solo**. Colaborar puede dar mayor beneficio, pero solo funciona si los demás también colaboran.
  - **Estudiar juntos** vs. **independiente**.

---

# **4. El juego de la coordinación con conflicto**

## **Matriz de Pagos**
Imaginemos que amigues  quiere decidir si el plan de la tarde es **ir a ver una película** (P) o **ir a un concierto** (C). A prefiere la película ligeramente más, B prefiere el concierto. Pero ambos valoran más **estar juntos** que ir separados.

|              | **B elige P** | **B elige C** |
|--------------|---------------|---------------|
| **A elige P**| $(2,1)$      | $(0,0)$      |
| **A elige C**| $(0,0)$      | $(1,2)$      |

- Si A elige P y B elige P, A gana 2, B gana 1.
- Si A elige C y B elige C, A gana 1, B gana 2.
- Si eligen **opciones distintas** (P vs. C), ambos obtienen 0 (separados).

## **Análisis y Equilibrios**
- **Equilibrios de Nash en puras**:
  - (P, P) y (C, C).
- **Interpretaciones**:
  - El **conflicto** radica en **quién** logra su plan preferido, pero **la coordinación** es clave.
  - "¿Salimos a comer pizza o sushi?" Uno prefiere pizza, el otro sushi, pero peor es no salir juntos.

---

# **5. "Enviar Mensaje a la Persona que te Gusta"**


- **Jugador A**: Tú, que decides si enviar un mensaje (M) o quedarte callado (N).
- **Jugador B**: La persona que te interesa. Puede "responder con interés real" (I) o "responder de forma manipuladora" (sea love bombing o gaslighting) (G).

## **Posible Matriz de Pagos (2x2)**

|                    | **B: Interés (I)** | **B: Manipulación (G)** |
|--------------------|--------------------|-----------------------|
| **A: Mensaje (M)** | $(+2, +2)$        | $(-2, +1)$           |
| **A: No Mensaje (N)**| $(0, 0)$        | $(0, -1)$            |

**Interpretación de pagos**:
- (M, I): Tú envías mensaje, la otra persona responde con interés genuino:
  - A se siente contento (+2). B también "gana" (+2) por una interacción honesta y satisfactoria.
- (M, G): Envío de mensaje y el otro responde manipulando (love bombing: halagos exagerados sin compromiso real, o gaslighting: confundiendo intencionalmente):
  - A sufre emocionalmente (-2). B obtiene una "ganancia" temporal (+1) sintiéndose con poder.
- (N, I): Si A no manda mensaje y la otra persona habría respondido con interés, realmente **no ocurre interacción** → $(0, 0)$.
- (N, G): Tampoco hay interacción, pero B "pierde un poco" (-1) por no poder manipular. A se queda neutral (0).

## **Análisis y Equilibrios**
1. Revisa si hay **estrategias dominantes**:
   - Para A: "Mensaje (M)" no siempre es mejor (con G, sale -2). "No Mensaje (N)" evita la pérdida, pero con I se pierde la oportunidad de +2. No hay dominancia.
   - Para B: Depende de la acción de A. Si A no envía mensaje, B obtiene 0 o -1, así que prefiere I para obtener 0 (mejor que -1). Si A envía mensaje, B puede elegir +2 (I) o +1 (G). Prefiere +2 > +1, así que I domina en caso de mensaje.
2. **Posible Equilibrio de Nash**:
   - Al observar la matriz, la mejor respuesta de B cuando A envía mensaje (M) es I (+2 en lugar de +1). La mejor respuesta de B cuando A no envía mensaje (N) es I (0 mejor que -1).
   - Para A, si B escoge I, su mejor respuesta es M (obtener +2 en lugar de 0).
   - Esto sugiere que (M, I) puede ser un Equilibrio de Nash (A no cambiaría a N, pues 0 < +2; B no cambiaría a G, pues +1 < +2).
   - Sin embargo, si B es manipulador y siempre hace G (por "personalidad"), cabe la posibilidad de desajustes (pues A se llevaría -2).
3. **Interpretaciones**:
   - Enviar o no "ese WhatsApp" a un/a compañero/a de clase para invitarle a estudiar juntos.
   - Las ganancias o pérdidas pueden adaptarse: a veces perder es "poner tu dignidad en riesgo" o "sufrir un ghosting".

---
