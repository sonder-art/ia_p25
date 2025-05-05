import numpy as np
import random
import time
from environment import SudokuEnvironment
from evaluation import (calculate_row_errors, calculate_col_errors,
                       calculate_subgrid_errors, count_empty_cells,
                       check_initial_clues)
from visualization import plot_sudoku_board, plot_convergence, close_plot

# --- Environment Configuration ---
# Students can modify these general settings for the Sudoku problem
SUDOKU_SIZE = 9       # Size of the Sudoku grid (must be a perfect square, e.g., 4, 9)
PUZZLE_DIFFICULTY = 0.5 # Proportion of cells to empty (0=easy, 1=hard)

# --- Student Implementation Section ---

# === Fitness Function Definitions ===
# Students should implement/modify fitness functions 2 and 3.
# The fitness function takes the candidate solution (board), the initial puzzle board,
# and the environment object, returning a numerical score (higher is better).

def fitness_function_1_binary(candidate_board, initial_board, env):
    """
    Fitness Function 1 (Naive Binary): Solved or Not Solved.
    Returns 1.0 if solved (respecting initial clues), 0.0 otherwise.
    """
    if check_initial_clues(candidate_board, initial_board) > 0:
        return 0.0 # Penalize changing initial clues immediately
    if env.is_solved(candidate_board):
        return 1.0
    else:
        return 0.0

def fitness_function_2_student(candidate_board, initial_board, env):
    """
    Fitness Function Variant 2: STUDENT IMPLEMENTATION REQUIRED.
    (This placeholder currently returns 0.0).
    """
    # --- Placeholder ---
    print("Warning: fitness_function_2_student is not implemented.")
    # Replace the line below with your fitness calculation
    return 0.0 # Return a default value
    # --- End Placeholder ---

def fitness_function_3_student(candidate_board, initial_board, env):
    """
    Fitness Function Variant 3: STUDENT IMPLEMENTATION REQUIRED.
    (This placeholder currently returns 0.0).
    """
    # --- Placeholder ---
    print("Warning: fitness_function_3_student is not implemented.")
    # Replace the line below with your fitness calculation
    return 0.0 # Return a default value
    # --- End Placeholder ---


# List of fitness functions for easy selection
FITNESS_FUNCTIONS = {
    "Fitness 1 (Binary Solved)": fitness_function_1_binary,
    "Fitness 2 (Student Defined)": fitness_function_2_student,
    "Fitness 3 (Student Defined)": fitness_function_3_student,
}

# === Genetic Algorithm Implementation ===
# Each variant below is self-contained with its own internal parameters.
# Students can modify these classes or add new ones.

