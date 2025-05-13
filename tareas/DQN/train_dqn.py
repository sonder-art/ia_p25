import gymnasium as gym
import torch
import numpy as np
import matplotlib.pyplot as plt
from dqn_agent import DQNAgent
import itertools
import time
from collections import deque

def moving_average(data, window_size):
    """Calculate the moving average of a list with the given window size."""
    if len(data) < window_size:
        return data
    
    moving_averages = []
    for i in range(len(data) - window_size + 1):
        window_average = sum(data[i:i+window_size]) / window_size
        moving_averages.append(window_average)
    
    return moving_averages

def train(env_name="CartPole-v1", 
          num_episodes=1000, 
          buffer_capacity=10000, 
          batch_size=128, 
          gamma=0.99, 
          learning_rate=1e-4, 
          epsilon_start=0.9, 
          epsilon_end=0.05, 
          epsilon_decay=1000, 
          target_update=500, 
          eval_interval=100, 
          render_after_training=True,
          max_steps_per_episode=1000):
    """
    Train a DQN agent
    
    Args:
        env_name (str): Name of the Gymnasium environment
        num_episodes (int): Number of episodes to train for
        buffer_capacity (int): Capacity of the replay buffer
        batch_size (int): Size of batches to sample from replay buffer
        gamma (float): Discount factor
        learning_rate (float): Learning rate for optimizer
        epsilon_start (float): Starting value for epsilon (exploration rate)
        epsilon_end (float): Minimum value for epsilon
        epsilon_decay (int): Steps over which to decay epsilon
        target_update (int): How often to update target network (in steps)
        eval_interval (int): How often to evaluate the agent (in episodes)
        render_after_training (bool): Whether to render the environment after training
        max_steps_per_episode (int): Maximum steps per episode
    """
    # Device configuration
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    # Create environment
    env = gym.make(env_name)
    
    # Get dimensions of observation and action spaces
    obs_dim = env.observation_space.shape[0]
    action_dim = env.action_space.n
    
    print(f"Environment: {env_name}")
    print(f"Observation Space Dimension: {obs_dim}")
    print(f"Action Space Dimension: {action_dim}")
    
    # Create DQN agent
    agent = DQNAgent(
        obs_dim=obs_dim,
        action_dim=action_dim,
        buffer_capacity=buffer_capacity,
        batch_size=batch_size,
        gamma=gamma,
        learning_rate=learning_rate,
        epsilon_start=epsilon_start,
        epsilon_end=epsilon_end,
        epsilon_decay=epsilon_decay,
        target_update_frequency=target_update,
        device=device
    )
    
    # Lists to store metrics
    episode_rewards = []
    episode_lengths = []
    losses = []
    epsilon_values = []
    
    # For evaluation
    best_eval_reward = -float('inf')
    eval_rewards = []
    
    # For tracking progress
    total_steps = 0
    progress_window = 10  # Print progress every 10 episodes
    
    # Training loop
    start_time = time.time()
    print("Starting training...")
    
    for i_episode in range(num_episodes):
        # Reset the environment
        state, _ = env.reset()
        episode_reward = 0
        episode_loss = 0
        num_updates = 0
        
        # Episode loop
        for t in itertools.count():
            # Select and perform an action
            action = agent.choose_action(state)
            
            # Take the action
            next_state, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            
            # Store the transition in replay buffer
            # Convert action to tensor format (scalar to tensor)
            if done:
                next_state = None
            
            # Store transition in replay buffer
            agent.replay_buffer.push(state, action, reward, next_state, done)
            
            # Move to the next state
            state = next_state
            
            # Perform one optimization step
            loss = agent.learn()
            if loss is not None:
                episode_loss += loss
                num_updates += 1
            
            # Update target network periodically
            if total_steps % agent.target_update_frequency == 0:
                agent.update_target_network()
            
            # Add reward to episode reward
            episode_reward += reward
            total_steps += 1
            
            # Break if episode is done
            if done:
                break
        
        # Store metrics
        episode_rewards.append(episode_reward)
        episode_lengths.append(t + 1)
        epsilon_values.append(agent.epsilon)
        
        if num_updates > 0:
            losses.append(episode_loss / num_updates)
        else:
            losses.append(0)
        
        # Print progress
        if (i_episode + 1) % progress_window == 0:
            avg_reward = sum(episode_rewards[-progress_window:]) / progress_window
            print(f"Episode {i_episode+1}/{num_episodes} | Avg Reward: {avg_reward:.2f} | "
                  f"Epsilon: {agent.epsilon:.2f} | Steps: {total_steps}")
        
        # Evaluate agent periodically
        if (i_episode + 1) % eval_interval == 0:
            eval_reward = evaluate_agent(agent, env_name, num_episodes=10)
            eval_rewards.append(eval_reward)
            print(f"Evaluation at episode {i_episode+1}: Average Reward = {eval_reward:.2f}")
            
            # Save best model
            if eval_reward > best_eval_reward:
                best_eval_reward = eval_reward
                torch.save(agent.policy_net.state_dict(), f"best_{env_name}_model.pth")
                print(f"New best model saved with reward: {best_eval_reward:.2f}")
    
    # Training time
    training_time = time.time() - start_time
    print(f"Training completed in {training_time:.2f} seconds")
    
    # Plot training metrics
    plot_metrics(episode_rewards, losses, epsilon_values, eval_rewards, eval_interval)
    
    # Render trained agent
    if render_after_training:
        print("Rendering trained agent...")
        render_agent(agent, env_name)
    
    # Close environment
    env.close()
    
    return agent

