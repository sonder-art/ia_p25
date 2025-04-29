import gymnasium as gym
import numpy as np
import time # For pausing during rendering
from agents import QLearningAgent, SarsaAgent
from visualizations import plot_rewards, plot_policy_q_values, display_plots

# --- Simulation Configurations --- (Students can modify these)

ENV_NAME = 'CliffWalking-v0'
NUM_RENDER_EPISODES = 3 # Number of episodes to render after training (0 to disable)
RENDER_DELAY = 0.2 # Seconds delay between steps during rendering

CONFIGS = [
    {
        "name": "Q-Learning",
        "agent_class": QLearningAgent,
        "hyperparameters": {
            "learning_rate": 0.1,
            "gamma": 0.99, # Discount factor (CliffWalking benefits from high gamma)
            "epsilon_start": 1.0,
            "epsilon_decay": 0.999,
            "epsilon_min": 0.01
        },
        # Reduced episodes for quicker testing, increase for better convergence (e.g., 1000)
        "episodes": 500 
    },
    {
        "name": "SARSA",
        "agent_class": SarsaAgent,
        "hyperparameters": {
            "learning_rate": 0.1,
            "gamma": 0.99,
            "epsilon_start": 1.0,
            "epsilon_decay": 0.999,
            "epsilon_min": 0.01
        },
        "episodes": 2000 # << Increased episodes for SARSA
    },
    # Add more configurations here to compare different hyperparameters, etc.
    # Example: Different learning rate
    # {
    #     "name": "Q-Learning (LR=0.5)",
    #     "agent_class": QLearningAgent,
    #     "hyperparameters": {
    #         "learning_rate": 0.5, 
    #         "gamma": 0.99,
    #         "epsilon_start": 1.0,
    #         "epsilon_decay": 0.999,
    #         "epsilon_min": 0.01
    #     },
    #     "episodes": 1000
    # },
]

SMOOTHING_WINDOW = 50 # For plotting rewards
MAX_EVAL_STEPS = 200 # Max steps per evaluation episode to prevent infinite loops
MAX_TRAINING_STEPS = 300 # Max steps per *training* episode

# --- Simulation Functions --- 

def run_training_episode(agent, env):
    """Runs a single training episode for the given agent and environment."""
    state, info = env.reset()
    episode_reward = 0
    terminated = False
    truncated = False
    steps = 0 # Step counter for training episode
    
    action = agent.choose_action(state)
    
    # Modified loop condition to include step limit
    while not terminated and not truncated and steps < MAX_TRAINING_STEPS: 
        next_state, reward, terminated, truncated, info = env.step(action)
        # Important: Choose next_action *before* the learn step for SARSA
        next_action = agent.choose_action(next_state) 
        
        # Agent learns based on its type
        if isinstance(agent, QLearningAgent):
            # Q-learning uses max Q of next state, doesn't need next_action here
            agent.learn(state, action, reward, next_state, terminated)
        elif isinstance(agent, SarsaAgent):
            # SARSA learns using the actual next action chosen
            agent.learn(state, action, reward, next_state, next_action, terminated)
            
        state = next_state
        action = next_action # Use the *chosen* next_action for the next step
        episode_reward += reward
        steps += 1 # Increment step counter
        
    # Note: We don't explicitly penalize for hitting the training step limit,
    # but the episode ending prevents infinite loops during training.
    return episode_reward

def run_evaluation_episode(agent_name, agent, env, delay=0.1):
    """Runs a single evaluation episode with rendering, following the learned policy."""
    state, info = env.reset()
    terminated = False
    truncated = False
    episode_reward = 0
    steps = 0 # Step counter
    print(f"\n--- Running Evaluation Episode for {agent_name} (Rendered) ---")
    
    # Modified loop condition
    while not terminated and not truncated and steps < MAX_EVAL_STEPS:
        env.render()
        time.sleep(delay)
        action = agent.get_best_action(state) # Use greedy policy
        next_state, reward, terminated, truncated, info = env.step(action)
        state = next_state
        episode_reward += reward
        steps += 1 # Increment step counter
        
        if terminated or truncated:
            env.render() # Render the final frame
            time.sleep(delay*2)
            
    if steps >= MAX_EVAL_STEPS:
        print(f"Evaluation episode terminated due to reaching max steps ({MAX_EVAL_STEPS}).")
        
    print(f"Evaluation episode finished. Reward: {episode_reward}, Steps: {steps}")
    print("---------------------------------------------")
    return episode_reward

