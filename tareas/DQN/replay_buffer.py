from collections import namedtuple, deque
import random
import torch
import numpy as np

# Define a named tuple to store transitions
Transition = namedtuple('Transition', ('state', 'action', 'reward', 'next_state', 'done'))

class ReplayBuffer:
    def __init__(self, capacity):
        """
        Initialize a Replay Buffer for storing experiences
        
        Args:
            capacity (int): Maximum size of the buffer
        """
        self.memory = deque([], maxlen=capacity)
    
    def push(self, state, action, reward, next_state, done):
        """
        Store a transition in the buffer
        
        Args:
            state: Current state
            action: Action taken
            reward: Reward received
            next_state: Next state observed
            done: Whether episode has ended
        """
        self.memory.append(Transition(state, action, reward, next_state, done))
    
    def sample(self, batch_size):
        """
        Sample a batch of transitions from the buffer
        
        Args:
            batch_size (int): Size of the batch to sample
            
        Returns:
            Tuple of (state_batch, action_batch, reward_batch, next_state_batch, done_batch)
        """
        transitions = random.sample(self.memory, batch_size)
        
        # Transpose the batch (convert list of Transitions to Transition of lists/tuples)
        batch = Transition(*zip(*transitions))
        
        # Convert components to PyTorch tensors with appropriate types
        state_batch = torch.cat([torch.tensor(s, dtype=torch.float32).unsqueeze(0) for s in batch.state])
        action_batch = torch.tensor(batch.action, dtype=torch.long).unsqueeze(1)  # Shape [batch_size, 1] for gather
        reward_batch = torch.tensor(batch.reward, dtype=torch.float32).unsqueeze(1)
        
        # Handle next_states (might contain None for terminal states)
        non_final_mask = torch.tensor([s is not None for s in batch.next_state], dtype=torch.bool)
        non_final_next_states = torch.cat([torch.tensor(s, dtype=torch.float32).unsqueeze(0) 
                                          for s in batch.next_state if s is not None])
        
        done_batch = torch.tensor(batch.done, dtype=torch.float32).unsqueeze(1)  # Float for multiplication
        
        return state_batch, action_batch, reward_batch, non_final_next_states, non_final_mask, done_batch
    
    def __len__(self):
        """Return the current size of the buffer"""
        return len(self.memory)