def evaluate_agent(agent, env_name, num_episodes=10):
    """
    Evaluate the agent without exploration
    
    Args:
        agent (DQNAgent): The agent to evaluate
        env_name (str): Name of the environment
        num_episodes (int): Number of episodes to evaluate
        
    Returns:
        float: Average reward across all evaluation episodes
    """
    eval_env = gym.make(env_name)
    total_rewards = []
    
    for _ in range(num_episodes):
        state, _ = eval_env.reset()
        episode_reward = 0
        done = False
        
        while not done:
            action = agent.choose_action(state, evaluate=True)
            next_state, reward, terminated, truncated, _ = eval_env.step(action)
            done = terminated or truncated
            episode_reward += reward
            state = next_state
        
        total_rewards.append(episode_reward)
    
    eval_env.close()
    return sum(total_rewards) / num_episodes

def render_agent(agent, env_name, num_episodes=3):
    """
    Render the agent's performance in the environment
    
    Args:
        agent (DQNAgent): The trained agent
        env_name (str): Name of the environment
        num_episodes (int): Number of episodes to render
    """
    try:
        render_env = gym.make(env_name, render_mode="human")
        
        for _ in range(num_episodes):
            state, _ = render_env.reset()
            episode_reward = 0
            done = False
            
            while not done:
                action = agent.choose_action(state, evaluate=True)
                next_state, reward, terminated, truncated, _ = render_env.step(action)
                done = terminated or truncated
                episode_reward += reward
                state = next_state
            
            print(f"Rendered episode reward: {episode_reward}")
        
        render_env.close()
    except Exception as e:
        print(f"Error rendering: {e}")
        print("Rendering may not be supported in this environment or current setup.")

def plot_metrics(rewards, losses, epsilons, eval_rewards, eval_interval):
    """
    Plot training metrics
    
    Args:
        rewards (list): Episode rewards
        losses (list): Average losses per episode
        epsilons (list): Epsilon values per episode
        eval_rewards (list): Evaluation rewards
        eval_interval (int): Evaluation interval
    """
    plt.figure(figsize=(15, 10))
    
    # Plot rewards
    plt.subplot(2, 2, 1)
    plt.plot(rewards, label='Episode Reward')
    
    # Plot moving average of rewards
    window_size = min(100, len(rewards) // 10) if len(rewards) > 10 else len(rewards)
    if window_size > 1:
        moving_avg = moving_average(rewards, window_size)
        plt.plot(range(window_size-1, window_size-1+len(moving_avg)), moving_avg, 'r-', label=f'Moving Avg ({window_size})')
    
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.title('Training Rewards')
    plt.legend()
    plt.grid(True)
    
    # Plot losses
    plt.subplot(2, 2, 2)
    if losses:  # Make sure losses list is not empty
        plt.plot(losses)
        plt.xlabel('Episode')
        plt.ylabel('Loss')
        plt.title('Training Loss per Episode')
        plt.grid(True)
    
    # Plot epsilon
    plt.subplot(2, 2, 3)
    plt.plot(epsilons)
    plt.xlabel('Episode')
    plt.ylabel('Epsilon')
    plt.title('Exploration Rate (Epsilon)')
    plt.grid(True)
    
    # Plot evaluation rewards
    plt.subplot(2, 2, 4)
    if eval_rewards:  # Make sure eval_rewards list is not empty
        eval_episodes = [i * eval_interval for i in range(len(eval_rewards))]
        plt.plot(eval_episodes, eval_rewards, 'g-o')
        plt.xlabel('Episode')
        plt.ylabel('Evaluation Reward')
        plt.title('Evaluation Rewards')
        plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('dqn_training_metrics.png')
    plt.show()

if __name__ == "__main__":
    # Configure environment and hyperparameters
    env_name = "CartPole-v1"  # Change to "LunarLander-v2" for a more complex environment
    
    # Hyperparameters
    hyperparams = {
        "num_episodes": 500,         # Number of episodes to train
        "buffer_capacity": 10000,    # Replay buffer size
        "batch_size": 128,           # Batch size for training
        "gamma": 0.99,               # Discount factor
        "learning_rate": 1e-4,       # Learning rate
        "epsilon_start": 0.9,        # Starting exploration rate
        "epsilon_end": 0.05,         # Minimum exploration rate
        "epsilon_decay": 1000,       # Exploration decay rate (in steps)
        "target_update": 500,        # Target network update frequency (in steps)
        "eval_interval": 50,         # Evaluation interval (in episodes)
        "render_after_training": True # Render agent after training
    }
    
    # Train the agent
    trained_agent = train(env_name=env_name, **hyperparams)
