# Modelación de un Juego Repetido entre Estudiantes

A continuación se presenta un ejemplo de **formulación matemática** y su **interpretación** para modelar un juego repetido donde un mismo equipo de $E$ estudiantes realiza varios trabajos (proyectos) a lo largo de $T$ periodos. La idea es mostrar con claridad las **definiciones formales**, la **naturaleza repetida del juego** y la **intuición** detrás de las decisiones de los estudiantes.

---

## 1. Definición del juego repetido

### 1.1. Conjunto de jugadores

- Sea $N = \{1, 2, \dots, E\}$ el conjunto de jugadores (estudiantes). Supondremos que $E$ es el tamaño del equipo.

### 1.2. Horizonte de tiempo y etapas

- El juego se desarrolla a lo largo de $T$ etapas (o periodos). En cada etapa $t \in \{1, 2, \dots, T\}$, el equipo debe realizar un **trabajo** (proyecto).

### 1.3. Acciones y esfuerzos

- En cada etapa $t$, cada jugador $e \in N$ elige un nivel de esfuerzo (en horas) denotado por $h_{e,t}$. 
- Se asume que los esfuerzos pertenecen a un conjunto factible, por ejemplo, $h_{e,t} \in [0, H_{\max}]$. (Se puede ajustar según el problema: a veces se asume un presupuesto de horas totales, a veces un intervalo continuo, etc.)

### 1.4. Función de producción o calificación

- Definamos la **calificación** $G_t$ del trabajo en la etapa $t$ como una función 
  $G_t = f(H_t)$, donde $H_t = \sum_{e=1}^E h_{e,t}$.
- $f(\cdot)$ es una función que modela cómo el esfuerzo total $H_t$ se traduce en la calificación del proyecto. Por ejemplo, se podría usar una función lineal $f(H_t) = \alpha H_t$ o una función creciente concava como $f(H_t) = \sqrt{H_t}$, etc. 

### 1.5. Horas totales disponibles y ocio

- Supondremos que cada estudiante $e$ dispone de $W$ horas *por etapa* (o bien $T \cdot W$ horas para todo el horizonte).  
- El **ocio** de un estudiante en la etapa $t$ sería $W - h_{e,t}$ (suponiendo $W \ge h_{e,t}$), que representa las horas que no dedicó al proyecto.

### 1.6. Utilidad de cada jugador

Para simplificar y reflejar la **idea principal** de que cada estudiante valora simultáneamente:
1. **La calificación final** (un promedio de las calificaciones en las $T$ etapas).  
2. **El ocio total** (las horas no trabajadas en todos los proyectos).

Definamos la **utilidad total** del estudiante $e$ como:
$U_e = \underbrace{\frac{1}{T}\sum_{t=1}^T f(H_t)}_{\text{calificación final (promedio)}} + \underbrace{\sum_{t=1}^T (W - h_{e,t})}_{\text{ocio total}}$.

- La primera parte es el promedio de las calificaciones $\frac{1}{T}\sum_{t=1}^T f(H_t)$.  
- La segunda parte $\sum_{t=1}^T (W - h_{e,t})$ refleja la suma de horas de ocio que disfrutó el estudiante a lo largo de los $T$ proyectos.

> **Intuición**:  
> - Todo el equipo se beneficia de una calificación grupal $f(H_t)$ que depende de la **suma de horas**.  
> - Sin embargo, cada estudiante afronta el **costo de oportunidad** de dedicar sus horas en lugar de tener ocio.  
> - El resultado final de su decisión equilibra la preferencia por maximizar la calificación (que se reparte entre todos) y el deseo de no sacrificar más horas de las necesarias.

---

## 2. Formulación como problema de decisión (juego repetido)

### 2.1. Etapa (stage game) y estrategias

Podemos ver cada proyecto (etapa $t$) como un **juego en forma normal** donde:
- Cada jugador $e$ elige un esfuerzo $h_{e,t}$.  
- Se obtiene una calificación $G_t = f(H_t)$ compartida.  

