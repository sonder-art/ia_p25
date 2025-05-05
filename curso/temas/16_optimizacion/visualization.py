import matplotlib.pyplot as plt
import numpy as np
import math
# Import evaluation functions to check for errors
from evaluation import calculate_row_errors, calculate_col_errors, calculate_subgrid_errors

_board_figure = None
_board_ax = None
_convergence_figure = None
_convergence_ax = None

def _get_conflicts(board):
    """Identifies the coordinates of cells causing conflicts."""
    size = board.shape[0]
    subgrid_size = int(math.sqrt(size))
    conflicts = set()

    for i in range(size):
        # Check rows
        row = board[i, :]
        unique_nums, counts = np.unique(row[row != 0], return_counts=True)
        duplicate_nums = unique_nums[counts > 1]
        for num in duplicate_nums:
            indices = np.where(row == num)[0]
            for idx in indices:
                conflicts.add((i, idx))

        # Check columns
        col = board[:, i]
        unique_nums, counts = np.unique(col[col != 0], return_counts=True)
        duplicate_nums = unique_nums[counts > 1]
        for num in duplicate_nums:
            indices = np.where(col == num)[0]
            for idx in indices:
                conflicts.add((idx, i))

    # Check subgrids
    for r_start in range(0, size, subgrid_size):
        for c_start in range(0, size, subgrid_size):
            subgrid = board[r_start:r_start+subgrid_size, c_start:c_start+subgrid_size]
            flat_subgrid = subgrid.flatten()
            unique_nums, counts = np.unique(flat_subgrid[flat_subgrid != 0], return_counts=True)
            duplicate_nums = unique_nums[counts > 1]
            for num in duplicate_nums:
                relative_indices = np.where(subgrid == num)
                for r_rel, c_rel in zip(*relative_indices):
                    conflicts.add((r_start + r_rel, c_start + c_rel))

    return conflicts

def plot_sudoku_board(board, initial_board=None, title="Sudoku Board", pause_time=0.1):
    """Plots the Sudoku board using Matplotlib, highlighting conflicts.

    Args:
        board (np.ndarray): The Sudoku board (N x N).
        initial_board (np.ndarray, optional): The initial puzzle board to show fixed clues.
                                             Defaults to None.
        title (str): Title for the plot window.
        pause_time (float): Time to pause after plotting. If 0, waits for user.
                           If called repeatedly, updates the existing plot.
    """
    global _board_figure, _board_ax
    size = board.shape[0]
    subgrid_size = int(math.sqrt(size))

    if initial_board is None:
        # If no initial board provided, assume all non-zero are initial clues
        initial_board = board.copy()

    conflicts = _get_conflicts(board)
    fixed_clues_indices = np.where(initial_board != 0)
    fixed_clues_set = set(zip(*fixed_clues_indices))

    if _board_figure is None or _board_ax is None:
        plt.ion() # Turn on interactive mode
        _board_figure, _board_ax = plt.subplots(figsize=(6, 6))
        _board_figure.canvas.manager.set_window_title("Sudoku Board Visualization")


    _board_ax.clear()
    _board_ax.set_title(title)

    # Draw grid lines
    for x in range(size + 1):
        lw = 2 if x % subgrid_size == 0 else 0.5
        _board_ax.axhline(x, color='black', linewidth=lw)
        _board_ax.axvline(x, color='black', linewidth=lw)

    # Fill numbers
    for r in range(size):
        for c in range(size):
            num = board[r, c]
            if num != 0:
                coord = (r, c)
                color = 'blue' # Default for GA-placed numbers
                weight = 'normal'

                if coord in fixed_clues_set:
                     # Check if the fixed clue itself was overwritten to cause a conflict
                     if initial_board[r, c] == board[r, c]:
                           color = 'black' # Original clue
                           weight = 'bold'
                     else:
                           color = 'magenta' # Original clue modified! (Should be penalized by fitness)
                           weight = 'bold'
                elif coord in conflicts:
                     color = 'red'   # Number causes a conflict
                     weight = 'bold'

                # Plot numbers centered in cells
                _board_ax.text(c + 0.5, size - (r + 0.5), str(num),
                             ha='center', va='center', fontsize=12, color=color, weight=weight)

    _board_ax.set_xlim(0, size)
    _board_ax.set_ylim(0, size)
    _board_ax.set_xticks([])
    _board_ax.set_yticks([])
    _board_ax.invert_yaxis() # Match typical Sudoku layout (0,0 at top-left)

    _board_figure.canvas.draw()
    _board_figure.canvas.flush_events()

    if pause_time > 0:
        plt.pause(pause_time)
    elif pause_time == 0:
        print("Showing board plot. Close the plot window to continue...")
        plt.show(block=True) # Block until closed if pause_time is 0
    # If pause_time < 0, don't pause or block

