import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import os

# ==================== FUNCIONES BÁSICAS ====================

def logistic_map(x, r):
    """Función del mapa logístico: x_{n+1} = r * x_n * (1 - x_n)"""
    return r * x * (1 - x)

def iterate_logistic(x0, r, n_iterations):
    """Itera el mapa logístico n veces desde x0"""
    x = np.zeros(n_iterations)
    x[0] = x0
    
    for i in range(1, n_iterations):
        x[i] = logistic_map(x[i-1], r)
    
    return x

def compute_bifurcation_diagram(r_min, r_max, n_points, x0, n_discard, n_save):
    """Calcula un diagrama de bifurcación simple"""
    r_values = np.linspace(r_min, r_max, n_points)
    x_values = []
    r_bifurcation = []
    
    for r in r_values:
        x = x0
        # Descartar transitorios
        for _ in range(n_discard):
            x = logistic_map(x, r)
        
        # Guardar valores después del transitorio
        for _ in range(n_save):
            x = logistic_map(x, r)
            x_values.append(x)
            r_bifurcation.append(r)
    
    return np.array(r_bifurcation), np.array(x_values)

# ==================== VISUALIZACIONES CLAVE ====================

def create_chaos_overview(output_dir="plots", filename="chaos_overview.png"):
    """Crea una visualización simple que muestra el camino del orden al caos y la guarda."""
    fig, axes = plt.subplots(3, 1, figsize=(10, 12))
    
    # 1. Diagrama de bifurcación: la visualización más clara del caos
    r_values, bifurcation_data = compute_bifurcation_diagram(2.5, 4.0, 500, 0.5, 200, 100)
    
    axes[0].plot(r_values, bifurcation_data, ',', color='blue', alpha=0.8, markersize=0.5)
    axes[0].set_title('Diagrama de Bifurcación: Ruta al Caos', fontsize=14)
    axes[0].set_xlabel('Parámetro r', fontsize=12)
    axes[0].set_ylabel('Valores Estacionarios', fontsize=12)
    axes[0].set_xlim(2.5, 4.0)
    axes[0].set_ylim(0, 1)
    
    # Marcar regiones clave
    axes[0].axvspan(2.5, 3.0, alpha=0.2, color='green', label='Punto Fijo')
    axes[0].axvspan(3.0, 3.45, alpha=0.2, color='yellow', label='Ciclo 2')
    axes[0].axvspan(3.45, 3.57, alpha=0.2, color='orange', label='Duplicación de Periodo')
    axes[0].axvspan(3.57, 4.0, alpha=0.2, color='red', label='Caos')
    
    axes[0].axvline(x=3.0, color='k', linestyle='--')
    axes[0].axvline(x=3.45, color='k', linestyle='--')
    axes[0].axvline(x=3.57, color='k', linestyle='--')
    
    axes[0].legend(loc='upper left')
    
    # 2. Serie temporal para diferentes valores de r (orden vs caos)
    r_values_to_show = [2.9, 3.2, 3.5, 3.9]
    colors = ['green', 'blue', 'purple', 'red']
    labels = ['r=2.9 (Punto Fijo)', 'r=3.2 (Ciclo 2)', 'r=3.5 (Ciclo 4)', 'r=3.9 (Caos)']
    
    for r, color, label in zip(r_values_to_show, colors, labels):
        x_series = iterate_logistic(0.5, r, 100)
        # Solo mostrar las últimas 50 iteraciones (después del transitorio)
        axes[1].plot(range(50, 100), x_series[50:], '.-', color=color, alpha=0.8, label=label, markersize=5)
    
    axes[1].set_title('Series Temporales: Orden vs Caos', fontsize=14)
    axes[1].set_xlabel('Iteración', fontsize=12)
    axes[1].set_ylabel('Valor x_n', fontsize=12)
    axes[1].set_ylim(0, 1)
    axes[1].legend(loc='upper right')
    axes[1].grid(True, alpha=0.3)
    
    # 3. Sensibilidad a condiciones iniciales (característica definitoria del caos)
    r_chaos = 3.9
    x0_1 = 0.5
    x0_2 = 0.5001  # Diferencia mínima
    
    n_iter = 50
    x_series1 = iterate_logistic(x0_1, r_chaos, n_iter)
    x_series2 = iterate_logistic(x0_2, r_chaos, n_iter)
    
    # Calcular la diferencia entre trayectorias
    difference = np.abs(x_series2 - x_series1)
    
    # Graficar las dos trayectorias juntas
    ax_twin = axes[2].twinx()
    
    axes[2].plot(range(n_iter), x_series1, 'b.-', label=f'x₀ = {x0_1}', alpha=0.7)
    axes[2].plot(range(n_iter), x_series2, 'r.-', label=f'x₀ = {x0_2}', alpha=0.7)
    axes[2].set_ylim(0, 1)
    axes[2].set_ylabel('Valor x_n', fontsize=12, color='blue')
    axes[2].tick_params(axis='y', labelcolor='blue')
    
    # Graficar la diferencia en escala logarítmica
    ax_twin.plot(range(n_iter), difference, 'g-', linewidth=2, label='Diferencia')
    ax_twin.set_yscale('log')
    ax_twin.set_ylabel('Diferencia (log)', fontsize=12, color='green')
    ax_twin.tick_params(axis='y', labelcolor='green')
    
    axes[2].set_title(f'Efecto Mariposa: Sensibilidad a Condiciones Iniciales (r={r_chaos})', fontsize=14)
    axes[2].set_xlabel('Iteración', fontsize=12)
    axes[2].legend(loc='upper left')
    ax_twin.legend(loc='lower right')
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath)
    plt.close(fig)
    return filepath

