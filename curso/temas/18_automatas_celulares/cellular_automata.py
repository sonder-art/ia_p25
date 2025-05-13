import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.colors as mcolors
from typing import Callable, List, Tuple, Optional
import os

class CellularAutomaton:
    def __init__(self, 
                 size: Tuple[int, int],
                 initial_state: Optional[np.ndarray] = None,
                 neighborhood_type: str = 'moore',
                 boundary_condition: str = 'periodic'):
        """
        Inicializa un autómata celular.
        
        Args:
            size: Tamaño de la retícula (filas, columnas)
            initial_state: Estado inicial (opcional)
            neighborhood_type: Tipo de vecindario ('moore' o 'von_neumann')
            boundary_condition: Condición de frontera ('periodic' o 'fixed')
        """
        self.size = size
        self.neighborhood_type = neighborhood_type
        self.boundary_condition = boundary_condition
        
        if initial_state is None:
            self.state = np.zeros(size, dtype=int)
        else:
            self.state = initial_state.copy()
            
        self.history = [self.state.copy()]
        
    def get_neighbors(self, i: int, j: int) -> List[Tuple[int, int]]:
        """Obtiene las coordenadas de los vecinos de una célula."""
        if self.neighborhood_type == 'moore':
            neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1),
                        (i, j-1),           (i, j+1),
                        (i+1, j-1), (i+1, j), (i+1, j+1)]
        else:  # von_neumann
            neighbors = [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]
            
        if self.boundary_condition == 'periodic':
            return [(n[0] % self.size[0], n[1] % self.size[1]) for n in neighbors]
        else:  # fixed
            return [(n[0], n[1]) for n in neighbors 
                   if 0 <= n[0] < self.size[0] and 0 <= n[1] < self.size[1]]
    
    def count_neighbors(self, i: int, j: int) -> int:
        """Cuenta el número de vecinos vivos de una célula."""
        return sum(self.state[n[0], n[1]] for n in self.get_neighbors(i, j))
    
    def update(self, rule: Callable[[int, int], int]):
        """Actualiza el estado del autómata según una regla dada."""
        new_state = np.zeros_like(self.state)
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                new_state[i, j] = rule(self.state[i, j], self.count_neighbors(i, j))
        self.state = new_state
        self.history.append(self.state.copy())
    
    def reset(self, initial_state: Optional[np.ndarray] = None):
        """Reinicia el autómata a su estado inicial."""
        if initial_state is not None:
            self.state = initial_state.copy()
        else:
            self.state = np.zeros(self.size, dtype=int)
        self.history = [self.state.copy()]

def game_of_life_rule(state: int, neighbors: int) -> int:
    """Implementa las reglas del Juego de la Vida de Conway."""
    if state == 1:
        return 1 if neighbors in [2, 3] else 0
    else:
        return 1 if neighbors == 3 else 0

def rule_30_1d(current: int, left: int, center: int, right: int) -> int:
    """
    Implementa la Regla 30 de Wolfram para autómatas celulares unidimensionales.
    
    Args:
        current: Estado actual de la célula
        left: Estado de la célula izquierda
        center: Estado de la célula central
        right: Estado de la célula derecha
        
    Returns:
        int: Nuevo estado de la célula (0 o 1)
    """
    pattern = (left, center, right)
    if pattern in [(1,0,0), (0,1,1), (0,1,0), (0,0,1)]:
        return 1
    return 0

def rule_90_1d(current: int, left: int, center: int, right: int) -> int:
    """
    Implementa la Regla 90 de Wolfram (Triángulo de Sierpinski).
    
    Args:
        current: Estado actual de la célula
        left: Estado de la célula izquierda
        center: Estado de la célula central
        right: Estado de la célula derecha
        
    Returns:
        int: Nuevo estado de la célula (0 o 1)
    """
    return left ^ right  # XOR entre izquierda y derecha

def rule_110_1d(current: int, left: int, center: int, right: int) -> int:
    """
    Implementa la Regla 110 de Wolfram (Universal).
    
    Args:
        current: Estado actual de la célula
        left: Estado de la célula izquierda
        center: Estado de la célula central
        right: Estado de la célula derecha
        
    Returns:
        int: Nuevo estado de la célula (0 o 1)
    """
    pattern = (left, center, right)
    if pattern in [(0,0,0), (1,1,1), (1,1,0)]:
        return 0
    return 1

def rule_184_1d(current: int, left: int, center: int, right: int) -> int:
    """
    Implementa la Regla 184 de Wolfram (Modelo de Tráfico).
    
    Args:
        current: Estado actual de la célula
        left: Estado de la célula izquierda
        center: Estado de la célula central
        right: Estado de la célula derecha
        
    Returns:
        int: Nuevo estado de la célula (0 o 1)
    """
    pattern = (left, center, right)
    if pattern in [(1,1,1), (1,0,0), (0,0,0)]:
        return 0
    return 1

