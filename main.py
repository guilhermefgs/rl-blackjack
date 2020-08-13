import gym
from agents import LogicAgent, QAgent

# TODO 
# create test_agent for any agent
# create base agent
# create pandas dataframe for game log

def print_game(observation=None, reward=None, action=None, i_episode=None, current_reward=None):
    """Void function for printing the game
    Args:
        - observation: (tuple) the state of the game
        - reward: (double) the reward of the game
        - action: (boolean) last action taken
        - i_episode: (int) game round
        - current_reward: (double) current table player's reward
    """
    print(f"Game Round - {i_episode}")
    print("Action: ", action)
    print("State: ", observation)
    print("Reward: ", reward)
    print("Current Game Reward: ", current_reward)
    print("\n")

def test_agent(agent, env, n_episodes=500):
    """Function that test the agent
    Args:
        - agent: (Agent) the player
        - env: (gym.env) the environment/ the game
        - n_episodes: (int) the number
    Returns:
    """
    final_reward = 0
    # simulate random Agente
    for i_episode in range(n_episodes):

        observation = env.reset()
        print_game(observation, i_episode)
        current_reward = 0 
        for t in range(100):
            
            action = agent.choose_action(observation)
            observation, reward, done, info = env.step(action)

            current_reward += reward
            print_game(observation, reward, action, i_episode, current_reward)
            
            if done:
                print("Episode finished after {} timesteps".format(t+1))
                print("\n")
                break

        final_reward += current_reward
        print("Final Reward: ", final_reward)
    env.close()


if __name__ == '__main__':

    # create environment
    env = gym.make('Blackjack-v0')
    agent = LogicAgent()

    test_agent(agent, env)