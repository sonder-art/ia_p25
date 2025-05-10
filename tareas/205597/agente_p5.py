import numpy as np
import gymnasium as gym
import random

class ExpectedSarsaAgent:
    def __init__(self, env: gym.Env, learning_rate: float, gamma: float, epsilon_start: float, epsilon_decay: float, epsilon_min: float):
        self.env = env
        self.lr = learning_rate
        self.gamma = gamma
        self.epsilon = epsilon_start
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        
        if isinstance(env.observation_space, gym.spaces.Discrete) and isinstance(env.action_space, gym.spaces.Discrete):
            self.q_table = np.zeros((env.observation_space.n, env.action_space.n))
            # self.q_table[env.observation_space.n-1, :] = 0 # Optional
        else:
            raise NotImplementedError("Only Discrete observation and action spaces are supported for tabular methods.")

    def choose_action(self, state: int) -> int:
        """Chooses an action using an epsilon-greedy strategy."""
        if random.uniform(0, 1) < self.epsilon:
            action = self.env.action_space.sample()
        else:
            action = self.get_best_action(state)
        return action

    def get_best_action(self, state: int) -> int:
        """Chooses the best action greedily from the Q-table."""
        q_values = self.q_table[state]
        max_q = np.max(q_values)
        best_actions = np.where(q_values == max_q)[0]
        return random.choice(best_actions)

    def learn(self, state: int, action: int, reward: float, next_state: int, terminated: bool):
        """Updates the Q-table using the Expected SARSA update rule."""
        if terminated:
            target = reward  # No future reward if terminated
        else:
            # Calcular el valor esperado para el siguiente estado
            num_actions = self.env.action_space.n
            next_q_values = self.q_table[next_state]
            
            # Determinar la acción greedy en el siguiente estado
            max_q = np.max(next_q_values)
            greedy_actions = np.where(next_q_values == max_q)[0]
            greedy_action = greedy_actions[0]  # Cualquier acción con valor máximo
            
            # Calcular las probabilidades de la política ε-greedy
            probabilities = np.ones(num_actions) * (self.epsilon / num_actions)  # Probabilidad base por exploración
            # La acción greedy tiene probabilidad adicional por explotación
            probabilities[greedy_action] += (1 - self.epsilon)
            
            # Calcular el valor esperado
            expected_value = np.sum(probabilities * next_q_values)
            
            # Calcular el target usando el valor esperado
            target = reward + self.gamma * expected_value
            
        # Calcular el TD error y actualizar el valor Q
        td_error = target - self.q_table[state, action]
        self.q_table[state, action] += self.lr * td_error

    def decay_epsilon(self):
        """Decays the exploration rate."""
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)