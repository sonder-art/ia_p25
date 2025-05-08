import os
import sys

# Determine the directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Add the script's directory to sys.path to ensure funcion_logistica can be imported
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

try:
    import funcion_logistica
except ImportError as e:
    print(f"Error: Could not import funcion_logistica from {script_dir}.")
    print(f"Details: {e}")
    print(f"Current sys.path: {sys.path}")
    sys.exit(1)

def generate_markdown_report():
    original_md_filename = "01_ecuacion_logistica.md"
    output_md_filename = "ecuacion_logistica_con_plots_reordenado.md"
    plot_output_dir_name = "plots_informe"

    original_md_abs_path = os.path.join(script_dir, original_md_filename)
    output_md_abs_path = os.path.join(script_dir, output_md_filename)
    plot_output_full_abs_dir = os.path.join(script_dir, plot_output_dir_name)

    if not os.path.exists(plot_output_full_abs_dir):
        os.makedirs(plot_output_full_abs_dir)
        print(f"Created directory for plots: {plot_output_full_abs_dir}")

    print("Generando gráficos para el informe reordenado...")
    bifurcation_plot_path = funcion_logistica.create_interactive_bifurcation_static(
        output_dir=plot_output_full_abs_dir, filename="bifurcation_diagram_static.png")
    specific_behaviors_plot_path = funcion_logistica.visualize_specific_behaviors(
        output_dir=plot_output_full_abs_dir, filename="specific_behaviors.png")
    chaos_zoom_plot_path = funcion_logistica.plot_chaos_zoom(
        output_dir=plot_output_full_abs_dir, filename="chaos_zoom_windows.png")
    sensitivity_plot_path = funcion_logistica.plot_sensitivity_effect(
        output_dir=plot_output_full_abs_dir, filename="sensitivity_effect.png")
    print(f"Gráficos generados y guardados en: {plot_output_full_abs_dir}")

    md_bifurcation_plot_path = os.path.join(plot_output_dir_name, os.path.basename(bifurcation_plot_path))
    md_specific_behaviors_plot_path = os.path.join(plot_output_dir_name, os.path.basename(specific_behaviors_plot_path))
    md_chaos_zoom_plot_path = os.path.join(plot_output_dir_name, os.path.basename(chaos_zoom_plot_path))
    md_sensitivity_plot_path = os.path.join(plot_output_dir_name, os.path.basename(sensitivity_plot_path))

    try:
        with open(original_md_abs_path, 'r', encoding='utf-8') as f:
            md_content_lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Original Markdown file not found at {original_md_abs_path}")
        return

    final_md_lines = []
    inserted_flags = {
        'history_interpret': False, 'fixed_points_intro': False,
        'bifurcation_plot': False, 'zoom_plot': False,
        'specific_behaviors_plot': False, 'sensitivity_plot': False
    }

    historical_interpretive_text_parts = [
        "\n\n#### Profundizando en el Modelo Poblacional: El Caso de los Conejos\n\n",
        "Para entender mejor el significado de $x_n$ y $r$, imaginemos que estamos modelando una población de conejos en una isla con recursos limitados. \n\n",
        "- **$x_n$ (Población Normalizada):** Representa la población de conejos en la generación $n$, pero no en número absoluto, sino como una fracción de la máxima población que la isla puede sostener (su *capacidad de carga*). Así, $x_n=0$ significa que no hay conejos, $x_n=1$ significa que la población ha alcanzado el máximo sostenible, y $x_n=0.5$ indica que la población está a la mitad de su capacidad de carga.\n\n",
        "- **$r$ (Tasa de Crecimiento y Fertilidad):** Este parámetro es crucial y encapsula la tasa reproductiva neta de los conejos. Un valor de $r$ más alto implica que los conejos son más fértiles o tienen una mayor tasa de supervivencia. \n",
        "  - Si $r$ es muy bajo (entre 0 y 1), la población no es sostenible y se extinguirá ($x_n \\to 0$). Por ejemplo, si $r=0.5$, cada conejo en promedio no logra reemplazarse a sí mismo antes de morir.\n",
        "  - Si $r$ está entre 1 y 3, la población tiende a estabilizarse en un valor de equilibrio. Por ejemplo, con $r=2$, la población podría estabilizarse al 50% de la capacidad de carga ($x^* = (2-1)/2 = 0.5$).\n",
        "  - Es cuando $r$ supera el valor de 3 que comenzamos a ver comportamientos más complejos: la población ya no se estabiliza, sino que empieza a oscilar, y eventualmente, para valores de $r$ aún mayores (cercanos a 4), estas oscilaciones se vuelven caóticas, haciendo imposible predecir la población a largo plazo a pesar de la simplicidad de la ecuación.\n\n",
        "El término $(1-x_n)$ es el factor de *limitación ambiental*. A medida que la población $x_n$ se acerca a la capacidad máxima (1), $(1-x_n)$ se acerca a 0, frenando el crecimiento.\n"
    ]

    fixed_points_intro_text_parts = [
        "\n\n### Comprendiendo los Puntos Fijos\n\n",
        "Antes de adentrarnos en la complejidad, es fundamental entender los **puntos fijos** del sistema. Un punto fijo, $x^*$, es un valor de la población que, una vez alcanzado, permanece constante en las siguientes generaciones. Es decir, si $x_n = x^*$, entonces $x_{n+1} = x^*$. Matemáticamente, satisfacen la ecuación $x^* = rx^*(1-x^*)$.\n\n",
        "Los puntos fijos son cruciales porque representan los **estados de equilibrio** del sistema. Indican hacia dónde podría tender la población a largo plazo bajo ciertas condiciones. Analizar su existencia y estabilidad (si una pequeña perturbación aleja al sistema del punto fijo, ¿regresa a él o se aleja más?) es el primer paso para caracterizar la dinámica del mapa logístico.\n"
    ]

    bifurcation_text_parts = [
        "\n\n#### Visualización de las Bifurcaciones: El Diagrama de Bifurcación\n\n",
        "El diagrama de bifurcación es una herramienta visual poderosa que ilustra cómo cambia el comportamiento a largo plazo de la población ($x_n$) a medida que varía el parámetro de crecimiento $r$. Cada valor de $r$ en el eje horizontal tiene asociados en el eje vertical los valores de $x_n$ a los que el sistema tiende tras un período transitorio.\n\n",
        f"![Diagrama de Bifurcación del Mapa Logístico]({md_bifurcation_plot_path})\n\n",
        "Este diagrama revela claramente la \"ruta hacia el caos\":\n",
        "- Para $1 < r < 3$, la población se estabiliza en un único valor (un punto fijo estable).\n",
        "- En $r=3$, este punto fijo pierde estabilidad y da lugar a un ciclo de período 2: la población comienza a oscilar entre dos valores.\n",
        "- A medida que $r$ aumenta, este ciclo de período 2 se bifurca en un ciclo de período 4, luego 8, y así sucesivamente, en una cascada de duplicaciones de período. Esta secuencia es universal para muchos sistemas que transitan al caos y está relacionada con las constantes de Feigenbaum.\n",
        "- Para $r \\gtrsim 3.57$, el sistema entra en un régimen mayoritariamente caótico, donde la población ya no sigue un patrón periódico simple y los valores de $x_n$ pueden llenar densas regiones del espacio de estados.\n"
    ]

    zoom_text_parts = [
        "\n\n#### Un Vistazo Más Cercano: Ventanas de Periodicidad en el Caos\n\n",
        "Dentro del aparente desorden del régimen caótico, existen \"ventanas de periodicidad\" – regiones estrechas de $r$ donde el sistema retorna sorpresivamente a un comportamiento periódico (por ejemplo, ciclos de período 3, 5, etc.). Estas ventanas también experimentan sus propias cascadas de bifurcaciones hacia el caos.\n\n",
        f"![Zoom en el Diagrama de Bifurcación: Ventanas de Periodicidad]({md_chaos_zoom_plot_path})\n\n",
        "La imagen superior magnifica una porción del diagrama de bifurcación en la zona caótica, revelando estas islas de orden. La más prominente es la ventana de período 3 alrededor de $r \\approx 3.83$. Esto subraya la compleja estructura fractal subyacente al comportamiento caótico.\n"
    ]

    specific_behaviors_text_parts = [
        "\n\n#### Evolución Temporal: Series de Tiempo para Diferentes Regímenes\n\n",
        "Las series temporales nos permiten observar directamente cómo evoluciona la población $x_n$ a lo largo de las generaciones $n$ para valores específicos de $r$. La siguiente gráfica muestra ejemplos de los distintos comportamientos dinámicos:\n\n",
        f"![Series Temporales para Diferentes Regímenes del Mapa Logístico]({md_specific_behaviors_plot_path})\n\n",
        "Interpretación de las series:\n",
        "- **Punto Fijo Estable (e.g., $r=2.9$):** La población converge a un valor constante.\n",
        "- **Ciclo de Período 2 (e.g., $r=3.2$):** La población oscila entre dos valores.\n",
        "- **Ciclo de Período 4 (e.g., $r=3.5$):** La oscilación se repite cada cuatro generaciones.\n",
        "- **Comportamiento Caótico (e.g., $r=3.9$):** La población fluctúa de manera irregular y no periódica, exhibiendo la impredictibilidad característica del caos.\n"
    ]

    sensitivity_plot_text_parts = [
        "\n\n#### El Efecto Mariposa: Sensibilidad Extrema a las Condiciones Iniciales\n\n",
        "Una característica definitoria del caos determinista es la sensibilidad extrema a las condiciones iniciales, popularmente conocida como el \"efecto mariposa\". Esto significa que dos trayectorias que comienzan con valores iniciales de población ($x_0$) infinitesimalmente cercanos divergirán exponencialmente con el tiempo si el sistema está en un régimen caótico.\n\n",
        f"![Sensibilidad a Condiciones Iniciales en el Mapa Logístico (Efecto Mariposa)]({md_sensitivity_plot_path})\n\n",
        "En la gráfica, dos poblaciones iniciales, $x_0$ (azul) y $x_0'$ (rojo), difieren en una cantidad minúscula. Inicialmente, sus trayectorias son casi indistinguibles. Sin embargo, después de unas pocas generaciones, las trayectorias divergen drásticamente. La línea verde (en escala logarítmica en el eje Y derecho) muestra cómo la diferencia absoluta entre las dos poblaciones crece exponencialmente, haciendo imposible la predicción a largo plazo a pesar de conocer perfectamente la ecuación que las rige.\n"
    ]

    # Phase 1: Initial sections (Intro, Equation, Rabbit Analogy, Descifrando)
    current_original_md_line_idx = 0
    while current_original_md_line_idx < len(md_content_lines):
        line = md_content_lines[current_original_md_line_idx]
        final_md_lines.append(line)
        current_original_md_line_idx += 1
        if "representa el mapa logístico: una función que determina la población en la siguiente generación ($x_{n+1}$) a partir de la población actual ($x_n$)" in line and not inserted_flags['history_interpret']:
            final_md_lines.extend(historical_interpretive_text_parts)
            inserted_flags['history_interpret'] = True
        if "## 12. Análisis Matemático del Mapa Logístico" in line:  # Found start of Section 12
            break  # Exit Phase 1 loop, Section 12 title is now in final_md_lines

    # Phase 2: Mathematical Analysis (Fixed Points, Bifurcations, Chaos with plots)
    # Insert Fixed Points Intro right after Section 12 title (which was the last line added in Phase 1)
    if not inserted_flags['fixed_points_intro']:
        final_md_lines.extend(fixed_points_intro_text_parts)
        inserted_flags['fixed_points_intro'] = True

    # Process content of Section 12 (12.1, 12.2, 12.3) and insert plots
    in_section_12_2 = False
    while current_original_md_line_idx < len(md_content_lines):
        line = md_content_lines[current_original_md_line_idx]
        if "### 12.1 Puntos Fijos y su Estabilidad" in line:
            in_section_12_2 = False  # Reset if we re-encounter 12.1 for some reason
        elif "### 12.2 Bifurcaciones y Duplicación de Periodo" in line:
            in_section_12_2 = True
        elif "### 12.3 Régimen Caótico y Ventanas de Periodicidad" in line:
            if in_section_12_2:  # Means we are exiting 12.2 and entering 12.3
                if not inserted_flags['bifurcation_plot']:
                    final_md_lines.extend(bifurcation_text_parts)
                    inserted_flags['bifurcation_plot'] = True
                if not inserted_flags['zoom_plot']:
                    final_md_lines.extend(zoom_text_parts)
                    inserted_flags['zoom_plot'] = True
            in_section_12_2 = False
        elif "## 13. Visualizaciones Clave para Comprender el Caos Logístico" in line:  # End of Section 12
            if in_section_12_2:  # If Section 12 ends with 12.2 content
                if not inserted_flags['bifurcation_plot']:
                    final_md_lines.extend(bifurcation_text_parts)
                    inserted_flags['bifurcation_plot'] = True
                if not inserted_flags['zoom_plot']:
                    final_md_lines.extend(zoom_text_parts)
                    inserted_flags['zoom_plot'] = True
            final_md_lines.append(line)  # Add the ## 13 title
            current_original_md_line_idx += 1
            break  # Exit Phase 2 loop
        final_md_lines.append(line)
        current_original_md_line_idx += 1
        if current_original_md_line_idx >= len(md_content_lines) and in_section_12_2:  # Reached EOF while in 12.2
            if not inserted_flags['bifurcation_plot']:
                final_md_lines.extend(bifurcation_text_parts)
                inserted_flags['bifurcation_plot'] = True
            if not inserted_flags['zoom_plot']:
                final_md_lines.extend(zoom_text_parts)
                inserted_flags['zoom_plot'] = True
            break  # Exit Phase 2 loop (EOF)

    # Phase 3: Visualizations (Series Temporales, Sensibilidad) and Remaining Content
    # current_original_md_line_idx should be at the start of Section 13 content or EOF

    # Helper to add original subsection content before plot insertion
    def add_original_subsection_content(start_idx, stop_headings_list_h3, stop_headings_list_h2):
        temp_buffer = []
        idx = start_idx
        while idx < len(md_content_lines):
            content_line = md_content_lines[idx]
            is_stop_h3 = any(sh3 in content_line for sh3 in stop_headings_list_h3)
            is_stop_h2 = any(sh2 in content_line for sh2 in stop_headings_list_h2)
            if is_stop_h3 or is_stop_h2:
                break
            temp_buffer.append(content_line)
            idx += 1
        final_md_lines.extend(temp_buffer)
        return idx  # Return new current_original_md_line_idx

    while current_original_md_line_idx < len(md_content_lines):
        line = md_content_lines[current_original_md_line_idx]
        if "### 13.1 El Diagrama de Bifurcación" in line:  # Handle redundant 13.1
            final_md_lines.append(line)  # Add the title of 13.1
            current_original_md_line_idx += 1
            # Skip the body of the original 13.1 section
            while current_original_md_line_idx < len(md_content_lines):
                next_line = md_content_lines[current_original_md_line_idx]
                if next_line.startswith("### ") or next_line.startswith("## "):
                    break
                current_original_md_line_idx += 1
            continue  # Continue to the next line in outer loop, which is now start of 13.2 or other
        elif "### 13.2 Series Temporales y sus Patrones" in line and not inserted_flags['specific_behaviors_plot']:
            final_md_lines.append(line)
            current_original_md_line_idx = add_original_subsection_content(
                current_original_md_line_idx + 1,
                ["### 13.1", "### 13.3", "### 13.4"],
                ["## 14."]
            )
            final_md_lines.extend(specific_behaviors_text_parts)
            inserted_flags['specific_behaviors_plot'] = True
            continue
        elif "### 13.4 Visualización de la Sensibilidad a Condiciones Iniciales" in line and not inserted_flags['sensitivity_plot']:
            final_md_lines.append(line)
            current_original_md_line_idx = add_original_subsection_content(
                current_original_md_line_idx + 1,
                ["### 13.1", "### 13.2", "### 13.3"],
                ["## 14."]
            )
            final_md_lines.extend(sensitivity_plot_text_parts)
            inserted_flags['sensitivity_plot'] = True
            continue
        final_md_lines.append(line)
        current_original_md_line_idx += 1

    with open(output_md_abs_path, 'w', encoding='utf-8') as f:
        f.writelines(final_md_lines)
    
    print(f"Markdown reordenado generado en: {output_md_abs_path}")
    for item_name, status in inserted_flags.items():
        if not status:
            print(f"Advertencia: El contenido/gráfico '{item_name}' no pudo ser insertado. Verifique los puntos de anclaje y la lógica del script.")

if __name__ == "__main__":
    generate_markdown_report() 