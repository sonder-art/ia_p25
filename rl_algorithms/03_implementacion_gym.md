# Implementación Práctica: Q-Learning y SARSA con Gymnasium

Este documento conecta la teoría de Aprendizaje por Refuerzo (RL) vista previamente con una implementación práctica utilizando la librería `gymnasium` de Python. Nos centraremos en comparar Q-Learning (off-policy) y SARSA (on-policy) en el entorno clásico `CliffWalking-v0`.

---

## 1. El Entorno: `CliffWalking-v0` de Gymnasium

Gymnasium (sucesor de OpenAI Gym) proporciona una interfaz estándar para interactuar con diversos entornos de RL. Usaremos `CliffWalking-v0`:

```text
Grid 4x12:
o o o o o o o o o o o o
o o o o o o o o o o o o
o o o o o o o o o o o o
S C C C C C C C C C C G
```

- **Objetivo**: Ir desde el inicio (S) hasta la meta (G).
- **Acciones**: Arriba, Abajo, Izquierda, Derecha.
- **Recompensas**:
    - `-1` por cada paso normal.
    - `-100` por caer al acantilado (C), lo que devuelve al agente al inicio (S).
- **Estados**: Cada celda de la cuadrícula (48 estados discretos).
- **Particularidad**: Existe un camino óptimo (más corto) justo al borde del acantilado, pero es muy arriesgado. Existe un camino más largo pero seguro, alejándose del acantilado.

Este entorno es ideal para visualizar la diferencia entre Q-Learning y SARSA:
- **Q-Learning (Off-policy)**: Aprende el valor del camino óptimo (riesgoso), ya que su actualización considera la *mejor* acción posible desde el siguiente estado, ignorando el coste de la exploración que podría llevar a caer.
- **SARSA (On-policy)**: Aprende el valor de seguir su política actual (que incluye exploración). Debido a la exploración ε-greedy, a veces caerá al acantilado. Esta penalización se incorpora a los valores Q de los estados cercanos al borde, haciendo que SARSA prefiera el camino seguro más largo.

---

## 2. Estructura del Código

Hemos organizado el código en varios archivos dentro del directorio `rl_algorithms/`:

- `requirements.txt`: Define las librerías necesarias (`gymnasium`, `numpy`, `matplotlib`, `pygame`).
- `agents.py`: Contiene la lógica de los agentes `QLearningAgent` y `SarsaAgent`.
- `visualizations.py`: Funciones para generar gráficos (recompensas, políticas, valores Q).
- `run_simulations.py`: El script principal que configura, entrena y evalúa los agentes, y llama a las visualizaciones.

---

## 3. Implementación del Agente (`agents.py`)

Ambos agentes (`QLearningAgent` y `SarsaAgent`) comparten una estructura similar pero difieren crucialmente en su método de aprendizaje.

### 3.1. Tabla Q (Q-Table)

Representamos la función de valor acción-estado \(Q(s, a)\) usando una tabla (matriz de NumPy):

```python
# En __init__ de cada agente:
self.q_table = np.zeros((env.observation_space.n, env.action_space.n))
```

- Dimensiones: `(número_de_estados, número_de_acciones)`. Para CliffWalking, es (48, 4).
- Inicialización: Se inicializa con ceros. El valor de los estados terminales o de penalización se aprende a través de las actualizaciones.

### 3.2. Hiperparámetros

Controlan el proceso de aprendizaje:

- `learning_rate` (\(\\alpha\)): Tasa de aprendizaje. Qué tanto peso le damos a la nueva información (TD error). Un valor típico es 0.1.
- `gamma` (\(\\gamma\)): Factor de descuento. Qué tanta importancia damos a las recompensas futuras. Valores cercanos a 1 (e.g., 0.99) consideran más el futuro.
- `epsilon_start`, `epsilon_decay`, `epsilon_min`: Parámetros para la exploración ε-greedy.
    - `epsilon_start`: Probabilidad inicial de explorar (e.g., 1.0).
    - `epsilon_decay`: Factor por el cual se multiplica epsilon tras cada episodio (e.g., 0.999) para reducir la exploración gradualmente.
    - `epsilon_min`: Probabilidad mínima de exploración (e.g., 0.01) para asegurar que siempre haya una pequeña chance de descubrir algo nuevo.

### 3.3. Selección de Acción (ε-Greedy)

Ambos agentes usan una política ε-greedy para balancear exploración y explotación durante el *entrenamiento*:

```python
# En choose_action(self, state):
if random.uniform(0, 1) < self.epsilon:
    # Explorar: elegir acción aleatoria
    action = self.env.action_space.sample()
else:
    # Explotar: elegir la mejor acción según la Q-Table actual
    action = self.get_best_action(state) # Llama a la función greedy
```

