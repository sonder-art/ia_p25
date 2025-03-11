Clave_Unica _____________________________________________ (Poner el nombre cause perder 100 puntos en el examen)  
Coloca tu clave unica en la esquina superior derecha en cada hoja adicional de respuestas.

# Parcial 1
## 1. Teoría
### 1.1 Teoría de Jaynes (25 puntos)
Define puntualmente cuál es el objetivo del robot de E.T. Jaynes descrito en el capítulo 1 de su libro *Probability: The Logic of Science*, y cuáles son los tres Desiderata que plantea. Describe brevemente y de manera puntual. Sé puntual en el objetivo del robot usando los Desiderata.

### Forma Canónica del Problema de Decisión (versión breve para el caso discreto)
Considera el siguiente **problema de decisión estático bajo incertidumbre**, con **espacios discretos** (la versión continua se obtiene reemplazando la suma por la integral) tanto para los estados de la naturaleza como para la información disponible. Luego de observar un valor $z$ de la variable aleatoria $Z$, se resuelve el siguiente problema de optimización:

**Problema de Optimización** (Versión de maximización):  
$\max_{d \in D} \;\sum_{\omega \in \Omega} p(\omega \mid z)\,U(d,\omega) \quad\text{sujeto a}\quad g_i(d)\,\leq\,0,\;i \in I, \quad h_j(d)\,=\,0,\;j \in J,$

**Elementos del Problema**:  
1. $\Omega$ es el **conjunto discreto** de todos los posibles estados de la naturaleza.
2. $Z$ es una **variable aleatoria discreta** que representa la información observada antes de tomar la decisión.
3. $p(\omega \mid z)$ es la **probabilidad posterior** del estado $\omega$ dado que se ha observado $z$. En la versión clásica del problema se usa estadística bayesiana, por ahora cualquier 'heurística' o algoritmo para inferir esto es válida. Cumple con la condición de normalización:
$\sum_{\omega \in \Omega} p(\omega \mid z) = 1.$
4. $D$ es el **conjunto de decisiones factibles** disponibles.
5. $U(d,\omega)$ es la **función de utilidad**, que mide la utilidad obtenida al tomar la decisión $d$ cuando ocurre el estado $\omega$.
6. $g_i(d) \leq 0$, $i \in I$, representan las **restricciones de desigualdad** sobre las decisiones.
7. $h_j(d) = 0$, $j \in J$, representan las **restricciones de igualdad** sobre las decisiones.

La **meta** del problema es maximizar la **utilidad esperada** bajo incertidumbre. En la versión más sencilla la distribución posterior $p(\omega \mid z)$.  

Este es el teorema de Bayes por si lo necesitan:  
$p(\omega \mid z) \;=\; \frac{p(z \mid \omega)\,p(\omega)} {\sum_{\omega' \in \Omega} p(z \mid \omega')\,p(\omega')}.$  

Para los siguientes problemas, cuando se te pida definir de manera **formal** o matemática el problema de decisión basta con definir el **Problema de Optimización** de manera correcta y describir cada uno de los **Elementos del Problema**. Además se puede requerir que expliques el **algoritmo** o **heurísticas** que utilizaste para proponer la solución al problema, incluyendo cómo estimaste **$p(\omega|z)$**, el algoritmo de optimización que usaste y demás especificaciones de cómo resolviste el problema.

## 2. Tareas
### 2.1 Definición del Problema 1 (25 puntos)
Describe de forma detallada pero breve el problema de decisión que planteaste de tarea siguiendo el siguiente orden:

**a.** Describe en lenguaje natural (texto) el problema o situación que elegiste.

**b.** Define formalmente (de manera matemática) el problema como un problema de decisión, especificando claramente cada variable. Básicamente traduce la **Forma Canónica del Problema de Decisión** a tu problema en específico y explica qué significa cada variable y función para el problema de decisión que tienes. Puede que no tengas restricciones.

**c.** Explica detalladamente por qué elegiste esa función a optimizar (utilidad) y cuál es su significado en el contexto de tu problema.

### 2.2 Algoritmo de Solución/Heurísticas 2 (25 puntos)
Ahora explica brevemente el algoritmo(s) que utilizaste para resolver tu problema de decisión, el por qué lo utilizaste y qué significa. 

a. Especifica si encuentra la solución óptima y si no lo hace por qué es buena aproximación.

## 3. Proyecto
### 3.1 Definir el Problema (25 puntos)
Define formalmente el problema de decisión del simulador de zombies, necesitas cumplir con los siguientes dos requisitos:

**a.** Define de manera detallada y explícita el problema de decisión que resolviste en el simulador de zombies. Incluye intuición de por qué definiste el problema así para cada elemento. No tienes que incluir la parte algorítmica, esto es para la siguiente pregunta. Solo define el problema de decisión, y para cada elemento describe muy puntual y detalladamente qué significa cada cosa. Es traducir la **Forma Canónica del Problema de Decisión** a este problema.

**b.** Para el caso de la función de utilidad explica a detalle por qué elegiste esa función de utilidad. Justifica su diseño matemático y fundamento moral.

**Nota:** Recuerda que existen restricciones en este problema. 

### 3.2 Solución Algorítmica (45 puntos)
Ahora para cada una de las situaciones planteadas describe qué hiciste para solucionarla, incluye el algoritmo y la intuición. Los escenarios son los siguientes:

a. No tienen acceso a datos, solo al grafo de la ciudad

b. No tienen acceso a datos, pero sí conocen el significado de los medidores y tendrán datos específicos de los medidores para la ciudad.

c. Tienen acceso a unos cuantos datos (unos 100), y pueden utilizar estadística o matemática básica (no machine learning)

d. Puedes hacer lo que quieras  
  
Para cada escenario debes describir el algoritmo/heurísticas que usaste para resolver el problema. No es necesario escribir el algoritmo en pseudocódigo basta con describirlo en texto natural mientras expliques la intuición, y lógica de manera explícita. Para cada situación debes explicar los siguientes puntos si aplican:  

1. Algoritmos o heurísticas para estimar $p(\omega|z)$
2. Algoritmos o heurísticas para asignar los recursos
3. Algoritmos o heurísticas para elegir el `path` o camino óptimo.
4. Otros algoritmos o heurísticas importantes

### 3.3 Nuevo Problema (50 puntos)
Ahora, modifica el problema anterior considerando que los `items` tienen costos diferentes. Antes, cada ítem tenía un costo de 1 unidad, pero ahora tienen un costo específico, denotado por $c_b$, $c_t$, $c_e$, donde:
* **b**: balas
* **t**: trajes de radiación
* **e**: explosivos

Sin entrar en detalles adicionales, plantea formalmente cómo cambiaría el problema de decisión considerando esta nueva restricción. Básicamente es traducir la **Forma Canónica del Problema de Decisión** pero a este problema.

**Nota:** Piensa si la solución óptima es simplemente agregar una restricción sobre la suma del costo de los ítems. Esto también te puede ayudar para la pregunta anterior.
