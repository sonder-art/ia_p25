import os
import sys
import numpy as np # For np.arange if needed, though plotting is in model script

# Determine the directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Add the script's directory to sys.path to ensure sandpile_model can be imported
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

try:
    import sandpile_model
except ImportError as e:
    print(f"Error: Could not import sandpile_model from {script_dir}.")
    print(f"Details: {e}")
    print(f"Current sys.path: {sys.path}")
    sys.exit(1)

def generate_sandpile_report():
    output_md_filename = "sandpile_report.md"
    plot_output_dir_name = "sandpile_report_plots"  # Directory name for plots for this report

    # Paths are relative to the script's directory (script_dir)
    output_md_abs_path = os.path.join(script_dir, output_md_filename)
    plot_output_full_abs_dir = os.path.join(script_dir, plot_output_dir_name)

    if not os.path.exists(plot_output_full_abs_dir):
        os.makedirs(plot_output_full_abs_dir)
        print(f"Created directory for report plots: {plot_output_full_abs_dir}")

    print("Generando gráficos para el informe del modelo de Sandpile...")

    # --- Simulation Parameters and Plot Generation ---
    rows, cols = 25, 25 # Slightly larger grid for report
    grid = sandpile_model.initialize_grid(rows, cols)
    center_r, center_c = rows // 2, cols // 2

    plot_paths = {}

    # 1. Initial State
    plot_paths['initial'] = sandpile_model.plot_sandpile_grid(
        grid, "Estado Inicial (0 Granos)", 
        plot_output_full_abs_dir, "sandpile_plot_0_initial.png")

    # 2. After a few grains (e.g., 50)
    temp_grid_50 = grid.copy()
    for _ in range(50):
        sandpile_model.add_sand(temp_grid_50, center_r, center_c, 1)
        temp_grid_50, _, _ = sandpile_model.stabilize_grid(temp_grid_50)
    plot_paths['few_grains'] = sandpile_model.plot_sandpile_grid(
        temp_grid_50, "Después de 50 Granos", 
        plot_output_full_abs_dir, "sandpile_plot_1_50_grains.png")

    # 3. Near/At Critical State (e.g., 2000 grains for a 25x25 grid - might need tuning)
    # Re-initialize for a longer run to reach critical state if needed, or continue from temp_grid_50
    # For simplicity, let's start a dedicated run for the critical state plot.
    critical_grid = sandpile_model.initialize_grid(rows, cols)
    grains_for_critical = rows * cols * (sandpile_model.SAND_THRESHOLD // 2) # Heuristic, might need more
    print(f"Simulando adición de {grains_for_critical} granos para estado crítico...")
    for i in range(grains_for_critical):
        sandpile_model.add_sand(critical_grid, np.random.randint(0,rows), np.random.randint(0,cols), 1) # Random additions
        critical_grid, _, _ = sandpile_model.stabilize_grid(critical_grid)
        if (i+1) % 500 == 0:
            print(f"... {i+1} granos añadidos para estado crítico.")
            
    plot_paths['critical_state'] = sandpile_model.plot_sandpile_grid(
        critical_grid, f"Estado Crítico (Después de {grains_for_critical} Granos)", 
        plot_output_full_abs_dir, "sandpile_plot_2_critical_state.png")

    # 4. During an avalanche (challenging to capture a specific one, let's show state before and after a large addition)
    # Use the critical_grid, add a significant amount of sand to the center to trigger a large avalanche.
    grid_before_avalanche = critical_grid.copy()
    sandpile_model.add_sand(grid_before_avalanche, center_r, center_c, sandpile_model.SAND_THRESHOLD * 5) # Add enough to make center very unstable
    plot_paths['before_large_avalanche'] = sandpile_model.plot_sandpile_grid(
        grid_before_avalanche, "Antes de una Gran Avalancha (Centro Sobrecargado)", 
        plot_output_full_abs_dir, "sandpile_plot_3a_before_avalanche.png")
    
    grid_after_avalanche, topples, duration = sandpile_model.stabilize_grid(grid_before_avalanche.copy()) # Stabilize a copy
    print(f"Avalancha inducida: Tamaño={topples}, Duración={duration}")
    plot_paths['after_large_avalanche'] = sandpile_model.plot_sandpile_grid(
        grid_after_avalanche, "Después de una Gran Avalancha", 
        plot_output_full_abs_dir, "sandpile_plot_3b_after_avalanche.png")

    print("Todos los gráficos para el informe han sido generados.")

    # --- Markdown Content Definition ---
    # Paths for MD need to be relative to the MD file itself
    md_plot_paths = {key: os.path.join(os.path.basename(plot_output_full_abs_dir), os.path.basename(path)) 
                     for key, path in plot_paths.items()}

    title_section = [
        "# El Modelo de Sandpile: Explorando la Criticalidad Auto-Organizada\n\n",
        "Este informe explora el modelo de sandpile, un ejemplo paradigmático de un sistema que exhibe **criticalidad auto-organizada (SOC)**. ",
        "Estos sistemas evolucionan espontáneamente hacia un estado crítico, donde pequeñas perturbaciones pueden desencadenar eventos de todos los tamaños, conocidos como \"avalanchas\". ",
        "El modelo de sandpile, aunque simple, captura la esencia de muchos fenómenos naturales complejos, desde terremotos y deslizamientos de tierra hasta la dinámica de los mercados financieros y las extinciones biológicas.\n\n"
    ]

    model_explanation_section = [
        "## El Modelo de Bak-Tang-Wiesenfeld (BTW)\n\n",
        "El modelo de sandpile más estudiado fue propuesto por Per Bak, Chao Tang y Kurt Wiesenfeld en 1987. Se define sobre una rejilla (grid) bidimensional, donde cada celda puede acumular \"granos de arena\". Las reglas son las siguientes:\n\n",
        "1.  **Rejilla:** Un sistema de celdas, por ejemplo, una matriz de $N \\times M$ celdas.\n",
        "2.  **Adición de Arena:** Se añaden granos de arena uno por uno a celdas seleccionadas aleatoriamente o a una celda específica (como el centro).\n",
        "3.  **Umbral de Estabilidad ($K$):** Cada celda tiene una altura $z_i$ (número de granos). Si la altura de una celda alcanza o supera un umbral crítico $K$ (típicamente $K=4$ para una rejilla 2D con 4 vecinos cardinales), la celda se vuelve inestable.\n",
        "4.  **Desmoronamiento (Toppling):** Una celda inestable ($z_i \\ge K$) se desmorona: distribuye $K$ de sus granos, pasando un grano a cada uno de sus vecinos directos (norte, sur, este, oeste). Su propia altura disminuye en $K$. En nuestro modelo, $z_i \\leftarrow z_i - 4$.\n",
        "5.  **Límites Abiertos:** Los granos que caen fuera de los bordes de la rejilla se pierden del sistema.\n",
        "6.  **Avalanchas:** Un solo desmoronamiento puede hacer que las celdas vecinas se vuelvan inestables, provocando una cascada de desmoronamientos. Esta secuencia de eventos se conoce como una avalancha. La avalancha continúa hasta que todas las celdas de la rejilla vuelvan a ser estables ($z_i < K$ para todas las $i$).\n\n",
        "A medida que se añaden granos al sistema, este evoluciona espontáneamente hacia un **estado crítico**. En este estado, la rejilla está llena de estructuras complejas y fractales, y la adición de un solo grano más tiene una probabilidad no despreciable de causar una avalancha de cualquier tamaño, desde muy pequeña hasta afectar a todo el sistema. Es esta falta de una escala característica para las avalanchas lo que define la criticalidad auto-organizada.\n\n"
    ]

    visualizations_section_intro = [
        "## Visualizando la Dinámica del Sandpile\n\n",
        "Las siguientes visualizaciones, generadas por nuestro script `sandpile_model.py`, nos ayudarán a entender cómo evoluciona el sistema.\n\n"
    ]

    plot_initial_text = [
        "### 1. Estado Inicial\n\n",
        "Comenzamos con una rejilla vacía, donde todas las celdas tienen cero granos.\n\n",
        f"![Estado Inicial del Sandpile]({md_plot_paths['initial']})\n\n"
    ]

    plot_few_grains_text = [
        "### 2. Después de Pocos Granos\n\n",
        "Tras añadir una pequeña cantidad de granos (por ejemplo, 50) al centro, vemos cómo se acumulan localmente. En esta etapa, es poco probable que se produzcan grandes avalanchas, ya que la mayoría de las celdas están muy por debajo del umbral de estabilidad.\n\n",
        f"![Sandpile Después de 50 Granos]({md_plot_paths['few_grains']})\n\n"
    ]

    plot_critical_state_text = [
        "### 3. Hacia un Estado Crítico\n\n",
        "Después de añadir una gran cantidad de granos (en este caso, se añadieron granos aleatoriamente hasta llenar significativamente la rejilla), el sistema se aproxima a su estado crítico. Observamos la formación de estructuras complejas y patrones recurrentes. En este estado, la adición de un solo grano más puede, con cierta probabilidad, desencadenar avalanchas de diversos tamaños.\n\n",
        f"![Sandpile en Estado Crítico]({md_plot_paths['critical_state']})\n\n"
    ]

    plot_avalanche_text = [
        "### 4. Observando una Avalancha\n\n",
        "Para ilustrar una avalancha, primero llevamos el sistema a un estado cercano al crítico o ya crítico. Luego, sobrecargamos deliberadamente una celda (por ejemplo, el centro) para inducir una inestabilidad significativa.\n\n",
        "**Antes de la avalancha (centro sobrecargado):**\n",
        f"![Sandpile Antes de una Gran Avalancha]({md_plot_paths['before_large_avalanche']})\n\n",
        "**Después de que la avalancha se ha propagado y el sistema se ha estabilizado:**\n",
        f"![Sandpile Después de una Gran Avalancha]({md_plot_paths['after_large_avalanche']})\n\n",
        "La diferencia entre estas dos imágenes muestra el alcance de la avalancha. El sistema ha redistribuido una cantidad significativa de arena, y la configuración final puede ser muy diferente de la inmediatamente anterior a la gran perturbación.\n\n"
    ]

    conclusion_text = [
        "## Conclusión (Preliminar)\n\n",
        "El modelo de sandpile, a pesar de sus reglas simples, demuestra cómo sistemas complejos pueden auto-organizarse en un estado crítico sin necesidad de ajustar finamente ningún parámetro externo. ",
        "Este estado se caracteriza por una susceptibilidad a perturbaciones que pueden generar respuestas (avalanchas) en todas las escalas. ",
        "Las visualizaciones generadas nos dan una idea intuitiva de esta dinámica y de la emergencia de patrones complejos a partir de interacciones locales.\n\n",
        "Exploraciones futuras podrían incluir el análisis estadístico de los tamaños y duraciones de las avalanchas para verificar la presencia de distribuciones de ley de potencias, una firma matemática de la criticalidad auto-organizada.\n"
    ]

    # --- Assemble Markdown --- 
    final_md_lines = []
    final_md_lines.extend(title_section)
    final_md_lines.extend(model_explanation_section)
    final_md_lines.extend(visualizations_section_intro)
    final_md_lines.extend(plot_initial_text)
    final_md_lines.extend(plot_few_grains_text)
    final_md_lines.extend(plot_critical_state_text)
    final_md_lines.extend(plot_avalanche_text)
    final_md_lines.extend(conclusion_text)
            
    with open(output_md_abs_path, 'w', encoding='utf-8') as f:
        f.writelines(final_md_lines)
    
    print(f"Informe del modelo de Sandpile generado en: {output_md_abs_path}")

if __name__ == "__main__":
    generate_sandpile_report() 