def create_interactive_bifurcation_static(output_dir="plots", filename="interactive_bifurcation_static.png"):
    """Crea un diagrama de bifurcación (estado inicial de la versión interactiva) y lo guarda."""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Valores iniciales
    r_min_init = 2.5
    r_max_init = 4.0
    x0 = 0.5
    
    # Calcular diagrama inicial
    r_values, bifurcation_data = compute_bifurcation_diagram(r_min_init, r_max_init, 500, x0, 200, 100)
    
    # Gráficar diagrama
    ax.scatter(r_values, bifurcation_data, s=0.5, c='blue', alpha=0.8)
    
    ax.set_title('Diagrama de Bifurcación (Estático)', fontsize=14)
    ax.set_xlabel('Parámetro r', fontsize=12)
    ax.set_ylabel('Valores Estacionarios', fontsize=12)
    ax.set_xlim(r_min_init, r_max_init)
    ax.set_ylim(0, 1)
    
    # Añadir anotaciones para regiones clave
    annotation_y = 1.05
    ax.annotate('Punto Fijo', xy=(2.75, annotation_y), xycoords=('data', 'axes fraction'),
               ha='center', va='bottom', fontsize=10, color='green')
    
    ax.annotate('Ciclo 2', xy=(3.2, annotation_y), xycoords=('data', 'axes fraction'),
               ha='center', va='bottom', fontsize=10, color='orange')
    
    ax.annotate('Ciclo 4', xy=(3.45, annotation_y), xycoords=('data', 'axes fraction'),
               ha='center', va='bottom', fontsize=10, color='red')
    
    ax.annotate('Caos', xy=(3.7, annotation_y), xycoords=('data', 'axes fraction'),
               ha='center', va='bottom', fontsize=10, color='purple')
    
    # Dibujar líneas verticales para las bifurcaciones principales
    ax.axvline(x=3.0, color='k', linestyle='--', alpha=0.5)
    ax.axvline(x=3.45, color='k', linestyle='--', alpha=0.5)
    ax.axvline(x=3.57, color='k', linestyle='--', alpha=0.5)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath)
    plt.close(fig)
    return filepath

