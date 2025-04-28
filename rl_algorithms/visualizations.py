import matplotlib.pyplot as plt
import numpy as np
import gymnasium as gym # Import gym

def plot_rewards(rewards_data: dict, title: str, smoothing_window: int = 100):
    """Plots the rewards per episode for one or more algorithms.

    Args:
        rewards_data: A dictionary where keys are algorithm names (e.g., 'Q-Learning')
                      and values are lists or arrays of rewards per episode.
        title: The title for the plot.
        smoothing_window: The window size for calculating the rolling average.
    """
    plt.figure(figsize=(12, 6))
    
    for name, rewards in rewards_data.items():
        # Calculate the rolling average
        if len(rewards) >= smoothing_window:
            # Use pandas rolling mean for potentially better handling of edges
            try:
                import pandas as pd
                # Calculate rolling mean - it will have NaNs at the start
                smoothed_rewards_full = pd.Series(rewards).rolling(window=smoothing_window, min_periods=smoothing_window).mean().to_numpy()
                # Slice to remove NaNs and align with episodes axis
                smoothed_rewards = smoothed_rewards_full[smoothing_window - 1:] 
                episodes = np.arange(smoothing_window - 1, len(rewards))
            except ImportError:
                print("(Pandas not found, using numpy convolve for smoothing)")
                smoothed_rewards = np.convolve(rewards, np.ones(smoothing_window)/smoothing_window, mode='valid')
                episodes = np.arange(smoothing_window - 1, len(rewards))
            plt.plot(episodes, smoothed_rewards, label=f'{name} (Smoothed {smoothing_window} episodes)')
        else:
            # Plot raw data if too few episodes for smoothing
            plt.plot(rewards, label=f'{name} (Raw)')

    plt.title(title)
    plt.xlabel('Episode')
    plt.ylabel(f'Total Reward')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    # plt.show() # Delay showing until all plots are ready or save figures


def plot_policy_q_values(agent, env, title: str):
    """Visualizes the learned policy and Q-values for a grid environment like CliffWalking.
    
    Args:
        agent: The trained agent with a `q_table` and `get_best_action` method.
        env: The gymnasium environment instance.
        title: The title prefix for the plots.
    """
    print(f"\n--- Visualizing Policy and Q-Values for: {title} ---")

    if not (hasattr(env.spec, 'id') and env.spec.id == 'CliffWalking-v0'):
        print("(Skipping grid/heatmap visualization for this environment)")
        print("Q-Table (sample):")
        print(agent.q_table[:min(5, agent.q_table.shape[0]), :]) # Print sample
        print("-"*50)
        return

    try:
        q_table = agent.q_table
        
        # --- Policy Grid --- 
        policy = np.array([agent.get_best_action(s) for s in range(env.observation_space.n)])
        policy_grid = np.array([''] * env.observation_space.n, dtype=str).reshape(4, 12)
        actions_map = {0: '↑', 1: '→', 2: '↓', 3: '←'} # Up, Right, Down, Left
        
        for state, action in enumerate(policy):
            row, col = np.unravel_index(state, (4, 12))
            # Cliff states are 37-46, Goal is 47
            if state == 47:
                policy_grid[row, col] = 'G' # Goal
            elif 37 <= state <= 46:
                policy_grid[row, col] = 'X' # Cliff
            else: 
                policy_grid[row, col] = actions_map[action]
        
        # Mark start state
        policy_grid[3, 0] = 'S'
        
        print("\nLearned Policy (Arrows indicate best action):")
        # Print with better formatting
        for row in policy_grid:
            print(" ".join(f'{cell:>1}' for cell in row))
        print("-"*30)
        
        # --- Q-Value Heatmaps --- 
        fig, axes = plt.subplots(1, env.action_space.n, figsize=(15, 4), sharey=True)
        fig.suptitle(f'{title} - Q-Value Heatmaps per Action', fontsize=16)
        
        action_names = ['Up', 'Right', 'Down', 'Left']
        grid_shape = (4, 12)
        
        # Calculate common color limits across all actions for better comparison
        q_min = np.min(q_table[policy != -1]) # Ignore cliff/terminal states if policy marked them
        q_max = np.max(q_table[policy != -1])
        # Add a small buffer if min and max are too close
        if np.isclose(q_min, q_max):
            q_min -= 0.1
            q_max += 0.1

        for i, ax in enumerate(axes):
            q_action = q_table[:, i].reshape(grid_shape)
            # Mask cliff/terminal states for visualization (optional, can show their Q-values too)
            # mask = np.zeros_like(q_action, dtype=bool)
            # mask[3, 1:] = True # Mask row 3, columns 1 to 11 (cliff)
            # mask[3, 11] = False # Unmask goal
            # q_action_masked = np.ma.masked_where(mask, q_action)
            
            im = ax.imshow(q_action, cmap='viridis', vmin=q_min, vmax=q_max)
            ax.set_title(f'Action: {action_names[i]} ({actions_map[i]})')
            ax.set_xticks(np.arange(grid_shape[1]))
            ax.set_yticks(np.arange(grid_shape[0]))
            ax.set_xticklabels(np.arange(grid_shape[1]))
            ax.set_yticklabels(np.arange(grid_shape[0]))
            ax.tick_params(axis='x', rotation=90)

            # Add Q-values as text
            for r in range(grid_shape[0]):
                for c in range(grid_shape[1]):
                    ax.text(c, r, f'{q_action[r, c]:.1f}', ha='center', va='center', color='white' if abs(q_action[r,c]) > (q_max - q_min)/2 else 'black', fontsize=8)

            # Mark Start (S) and Goal (G) for context
            ax.text(0, 3, 'S', ha='center', va='center', color='red', weight='bold')
            ax.text(11, 3, 'G', ha='center', va='center', color='lime', weight='bold')

        fig.colorbar(im, ax=axes.ravel().tolist(), shrink=0.75, label='Q-Value')
        plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to prevent title overlap
        # plt.show() # Delay showing

    except Exception as e:
        print(f"Could not generate policy/Q-value visualization: {e}")
        import traceback
        traceback.print_exc()
        print("Q-Table (sample):")
        print(agent.q_table[:min(5, agent.q_table.shape[0]), :]) # Print sample
    print("-"*50)

# Make sure plots are displayed at the end
def display_plots():
    plt.show() 