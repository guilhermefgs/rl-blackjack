import gym
from LogicAgent import LogicAgent

def print_game(observation=None, reward=None, action=None, i_episode=None):
    """Void function for printing the game
    Args:
        - observation: (tuple) the state of the game
        - reward: (double) the reward of the game
        - action: (boolean) last action taken
        - episode: (int) game round
    """
    print(f"Game Round - {i_episode}")
    print("Action: ", action)
    print("State: ", observation)
    print("Reward: ", reward)

if __name__ == '__main__':

    # create environment
    env = gym.make('Blackjack-v0')
    agent = LogicAgent()
    cumulative_reward = 0

    # simulate random Agente
    for i_episode in range(20):

        observation = env.reset()
        print_game(observation, i_episode)
        
        for t in range(100):
            
            action = agent.action(observation)

            observation, reward, done, info = env.step(action)
            print_game(observation, reward, action, i_episode)
            cumulative_reward += reward
            
            if done:
                print("Episode finished after {} timesteps".format(t+1))
                print("\n")
                break

        print("Current Reward: ", cumulative_reward)
    print("Final Reward: ", cumulative_reward)
    env.close()