def close_plot(figure_type="board"):
     """Closes the specified Matplotlib plot window."""
     global _board_figure, _convergence_figure
     if figure_type == "board" and _board_figure is not None:
          plt.close(_board_figure)
          _board_figure = None
          _board_ax = None
          plt.ioff() # Turn off interactive mode if closing the main board
     elif figure_type == "convergence" and _convergence_figure is not None:
          plt.close(_convergence_figure)
          _convergence_figure = None
          _convergence_ax = None
     # Add more types if needed


def plot_convergence(fitness_history, title="GA Convergence"):
    """Plots the best fitness score over generations.

    Args:
        fitness_history (list or np.ndarray): List of best fitness scores per generation.
        title (str): Title for the plot window.
    """
    global _convergence_figure, _convergence_ax

    if _convergence_figure is None or _convergence_ax is None:
        # Create a new figure specifically for convergence
        _convergence_figure, _convergence_ax = plt.subplots(figsize=(8, 5))
        _convergence_figure.canvas.manager.set_window_title("Convergence Plot")
    else:
        _convergence_ax.clear() # Clear previous convergence plot if reusing window

    _convergence_ax.plot(fitness_history, marker='.', linestyle='-')
    _convergence_ax.set_xlabel("Generation")
    _convergence_ax.set_ylabel("Best Fitness Score")
    _convergence_ax.set_title(title)
    _convergence_ax.grid(True)

    print("Showing convergence plot. Close the plot window to continue...")
    plt.show(block=True) # Show and block until closed
    close_plot(figure_type="convergence") # Ensure it gets closed variable-wise

# Example usage (optional)
if __name__ == "__main__":
    # Example 9x9 board
    example_board = np.array([
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 0] # Intentionally leave one 0
    ])

    print("Plotting example board...")
    plot_sudoku_board(example_board, title="Example Sudoku", pause_time=0)
    # close_plot("board") # Close manually if pause_time=0

    print("\nPlotting example convergence...")
    example_fitness = np.linspace(0.1, 0.95, 50) + np.random.rand(50) * 0.1 # Simulate fitness increase
    plot_convergence(example_fitness, title="Example Convergence")
    # close_plot("convergence") # Close manually

    print("\nSimulating dynamic board update...")
    board_dynamic = example_board.copy()
    # Simulate some GA steps filling cells, potentially with errors
    board_dynamic[8, 8] = 9 # Fill last cell
    board_dynamic[0, 2] = 5 # Creates row conflict with (0,0)
    board_dynamic[1, 1] = 7 # Creates subgrid conflict with (1, 6)
    board_dynamic[5, 1] = 1 # OK

    plot_sudoku_board(board_dynamic, title="Dynamic Update 1", pause_time=1.5)
    board_dynamic[0, 2] = 4 # Fix one conflict
    plot_sudoku_board(board_dynamic, title="Dynamic Update 2", pause_time=1.5)
    close_plot("board")
    print("Done.") 