def plot_chaos_zoom(output_dir="plots", filename="chaos_zoom.png"):
    """Muestra una ampliación de la región caótica con las ventanas de periodicidad y la guarda."""
    fig, axes = plt.subplots(2, 1, figsize=(12, 12))
    
    # 1. Vista general del diagrama de bifurcación
    r_values, bifurcation_data = compute_bifurcation_diagram(2.5, 4.0, 1000, 0.5, 200, 100)
    
    axes[0].plot(r_values, bifurcation_data, ',', color='blue', alpha=0.8, markersize=0.5)
    axes[0].set_title('Diagrama de Bifurcación Completo', fontsize=14)
    axes[0].set_xlabel('Parámetro r', fontsize=12)
    axes[0].set_ylabel('Valores Estacionarios', fontsize=12)
    axes[0].set_xlim(2.5, 4.0)
    axes[0].set_ylim(0, 1)
    
    # Resaltar región a ampliar
    axes[0].axvspan(3.7, 3.9, alpha=0.3, color='red')
    
    # 2. Zoom en la región caótica (3.7-3.9) mostrando ventanas de periodicidad
    r_values_zoom, bifurcation_data_zoom = compute_bifurcation_diagram(3.7, 3.9, 2000, 0.5, 300, 100)
    
    axes[1].plot(r_values_zoom, bifurcation_data_zoom, ',', color='blue', alpha=0.8, markersize=0.5)
    axes[1].set_title('Zoom: Ventanas de Periodicidad dentro del Caos (r = 3.7-3.9)', fontsize=14)
    axes[1].set_xlabel('Parámetro r', fontsize=12)
    axes[1].set_ylabel('Valores Estacionarios', fontsize=12)
    
    # Destacar ventanas específicas
    # Ventana de periodo 3 cerca de r = 3.83
    axes[1].axvspan(3.82, 3.84, alpha=0.3, color='green')
    axes[1].annotate('Ventana\nde periodo 3', xy=(3.83, 0.7), xytext=(3.83, 0.5),
                   arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
                   ha='center', fontsize=10)
    
    # Otras ventanas
    axes[1].axvspan(3.74, 3.75, alpha=0.3, color='orange')
    axes[1].annotate('Ventana\nde periodo 5', xy=(3.745, 0.5), xytext=(3.745, 0.3),
                   arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
                   ha='center', fontsize=10)
    
    axes[1].axvspan(3.88, 3.89, alpha=0.3, color='purple')
    axes[1].annotate('Ventana\nde periodo 3', xy=(3.885, 0.2), xytext=(3.885, 0.4),
                   arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
                   ha='center', fontsize=10)
    
    plt.tight_layout()
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath)
    plt.close(fig)
    return filepath