Sin embargo, la **utilidad real** de cada estudiante no se calcula etapa por etapa, sino que se resume al final de los $T$ periodos (o mediante un criterio de descuento, si se desea modelar preferencias intertemporales). Para un **juego repetido** de horizonte finito $T$:

1. En cada etapa $t$, cada jugador observa (o no, dependiendo de la información) las acciones y resultados anteriores.  
2. Con base en esa información y en su **estrategia** (posiblemente contingente a la historia previa), decide $h_{e,t}$.  
3. Al concluir el periodo $T$, se determina la utilidad $U_e$ según la fórmula anterior.

> **Estrategia**:  
> Una **estrategia** para el jugador $e$ es una regla de decisión que especifica la acción (horas a dedicar) para cada etapa, en función de la información disponible (historial de esfuerzos previos y calificaciones). Formalmente,  
> $s_e = (s_{e,1}, s_{e,2}, \dots, s_{e,T})$,  
> donde cada $s_{e,t}$ puede depender de la historia $H^{t-1}$ (conjunto de acciones y resultados hasta la etapa $t-1$) y produce $h_{e,t}$.

### 2.2. Forma general y solución

La **forma canónica** de un juego repetido finito con acciones $\{h_{e,t}\}$ y utilidades $\{U_e\}$ puede escribirse como:

- **Jugadores**: $e \in \{1, \dots, E\}$.  
- **Conjuntos de acciones**: en cada etapa $t$, $A_e$ (en este caso $A_e = [0, H_{\max}]$).  
- **Funciones de utilidad**: $U_e( (h_{1,1},\dots,h_{1,T}), \dots, (h_{E,1},\dots,h_{E,T}) )$ definidas como arriba.  

La búsqueda de **soluciones** (por ejemplo, **equilibrios de Nash** o **equilibrios perfectos en subjuegos**) se realiza teniendo en cuenta la naturaleza repetida. Una forma típica de análisis es:

1. **Resolver el juego estático (de una sola etapa)** para ver qué pasa en equilibrio en cada etapa de manera independiente.  
2. **Incorporar la repetición** y explorar si existen estrategias de castigo y recompensa (cooperación) que permitan resultados distintos al equilibrio estático de una sola etapa. Esto depende de la posibilidad de "amenazar" con cambios de comportamiento en etapas futuras si alguien no colabora.

> **Intuición del análisis**:  
> - En un solo periodo, cada estudiante podría verse tentado a "esforzarse menos" y que otros compensen para obtener una buena calificación. Esto crea un problema de **free-rider**.  
> - Sin embargo, al repetirse el juego, se puede castigar a quien no ponga suficiente esfuerzo en un periodo (reduciendo el esfuerzo futuro o aplicando alguna sanción en la estrategia). Con ello, a veces se alcanzan niveles más altos de esfuerzo que benefician a todos.  
> - El método de solución implicará analizar estos equilibrios dinámicos, **especialmente** si $T$ es grande o si hay factores de descuento en la utilidad.

---

## 3. Problema de optimización (vista individual vs. vista colectiva)

### 3.1. Optimización individual

Cada estudiante $e$ quiere **maximizar** su utilidad $U_e$:
$\max_{\{h_{e,t}\}_{t=1}^T} \quad \frac{1}{T}\sum_{t=1}^T f(\sum_{i=1}^E h_{i,t}) + \sum_{t=1}^T (W - h_{e,t})$,

sujeto a
$0 \le h_{e,t} \le H_{\max}, \quad t = 1,\dots,T$,

y **donde** $\{h_{i,t}\}_{i\neq e}$ se asume dado (o se modela simultáneamente en equilibrio de Nash).

### 3.2. Óptimo social (colaboración perfecta)

En un escenario plenamente **colaborativo**, se podría buscar la **maximización de la suma de utilidades** o de alguna función agregada. Por ejemplo, el problema colectivo:
$\max_{\{h_{e,t}\}} \quad \sum_{e=1}^E \Big[ \frac{1}{T}\sum_{t=1}^T f(\sum_{i=1}^E h_{i,t}) + \sum_{t=1}^T (W - h_{e,t}) \Big]$.