def rule_250_1d(current: int, left: int, center: int, right: int) -> int:
    """
    Implementa la Regla 250 de Wolfram (Estable).
    
    Args:
        current: Estado actual de la célula
        left: Estado de la célula izquierda
        center: Estado de la célula central
        right: Estado de la célula derecha
        
    Returns:
        int: Nuevo estado de la célula (0 o 1)
    """
    return center  # Simplemente mantiene el estado actual

def create_glider(size: Tuple[int, int]) -> np.ndarray:
    """Crea un planeador (glider) para el Juego de la Vida."""
    state = np.zeros(size, dtype=int)
    # Posición del planeador
    glider = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ])
    # Colocar el planeador en el centro
    center = (size[0]//2 - 1, size[1]//2 - 1)
    state[center[0]:center[0]+3, center[1]:center[1]+3] = glider
    return state

def create_blinker(size: Tuple[int, int]) -> np.ndarray:
    """Crea un parpadeador (blinker) para el Juego de la Vida."""
    state = np.zeros(size, dtype=int)
    center = (size[0]//2, size[1]//2)
    state[center[0]-1:center[0]+2, center[1]] = 1
    return state

def create_block(size: Tuple[int, int]) -> np.ndarray:
    """Crea un bloque estable para el Juego de la Vida."""
    state = np.zeros(size, dtype=int)
    center = (size[0]//2, size[1]//2)
    state[center[0]:center[0]+2, center[1]:center[1]+2] = 1
    return state

def visualize_automaton(automaton: CellularAutomaton, 
                       title: str = "Autómata Celular",
                       save_path: Optional[str] = None):
    """Visualiza el estado actual del autómata."""
    plt.figure(figsize=(8, 8))
    plt.imshow(automaton.state, cmap='binary')
    plt.title(title)
    plt.axis('off')
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.close()

def create_animation(automaton: CellularAutomaton,
                    rule: Callable[[int, int], int],
                    steps: int,
                    title: str = "Evolución del Autómata Celular",
                    save_path: Optional[str] = None):
    """Crea una animación de la evolución del autómata."""
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Crear colormap personalizado para visualización de vecindarios
    if any(3 in state for state in automaton.history):
        # Colormap para visualización de vecindarios (3 estados)
        colors = ['white', 'black', 'red', 'blue']
        cmap = mcolors.ListedColormap(colors)
    else:
        # Colormap binario normal
        cmap = 'binary'
    
    def update(frame):
        ax.clear()
        automaton.update(rule)
        ax.imshow(automaton.state, cmap=cmap)
        ax.set_title(f"{title}\nPaso {frame + 1}")
        ax.axis('off')
    
    anim = FuncAnimation(fig, update, frames=steps, interval=200)
    if save_path:
        anim.save(save_path, writer='pillow', fps=5)
    plt.close()
    return anim

def visualize_rule_30(steps: int = 100, width: int = 100, save_path: Optional[str] = None):
    """Visualiza la Regla 30 de Wolfram."""
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
    
    # Visualizar
    plt.figure(figsize=(12, 8))
    plt.imshow(state, cmap='binary')
    plt.title("Regla 30 de Wolfram")
    plt.axis('off')
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.close()

def create_rule_evolution(rule_func: Callable[[int, int, int, int], int],
                         steps: int = 100,
                         width: int = 100,
                         save_path: Optional[str] = None):
    """
    Crea una animación de la evolución de cualquier regla de Wolfram.
    
    Args:
        rule_func: Función que implementa la regla
        steps: Número de pasos de evolución
        width: Ancho de la retícula
        save_path: Ruta donde guardar la animación
    """
    # Inicializar con un solo 1 en el centro
    state = np.zeros((steps, width), dtype=int)
    state[0, width//2] = 1
    
    # Evolucionar el autómata
    for i in range(1, steps):
        for j in range(width):
            left = state[i-1, (j-1) % width]
            center = state[i-1, j]
            right = state[i-1, (j+1) % width]
            state[i, j] = rule_func(state[i-1, j], left, center, right)
    
    # Crear animación
    fig, ax = plt.subplots(figsize=(12, 8))
    
    def update(frame):
        ax.clear()
        ax.imshow(state[:frame+1], cmap='binary')
        ax.set_title(f"Evolución de la Regla\nPaso {frame + 1}")
        ax.axis('off')
    
    anim = FuncAnimation(fig, update, frames=steps, interval=100)
    if save_path:
        anim.save(save_path, writer='pillow', fps=10)
    plt.close()

def create_plots_directory():
    """Crea el directorio para las visualizaciones si no existe."""
    plots_dir = os.path.join(os.path.dirname(__file__), 'plots')
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
    return plots_dir 