def visualize_specific_behaviors(output_dir="plots", filename="specific_behaviors.png"):
    """Visualiza comportamientos específicos para valores clave de r y los guarda."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    # 1. Punto fijo (r = 2.9)
    r1 = 2.9
    x_series1 = iterate_logistic(0.5, r1, 100)
    
    axes[0].plot(range(50, 100), x_series1[50:], 'g.-', markersize=8)
    axes[0].axhline(y=(r1-1)/r1, color='r', linestyle='--', 
                   label=f'Punto fijo = {(r1-1)/r1:.3f}')
    axes[0].set_title(f'Punto Fijo (r = {r1})', fontsize=14)
    axes[0].set_ylabel('Valor x_n', fontsize=12)
    axes[0].set_ylim(0, 1)
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # 2. Ciclo de periodo 2 (r = 3.2)
    r2 = 3.2
    x_series2 = iterate_logistic(0.5, r2, 100)
    
    axes[1].plot(range(50, 100), x_series2[50:], 'b.-', markersize=8)
    axes[1].set_title(f'Ciclo de Periodo 2 (r = {r2})', fontsize=14)
    axes[1].set_ylabel('Valor x_n', fontsize=12)
    axes[1].set_ylim(0, 1)
    axes[1].grid(True, alpha=0.3)
    
    # 3. Ciclo de periodo 4 (r = 3.5)
    r3 = 3.5
    x_series3 = iterate_logistic(0.5, r3, 100)
    
    axes[2].plot(range(50, 100), x_series3[50:], 'm.-', markersize=8)
    axes[2].set_title(f'Ciclo de Periodo 4 (r = {r3})', fontsize=14)
    axes[2].set_xlabel('Iteración', fontsize=12)
    axes[2].set_ylabel('Valor x_n', fontsize=12)
    axes[2].set_ylim(0, 1)
    axes[2].grid(True, alpha=0.3)
    
    # 4. Comportamiento caótico (r = 3.9)
    r4 = 3.9
    x_series4 = iterate_logistic(0.5, r4, 100)
    
    axes[3].plot(range(50, 100), x_series4[50:], 'r.-', markersize=8)
    axes[3].set_title(f'Comportamiento Caótico (r = {r4})', fontsize=14)
    axes[3].set_xlabel('Iteración', fontsize=12)
    axes[3].set_ylabel('Valor x_n', fontsize=12)
    axes[3].set_ylim(0, 1)
    axes[3].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath)
    plt.close(fig)
    return filepath

def plot_sensitivity_effect(output_dir="plots", filename="sensitivity_effect.png", r_chaos=3.9, x0_1=0.5, x0_2=0.50000000001, n_iter=60):
    """Visualiza el efecto mariposa (sensibilidad a condiciones iniciales) y guarda el gráfico."""
    fig, ax = plt.subplots(figsize=(10, 6))

    x_series1 = iterate_logistic(x0_1, r_chaos, n_iter)
    x_series2 = iterate_logistic(x0_2, r_chaos, n_iter)
    
    difference = np.abs(x_series2 - x_series1)
    
    # Graficar las dos trayectorias juntas
    ax.plot(range(n_iter), x_series1, 'b.-', label=f'x₀ = {x0_1}', alpha=0.7, markersize=5)
    ax.plot(range(n_iter), x_series2, 'r.-', label=f'x₀ = {x0_2}', alpha=0.7, markersize=5)
    ax.set_ylim(0, 1)
    ax.set_ylabel('Valor x_n', fontsize=12)
    ax.tick_params(axis='y')
    
    # Graficar la diferencia en escala logarítmica en un eje Y secundario
    ax_twin = ax.twinx()
    ax_twin.plot(range(n_iter), difference, 'g--', linewidth=2, label='Diferencia |x₁ - x₂|') # Dashed line for difference
    ax_twin.set_yscale('log')
    ax_twin.set_ylabel('Diferencia (escala log)', fontsize=12, color='green')
    ax_twin.tick_params(axis='y', labelcolor='green')
    
    ax.set_title(f'Efecto Mariposa: Sensibilidad a Condiciones Iniciales (r={r_chaos})', fontsize=14)
    ax.set_xlabel('Iteración (n)', fontsize=12)
    
    # Combine legends
    lines, labels = ax.get_legend_handles_labels()
    lines2, labels2 = ax_twin.get_legend_handles_labels()
    ax_twin.legend(lines + lines2, labels + labels2, loc='upper left')
    
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath)
    plt.close(fig)
    return filepath

# ==================== FUNCIÓN PRINCIPAL ====================

def main():
    """Función principal que genera y guarda las visualizaciones clave."""
    print("\n=== La Ecuación Logística: Generando y Guardando Visualizaciones ===\n")
    
    output_dir = "plots_generated_by_script"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Crear figuras y guardar
    # path_overview = create_chaos_overview(output_dir=output_dir, filename="chaos_overview.png") # No longer primary
    # print(f"Visión general del caos guardada en: {path_overview}")
    
    path_bifurcation = create_interactive_bifurcation_static(output_dir=output_dir, filename="interactive_bifurcation_static.png")
    print(f"Diagrama de bifurcación estático guardado en: {path_bifurcation}")
    
    path_zoom = plot_chaos_zoom(output_dir=output_dir, filename="chaos_zoom_windows.png")
    print(f"Zoom en región caótica guardado en: {path_zoom}")
    
    path_behaviors = visualize_specific_behaviors(output_dir=output_dir, filename="specific_behaviors.png")
    print(f"Comportamientos específicos guardados en: {path_behaviors}")

    path_sensitivity = plot_sensitivity_effect(output_dir=output_dir, filename="sensitivity_effect.png") # Added call
    print(f"Efecto de sensibilidad guardado en: {path_sensitivity}")
    
    print("\nTodas las figuras han sido generadas y guardadas en el directorio:", output_dir)

if __name__ == "__main__":
    main()