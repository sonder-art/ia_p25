import numpy as np
import gymnasium as gym
import random

class QLearningAgent:
    def __init__(self, env: gym.Env, learning_rate: float, gamma: float, epsilon_start: float, epsilon_decay: float, epsilon_min: float):
        self.env = env
        self.lr = learning_rate
        self.gamma = gamma
        self.epsilon = epsilon_start
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        
        # Initialize Q-table with zeros
        # For discrete environments, action_space.n and observation_space.n exist
        # Adjust if using non-discrete spaces later
        if isinstance(env.observation_space, gym.spaces.Discrete) and isinstance(env.action_space, gym.spaces.Discrete):
            self.q_table = np.zeros((env.observation_space.n, env.action_space.n))
            # Set Q-value for terminal states to 0 if needed (though often handled by terminated flag)
            # Example for CliffWalking: State 47 is terminal, states 37-46 are cliffs
            # self.q_table[env.observation_space.n-1, :] = 0 # Optional: Ensure terminal state value is 0
        else:
            # Handle non-discrete spaces if necessary (more complex)
            raise NotImplementedError("Only Discrete observation and action spaces are supported for tabular methods.")

    def choose_action(self, state: int) -> int:
        """Chooses an action using an epsilon-greedy strategy."""
        if random.uniform(0, 1) < self.epsilon:
            # Explore: choose a random action
            action = self.env.action_space.sample()
        else:
            # Exploit: choose the best action from Q-table
            action = self.get_best_action(state)
        return action
        
    def get_best_action(self, state: int) -> int:
        """Chooses the best action greedily from the Q-table."""
        q_values = self.q_table[state]
        max_q = np.max(q_values)
        # Handle ties by selecting randomly among best actions
        best_actions = np.where(q_values == max_q)[0]
        return random.choice(best_actions)

    def learn(self, state: int, action: int, reward: float, next_state: int, terminated: bool):
        """Updates the Q-table using the Q-learning update rule."""
        # Find the maximum Q-value for the next state (handle terminal state)
        if terminated:
            target = reward # No future reward if terminated
        else:
            max_next_q = np.max(self.q_table[next_state])
            target = reward + self.gamma * max_next_q
            
        # Calculate the TD error and update Q-value
        td_error = target - self.q_table[state, action]
        self.q_table[state, action] += self.lr * td_error

    def decay_epsilon(self):
        """Decays the exploration rate."""
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)


class SarsaAgent:
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

    def learn(self, state: int, action: int, reward: float, next_state: int, next_action: int, terminated: bool):
        """Updates the Q-table using the SARSA update rule."""
        # Get the Q-value for the next state and *next action* (handle terminal state)
        if terminated:
            target = reward # No future reward if terminated
        else:
            next_q = self.q_table[next_state, next_action]
            target = reward + self.gamma * next_q
            
        # Calculate the TD error and update Q-value
        td_error = target - self.q_table[state, action]
        self.q_table[state, action] += self.lr * td_error

    def decay_epsilon(self):
        """Decays the exploration rate."""
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay) 