- Con probabilidad \(\\epsilon\), se elige una acción al azar.
- Con probabilidad \(1-\epsilon\), se elige la acción que maximiza \(Q(s, a)\) (política *greedy*). La función `get_best_action` se encarga de esto, incluyendo el desempate aleatorio si varias acciones tienen el mismo valor máximo.

Para la *evaluación* (ver el agente jugar después de entrenar), usamos `get_best_action` directamente (sin \(\\epsilon\)).

### 3.4. Actualización de Aprendizaje (TD Error)

Aquí radica la diferencia fundamental entre Q-Learning y SARSA. Ambos usan el error de diferencia temporal (TD Error), pero calculan el "valor objetivo" (la estimación mejorada del valor) de forma distinta.

El TD Error se calcula como:
\[ \delta_t = \text{Target} - Q(S_t, A_t) \]
Y la actualización es:
\[ Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha \delta_t \]

La diferencia está en el **Target**:

- **Q-Learning (`QLearningAgent.learn`)**:
  \[ \text{Target} = R_{t+1} + \gamma \max_{a'} Q(S_{t+1}, a') \]
  Usa la recompensa observada \(R_{t+1}\) más el valor descontado de la *mejor acción posible* desde el siguiente estado \(S_{t+1}\), sin importar qué acción se tomará realmente. Es **off-policy**.

  ```python
  # En QLearningAgent.learn:
  if terminated:
      target = reward
  else:
      max_next_q = np.max(self.q_table[next_state]) # Max sobre acciones futuras
      target = reward + self.gamma * max_next_q
  td_error = target - self.q_table[state, action]
  self.q_table[state, action] += self.lr * td_error
  ```

- **SARSA (`SarsaAgent.learn`)**:
  \[ \text{Target} = R_{t+1} + \gamma Q(S_{t+1}, A_{t+1}) \]
  Usa la recompensa observada \(R_{t+1}\) más el valor descontado de la acción \(A_{t+1}\) que *realmente se eligió* para el siguiente estado \(S_{t+1}\) (siguiendo la política ε-greedy actual). Es **on-policy**. El nombre SARSA viene de la tupla \( (S_t, A_t, R_{t+1}, S_{t+1}, A_{t+1}) \) usada en la actualización.

  ```python
  # En SarsaAgent.learn (requiere state, action, reward, next_state, next_action):
  if terminated:
      target = reward
  else:
      next_q = self.q_table[next_state, next_action] # Valor de la acción que se tomará
      target = reward + self.gamma * next_q
  td_error = target - self.q_table[state, action]
  self.q_table[state, action] += self.lr * td_error
  ```

---

## 4. Bucle de Simulación (`run_simulations.py`)

El script principal orquesta el proceso:

### 4.1. Configuración

Se define una lista `CONFIGS` donde cada elemento es un diccionario que especifica:
- `name`: Nombre para identificar la simulación (e.g., "Q-Learning", "SARSA").
- `agent_class`: La clase del agente a usar (`QLearningAgent` o `SarsaAgent`).
- `hyperparameters`: Un diccionario con los valores de `learning_rate`, `gamma`, `epsilon_*`.
- `episodes`: Número de episodios para el entrenamiento.

Esto permite a los estudiantes modificar fácilmente los parámetros y comparar resultados.

### 4.2. Bucle de Entrenamiento (`run_training_episode`)

Para cada episodio:
1.  Se resetea el entorno: `state, info = env.reset()`.
2.  Se elige la primera acción `action = agent.choose_action(state)`.
3.  Se entra en un bucle `while not terminated and not truncated and steps < MAX_TRAINING_STEPS`:
    a.  Se ejecuta la acción en el entorno: `next_state, reward, ... = env.step(action)`.
    b.  Se elige la *siguiente* acción (importante para SARSA): `next_action = agent.choose_action(next_state)`.
    c.  Se llama al método `agent.learn(...)`. Q-Learning usa `(state, action, reward, next_state, terminated)`. SARSA usa `(state, action, reward, next_state, next_action, terminated)`.
    d.  Se actualiza el estado y la acción para el siguiente paso: `state = next_state`, `action = next_action`.
    e.  Se acumula la recompensa y se incrementa el contador de pasos.
4.  Al final del episodio, se reduce `epsilon`: `agent.decay_epsilon()`.

El `MAX_TRAINING_STEPS` asegura que los episodios terminen incluso si el agente se queda atascado, permitiendo que el entrenamiento continúe.

---

## 5. Evaluación y Renderizado (`run_evaluation_episode`)

Después del entrenamiento, queremos ver cómo se comporta la política aprendida:

