import numpy as np
import math

def calculate_row_errors(board):
    """Calculates the number of duplicate numbers in each row."""
    size = board.shape[0]
    errors = 0
    for r in range(size):
        row = board[r, :]
        counts = np.unique(row[row != 0], return_counts=True)[1]
        errors += np.sum(counts[counts > 1] - 1)
    return errors

def calculate_col_errors(board):
    """Calculates the number of duplicate numbers in each column."""
    size = board.shape[0]
    errors = 0
    for c in range(size):
        col = board[:, c]
        counts = np.unique(col[col != 0], return_counts=True)[1]
        errors += np.sum(counts[counts > 1] - 1)
    return errors

def calculate_subgrid_errors(board):
    """Calculates the number of duplicate numbers in each subgrid."""
    size = board.shape[0]
    subgrid_size = int(math.sqrt(size))
    errors = 0
    for r in range(0, size, subgrid_size):
        for c in range(0, size, subgrid_size):
            subgrid = board[r:r+subgrid_size, c:c+subgrid_size].flatten()
            counts = np.unique(subgrid[subgrid != 0], return_counts=True)[1]
            errors += np.sum(counts[counts > 1] - 1)
    return errors

def count_empty_cells(board):
    """Counts the number of empty cells (0s) on the board."""
    return np.count_nonzero(board == 0)

def check_initial_clues(candidate_board, initial_board):
    """Checks if the candidate solution has illegally modified the initial clues.

    Returns:
        int: The number of initial clues that were changed.
    """
    initial_clues_indices = np.where(initial_board != 0)
    changed_clues = 0
    for r, c in zip(*initial_clues_indices):
        if candidate_board[r, c] != initial_board[r, c]:
            changed_clues += 1
    return changed_clues

# Note: The actual fitness function (combining these metrics) should be
# defined in solution.py as per the user request, allowing students to modify it.

# Example usage (optional)
if __name__ == "__main__":
    # Example board (partially filled 9x9)
    test_board = np.array([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])

    initial_puzzle = test_board.copy() # Assume this was the starting puzzle

    # Simulate a candidate solution with errors
    candidate = test_board.copy()
    candidate[0, 2] = 3 # Row error (duplicate 3)
    candidate[1, 1] = 6 # Col error (duplicate 6)
    candidate[1, 2] = 6 # Subgrid error (duplicate 6)
    candidate[0, 0] = 9 # Changed initial clue

    print("Candidate Board:")
    print(candidate)
    print("\nInitial Board:")
    print(initial_puzzle)

    row_e = calculate_row_errors(candidate)
    col_e = calculate_col_errors(candidate)
    sub_e = calculate_subgrid_errors(candidate)
    empty = count_empty_cells(candidate)
    clue_e = check_initial_clues(candidate, initial_puzzle)

    print(f"\nRow Errors: {row_e}")
    print(f"Column Errors: {col_e}")
    print(f"Subgrid Errors: {sub_e}")
    print(f"Empty Cells: {empty}")
    print(f"Changed Initial Clues: {clue_e}") 