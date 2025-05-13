import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
from typing import Tuple, List, Dict, Any
import seaborn as sns
from matplotlib.colors import ListedColormap, BoundaryNorm
import networkx as nx

class VonNeumannVisualizer:
    def __init__(self, plots_dir: str = 'curso/temas/18_automatas_celulares/plots'):
        """Initialize the visualizer with a directory for plots."""
        self.plots_dir = plots_dir
        os.makedirs(plots_dir, exist_ok=True)
        self.setup_style()
    
    def setup_style(self):
        """Setup the visualization style."""
        try:
            plt.style.use('seaborn-v0_8-whitegrid')
        except OSError:
            plt.style.use('seaborn-whitegrid')
        sns.set_theme(style="whitegrid")
        
        self.detailed_colors = plt.get_cmap('tab20', 29)
        self.base_colors = ListedColormap(['#FFFFFF', '#1f77b4', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f'])
        
        plt.rcParams['figure.figsize'] = [12, 8]
        plt.rcParams['font.size'] = 10
        plt.rcParams['axes.titlesize'] = 12
        plt.rcParams['axes.labelsize'] = 10
        plt.rcParams['animation.writer'] = 'pillow'

    def create_state_visualization(self, base_size: Tuple[int, int] = (5, 5)):
        """Create a detailed visualization of von Neumann's 29 states, grouped by function."""
        # Define state groups and their corresponding colors
        state_groups = {
            "Transmisión": (list(range(1, 5)), '#1f77b4'),      # Indices 1-4
            "Construcción": (list(range(5, 9)), '#2ca02c'),     # Indices 5-8 (simplified grouping)
            "Control": (list(range(9, 13)), '#d62728'),        # Indices 9-12 (simplified grouping)
            "Memoria": (list(range(13, 19)), '#9467bd'),      # Indices 13-18 (simplified grouping)
            "Sensibilización/Especial": (list(range(19, 26)), '#ff7f0e'), # Indices 19-25
            "Disolución/Otros": (list(range(26, 30)), '#7f7f7f'),  # Indices 26-29
        }
        # State 0 is quiescent (background)

        num_states = 29
        cols = 6 # Max columns
        num_plots = num_states + len(state_groups) # States + Group titles
        rows = int(np.ceil(num_plots / cols))

        fig, axes = plt.subplots(rows, cols, figsize=(18, rows * 3.5))
        fig.suptitle('Estados Funcionales del Autómata de Von Neumann (Representación Esquemática)', fontsize=18, y=0.98)
        axes_flat = axes.flatten()

        # Use a distinct colormap for the states within their blocks
        cmap_states = plt.get_cmap('viridis', num_states + 1) # +1 for background 0
        norm_states = BoundaryNorm(np.arange(num_states + 1) - 0.5, cmap_states.N)

        plot_idx = 0
        state_id_counter = 1 # Start from state 1

        # Add titles and states for each group
        for group_name, (state_ids_in_group, group_color) in state_groups.items():
            
            # Add Group Title
            if plot_idx < len(axes_flat):
                ax_title = axes_flat[plot_idx]
                ax_title.text(0.5, 0.5, group_name, ha='center', va='center', fontsize=14, fontweight='bold', color=group_color)
                ax_title.axis('off')
                plot_idx += 1
            
            # Plot states within this group
            for state_id in state_ids_in_group:
                if state_id <= num_states and plot_idx < len(axes_flat): # Ensure we don't exceed 29 states
                    ax = axes_flat[plot_idx]
                    
                    state_grid = np.zeros(base_size)
                    # Make a simple pattern
                    state_grid[base_size[0]//2, base_size[1]//2] = state_id 
                    if base_size[0] > 2 and base_size[1] > 2:
                         state_grid[base_size[0]//2-1:base_size[0]//2+2, base_size[1]//2-1:base_size[1]//2+2] = state_id * 0.7 # Dimmer border

                    im = ax.imshow(state_grid, cmap=cmap_states, norm=norm_states, interpolation='nearest')
                    ax.set_title(f'Estado {state_id}', fontsize=10)
                    ax.set_xticks([])
                    ax.set_yticks([])
                    ax.patch.set_edgecolor(group_color) # Color border based on group
                    ax.patch.set_linewidth(2)

                    plot_idx += 1
                    state_id_counter += 1

        # Turn off any remaining unused subplots
        for i in range(plot_idx, len(axes_flat)):
            axes_flat[i].axis('off')
            
        # Add a colorbar (optional, might be redundant with labels)
        # fig.colorbar(im, ax=axes.ravel().tolist(), orientation='horizontal', fraction=0.02, pad=0.08, aspect=50,
        #                     label="Identificador Numérico del Estado")

        fig.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to prevent title overlap
        
        save_path = os.path.join(self.plots_dir, 'von_neumann_states.png')
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Saved state visualization to {save_path}")
        plt.close(fig)
    
    def create_state_evolution_animation(self, size: Tuple[int, int] = (20, 20), steps: int = 50):
        """Create an animation showing how states evolve over time."""
        grid = np.zeros(size)
        grid[size[0]//2, size[1]//2] = 1
        
        fig, ax = plt.subplots(figsize=(12, 12))
        
        def update(frame):
            ax.clear()
            if frame < 10:
                # Show transmission states
                grid[size[0]//2-frame:size[0]//2+frame+1, size[1]//2-frame:size[1]//2+frame+1] = 1
                phase = "Transmisión"
            elif frame < 20:
                # Show construction states
                grid[size[0]//2-frame:size[0]//2+frame+1, size[1]//2-frame:size[1]//2+frame+1] = 2
                phase = "Construcción"
            elif frame < 30:
                # Show control states
                grid[size[0]//2-frame:size[0]//2+frame+1, size[1]//2-frame:size[1]//2+frame+1] = 3
                phase = "Control"
            else:
                # Show memory states
                grid[size[0]//2-frame:size[0]//2+frame+1, size[1]//2-frame:size[1]//2+frame+1] = 4
                phase = "Memoria"
            
            im = ax.imshow(grid, cmap=self.colors)
            ax.set_title(f'Evolución de Estados - Fase: {phase}\nPaso {frame}')
            plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        
        anim = FuncAnimation(fig, update, frames=steps, interval=200)
        anim.save(os.path.join(self.plots_dir, 'state_evolution.gif'), writer='pillow')
        plt.close()
    
    def create_self_replication_animation(self, grid_size: int = 40, steps: int = 120):
        """Create a schematic animation of the self-replication process with clearer phases."""
        grid = np.zeros((grid_size, grid_size))
        original_pos = (grid_size // 4, grid_size // 2)
        new_pos = (3 * grid_size // 4, grid_size // 2)
        
        # Simple representation of a structure
        structure = np.array([[1,1,1],[1,2,1],[1,1,1]]) # Added a central element (2)
        struct_h, struct_w = structure.shape

        # Define distinct colors/values for different elements/phases
        # 0: Background (White)
        # 1: Original Structure Body (Blue)
        # 2: Original Structure Core (Lighter Blue)
        # 3: Construction Arm/Signal (Green)
        # 4: New Structure Body (being built) (Light Green)
        # 5: New Structure Core (being built) (Yellow)
        # 6: Copied Instruction Signal (Red)
        # 7: Activated Original Core (Purple)
        # 8: Activated New Core (Orange)
        cmap = ListedColormap(['white', '#1f77b4', '#aec7e8', '#2ca02c', '#98df8a', '#FFFF00', '#d62728', '#9467bd', '#ff7f0e'])
        norm = BoundaryNorm(np.arange(cmap.N + 1) - 0.5, cmap.N)
        
        def place_structure(g, pos, structure_array, base_value=1):
            h, w = structure_array.shape
            top, left = pos[0] - h // 2, pos[1] - w // 2
            g[top:top+h, left:left+w] = np.where(structure_array > 0, structure_array + base_value - 1, 0)

        # Place initial structure (values 1 and 2)
        place_structure(grid, original_pos, structure, base_value=1)

        fig, ax = plt.subplots(figsize=(11,11))
        im = ax.imshow(grid, cmap=cmap, norm=norm, interpolation='nearest')
        phase_text = ax.text(0.5, 1.05, "", ha='center', va='center', transform=ax.transAxes, fontsize=12)

        def update(frame):
            current_grid = np.zeros_like(grid) # Start fresh each frame for clarity
            phase_desc = ""
            current_step = frame + 1

            # --- Phase 1: Reading Instructions --- (e.g., first 25% of steps)
            if frame < steps // 4:
                phase_desc = f"1. Lectura (Paso {current_step}/{steps})"
                # Show original structure, maybe core flashes (using value 2 -> 7 -> 2)
                core_val = 7 if (frame // 4) % 2 == 0 else 2
                temp_struct = structure.copy()
                temp_struct[temp_struct == 2] = core_val
                place_structure(current_grid, original_pos, temp_struct, base_value=1)
                
            # --- Phase 2: Construction --- (e.g., steps 25% to 50%)
            elif frame < steps // 2:
                phase_desc = f"2. Construcción (Paso {current_step}/{steps})"
                place_structure(current_grid, original_pos, structure, base_value=1) # Original is static
                
                # Simulate construction arm / progress
                progress = (frame - steps // 4) / (steps // 4)
                arm_len = int(progress * (new_pos[0] - original_pos[0]))
                if arm_len > 0:
                    current_grid[original_pos[0] : original_pos[0] + arm_len, original_pos[1]] = 3 # Construction signal/arm
                
                # Build new structure progressively (values 4 and 5)
                rows_to_show = int(np.ceil(struct_h * progress))
                cols_to_show = int(np.ceil(struct_w * progress))
                if rows_to_show > 0 and cols_to_show > 0:
                     sub_structure_mask = np.zeros_like(structure)
                     sub_structure_mask[:rows_to_show, :cols_to_show] = 1
                     building_structure = structure * sub_structure_mask
                     place_structure(current_grid, new_pos, building_structure, base_value=4)
            
            # --- Phase 3: Copying Instructions --- (e.g., steps 50% to 75%)
            elif frame < 3 * steps // 4:
                phase_desc = f"3. Copia Instr. (Paso {current_step}/{steps})"
                place_structure(current_grid, original_pos, structure, base_value=1) # Original
                place_structure(current_grid, new_pos, structure, base_value=4)     # New structure complete
                
                # Simulate copying signal (value 6)
                copy_progress = (frame - steps // 2) / (steps // 4)
                signal_pos = int(original_pos[0] + copy_progress * (new_pos[0] - original_pos[0]))
                current_grid[signal_pos, original_pos[1]:new_pos[1]+1] = 6 # Signal path
                # Flash core of new structure as it receives instructions?
                if (frame // 3) % 2 == 0:
                     temp_struct_new = structure.copy()
                     temp_struct_new[temp_struct_new == 2] = 5 # Use yellow for receiving core
                     place_structure(current_grid, new_pos, temp_struct_new, base_value=4)
            
            # --- Phase 4: Activation --- (e.g., steps 75% to 100%)
            else:
                phase_desc = f"4. Activación (Paso {current_step}/{steps})"
                # Show both structures with activated cores (values 7 and 8)
                activated_orig_struct = structure.copy()
                activated_orig_struct[activated_orig_struct == 2] = 7 # Purple core
                place_structure(current_grid, original_pos, activated_orig_struct, base_value=1)
                
                activated_new_struct = structure.copy()
                activated_new_struct[activated_new_struct == 2] = 8 # Orange core
                place_structure(current_grid, new_pos, activated_new_struct, base_value=4)
                
                # Optional: activation signal flash
                if frame == 3 * steps // 4:
                    current_grid[new_pos[0]-1 : new_pos[0]+2, new_pos[1]-1 : new_pos[1]+2] = 8

            im.set_data(current_grid)
            phase_text.set_text(f'Proceso de Auto-replicación Esquemático\n{phase_desc}')
            ax.set_title('') # Remove old title, use text annotation instead
            return [im, phase_text]

        anim = FuncAnimation(fig, update, frames=steps, interval=150, blit=True)
        save_path = os.path.join(self.plots_dir, 'self_replication.gif')
        anim.save(save_path)
        print(f"Saved self-replication animation to {save_path}")
        plt.close(fig)
    
    def create_neighborhood_visualization(self, size: Tuple[int, int] = (7, 7)):
        grid_vn = np.zeros(size)
        center = (size[0]//2, size[1]//2)
        grid_vn[center[0], center[1]] = 2
        for r_offset, c_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= center[0] + r_offset < size[0] and 0 <= center[1] + c_offset < size[1]:
                grid_vn[center[0] + r_offset, center[1] + c_offset] = 1
        
        grid_moore = np.zeros(size)
        grid_moore[center[0], center[1]] = 2
        for r_offset in [-1, 0, 1]:
            for c_offset in [-1, 0, 1]:
                if r_offset == 0 and c_offset == 0: continue
                if 0 <= center[0] + r_offset < size[0] and 0 <= center[1] + c_offset < size[1]:
                     grid_moore[center[0] + r_offset, center[1] + c_offset] = 1
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
        cmap_neigh = ListedColormap(['#FFFFFF', '#FFC0CB', '#00008B'])
        
        im1 = ax1.imshow(grid_vn, cmap=cmap_neigh, interpolation='nearest')
        ax1.set_title('Vecindario de Von Neumann', fontsize=11)

        im2 = ax2.imshow(grid_moore, cmap=cmap_neigh, interpolation='nearest')
        ax2.set_title('Vecindario de Moore', fontsize=11)
        
        for ax_ in [ax1, ax2]:
            ax_.set_xticks([])
            ax_.set_yticks([])
            for r_idx in range(size[0]):
                ax_.axhline(r_idx - 0.5, color='gray', linewidth=0.5)
            for c_idx in range(size[1]):
                ax_.axvline(c_idx - 0.5, color='gray', linewidth=0.5)

        fig.suptitle('Tipos de Vecindarios en Autómatas Celulares', fontsize=14)
        fig.tight_layout(rect=[0,0,1,0.95])
        plt.savefig(os.path.join(self.plots_dir, 'neighborhoods.png'), dpi=150, bbox_inches='tight')
        plt.close(fig)
    
    def create_state_transition_diagram(self):
        G = nx.DiGraph()
        state_types = ['Transmisión', 'Construcción', 'Control', 'Memoria']
        colors = ['#87CEEB', '#90EE90', '#FFB6C1', '#FFFFE0']
        
        for i, state_type in enumerate(state_types):
            G.add_node(state_type, color=colors[i])
        
        transitions = [
            ('Transmisión', 'Construcción'), ('Construcción', 'Control'),
            ('Control', 'Memoria'), ('Memoria', 'Transmisión'),
            ('Control', 'Construcción')
        ]
        G.add_edges_from(transitions)
        
        fig, ax = plt.subplots(figsize=(10, 7))
        node_colors_map = [G.nodes[node]['color'] for node in G.nodes()]
        pos = nx.circular_layout(G)
        
        nx.draw(G, pos, ax=ax, with_labels=True, node_color=node_colors_map, node_size=4500, 
                font_size=9, font_weight='bold', arrowsize=20, edge_color='gray', width=1.5)
        ax.set_title('Diagrama Esquemático de Transiciones entre Tipos de Estado', fontsize=14, pad=20)
        plt.savefig(os.path.join(self.plots_dir, 'state_transitions.png'), dpi=150, bbox_inches='tight')
        plt.close(fig)
    
    def _simple_ca_update(self, grid, rule_type='game_of_life'):
        new_grid = grid.copy()
        changed_cells_mask = np.zeros_like(grid, dtype=bool) # To track changes
        rows, cols = grid.shape
        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if i == 0 and j == 0: continue
                        nr, nc = (r + i + rows) % rows, (c + j + cols) % cols
                        if grid[nr, nc] == 1: # Assuming 1 is the 'live' state for simplicity
                            live_neighbors += 1
                
                current_cell_state = grid[r,c]
                new_cell_state = current_cell_state

                if rule_type == 'game_of_life':
                    if current_cell_state == 1: # Live cell
                        if live_neighbors < 2 or live_neighbors > 3: 
                            new_cell_state = 0 # Dies
                    else: # Dead cell
                        if live_neighbors == 3: 
                            new_cell_state = 1 # Becomes live
                elif rule_type == 'rule30_like': # A more active rule for variety
                    if current_cell_state == 1:
                        if live_neighbors == 1 or live_neighbors == 4 or live_neighbors == 5: # Example: survives with 1,4,5
                           new_cell_state = 1
                        else:
                           new_cell_state = 0 
                    else:
                        if live_neighbors == 2 or live_neighbors == 3: # Example: birth with 2,3
                           new_cell_state = 1
                
                if new_cell_state != current_cell_state:
                    new_grid[r, c] = new_cell_state
                    changed_cells_mask[r,c] = True

        return new_grid, changed_cells_mask

    def create_transition_rules_animation(self, grid_size: int = 30, steps: int = 50):
        """Illustrate generic transition rules in action (Game of Life) with highlighted changes."""
        grid = np.random.choice([0, 1], size=(grid_size, grid_size), p=[0.7, 0.3]) # More sparse for clarity
        
        fig, ax = plt.subplots(figsize=(8,8))
        # Colors: 0=White (dead), 1=Black (alive), 2=Red (just changed)
        cmap_ca = ListedColormap(['#FFFFFF', '#000000', '#FF0000'])
        norm = BoundaryNorm([-0.5, 0.5, 1.5, 2.5], cmap_ca.N)
        
        display_grid = grid.copy()
        im = ax.imshow(display_grid, cmap=cmap_ca, norm=norm, interpolation='nearest')
        ax.set_xticks([])
        ax.set_yticks([])
        title = ax.set_title(f'Aplicación de Reglas (Ej: Juego de la Vida) - Paso 1', fontsize=11)
        
        def update(frame):
            nonlocal grid, display_grid
            new_grid_state, changed_mask = self._simple_ca_update(grid, 'game_of_life')
            grid = new_grid_state
            
            # Create display grid: 0 for dead, 1 for alive, 2 for just changed
            display_grid = grid.copy()
            display_grid[changed_mask] = 2 # Highlight changed cells
            
            im.set_data(display_grid)
            title.set_text(f'Aplicación de Reglas (Ej: Juego de la Vida) - Paso {frame+1}')
            return [im, title]

        anim = FuncAnimation(fig, update, frames=steps, interval=200, blit=True)
        save_path = os.path.join(self.plots_dir, 'transition_rules.gif')
        anim.save(save_path)
        print(f"Saved transition rules animation to {save_path}")
        plt.close(fig)

    def create_emergent_patterns_animation(self, grid_size: int = 60, steps: int = 150):
        """Show emergence of patterns from simple rules (Game of Life like) with highlights."""
        grid = np.zeros((grid_size, grid_size))
        # Add a glider
        glider = np.array([[0,1,0],[0,0,1],[1,1,1]])
        grid[5:5+glider.shape[0], 5:5+glider.shape[1]] = glider
        # Add a puffer train starter
        grid[30, 10:13] = 1
        grid[31, 10] = 1
        grid[32, 11] = 1

        fig, ax = plt.subplots(figsize=(9,9))
        # Colors: 0=White, 1=DarkGreen (stable/moving), 2=LightGreen (just changed)
        cmap_ca = ListedColormap(['#FFFFFF', '#006400', '#90EE90'])
        norm = BoundaryNorm([-0.5, 0.5, 1.5, 2.5], cmap_ca.N)
        
        display_grid = grid.copy()
        im = ax.imshow(display_grid, cmap=cmap_ca, norm=norm, interpolation='nearest')
        ax.set_xticks([])
        ax.set_yticks([])
        title = ax.set_title(f'Emergencia de Patrones (Ej: Planeadores) - Paso 1', fontsize=11)

        def update(frame):
            nonlocal grid, display_grid
            new_grid_state, changed_mask = self._simple_ca_update(grid, 'game_of_life')
            grid = new_grid_state
            
            display_grid = grid.copy()
            display_grid[changed_mask] = 2 # Highlight changed cells

            im.set_data(display_grid)
            title.set_text(f'Emergencia de Patrones (Ej: Planeadores) - Paso {frame+1}')
            return [im, title]

        anim = FuncAnimation(fig, update, frames=steps, interval=120, blit=True)
        save_path = os.path.join(self.plots_dir, 'emergent_patterns.gif')
        anim.save(save_path)
        print(f"Saved emergent patterns animation to {save_path}")
        plt.close(fig)

    def create_temporal_evolution_animation(self, grid_size: int = 40, steps: int = 70):
        """Show temporal evolution of a structure (using a more active custom rule) with highlights."""
        grid = np.zeros((grid_size, grid_size))
        # Start with a small, asymmetric seed
        grid[grid_size//2, grid_size//2] = 1
        grid[grid_size//2 + 1, grid_size//2 + 1] = 1
        grid[grid_size//2 - 1, grid_size//2 + 1] = 1

        fig, ax = plt.subplots(figsize=(8,8))
        # Colors: 0=White, 1=Indigo (stable), 2=Plum (just changed)
        cmap_ca = ListedColormap(['#FFFFFF', '#4B0082', '#DDA0DD'])
        norm = BoundaryNorm([-0.5, 0.5, 1.5, 2.5], cmap_ca.N)
        
        display_grid = grid.copy()
        im = ax.imshow(display_grid, cmap=cmap_ca, norm=norm, interpolation='nearest')
        ax.set_xticks([])
        ax.set_yticks([])
        title = ax.set_title(f'Evolución Temporal de una Estructura - Paso 1', fontsize=11)

        def update(frame):
            nonlocal grid, display_grid
            # Use the more active rule here
            new_grid_state, changed_mask = self._simple_ca_update(grid, 'rule30_like') 
            grid = new_grid_state

            display_grid = grid.copy()
            display_grid[changed_mask] = 2 # Highlight changed cells
            
            im.set_data(display_grid)
            title.set_text(f'Evolución Temporal de una Estructura - Paso {frame+1}')
            return [im, title]

        anim = FuncAnimation(fig, update, frames=steps, interval=180, blit=True) # Slightly slower interval
        save_path = os.path.join(self.plots_dir, 'temporal_evolution.gif')
        anim.save(save_path)
        print(f"Saved temporal evolution animation to {save_path}")
        plt.close(fig)

    def create_ullman_comparison(self, size_vn: Tuple[int, int] = (5,6), size_ul: Tuple[int,int] = (2,4)):
        vn_display_grid = np.full(size_vn, -1, dtype=float)
        for i in range(29):
            row, col = i // size_vn[1], i % size_vn[1]
            if row < size_vn[0]: vn_display_grid[row, col] = i + 1
        
        ul_display_grid = np.full(size_ul, -1, dtype=float)
        for i in range(8):
            row, col = i // size_ul[1], i % size_ul[1]
            if row < size_ul[0]: ul_display_grid[row, col] = i + 1
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        cmap_comp = plt.get_cmap('viridis', 30)
        cmap_comp.set_under('lightgray')

        im1 = ax1.imshow(vn_display_grid, cmap=cmap_comp, vmin=0, vmax=29, interpolation='nearest')
        ax1.set_title(f'Autómata de Von Neumann\n({vn_display_grid[vn_display_grid != -1].size} estados representados)', fontsize=10)
        fig.colorbar(im1, ax=ax1, fraction=0.046, pad=0.04, label="ID del Estado")
        
        im2 = ax2.imshow(ul_display_grid, cmap=cmap_comp, vmin=0, vmax=8, interpolation='nearest')
        ax2.set_title(f'Autómata de Ullman\n({ul_display_grid[ul_display_grid != -1].size} estados representados)', fontsize=10)
        fig.colorbar(im2, ax=ax2, fraction=0.046, pad=0.04, label="ID del Estado")

        for ax_ in [ax1, ax2]:
            ax_.set_xticks([])
            ax_.set_yticks([])

        fig.suptitle('Comparación Esquemática de Conjuntos de Estados', fontsize=14)
        fig.tight_layout(rect=[0,0,1,0.93])
        plt.savefig(os.path.join(self.plots_dir, 'state_comparison.png'), dpi=150, bbox_inches='tight')
        plt.close(fig)
    
    def create_dna_analogy(self):
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 12))
        sns.set_style("whitegrid")

        x = np.linspace(0, 10, 100)
        y_dna = np.sin(x) * 0.8
        y_automaton = np.cos(x) * 0.8
        ax1.plot(x, y_dna, color='#1f77b4', label='Información Genética (ADN)', linewidth=2)
        ax1.plot(x, y_automaton, color='#ff7f0e', label='Cinta de Instrucciones (Autómata)', linewidth=2, linestyle='--')
        ax1.set_title('1. Almacenamiento de Información', pad=15, fontsize=11)
        ax1.legend(fontsize=9)
        ax1.set_yticks([])

        ax2.add_patch(plt.Circle((0.5, 0.5), 0.3, color='#2ca02c', alpha=0.6, label='Entidad Original'))
        ax2.add_patch(plt.Circle((1.5, 0.5), 0.3, color='#90ee90', alpha=0.6, label='Copia Generada'))
        ax2.arrow(0.8, 0.5, 0.4, 0, head_width=0.05, head_length=0.1, fc='black', ec='black')
        ax2.set_xlim(0, 2)
        ax2.set_ylim(0, 1)
        ax2.set_title('2. Proceso de Replicación', pad=15, fontsize=11)
        ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=2, fontsize=9)
        ax2.set_aspect('equal', adjustable='box')
        ax2.axis('off')
        
        G = nx.DiGraph()
        node_dna = "ADN\n(Información Genética)"
        node_rna = "ARN\n(Mensajero)"
        node_protein = "Proteínas\n(Función Biológica)"
        node_tape = "Cinta de Instrucciones\n(Estado del Autómata)"
        node_rules = "Procesador de Reglas\n(Lógica de Transición)"
        node_new_config = "Nueva Configuración\n(Construcción/Acción)"
        G.add_edges_from([
            (node_dna, node_rna), (node_rna, node_protein),
            (node_tape, node_rules), (node_rules, node_new_config)
        ])
        pos = {node_dna: (0,1), node_rna: (1,1), node_protein: (2,1),
               node_tape: (0,0), node_rules: (1,0), node_new_config: (2,0)}
        node_colors_map = ['#1f77b4','#aec7e8','#17becf', '#ff7f0e','#ffbb78','#d62728']
        nx.draw(G, pos, ax=ax3, with_labels=True, node_color=node_colors_map, node_size=3000, 
                font_size=6, arrowsize=15, width=1.5, connectionstyle='arc3,rad=0.1')
        ax3.set_title('3. Flujo de Información y Procesamiento', pad=15, fontsize=11)
        
        categories = ['Proteínas Diversas\n(desde ADN)', 'Máquinas Variadas\n(desde Autómata)']
        values = [8, 7]
        bar_colors=['#2ca02c', '#9467bd']
        ax4.bar(categories, values, color=bar_colors)
        ax4.set_ylabel('Capacidad de Construcción', fontsize=9)
        ax4.set_title('4. Universalidad de Construcción', pad=15, fontsize=11)
        ax4.set_xticks(np.arange(len(categories)))
        ax4.set_xticklabels(categories, rotation=10, ha="right", fontsize=9)
        
        fig.suptitle('Analogía Conceptual: Autómatas Celulares y Sistemas Biológicos (ADN)', fontsize=16)
        fig.tight_layout(rect=[0, 0, 1, 0.95])
        plt.savefig(os.path.join(self.plots_dir, 'dna_analogy.png'), dpi=150, bbox_inches='tight')
        plt.close(fig)
        
    def create_modern_applications(self):
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        sns.set_style("whitegrid")

        bio_apps = ['Modelado de Crecimiento\nTumoral', 'Simulación de Redes\nGenéticas', 'Análisis de Patrones\nTisulares', 'Predicción de Evolución\nViral']
        bio_impact = [8, 7, 6, 7.5]
        axes[0,0].barh(bio_apps, bio_impact, color=sns.color_palette("viridis", len(bio_apps)))
        axes[0,0].set_title('A. Biología Computacional', fontsize=11)

        mol_comps = ['Circuitos Lógicos\nde ADN', 'Nanobots\nMoleculares', 'Almacenamiento de\nDatos en ADN', 'Computación Paralela\nMasiva']
        mol_potential = [8.5, 9, 7.5, 8]
        axes[0,1].barh(mol_comps, mol_potential, color=sns.color_palette("magma", len(mol_comps)))
        axes[0,1].set_title('B. Computación Molecular', fontsize=11)

        cs_models = ['Dinámica de\nPoblaciones', 'Propagación de Epidemias\n(Simplificado)', 'Flujo de Tráfico\nUrbano', 'Formación de Opiniones\nSociales']
        cs_complexity = [7, 8, 6.5, 7.5]
        axes[1,0].barh(cs_models, cs_complexity, color=sns.color_palette("crest", len(cs_models)))
        axes[1,0].set_title('C. Modelado de Sistemas Complejos', fontsize=11)

        alife_apps = ['Simulación de Ecosistemas\nDigitales', 'Generación de Texturas\ny Patrones', 'Música y Arte\nEvolutivo', 'Diseño de Agentes\nAutónomos Simples']
        alife_creativity = [8, 7, 7.5, 6.5]
        axes[1,1].barh(alife_apps, alife_creativity, color=sns.color_palette("rocket", len(alife_apps)))
        axes[1,1].set_title('D. Vida Artificial y Arte Generativo', fontsize=11)
        
        for i, ax_row in enumerate(axes):
            for j, ax_ in enumerate(ax_row):
                ax_.tick_params(axis='y', labelsize=8)
                ax_.tick_params(axis='x', labelsize=9)
                if i == 1 : ax_.set_xlabel("Impacto / Potencial (Conceptual)", fontsize=9)

        fig.suptitle('Aplicaciones e Inspiraciones Modernas de Conceptos de Autómatas Celulares', fontsize=16)
        fig.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.savefig(os.path.join(self.plots_dir, 'modern_applications.png'), dpi=150, bbox_inches='tight')
        plt.close(fig)

    def create_legacy_visualization(self):
        fig, ax = plt.subplots(figsize=(10,6.5))
        eras = [
            "Fundacional\n(Von Neumann, '40s-'50s)", 
            "Desarrollo Teórico\n(Ullman, Wolfram, '60s-'80s)", 
            "Aplicaciones Nicho\n('90s-'00s)", 
            "Renacimiento en Biocomp.\ny Sist. Complejos ('10s-Hoy)"
        ]
        impact_score = [8, 8.5, 7, 9]
        
        ax.plot(eras, impact_score, marker='o', linestyle='-', color='#003366', linewidth=2, markersize=8)
        
        for i, txt in enumerate(impact_score):
            ax.annotate(f"{txt}", (eras[i], impact_score[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

        ax.set_title("Legado e Impacto Evolutivo de los Autómatas Celulares", fontsize=14, pad=15)
        ax.set_ylabel("Impacto Científico y Tecnológico (Conceptual)", fontsize=10)
        ax.tick_params(axis='x', rotation=10, labelsize=9)
        ax.grid(True, linestyle='--', alpha=0.7)
        plt.ylim(bottom=6.5, top=max(impact_score) + 0.5)
        fig.tight_layout()
        plt.savefig(os.path.join(self.plots_dir, 'legacy.png'), dpi=150, bbox_inches='tight')
        plt.close(fig)
    
    def create_all_visualizations(self):
        print("Generando visualizaciones de von Neumann y Ullman...")
        
        self.create_state_visualization()
        self.create_self_replication_animation()
        self.create_neighborhood_visualization()
        self.create_state_transition_diagram()
        
        self.create_transition_rules_animation()
        self.create_emergent_patterns_animation()
        self.create_temporal_evolution_animation()
        
        self.create_ullman_comparison()
        self.create_dna_analogy()
        self.create_modern_applications()
        self.create_legacy_visualization()
        
        print(f"Todas las visualizaciones han sido generadas en: {self.plots_dir}")

if __name__ == "__main__":
    visualizer = VonNeumannVisualizer()
    visualizer.create_all_visualizations() 