class GeneticAlgorithmVariant1_NaiveStdParams:
    """
    Naive GA Variant 1: Standard Parameters.
    Uses basic operators and standard internal parameters.
    """
    def __init__(self, env: SudokuEnvironment, fitness_func):
        self.env = env
        self.fitness_func = fitness_func
        self.initial_board = env.get_initial_board()
        self.size = env.get_size()
        self.subgrid_size = int(np.sqrt(self.size))
        self.fixed_indices = np.where(self.initial_board != 0)

        # --- Internal Parameters for this Variant ---
        self.pop_size = 100
        self.crossover_rate = 0.8
        self.mutation_rate = 0.15 # Per gene
        self.elitism_count = 2
        self.tournament_size = 3
        # --- End Internal Parameters ---

        self.population = self._initialize_population()

    def _initialize_population(self):
        population = []
        for _ in range(self.pop_size):
             individual = self.initial_board.copy()
             empty_cells = np.argwhere(individual == 0)
             for idx in empty_cells:
                 row, col = idx
                 individual[row, col] = random.randint(1, self.size)
             population.append(individual)
        return population

    def _selection(self, fitness_scores):
        selected_parents = []
        num_parents_needed = self.pop_size
        for _ in range(num_parents_needed):
            contender_indices = random.sample(range(self.pop_size), self.tournament_size)
            contender_fitness = [fitness_scores[i] for i in contender_indices]
            winner_idx = contender_indices[np.argmax(contender_fitness)]
            selected_parents.append(self.population[winner_idx])
        return selected_parents

    def _crossover(self, parent1, parent2):
        child1 = parent1.copy()
        child2 = parent2.copy()
        if random.random() < self.crossover_rate:
            for r in range(self.size):
                for c in range(self.size):
                     is_fixed = False
                     if r in self.fixed_indices[0] and c in self.fixed_indices[1]:
                          if np.any((self.fixed_indices[0] == r) & (self.fixed_indices[1] == c)):
                               is_fixed = True
                     if not is_fixed:
                         if random.random() < 0.5:
                             child1[r, c], child2[r, c] = parent2[r, c], parent1[r, c]
        return child1, child2

    def _mutation(self, individual):
        mutated_individual = individual.copy()
        for r in range(self.size):
            for c in range(self.size):
                is_fixed = False
                if r in self.fixed_indices[0] and c in self.fixed_indices[1]:
                     if np.any((self.fixed_indices[0] == r) & (self.fixed_indices[1] == c)):
                          is_fixed = True
                if not is_fixed:
                     if random.random() < self.mutation_rate:
                         mutated_individual[r, c] = random.randint(1, self.size)
        return mutated_individual

    def run(self, max_generations, visualize=True):
        print(f"Running {self.__class__.__name__} with {self.fitness_func.__name__}...")
        print(f"   Internal Params: Pop={self.pop_size}, CX={self.crossover_rate}, Mut={self.mutation_rate}, Elite={self.elitism_count}, Tourn={self.tournament_size}")
        best_fitness_history = []
        best_solution = None
        best_fitness_overall = -np.inf
        start_time = time.time()

        for generation in range(max_generations):
            fitness_scores = [self.fitness_func(ind, self.initial_board, self.env) for ind in self.population]
            current_best_fitness = np.max(fitness_scores)
            current_best_index = np.argmax(fitness_scores)
            best_fitness_history.append(current_best_fitness)

            if current_best_fitness > best_fitness_overall:
                best_fitness_overall = current_best_fitness
                best_solution = self.population[current_best_index].copy()
                if visualize:
                     plot_sudoku_board(best_solution, initial_board=self.initial_board, title=f"{self.__class__.__name__} - Gen {generation+1} - Best Fit: {best_fitness_overall:.4f}", pause_time=0.05)

            if best_fitness_overall >= 1.0: # Binary fitness target is 1.0
                 print(f"\n*** Solved (Fitness >= 1.0) in Generation {generation+1}! ***")
                 if visualize:
                      plot_sudoku_board(best_solution, initial_board=self.initial_board, title=f"{self.__class__.__name__} - Solved! Gen {generation+1}", pause_time=1.0)
                 break

            parents = self._selection(fitness_scores)
            next_population = []

            if self.elitism_count > 0:
                sorted_indices = np.argsort(fitness_scores)[::-1]
                for i in range(min(self.elitism_count, self.pop_size)):
                    next_population.append(self.population[sorted_indices[i]])

            num_offspring_needed = self.pop_size - len(next_population)
            parent_indices = list(range(len(parents)))
            current_offspring_count = 0
            while current_offspring_count < num_offspring_needed:
                 if len(parent_indices) < 2:
                     parent_indices = list(range(len(parents)))
                     random.shuffle(parent_indices)
                     if len(parent_indices) < 2:
                          if len(parents) > 0:
                              idx1 = parent_indices.pop(random.randrange(len(parent_indices))) if parent_indices else 0
                              child1 = self._mutation(parents[idx1].copy())
                              next_population.append(child1)
                              current_offspring_count +=1
                              if current_offspring_count >= num_offspring_needed: break
                          else: break # Should not happen

                 idx1 = parent_indices.pop(random.randrange(len(parent_indices)))
                 idx2 = parent_indices.pop(random.randrange(len(parent_indices)))
                 parent1 = parents[idx1]
                 parent2 = parents[idx2]
                 child1, child2 = self._crossover(parent1, parent2)
                 child1 = self._mutation(child1)
                 child2 = self._mutation(child2)
                 next_population.append(child1)
                 current_offspring_count += 1
                 if current_offspring_count < num_offspring_needed:
                    next_population.append(child2)
                    current_offspring_count += 1

            self.population = next_population[:self.pop_size]

            if (generation + 1) % 50 == 0:
                print(f"Generation {generation+1}/{max_generations} - Best Fitness: {best_fitness_overall:.4f}")

        if visualize: close_plot()
        end_time = time.time()
        print(f"{self.__class__.__name__} execution finished. Time: {end_time - start_time:.2f} sec.")
        return best_solution, best_fitness_history


