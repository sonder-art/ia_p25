# Autómatas Celulares

Este directorio contiene el material para estudiar autómatas celulares, incluyendo una introducción teórica y código para generar visualizaciones interactivas.

## Estructura del Directorio

- `00_intro.md`: Documento principal con la introducción teórica
- `cellular_automata.py`: Implementación de la clase base y funciones para autómatas celulares
- `generate_visualizations.py`: Script para generar las visualizaciones
- `requirements.txt`: Dependencias necesarias
- `plots/`: Directorio donde se guardan las visualizaciones generadas

## Requisitos

Para ejecutar el código, necesitas tener Python 3.7 o superior y las siguientes dependencias:

```bash
pip install -r requirements.txt
```

## Generando Visualizaciones

Para generar todas las visualizaciones mencionadas en el documento:

```bash
python generate_visualizations.py
```

Esto creará:
- Visualizaciones de la Regla 30 de Wolfram
- Patrones básicos del Juego de la Vida (bloque, parpadeador, planeador)
- Comparación de vecindarios (Moore vs Von Neumann)
- Evolución de patrones aleatorios

## Experimentando con el Código

Puedes crear tus propios autómatas celulares usando la clase `CellularAutomaton`. Por ejemplo:

```python
from cellular_automata import CellularAutomaton, game_of_life_rule

# Crear un autómata de 20x20
automaton = CellularAutomaton(size=(20, 20))

# Configurar un estado inicial
automaton.state[10, 10] = 1  # Activar una célula en el centro

# Evolucionar el autómata
for _ in range(10):
    automaton.update(game_of_life_rule)
```

## Visualizando Resultados

Puedes visualizar el estado actual de un autómata usando:

```python
from cellular_automata import visualize_automaton

visualize_automaton(automaton, title="Mi Autómata")
```

O crear una animación de la evolución:

```python
from cellular_automata import create_animation

create_animation(automaton, game_of_life_rule, steps=20)
```

## Contribuciones

Siéntete libre de experimentar con el código y crear tus propios patrones y reglas. Algunas ideas para explorar:

1. Implementar nuevas reglas de transición
2. Crear patrones iniciales más complejos
3. Experimentar con diferentes condiciones de frontera
4. Visualizar propiedades estadísticas de la evolución 