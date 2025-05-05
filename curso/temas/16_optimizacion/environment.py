import numpy as np
import random
import math

class SudokuEnvironment:
    """Represents the Sudoku environment, handling puzzle generation and validation."""
    def __init__(self, size=9):
        if not self._is_perfect_square(size):
            raise ValueError("Sudoku size must be a perfect square (e.g., 4, 9, 16).")
        self.size = size
        self.subgrid_size = int(math.sqrt(size))
        self._solution = self._generate_full_solution()
        self._initial_board = None

    def _is_perfect_square(self, n):
        if n < 1: return False
        sqrt_n = int(math.sqrt(n))
        return sqrt_n * sqrt_n == n

    def _is_valid(self, board, row, col, num):
        """Checks if placing num at (row, col) is valid in the current board state."""
        # Check row
        if num in board[row, :]:
            return False
        # Check column
        if num in board[:, col]:
            return False
        # Check subgrid
        start_row, start_col = self.subgrid_size * (row // self.subgrid_size), self.subgrid_size * (col // self.subgrid_size)
        if num in board[start_row:start_row + self.subgrid_size, start_col:start_col + self.subgrid_size]:
            return False
        return True

    def _find_empty(self, board):
        """Finds the next empty cell (represented by 0)."""
        for r in range(self.size):
            for c in range(self.size):
                if board[r, c] == 0:
                    return (r, c)
        return None

    def _solve_sudoku(self, board):
        """Solves the Sudoku board using backtracking (used for generation)."""
        find = self._find_empty(board)
        if not find:
            return True  # Solved
        else:
            row, col = find

        nums = list(range(1, self.size + 1))
        random.shuffle(nums) # Introduce randomness for generating different puzzles

        for num in nums:
            if self._is_valid(board, row, col, num):
                board[row, col] = num
                if self._solve_sudoku(board):
                    return True
                board[row, col] = 0 # Backtrack
        return False

    def _generate_full_solution(self):
        """Generates a complete, valid Sudoku grid."""
        board = np.zeros((self.size, self.size), dtype=int)
        self._solve_sudoku(board)
        return board

    def generate_puzzle(self, difficulty=0.5):
        """Generates a puzzle by removing cells from a full solution.

        Args:
            difficulty (float): A value between 0 (easy) and 1 (hard) indicating
                              the proportion of cells to empty. Higher values mean
                              more empty cells.
        Returns:
            np.ndarray: The Sudoku puzzle board with some cells empty (0).
        """
        if not 0 <= difficulty <= 1:
            raise ValueError("Difficulty must be between 0 and 1.")

        self._initial_board = self._solution.copy()
        num_cells = self.size * self.size
        num_to_remove = int(num_cells * difficulty)

        # Ensure we don't remove too many, potentially making it unsolvable or trivial
        # Adjust bounds as needed, this is a heuristic
        num_to_remove = max(0, min(num_to_remove, num_cells - (self.size * 2))) # Keep at least ~2N clues

        attempts = 0
        max_attempts = num_cells * 5 # Limit attempts to avoid infinite loops

        removed_count = 0
        while removed_count < num_to_remove and attempts < max_attempts:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            attempts += 1

            if self._initial_board[row, col] != 0:
                # Simple removal strategy: just remove cells randomly.
                # More complex strategies exist (e.g., checking for unique solutions),
                # but are much harder to implement.
                self._initial_board[row, col] = 0
                removed_count += 1

        if removed_count < num_to_remove:
             print(f"Warning: Could only remove {removed_count}/{num_to_remove} cells while maintaining basic structure.")


        return self._initial_board.copy() # Return a copy

    def get_initial_board(self):
        """Returns the generated puzzle board."""
        if self._initial_board is None:
            raise RuntimeError("Puzzle has not been generated yet. Call generate_puzzle() first.")
        return self._initial_board.copy()

    def get_solution(self):
        """Returns the complete solution board (for reference/cheating!)."""
        return self._solution.copy()

    def get_size(self):
        """Returns the size (N) of the Sudoku grid."""
        return self.size

    def is_solved(self, board):
        """Checks if a given board is a complete and valid Sudoku solution."""
        if not isinstance(board, np.ndarray) or board.shape != (self.size, self.size):
            return False # Incorrect shape

        # Check for empty cells (0s)
        if 0 in board:
            return False

        # Check rows, columns, and subgrids for duplicates
        for i in range(self.size):
            if len(set(board[i, :])) != self.size: return False # Row check
            if len(set(board[:, i])) != self.size: return False # Column check

        for r in range(0, self.size, self.subgrid_size):
            for c in range(0, self.size, self.subgrid_size):
                subgrid = board[r:r+self.subgrid_size, c:c+self.subgrid_size]
                if len(set(subgrid.flatten())) != self.size: return False # Subgrid check

        return True

# Example usage (optional)
if __name__ == "__main__":
    try:
        env = SudokuEnvironment(size=9)
        puzzle = env.generate_puzzle(difficulty=0.6)
        solution = env.get_solution()

        print("Generated Puzzle:")
        print(puzzle)
        print("\nFull Solution:")
        print(solution)

        print(f"\nIs the puzzle solved? {env.is_solved(puzzle)}")
        print(f"Is the solution solved? {env.is_solved(solution)}")

        # Example of checking a slightly modified board
        test_board = puzzle.copy()
        # Find an empty cell and fill it (might be wrong)
        empty = env._find_empty(test_board)
        if empty:
            test_board[empty] = 1
        print(f"\nIs slightly filled board solved? {env.is_solved(test_board)}")

    except ValueError as e:
        print(f"Error: {e}") 