def run_simulation(config):
    """Runs a full simulation (training) based on the provided config."""
    print(f"\n========== Running Simulation: {config['name']} ==========")
    
    train_env = gym.make(ENV_NAME)
    agent = config["agent_class"](env=train_env, **config["hyperparameters"])
    total_rewards_per_episode = []
    num_episodes = config["episodes"]

    for episode in range(num_episodes):
        episode_reward = run_training_episode(agent, train_env)
        total_rewards_per_episode.append(episode_reward)
        agent.decay_epsilon()
        
        # Print progress periodically
        if num_episodes > 0 and (episode + 1) % max(1, (num_episodes // 10)) == 0:
            # Calculate average reward of the last 100 episodes (or fewer if less than 100 total)
            avg_reward = np.mean(total_rewards_per_episode[max(0, episode-99):episode+1]) 
            print(f"  Episode {episode + 1}/{num_episodes} | Avg Reward (last 100): {avg_reward:.2f} | Epsilon: {agent.epsilon:.3f}")
            
    train_env.close()
    print(f"========== Simulation {config['name']} Training Finished ==========")
    return agent, total_rewards_per_episode

# --- Main Execution --- 

if __name__ == "__main__":
    results = {}
    final_agents = {}

    # --- Training Phase --- 
    print("\n========= Starting Training Phase =========")
    for config in CONFIGS:
        final_agent, rewards = run_simulation(config)
        results[config["name"]] = rewards
        final_agents[config["name"]] = final_agent
        
    print("\n========= Training Complete for all Configurations =========")

    # --- Visualization Phase (Static Plots) --- 
    print("\n========= Starting Visualization Phase =========")
    # Create one env instance for policy/Q-value plotting (no render needed)
    plot_env = gym.make(ENV_NAME)
    for name, agent in final_agents.items():
        # Plot Policy Grid and Q-Value Heatmaps for each agent
        plot_policy_q_values(agent, plot_env, f"{name}") 
    plot_env.close()

    # Plot comparative rewards (creates the figure)
    plot_rewards(results, f"Total Rewards per Episode ({ENV_NAME})", smoothing_window=SMOOTHING_WINDOW)

    # Display all generated matplotlib plots together
    print("\nDisplaying plots... Close plot windows to continue to rendering (if enabled).")
    display_plots() # This calls plt.show() once

    # --- Pygame Display Test ---
    print("\n--- Testing Pygame Display --- ")
    try:
        import pygame
        pygame.init()
        screen = pygame.display.set_mode([100, 100])
        pygame.display.set_caption("Pygame Test Window")
        print("Pygame display initialized successfully. Closing test window...")
        pygame.quit()
    except Exception as e:
        print(f"!!! Pygame display test FAILED: {e}")
        print("!!! Rendering will likely not work. Check display configuration (DISPLAY variable, X11 forwarding if using SSH, etc.)")
    print("----------------------------")

    # --- Optional Rendering Phase (Live Gameplay) ---
    if NUM_RENDER_EPISODES > 0:
        print(f"\n========= Running {NUM_RENDER_EPISODES} Rendered Evaluation Episodes =========")
        # Loop through the number of episodes to render
        for i in range(NUM_RENDER_EPISODES):
            print(f"\n--- Evaluation Run {i+1}/{NUM_RENDER_EPISODES} ---")
            # Loop through each trained agent
            for name, agent in final_agents.items():
                # Create a *new* environment WITH render_mode='human' for each agent evaluation
                render_env = gym.make(ENV_NAME, render_mode="human") # <<< THE KEY CHANGE
                try:
                    run_evaluation_episode(name, agent, render_env, delay=RENDER_DELAY)
                except Exception as e:
                    print(f"Error during rendering for {name}: {e}")
                finally:
                    # Important: Close the render environment window
                    render_env.close() # <<< ENSURE CLOSURE
    else:
         print("\nSkipping rendered evaluation episodes (NUM_RENDER_EPISODES = 0).") # Added else

    print("\nAll simulations complete.") 