- Se ejecuta un número fijo de episodios (`NUM_RENDER_EPISODES`).
- Se crea un entorno con `render_mode="human"` para poder visualizarlo.
- En cada paso, se elige la acción *greedy* (la mejor según la Q-Table final) usando `agent.get_best_action(state)`. No hay exploración (\(\\epsilon=0\)).
- Se introduce un pequeño retraso (`RENDER_DELAY`) para poder observar la acción.
- Se aplica un límite de pasos (`MAX_EVAL_STEPS`) para evitar que la visualización se cuelgue si la política aprendida tiene bucles.

---

## 6. Visualización (`visualizations.py`)

Generamos gráficos para entender los resultados:

- `plot_rewards`: Muestra la recompensa total obtenida por episodio. Se suele aplicar una media móvil (`smoothing_window`) para ver la tendencia general del aprendizaje y comparar el rendimiento promedio de Q-Learning vs SARSA.
- `plot_policy_q_values`: Para entornos de cuadrícula como CliffWalking:
    - **Policy Grid**: Muestra una flecha en cada celda indicando la mejor acción según la Q-Table final (\(\\arg\max_a Q(s,a)\)). Permite ver visualmente el camino que seguiría el agente.
    - **Q-Value Heatmaps**: Genera un mapa de calor para cada acción posible (Arriba, Abajo, Izquierda, Derecha). La intensidad del color en cada celda indica el valor \(Q(s, a)\) aprendido para esa acción específica en ese estado. Ayuda a entender *por qué* la política elige ciertas acciones (aquellas con mayor valor Q).

---

## 7. Resultados Esperados en CliffWalking

Al ejecutar `run_simulations.py`:

- **Q-Learning**:
    - Política: Debería mostrar flechas que van justo por el borde del acantilado (camino óptimo pero arriesgado).
    - Recompensa: Puede tener mayor varianza durante el entrenamiento (caídas) pero alcanzar un promedio ligeramente mejor al final (si no cae).
    - Renderizado: Debería seguir el camino pegado al acantilado.
- **SARSA**:
    - Política: Debería mostrar flechas que se desvían hacia arriba, rodean la zona del acantilado y luego bajan (camino seguro pero subóptimo).
    - Recompensa: Debería ser más estable (menos caídas) pero con un promedio final ligeramente peor debido al camino más largo.
    - Renderizado: Debería seguir el camino seguro. Si no ha entrenado lo suficiente (pocos `episodes`), podría quedarse atascado en bucles en la zona segura, como se observó anteriormente (requiere suficientes episodios para que los valores Q diferencien claramente el camino hacia la meta).

Esta diferencia visual y en rendimiento ilustra perfectamente el compromiso entre optimalidad y seguridad derivado de las naturalezas off-policy y on-policy de los algoritmos.

---

## 8. Conclusión

Esta implementación práctica permite experimentar con Q-Learning y SARSA, modificar hiperparámetros y visualizar sus diferencias de comportamiento en un entorno diseñado para resaltarlas. Conecta los conceptos teóricos de TD error, políticas on/off-policy y exploración/explotación con código funcional y resultados observables.

---

## 9. Ejercicios Propuestos

Estos ejercicios están diseñados para profundizar la comprensión de los conceptos y experimentar con el código proporcionado (`rl_algorithms/`).

**Parte 1: Exploración de Hiperparámetros y Convergencia**

1.  **Efecto de la Tasa de Aprendizaje (\(\alpha\)):**
    *   **Tarea:** En `run_simulations.py`, modifica la `learning_rate` para Q-Learning y SARSA. Prueba valores como 0.01, 0.1 (actual), 0.5 y 0.9.
    *   **Preguntas:**
        *   ¿Cómo afecta una \(\alpha\) baja (0.01) vs. una alta (0.9) a la velocidad con la que las curvas de recompensa (gráfica `plot_rewards`) se estabilizan?
        *   ¿Observas inestabilidad (fluctuaciones grandes y erráticas en la recompensa incluso al final del entrenamiento) con valores altos de \(\alpha\)? ¿Por qué podría ocurrir esto?
        *   Compara las Policy Grids finales para \(\alpha=0.01\) y \(\alpha=0.5\). ¿Cuál parece haber aprendido una ruta más definida hacia la meta G, dado el número de episodios actual? ¿Sugiere esto que una \(\alpha\) baja podría necesitar más episodios?

2.  **Efecto del Factor de Descuento (\(\gamma\)):**
    *   **Tarea:** Compara el `gamma` actual (0.99) con uno más bajo (e.g., 0.90) en `run_simulations.py`.
    *   **Preguntas:**
        *   Observa la Policy Grid de SARSA. ¿La política se vuelve más "conservadora" (se aleja más del acantilado) o más "directa" con \(\gamma=0.90\)? ¿Por qué un \(\gamma\) más bajo haría que el agente se preocupe menos por recompensas (o penalizaciones) lejanas?
        *   ¿Esperarías que el cambio en \(\gamma\) afecte más a SARSA o a Q-Learning en este entorno? Justifica tu respuesta basándote en las políticas típicas que aprende cada uno.