class GeneticAlgorithmVariant2_HighMutation:
    """
    Naive GA Variant 2: High Mutation Rate.
    Same logic as Variant 1, different internal parameters.
    """
    def __init__(self, env: SudokuEnvironment, fitness_func):
        self.env = env
        self.fitness_func = fitness_func
        self.initial_board = env.get_initial_board()
        self.size = env.get_size()
        self.subgrid_size = int(np.sqrt(self.size))
        self.fixed_indices = np.where(self.initial_board != 0)

        # --- Internal Parameters for this Variant ---
        self.pop_size = 100
        self.crossover_rate = 0.8
        self.mutation_rate = 0.6 # << High Mutation Rate
        self.elitism_count = 2
        self.tournament_size = 3
        # --- End Internal Parameters ---

        self.population = self._initialize_population()

    def _initialize_population(self):
        population = []
        for _ in range(self.pop_size):
             individual = self.initial_board.copy()
             empty_cells = np.argwhere(individual == 0)
             for idx in empty_cells:
                 row, col = idx
                 individual[row, col] = random.randint(1, self.size)
             population.append(individual)
        return population

    def _selection(self, fitness_scores):
        selected_parents = []
        num_parents_needed = self.pop_size
        for _ in range(num_parents_needed):
            contender_indices = random.sample(range(self.pop_size), self.tournament_size)
            contender_fitness = [fitness_scores[i] for i in contender_indices]
            winner_idx = contender_indices[np.argmax(contender_fitness)]
            selected_parents.append(self.population[winner_idx])
        return selected_parents

    def _crossover(self, parent1, parent2):
        child1 = parent1.copy()
        child2 = parent2.copy()
        if random.random() < self.crossover_rate:
            for r in range(self.size):
                for c in range(self.size):
                     is_fixed = False
                     if r in self.fixed_indices[0] and c in self.fixed_indices[1]:
                          if np.any((self.fixed_indices[0] == r) & (self.fixed_indices[1] == c)):
                               is_fixed = True
                     if not is_fixed:
                         if random.random() < 0.5:
                             child1[r, c], child2[r, c] = parent2[r, c], parent1[r, c]
        return child1, child2

    def _mutation(self, individual):
        mutated_individual = individual.copy()
        for r in range(self.size):
            for c in range(self.size):
                is_fixed = False
                if r in self.fixed_indices[0] and c in self.fixed_indices[1]:
                     if np.any((self.fixed_indices[0] == r) & (self.fixed_indices[1] == c)):
                          is_fixed = True
                if not is_fixed:
                     if random.random() < self.mutation_rate:
                         mutated_individual[r, c] = random.randint(1, self.size)
        return mutated_individual

    def run(self, max_generations, visualize=True):
        print(f"Running {self.__class__.__name__} with {self.fitness_func.__name__}...")
        print(f"   Internal Params: Pop={self.pop_size}, CX={self.crossover_rate}, Mut={self.mutation_rate}, Elite={self.elitism_count}, Tourn={self.tournament_size}")
        best_fitness_history = []
        best_solution = None
        best_fitness_overall = -np.inf
        start_time = time.time()

        for generation in range(max_generations):
            fitness_scores = [self.fitness_func(ind, self.initial_board, self.env) for ind in self.population]
            current_best_fitness = np.max(fitness_scores)
            current_best_index = np.argmax(fitness_scores)
            best_fitness_history.append(current_best_fitness)

            if current_best_fitness > best_fitness_overall:
                best_fitness_overall = current_best_fitness
                best_solution = self.population[current_best_index].copy()
                if visualize:
                     plot_sudoku_board(best_solution, initial_board=self.initial_board, title=f"{self.__class__.__name__} - Gen {generation+1} - Best Fit: {best_fitness_overall:.4f}", pause_time=0.05)

            if best_fitness_overall >= 1.0:
                 print(f"\n*** Solved (Fitness >= 1.0) in Generation {generation+1}! ***")
                 if visualize:
                      plot_sudoku_board(best_solution, initial_board=self.initial_board, title=f"{self.__class__.__name__} - Solved! Gen {generation+1}", pause_time=1.0)
                 break

            parents = self._selection(fitness_scores)
            next_population = []

            if self.elitism_count > 0:
                sorted_indices = np.argsort(fitness_scores)[::-1]
                for i in range(min(self.elitism_count, self.pop_size)):
                    next_population.append(self.population[sorted_indices[i]])

            num_offspring_needed = self.pop_size - len(next_population)
            parent_indices = list(range(len(parents)))
            current_offspring_count = 0
            while current_offspring_count < num_offspring_needed:
                 if len(parent_indices) < 2:
                     parent_indices = list(range(len(parents)))
                     random.shuffle(parent_indices)
                     if len(parent_indices) < 2:
                          if len(parents) > 0:
                              idx1 = parent_indices.pop(random.randrange(len(parent_indices))) if parent_indices else 0
                              child1 = self._mutation(parents[idx1].copy())
                              next_population.append(child1)
                              current_offspring_count +=1
                              if current_offspring_count >= num_offspring_needed: break
                          else: break

                 idx1 = parent_indices.pop(random.randrange(len(parent_indices)))
                 idx2 = parent_indices.pop(random.randrange(len(parent_indices)))
                 parent1 = parents[idx1]
                 parent2 = parents[idx2]
                 child1, child2 = self._crossover(parent1, parent2)
                 child1 = self._mutation(child1)
                 child2 = self._mutation(child2)
                 next_population.append(child1)
                 current_offspring_count += 1
                 if current_offspring_count < num_offspring_needed:
                    next_population.append(child2)
                    current_offspring_count += 1

            self.population = next_population[:self.pop_size]

            if (generation + 1) % 50 == 0:
                print(f"Generation {generation+1}/{max_generations} - Best Fitness: {best_fitness_overall:.4f}")

        if visualize: close_plot()
        end_time = time.time()
        print(f"{self.__class__.__name__} execution finished. Time: {end_time - start_time:.2f} sec.")
        return best_solution, best_fitness_history