En este caso, se busca un **óptimo social** que puede diferir de la solución de equilibrio individual (Nash), ya que internamente la cooperación está garantizada.

> **Intuición**:  
> - El óptimo social identifica cuánto **conviene** (globalmente) que cada uno contribuya para maximizar la utilidad agregada.  
> - El equilibrio de Nash (sin mecanismos de cooperación) podría llevar a un **subóptimo** por la tentación de reducir el esfuerzo y "aprovechar" el de los demás.

---

## 4. Conclusiones y visión del modelo

1. **Juego repetido**:  
   - La repetición de los trabajos (proyectos) a lo largo de $T$ periodos permite la posibilidad de diseñar estrategias de cooperación o castigo.  
   - Si $T$ es grande (o infinito con factor de descuento), hay más oportunidades de cooperar y evitar comportamientos oportunistas.

2. **Calificación compartida**:  
   - La calificación de cada proyecto $G_t = f(H_t)$ depende de la suma de esfuerzos. Esto genera un **bien colectivo** (la calificación), mientras los costos de esfuerzo (perder ocio) son individuales.  
   - Se produce un **dilema de acción colectiva** clásico: cada estudiante prefiere que otros hagan el mayor esfuerzo, pero todos se benefician si aumentan la calificación.

3. **Funciones de utilidad**:  
   - Hemos supuesto que todos los estudiantes tienen la **misma** función de utilidad y mismas preferencias.  
   - Se pueden hacer extensiones donde las funciones de utilidad difieran (por ejemplo, estudiantes con distintas capacidades o costos de oportunidad).

4. **Análisis del diseño**:  
   - Este modelo formaliza el problema de cómo se comportan los estudiantes dentro de un equipo que repite proyectos.  
   - A nivel de teoría de juegos, se analizan **equilibrios** (Nash repetido o perfecto en subjuegos) para ver qué perfiles de esfuerzo emergen y bajo qué condiciones es posible sostener cooperación.

---

### Ejemplo de simplificación adicional

Si se desea una forma **muy sencilla**, se puede suponer:
- $f(H_t) = \alpha H_t$, con $\alpha > 0$.  
- Cada estudiante tiene $W$ horas disponibles por periodo.  
- Entonces la utilidad de cada estudiante $e$ se vuelve:
  $U_e = \frac{1}{T}\sum_{t=1}^T \alpha (\sum_{i=1}^E h_{i,t}) + \sum_{t=1}^T (W - h_{e,t})$.
- El análisis de incentivos sigue el mismo patrón, pero la función lineal simplifica el cálculo de derivadas y la identificación de esfuerzos óptimos.

---

## 5. Resumen

En resumen, hemos definido **un juego repetido** con:
1. **Jugadores**: $E$ estudiantes.  
2. **Horizonte de tiempo**: $T$ proyectos (etapas).  
3. **Acciones**: cada jugador elige cuántas horas $h_{e,t}$ dedicar en cada proyecto.  
4. **Resultado (calificación)**: $G_t = f(\sum_{e=1}^E h_{e,t})$.  
5. **Utilidad individual**: promedio de las calificaciones más las horas de ocio totales.  
6. **Objetivo**: Analizar (a) cuál es la decisión individual en equilibrio de Nash repetido, y (b) cómo podría diseñarse o sostenerse la cooperación para mejorar resultados.

La **intuición** es que cada estudiante trata de equilibrar su necesidad de un buen promedio de calificación (que depende del esfuerzo total) con su preferencia por mantener la mayor cantidad de ocio (horas libres). Al estructurar esto como un **juego repetido**, se abre la posibilidad de que acuerdos cooperativos o amenazas creíbles de reducir el esfuerzo en futuros trabajos, si alguien no coopera, puedan alterar los resultados que, de otro modo, serían subóptimos desde el punto de vista del grupo.
