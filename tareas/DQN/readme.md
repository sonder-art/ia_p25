# Implementación de Deep Q-Networks (DQN)

Este proyecto implementa un agente de Deep Q-Networks (DQN) utilizando PyTorch para resolver entornos de control proporcionados por la librería Gymnasium.

## Estructura del código

- **models.py**: Define la arquitectura de la red neuronal Q-Network utilizando PyTorch.
- **replay_buffer.py**: Implementa el buffer de experiencia para almacenar y muestrear transiciones.
- **dqn_agent.py**: Contiene la clase principal DQNAgent que integra la red Q, el buffer y los algoritmos de aprendizaje.
- **train_dqn.py**: Script principal para configurar, entrenar, evaluar y visualizar el agente.
- **requirements.txt**: Lista de dependencias necesarias.

## Características implementadas

1. **Red Neuronal Q-Network**: Una red fully-connected que mapea estados a valores Q para cada acción.
2. **Experience Replay Buffer**: Almacena transiciones (estado, acción, recompensa, siguiente estado, done) y permite muestreo aleatorio.
3. **Target Network**: Una copia de la red principal que se actualiza periódicamente para estabilizar el aprendizaje.
4. **Exploración ε-greedy**: Balance entre exploración y explotación con decaimiento exponencial de epsilon.

## Hiperparámetros utilizados

### Para CartPole-v1:

```
num_episodes = 500
buffer_capacity = 10000
batch_size = 128
gamma = 0.99
learning_rate = 1e-4
epsilon_start = 0.9
epsilon_end = 0.05
epsilon_decay = 1000
target_update = 500
```

### Para LunarLander-v2 (ajustes recomendados):

```
num_episodes = 2000
buffer_capacity = 50000
batch_size = 128
gamma = 0.99
learning_rate = 5e-4
epsilon_start = 1.0
epsilon_end = 0.01
epsilon_decay = 5000
target_update = 1000
```

## Análisis de Componentes DQN

### Efecto del Replay Buffer

**Pregunta**: ¿Cómo afecta un buffer pequeño al aprendizaje? ¿Por qué el Experience Replay es crucial para la estabilidad?

**Respuesta**: Un buffer pequeño reduce significativamente la estabilidad del aprendizaje. Esto ocurre porque:

1. **Correlación temporal**: Las muestras consecutivas en RL están altamente correlacionadas. Un buffer pequeño no puede romper estas correlaciones eficazmente, llevando a sobreajuste a secuencias específicas.
2. **Diversidad de datos**: Un buffer más grande contiene una mayor variedad de situaciones y transiciones, lo que permite un aprendizaje más general.
3. **Eficiencia de datos**: El buffer permite reutilizar experiencias múltiples veces, mejorando la eficiencia de datos.

Con un buffer demasiado pequeño (ej. 500), el aprendizaje mostró:
- Mayor varianza en las recompensas episódicas
- Convergencia más lenta 
- Mayor probabilidad de "olvidar" comportamientos previamente aprendidos

### Efecto de la Target Network

**Pregunta**: ¿Cómo afecta la actualización frecuente de la target network al aprendizaje? Explique el problema del "objetivo móvil".

**Respuesta**: Actualizar la target network con demasiada frecuencia (ej. TARGET_UPDATE=1) o eliminarla completamente provoca:

1. **Inestabilidad en el aprendizaje**: Oscilaciones severas en los valores Q y dificultad para converger.
2. **Problema del "objetivo móvil"**: En DQN, aprendemos estimando valores Q mediante bootstrapping (usando estimaciones de otros valores Q). Sin una target network separada, cada actualización de la política modifica también los objetivos que estamos tratando de alcanzar, creando un círculo vicioso que puede llevar a divergencia.

La target network proporciona objetivos estables durante múltiples pasos de actualización, permitiendo que el aprendizaje converja gradualmente hacia una política óptima.

### Efecto de la Frecuencia de Actualización del Target

**Pregunta**: ¿Hay una diferencia notable en la estabilidad o velocidad de convergencia con diferentes valores de TARGET_UPDATE?

**Respuesta**: Sí, existe un balance importante:

- **TARGET_UPDATE muy bajo (ej. 10)**: Mayor inestabilidad, similar a no tener target network.
- **TARGET_UPDATE moderado (ej. 500)**: Buen balance entre estabilidad y adaptación.
- **TARGET_UPDATE muy alto (ej. 5000)**: Aprendizaje más estable pero mucho más lento, ya que la target network tarda demasiado en incorporar las mejoras de la policy network.

El valor óptimo depende de la complejidad del entorno. Para CartPole-v1, un valor entre 200-500 funcionó bien, mientras que para LunarLander-v2, valores entre 500-1000 parecieron más apropiados.

## Ajuste de Hiperparámetros

### Tasa de Aprendizaje (Learning Rate)

**Pregunta**: ¿Cómo afecta el LR a la velocidad y estabil