class GeneticAlgorithmVariant3_LowCXNoElite:
    """
    Naive GA Variant 3: Low Crossover, No Elitism.
    Same logic as Variant 1, different internal parameters.
    """
    def __init__(self, env: SudokuEnvironment, fitness_func):
        self.env = env
        self.fitness_func = fitness_func
        self.initial_board = env.get_initial_board()
        self.size = env.get_size()
        self.subgrid_size = int(np.sqrt(self.size))
        self.fixed_indices = np.where(self.initial_board != 0)

        # --- Internal Parameters for this Variant ---
        self.pop_size = 100
        self.crossover_rate = 0.3 # << Low Crossover Rate
        self.mutation_rate = 0.15
        self.elitism_count = 0    # << No Elitism
        self.tournament_size = 3
        # --- End Internal Parameters ---

        self.population = self._initialize_population()

    def _initialize_population(self):
        population = []
        for _ in range(self.pop_size):
             individual = self.initial_board.copy()
             empty_cells = np.argwhere(individual == 0)
             for idx in empty_cells:
                 row, col = idx
                 individual[row, col] = random.randint(1, self.size)
             population.append(individual)
        return population

    def _selection(self, fitness_scores):
        selected_parents = []
        num_parents_needed = self.pop_size
        for _ in range(num_parents_needed):
            contender_indices = random.sample(range(self.pop_size), self.tournament_size)
            contender_fitness = [fitness_scores[i] for i in contender_indices]
            winner_idx = contender_indices[np.argmax(contender_fitness)]
            selected_parents.append(self.population[winner_idx])
        return selected_parents

    def _crossover(self, parent1, parent2):
        child1 = parent1.copy()
        child2 = parent2.copy()
        if random.random() < self.crossover_rate:
            for r in range(self.size):
                for c in range(self.size):
                     is_fixed = False
                     if r in self.fixed_indices[0] and c in self.fixed_indices[1]:
                          if np.any((self.fixed_indices[0] == r) & (self.fixed_indices[1] == c)):
                               is_fixed = True
                     if not is_fixed:
                         if random.random() < 0.5:
                             child1[r, c], child2[r, c] = parent2[r, c], parent1[r, c]
        return child1, child2

    def _mutation(self, individual):
        mutated_individual = individual.copy()
        for r in range(self.size):
            for c in range(self.size):
                is_fixed = False
                if r in self.fixed_indices[0] and c in self.fixed_indices[1]:
                     if np.any((self.fixed_indices[0] == r) & (self.fixed_indices[1] == c)):
                          is_fixed = True
                if not is_fixed:
                     if random.random() < self.mutation_rate:
                         mutated_individual[r, c] = random.randint(1, self.size)
        return mutated_individual

    def run(self, max_generations, visualize=True):
        print(f"Running {self.__class__.__name__} with {self.fitness_func.__name__}...")
        print(f"   Internal Params: Pop={self.pop_size}, CX={self.crossover_rate}, Mut={self.mutation_rate}, Elite={self.elitism_count}, Tourn={self.tournament_size}")
        best_fitness_history = []
        best_solution = None
        best_fitness_overall = -np.inf
        start_time = time.time()

        for generation in range(max_generations):
            fitness_scores = [self.fitness_func(ind, self.initial_board, self.env) for ind in self.population]
            current_best_fitness = np.max(fitness_scores)
            current_best_index = np.argmax(fitness_scores)
            best_fitness_history.append(current_best_fitness)

            if current_best_fitness > best_fitness_overall:
                best_fitness_overall = current_best_fitness
                best_solution = self.population[current_best_index].copy()
                if visualize:
                     plot_sudoku_board(best_solution, initial_board=self.initial_board, title=f"{self.__class__.__name__} - Gen {generation+1} - Best Fit: {best_fitness_overall:.4f}", pause_time=0.05)

            if best_fitness_overall >= 1.0:
                 print(f"\n*** Solved (Fitness >= 1.0) in Generation {generation+1}! ***")
                 if visualize:
                      plot_sudoku_board(best_solution, initial_board=self.initial_board, title=f"{self.__class__.__name__} - Solved! Gen {generation+1}", pause_time=1.0)
                 break

            parents = self._selection(fitness_scores)
            next_population = []

            if self.elitism_count > 0:
                sorted_indices = np.argsort(fitness_scores)[::-1]
                for i in range(min(self.elitism_count, self.pop_size)):
                    next_population.append(self.population[sorted_indices[i]])

            num_offspring_needed = self.pop_size - len(next_population)
            parent_indices = list(range(len(parents)))
            current_offspring_count = 0
            while current_offspring_count < num_offspring_needed:
                 if len(parent_indices) < 2:
                     parent_indices = list(range(len(parents)))
                     random.shuffle(parent_indices)
                     if len(parent_indices) < 2:
                          if len(parents) > 0:
                              idx1 = parent_indices.pop(random.randrange(len(parent_indices))) if parent_indices else 0
                              child1 = self._mutation(parents[idx1].copy())
                              next_population.append(child1)
                              current_offspring_count +=1
                              if current_offspring_count >= num_offspring_needed: break
                          else: break

                 idx1 = parent_indices.pop(random.randrange(len(parent_indices)))
                 idx2 = parent_indices.pop(random.randrange(len(parent_indices)))
                 parent1 = parents[idx1]
                 parent2 = parents[idx2]
                 child1, child2 = self._crossover(parent1, parent2)
                 child1 = self._mutation(child1)
                 child2 = self._mutation(child2)
                 next_population.append(child1)
                 current_offspring_count += 1
                 if current_offspring_count < num_offspring_needed:
                    next_population.append(child2)
                    current_offspring_count += 1

            self.population = next_population[:self.pop_size]

            if (generation + 1) % 50 == 0:
                print(f"Generation {generation+1}/{max_generations} - Best Fitness: {best_fitness_overall:.4f}")

        if visualize: close_plot()
        end_time = time.time()
        print(f"{self.__class__.__name__} execution finished. Time: {end_time - start_time:.2f} sec.")
        return best_solution, best_fitness_history


