import os
import numpy as np
from cellular_automata import (
    CellularAutomaton, game_of_life_rule, create_glider,
    create_blinker, create_block, visualize_automaton,
    create_animation, visualize_rule_30, create_plots_directory,
    rule_30_1d, rule_90_1d, rule_110_1d, rule_184_1d, rule_250_1d,
    create_rule_evolution
)
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from typing import Tuple

def create_neighborhood_visualization(size: Tuple[int, int], 
                                   neighborhood_type: str,
                                   steps: int,
                                   title: str,
                                   save_path: str):
    """Crea una visualización animada de cómo evoluciona un vecindario."""
    # Crear estado inicial con un patrón que muestre el vecindario
    state = np.zeros(size, dtype=int)
    center = (size[0]//2, size[1]//2)
    
    # Célula central
    state[center[0], center[1]] = 1
    
    # Vecinos según el tipo
    if neighborhood_type == 'moore':
        # 8 vecinos
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                state[center[0] + i, center[1] + j] = 2
    else:  # von_neumann
        # 4 vecinos
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            state[center[0] + i, center[1] + j] = 2
    
    # Crear autómata y animación
    automaton = CellularAutomaton(size, state, neighborhood_type=neighborhood_type)
    
    # Regla personalizada para visualizar el vecindario con efecto pulsante
    def neighborhood_rule(state: int, neighbors: int) -> int:
        if state == 1:  # Célula central
            return 1
        elif state == 2:  # Vecinos
            # Alternar entre 2 y 3 para crear efecto pulsante
            return 3 if state == 2 else 2
        return 0
    
    create_animation(
        automaton,
        neighborhood_rule,
        steps=steps,
        title=title,
        save_path=save_path
    )

def create_rule_30_evolution(save_path: str, steps: int = 100, width: int = 100):
    """Crea una animación de la evolución de la Regla 30."""
    # Inicializar con un solo 1 en el centro
    state = np.zeros((steps, width), dtype=int)
    state[0, width//2] = 1
    
    # Evolucionar el autómata
    for i in range(1, steps):
        for j in range(width):
            left = state[i-1, (j-1) % width]
            center = state[i-1, j]
            right = state[i-1, (j+1) % width]
            state[i, j] = rule_30_1d(state[i-1, j], left, center, right)
    
    # Crear animación
    fig, ax = plt.subplots(figsize=(12, 8))
    
    def update(frame):
        ax.clear()
        ax.imshow(state[:frame+1], cmap='binary')
        ax.set_title(f"Regla 30 de Wolfram\nPaso {frame + 1}")
        ax.axis('off')
    
    anim = FuncAnimation(fig, update, frames=steps, interval=100)
    anim.save(save_path, writer='pillow', fps=10)
    plt.close()

def create_glider_gun(size: Tuple[int, int]) -> np.ndarray:
    """Crea un cañón de planeadores de Gosper."""
    # Ensure the size is large enough for the gun pattern
    state = np.zeros((max(size[0], 40), max(size[1], 40)), dtype=int)
    # Posición del cañón
    gun = np.array([
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ])
    
    # Colocar el cañón en la esquina superior izquierda
    state[1:10, 1:37] = gun
    return state

def create_pulsar(size: Tuple[int, int]) -> np.ndarray:
    """Crea un pulsar (oscilador de período 3)."""
    state = np.zeros(size, dtype=int)
    center = (size[0]//2, size[1]//2)
    
    # Patrón del pulsar
    pulsar = np.array([
        [0,0,1,1,1,0,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,1,0,1,0,0,0,0,1],
        [1,0,0,0,0,1,0,1,0,0,0,0,1],
        [1,0,0,0,0,1,0,1,0,0,0,0,1],
        [0,0,1,1,1,0,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,0,0,0,1,1,1,0,0],
        [1,0,0,0,0,1,0,1,0,0,0,0,1],
        [1,0,0,0,0,1,0,1,0,0,0,0,1],
        [1,0,0,0,0,1,0,1,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,0,0,0,1,1,1,0,0]
    ])
    
    # Colocar el pulsar en el centro
    start_i = center[0] - pulsar.shape[0]//2
    start_j = center[1] - pulsar.shape[1]//2
    state[start_i:start_i+pulsar.shape[0], start_j:start_j+pulsar.shape[1]] = pulsar
    return state

def generate_all_visualizations():
    """Genera todas las visualizaciones para el documento."""
    plots_dir = create_plots_directory()
    
    # 1. Visualizaciones de las Reglas de Wolfram
    print("Generando visualizaciones de las Reglas de Wolfram...")
    
    # 1.1 Regla 30
    print("Generando visualización de la Regla 30...")
    visualize_rule_30(
        steps=100,
        width=100,
        save_path=os.path.join(plots_dir, 'rule_30.png')
    )
    create_rule_evolution(
        rule_30_1d,
        steps=100,
        width=100,
        save_path=os.path.join(plots_dir, 'rule_30_evolution.gif')
    )
    
    # 1.2 Regla 90 (Triángulo de Sierpinski)
    print("Generando visualización de la Regla 90...")
    create_rule_evolution(
        rule_90_1d,
        steps=100,
        width=100,
        save_path=os.path.join(plots_dir, 'rule_90.gif')
    )
    
    # 1.3 Regla 110 (Universal)
    print("Generando visualización de la Regla 110...")
    create_rule_evolution(
        rule_110_1d,
        steps=100,
        width=100,
        save_path=os.path.join(plots_dir, 'rule_110.gif')
    )
    
    # 1.4 Regla 184 (Tráfico)
    print("Generando visualización de la Regla 184...")
    create_rule_evolution(
        rule_184_1d,
        steps=100,
        width=100,
        save_path=os.path.join(plots_dir, 'rule_184.gif')
    )
    
    # 1.5 Regla 250 (Estable)
    print("Generando visualización de la Regla 250...")
    create_rule_evolution(
        rule_250_1d,
        steps=100,
        width=100,
        save_path=os.path.join(plots_dir, 'rule_250.gif')
    )
    
    # 2. Patrones del Juego de la Vida
    size = (50, 50)
    
    # 2.1 Patrones básicos
    print("Generando visualizaciones de patrones básicos...")
    # Bloque estable
    block = CellularAutomaton(size, create_block(size))
    visualize_automaton(
        block,
        title="Bloque Estable en el Juego de la Vida",
        save_path=os.path.join(plots_dir, 'block.png')
    )
    
    # Parpadeador
    blinker = CellularAutomaton(size, create_blinker(size))
    create_animation(
        blinker,
        game_of_life_rule,
        steps=4,
        title="Parpadeador (Blinker) en el Juego de la Vida",
        save_path=os.path.join(plots_dir, 'blinker.gif')
    )
    
    # Planeador
    glider = CellularAutomaton(size, create_glider(size))
    create_animation(
        glider,
        game_of_life_rule,
        steps=20,
        title="Planeador (Glider) en el Juego de la Vida",
        save_path=os.path.join(plots_dir, 'glider.gif')
    )
    
    # 2.2 Patrones complejos
    print("Generando visualizaciones de patrones complejos...")
    # Pulsar
    pulsar = CellularAutomaton(size, create_pulsar(size))
    create_animation(
        pulsar,
        game_of_life_rule,
        steps=12,
        title="Pulsar (Oscilador de Período 3) en el Juego de la Vida",
        save_path=os.path.join(plots_dir, 'pulsar.gif')
    )
    
    # Cañón de planeadores
    gun = CellularAutomaton(size, create_glider_gun(size))
    create_animation(
        gun,
        game_of_life_rule,
        steps=100,
        title="Cañón de Planeadores de Gosper en el Juego de la Vida",
        save_path=os.path.join(plots_dir, 'glider_gun.gif')
    )
    
    # 3. Visualizaciones de vecindarios
    print("Generando visualizaciones de vecindarios...")
    size = (20, 20)
    
    # Vecindario de Moore
    create_neighborhood_visualization(
        size=size,
        neighborhood_type='moore',
        steps=10,
        title="Vecindario de Moore (8 células)",
        save_path=os.path.join(plots_dir, 'moore_neighborhood.gif')
    )
    
    # Vecindario de Von Neumann
    create_neighborhood_visualization(
        size=size,
        neighborhood_type='von_neumann',
        steps=10,
        title="Vecindario de Von Neumann (4 células)",
        save_path=os.path.join(plots_dir, 'von_neumann_neighborhood.gif')
    )
    
    # 4. Patrones aleatorios y su evolución
    print("Generando visualizaciones de patrones aleatorios...")
    # 4.1 Patrón aleatorio simple
    size = (50, 50)
    random_state = np.random.choice([0, 1], size=size, p=[0.85, 0.15])
    random_automaton = CellularAutomaton(size, random_state)
    create_animation(
        random_automaton,
        game_of_life_rule,
        steps=50,
        title="Evolución de un Patrón Aleatorio en el Juego de la Vida",
        save_path=os.path.join(plots_dir, 'random_pattern.gif')
    )
    
    # 4.2 Múltiples patrones aleatorios
    print("Generando visualización de múltiples patrones aleatorios...")
    size = (100, 100)
    random_states = [np.random.choice([0, 1], size=size, p=[0.85, 0.15]) for _ in range(4)]
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    for i, (ax, state) in enumerate(zip(axes.flat, random_states)):
        automaton = CellularAutomaton(size, state)
        for _ in range(20):  # Evolucionar 20 pasos
            automaton.update(game_of_life_rule)
        ax.imshow(automaton.state, cmap='binary')
        ax.set_title(f"Patrón Aleatorio {i+1} después de 20 pasos")
        ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, 'multiple_random_patterns.png'), 
                bbox_inches='tight', dpi=300)
    plt.close()
    
    print(f"Todas las visualizaciones han sido generadas en: {plots_dir}")

if __name__ == "__main__":
    generate_all_visualizations() 