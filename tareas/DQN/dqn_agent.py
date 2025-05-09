import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random
import math
from models import QNetwork
from replay_buffer import ReplayBuffer

class DQNAgent:
    def __init__(self, 
                 obs_dim, 
                 action_dim, 
                 buffer_capacity=10000,
                 batch_size=128, 
                 gamma=0.99, 
                 learning_rate=1e-4,
                 epsilon_start=0.9, 
                 epsilon_end=0.05, 
                 epsilon_decay=1000,
                 target_update_frequency=500,
                 device=None):
        """
        Initialize a DQN Agent
        
        Args:
            obs_dim (int): Dimension of the observation space
            action_dim (int): Dimension of the action space
            buffer_capacity (int): Capacity of the replay buffer
            batch_size (int): Size of batches to sample from replay buffer
            gamma (float): Discount factor
            learning_rate (float): Learning rate for optimizer
            epsilon_start (float): Starting value for epsilon (exploration rate)
            epsilon_end (float): Minimum value for epsilon
            epsilon_decay (int): Steps over which to decay epsilon
            target_update_frequency (int): How often to update target network
            device: Device to run computations on (CPU/GPU)
        """
        # Set device
        self.device = device if device else torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        # Initialize networks
        self.policy_net = QNetwork(obs_dim, action_dim).to(self.device)
        self.target_net = QNetwork(obs_dim, action_dim).to(self.device)
        
        # Copy weights from policy_net to target_net
        self.target_net.load_state_dict(self.policy_net.state_dict())
        self.target_net.eval()  # Set target net to evaluation mode
        
        # Setup optimizer
        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=learning_rate)
        
        # Initialize replay buffer
        self.replay_buffer = ReplayBuffer(buffer_capacity)
        
        # Save hyperparameters
        self.batch_size = batch_size
        self.gamma = gamma
        self.epsilon_start = epsilon_start
        self.epsilon_end = epsilon_end
        self.epsilon_decay = epsilon_decay
        self.target_update_frequency = target_update_frequency
        self.action_dim = action_dim
        
        # Initialize exploration parameters
        self.epsilon = epsilon_start
        self.steps_done = 0
    
    def choose_action(self, state, evaluate=False):
        """
        Select an action using epsilon-greedy policy
        
        Args:
            state: Current observation/state
            evaluate (bool): If True, use greedy policy (no exploration)
            
        Returns:
            int: Selected action
        """
        # Calculate current epsilon based on step count
        epsilon = self.epsilon_end + (self.epsilon_start - self.epsilon_end) * \
                  math.exp(-1. * self.steps_done / self.epsilon_decay)
        
        self.epsilon = epsilon
        self.steps_done += 1
        
        # Convert state to tensor
        state_tensor = torch.tensor(state, dtype=torch.float32, device=self.device).unsqueeze(0)
        
        # Use greedy policy during evaluation, or if random sample > epsilon
        if evaluate or random.random() > epsilon:
            with torch.no_grad():
                # Get action with maximum Q-value
                q_values = self.policy_net(state_tensor)
                action = q_values.max(1)[1].item()
        else:
            # Random action for exploration
            action = random.randrange(self.action_dim)
            
        return action
        
    def learn(self):
        """
        Update policy network using a batch from replay buffer
        """
        # Check if we have enough samples in buffer
        if len(self.replay_buffer) < self.batch_size:
            return
        
        # Sample a batch from replay buffer
        states, actions, rewards, non_final_next_states, non_final_mask, dones = \
            self.replay_buffer.sample(self.batch_size)
        
        # Move tensors to the configured device
        states = states.to(self.device)
        actions = actions.to(self.device)
        rewards = rewards.to(self.device)
        non_final_next_states = non_final_next_states.to(self.device)
        non_final_mask = non_final_mask.to(self.device)
        dones = dones.to(self.device)
        
        # Compute Q(s_t, a) - the model computes Q(s_t), then we select the columns of actions taken
        current_q_values = self.policy_net(states).gather(1, actions)
        
        # Compute V(s_{t+1}) for all next states
        next_q_values = torch.zeros(self.batch_size, 1, device=self.device)
        
        with torch.no_grad():
            # Only compute V(s_{t+1}) for non-terminal states
            next_q_values[non_final_mask] = self.target_net(non_final_next_states).max(1)[0].unsqueeze(1)
        
        # Compute the expected Q values: Q* = r + γ * max_a' Q(s', a')
        target_q_values = rewards + (self.gamma * next_q_values * (1 - dones))
        
        # Compute Huber loss (smoothL1Loss)
        criterion = nn.SmoothL1Loss()
        loss = criterion(current_q_values, target_q_values)
        
        # Optimize the model
        self.optimizer.zero_grad()
        loss.backward()
        
        # In-place gradient clipping
        torch.nn.utils.clip_grad_value_(self.policy_net.parameters(), 100)
        
        self.optimizer.step()
        
        return loss.item()
    
    def update_target_network(self):
        """
        Update the target network with the policy network's weights
        """
        self.target_net.load_state_dict(self.policy_net.state_dict())
