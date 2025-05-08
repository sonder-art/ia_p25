import numpy as np
import matplotlib.pyplot as plt
import os

SAND_THRESHOLD = 4

def initialize_grid(rows: int, cols: int) -> np.ndarray:
    """Initializes an empty grid."""
    return np.zeros((rows, cols), dtype=int)

def add_sand(grid: np.ndarray, row: int, col: int, amount: int = 1):
    """Adds a specified amount of sand to a cell."""
    if 0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]:
        grid[row, col] += amount

def topple_once(grid: np.ndarray) -> tuple[np.ndarray, int]:
    """
    Performs one toppling pass:
    Identifies all unstable cells, topples them simultaneously (conceptually),
    and returns the new grid state and the number of cells that toppled in this pass.
    Sand falling off the edges is lost.
    """
    rows, cols = grid.shape
    new_grid = grid.copy()
    toppled_count_this_pass = 0
    
    # Identify all cells that will topple in this step
    # Important: Use the original grid state to check for toppling conditions
    unstable_cells_coords = np.where(grid >= SAND_THRESHOLD)

    if len(unstable_cells_coords[0]) == 0:
        return new_grid, 0 # No cells to topple

    for r, c in zip(unstable_cells_coords[0], unstable_cells_coords[1]):
        if grid[r, c] >= SAND_THRESHOLD: # Check original grid again, in case of multiple passes logic (though current is single pass)
            new_grid[r, c] -= SAND_THRESHOLD
            toppled_count_this_pass += 1
            # Distribute sand to neighbors
            # North
            if r > 0:
                new_grid[r - 1, c] += 1
            # South
            if r < rows - 1:
                new_grid[r + 1, c] += 1
            # West
            if c > 0:
                new_grid[r, c - 1] += 1
            # East
            if c < cols - 1:
                new_grid[r, c + 1] += 1
                
    return new_grid, toppled_count_this_pass

def stabilize_grid(grid: np.ndarray) -> tuple[np.ndarray, int, int]:
    """
    Repeatedly topples unstable cells until the grid is stable.
    Returns the stable grid, total number of topples in this stabilization phase (avalanche size),
    and number of passes for stabilization (avalanche duration).
    """
    current_grid = grid.copy()
    total_topples_in_avalanche = 0
    avalanche_duration = 0
    
    while True:
        next_grid_state, toppled_this_pass = topple_once(current_grid)
        if toppled_this_pass == 0:
            break # Grid is stable
        current_grid = next_grid_state
        total_topples_in_avalanche += toppled_this_pass
        avalanche_duration += 1
        
    return current_grid, total_topples_in_avalanche, avalanche_duration

def plot_sandpile_grid(grid: np.ndarray, step_label: str, output_dir: str, filename: str):
    """Plots the sandpile grid and saves it to a file."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    plt.figure(figsize=(8, 8))
    # Display up to SAND_THRESHOLD + 1 distinct values, values >= SAND_THRESHOLD will be capped by cmap
    # Or use discrete colormap for better visual distinction of 0, 1, 2, 3 grains.
    cmap = plt.cm.get_cmap('viridis', SAND_THRESHOLD +1) 
    plt.imshow(grid, cmap=cmap, vmin=-0.5, vmax=SAND_THRESHOLD + 0.5) # Adjust vmin/vmax for centering discrete colors
    
    plt.colorbar(ticks=np.arange(0, SAND_THRESHOLD + 1), label='Number of Grains')
    plt.title(f"Sandpile State: {step_label}", fontsize=15)
    plt.xticks([])
    plt.yticks([])
    
    filepath = os.path.join(output_dir, filename)
    plt.savefig(filepath)
    plt.close()
    print(f"Saved plot: {filepath}")
    return filepath

def main():
    """Main function to run a simple sandpile simulation."""
    rows, cols = 21, 21
    grid = initialize_grid(rows, cols)
    
    output_dir = "sandpile_plots_generated"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Initial state
    plot_sandpile_grid(grid, "Initial State (0 grains)", output_dir, "sandpile_0_initial.png")

    center_r, center_c = rows // 2, cols // 2
    
    total_grains_added = 0
    grains_to_add_sequence = [1, 10, 100, 500, 1000] # Cumulative grains after which to plot
    plot_counter = 1

    max_grains_overall = grains_to_add_sequence[-1]

    for i in range(1, max_grains_overall + 1):
        add_sand(grid, center_r, center_c, 1)
        grid, topples, duration = stabilize_grid(grid)
        total_grains_added +=1
        
        if total_grains_added in grains_to_add_sequence:
            plot_sandpile_grid(grid, f"{total_grains_added} Grains Added", output_dir, f"sandpile_{plot_counter}_{total_grains_added}_grains.png")
            plot_counter +=1
            if topples > 0:
                print(f"After {total_grains_added} grains: Avalanche size={topples}, Duration={duration} steps.")
            else:
                print(f"After {total_grains_added} grains: No avalanche.")

    print("\nSimulation finished.")
    print(f"Final grid state after {total_grains_added} grains (not plotted in loop but can be):")
    # plot_sandpile_grid(grid, f"Final State ({total_grains_added} grains)", output_dir, "sandpile_final.png")


if __name__ == "__main__":
    main() 