# List of GA implementations for easy selection
GA_VARIANTS = {
    "GA Variant 1 (Std Params)": GeneticAlgorithmVariant1_NaiveStdParams,
    "GA Variant 2 (High Mutation)": GeneticAlgorithmVariant2_HighMutation,
    "GA Variant 3 (Low CX, No Elite)": GeneticAlgorithmVariant3_LowCXNoElite,
}


# --- Main Execution Logic ---
if __name__ == "__main__":
    # 1. Setup Environment
    sudoku_env = SudokuEnvironment(size=SUDOKU_SIZE)
    puzzle_board = sudoku_env.generate_puzzle(difficulty=PUZZLE_DIFFICULTY)

    print("Generated Sudoku Puzzle:")
    plot_sudoku_board(puzzle_board, initial_board=puzzle_board, title="Initial Puzzle", pause_time=0)

    # --- Experimentation Setup ---
    # >>> Select which GA and Fitness function to run <<<
    selected_ga_name = "GA Variant 1 (Std Params)"      # Choose from GA_VARIANTS keys
    selected_fitness_name = "Fitness 1 (Binary Solved)" # Choose from FITNESS_FUNCTIONS keys

    # --- Define Max Generations (External Parameter) ---
    MAX_GENERATIONS = 1000 # How long to run the selected algorithm

    # Check if selections are valid
    if selected_ga_name not in GA_VARIANTS or selected_fitness_name not in FITNESS_FUNCTIONS:
        print(f"Error: Selected GA ('{selected_ga_name}') or Fitness function ('{selected_fitness_name}') name not found.")
        exit()

    GA_Class = GA_VARIANTS[selected_ga_name]
    fitness_func = FITNESS_FUNCTIONS[selected_fitness_name]

    print(f"\n--- Running Experiment ---")
    print(f"   Algorithm: {selected_ga_name}")
    print(f"   Fitness Fn: {selected_fitness_name}")
    print(f"   Max Generations: {MAX_GENERATIONS}")
    print("   (Internal GA parameters are defined within the selected class)")
    print("-" * 25)

    try:
        # Instantiate the selected GA (only env and fitness func needed externally)
        ga_instance = GA_Class(
            env=sudoku_env,
            fitness_func=fitness_func
        )

        # Run the GA, passing only max generations
        best_solution_found, fitness_log = ga_instance.run(MAX_GENERATIONS, visualize=True)

    except NotImplementedError:
        print(f"\n--- Experiment Aborted ---")
        print(f"ERROR: {selected_ga_name} seems to be missing its implementation.")
        exit()
    except Exception as e:
         print(f"\n--- An Error Occurred During GA Execution --- ")
         print(e)
         import traceback
         traceback.print_exc()
         exit()


    # --- Display Results ---
    print(f"\n--- Experiment Finished ({selected_ga_name} / {selected_fitness_name}) ---")

    if best_solution_found is not None:
        print("\nBest solution found (may not be perfect):")
        plot_sudoku_board(best_solution_found, initial_board=sudoku_env.get_initial_board(), title=f"Best Solution Found - {selected_ga_name}", pause_time=0)

        final_fitness = fitness_func(best_solution_found, sudoku_env.get_initial_board(), sudoku_env)
        print(f"Final Fitness Score: {final_fitness:.6f}")

        if sudoku_env.is_solved(best_solution_found):
            print("\n*** The found solution is a VALID and COMPLETE Sudoku solution! ***")
        else:
            print("\nThe found solution is NOT a complete valid Sudoku.")
            print(f"  (Final check: Row errors: {calculate_row_errors(best_solution_found)}, Col errors: {calculate_col_errors(best_solution_found)}, Subgrid errors: {calculate_subgrid_errors(best_solution_found)}, Changed clues: {check_initial_clues(best_solution_found, sudoku_env.get_initial_board())})")

        # Plot convergence
        plot_convergence(fitness_log, title=f"Convergence - {selected_ga_name} / {selected_fitness_name}")
    else:
        print("\nNo solution could be determined by the algorithm within the generation limit.")

    # --- Instructions for Students ---
    print("\n------------------------------------")
    print("Experiment Complete. To try other configurations:")
    print("1. Modify 'selected_ga_name' and 'selected_fitness_name' in the 'Experimentation Setup' section.")
    print("2. Modify the internal parameters within the chosen GA class (e.g., pop_size, rates).")
    print("3. Implement your own fitness logic in 'fitness_function_2_student'/'fitness_function_3_student'.")
    print("4. Modify the GA logic (selection, crossover, mutation) within a GA class or create a new GA class.")
    print("------------------------------------") 