3.  **Efecto de la Exploración (\(\epsilon\)):**
    *   **Tarea:** Modifica `epsilon_decay` a 0.99 (decae más rápido) y 0.9999 (decae más lento). Compara también `epsilon_min = 0.0` vs. 0.01.
    *   **Preguntas:**
        *   ¿Cómo se refleja un decaimiento más rápido (0.99) en la curva de recompensa inicial comparado con uno más lento (0.9999)? ¿Qué agente podría "estancarse" en una solución subóptima si deja de explorar demasiado pronto?
        *   ¿Hay alguna diferencia visible en el rendimiento final o la política si `epsilon_min` es 0.0? ¿Cuándo podría ser beneficioso mantener un mínimo de exploración incluso después de muchas episodios?

4.  **Importancia de los Episodios de Entrenamiento:**
    *   **Tarea:** Reduce los `episodes` para SARSA a 300. Ejecuta y observa la fase de renderizado.
    *   **Preguntas:**
        *   ¿Consigue el agente SARSA llegar a la meta consistentemente durante el renderizado, o se queda atascado en bucles (como discutimos)?
        *   Compara la Policy Grid con la obtenida con 2000 episodios. ¿Por qué la falta de episodios afecta más a SARSA en este escenario para encontrar una ruta funcional?

**Parte 2: Comparación On-Policy vs. Off-Policy**

5.  **Análisis de Heatmaps y Políticas:**
    *   **Tarea:** Ejecuta la simulación con los parámetros por defecto (o los que te dieron mejor resultado).
    *   **Preguntas:**
        *   En los Q-Value Heatmaps, mira el estado (fila=2, col=5). Compara el valor del heatmap para la acción 'Abajo' (↓) entre Q-Learning y SARSA. ¿Cuál tiene un valor más negativo? Explica por qué basándote en la diferencia entre `target = reward + gamma * max(Q(next_state))` y `target = reward + gamma * Q(next_state, next_action)`.
        *   Describe las rutas mostradas en las Policy Grids finales de Q-Learning y SARSA. ¿Cuál es objetivamente más corta? ¿Cuál es más segura? Relaciona esto directamente con los términos *on-policy* y *off-policy*.

6.  **Análisis de Recompensas:**
    *   **Tarea:** Observa el gráfico `plot_rewards`.
    *   **Preguntas:**
        *   ¿Qué algoritmo muestra "caídas" más pronunciadas en la recompensa durante el entrenamiento? ¿A qué evento del entorno corresponde esto?
        *   Aunque Q-Learning aprende la ruta óptima, ¿por qué su recompensa promedio final en la gráfica podría no ser significativamente mejor (o incluso peor a veces) que la de SARSA?

**Parte 3: Experimentación con Entornos**

7.  **Otro Entorno: FrozenLake:**
    *   **Tarea:** Cambia `ENV_NAME` a `'FrozenLake-v1'`. Prueba primero con `is_slippery=False`. Ajusta los hiperparámetros si es necesario (puede requerir más episodios, ~5000-10000).
    *   **Preguntas:**
        *   En el entorno determinista (`is_slippery=False`), ¿esperarías una gran diferencia en la política final aprendida por Q-Learning y SARSA? ¿Por qué? Ejecuta y verifica.
        *   *(Opcional)* Prueba con `is_slippery=True`. Ahora las acciones tienen un resultado estocástico (puedes resbalar). ¿Cómo afecta esto al aprendizaje? ¿Se vuelve más importante la diferencia entre on-policy y off-policy ahora? Explica.

**Parte 4: Extensiones (Opcional Avanzado)**

8.  **Implementar Expected SARSA:**
    *   **Tarea:** Crea `ExpectedSarsaAgent` en `agents.py`. El cambio principal está en el `target` dentro de `learn`. Necesitas calcular el valor esperado del siguiente estado, ponderando los Q-values del siguiente estado por la probabilidad de tomar cada acción según la política actual ε-greedy.
        *   Calcula las probabilidades \(\pi(a'|S_{t+1})\) para todas las acciones \(a'\) en el estado \(S_{t+1}\): la acción greedy \(a^* = \arg\max_a Q(S_{t+1}, a)\) tiene probabilidad \(1 - \epsilon + \epsilon / N_{acciones}\), y las otras acciones tienen probabilidad \(\epsilon / N_{acciones}\).
        *   El valor esperado es \(\sum_{a'} \pi(a'|S_{t+1}) Q(S_{t+1}, a')\).
        *   El target es \(R_{t+1} + \gamma \times \text{Valor Esperado}\).
    *   **Preguntas:** Compara la curva de recompensas de Expected SARSA con SARSA y Q-Learning. ¿Se parece más a alguno de los dos? ¿Por qué podría Expected SARSA tener menor varianza que SARSA? 