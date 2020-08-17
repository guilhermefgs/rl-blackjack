import gym
from agents import LogicAgent, QAgent

# TODO 
# create base agent
# create pandas dataframe for game log

def print_game(obs=None, reward=None, action=None, i_episode=None, current_reward=None):
    """Void function for printing the game
    Args:
        - obs: (tuple) the state of the game
        - reward: (double) the reward of the game
        - action: (boolean) last action taken
        - i_episode: (int) game round
        - current_reward: (double) current table player's reward
    """
    print(f"Game Round - {i_episode}")
    print("Action: ", action)
    print("State: ", obs)
    print("Reward: ", reward)
    print("Current Game Reward: ", current_reward)
    print("\n")

def train_agent(agent, env, n_episodes=500):
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
        # get first state
        state = env.reset()

        # print game
        print_game(obs=state, i_episode=i_episode)
        current_reward = 0 
        for t in range(100):
            # take action
            action = agent.choose_action(state)
            next_state, reward, done, info = env.step(action)

            # update q
            agent.feedback(state, action, reward, next_state)
            state = next_state

            # print game
            current_reward += reward
            print_game(next_state, reward, action, i_episode, current_reward)
            
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
    agent = QAgent()

    train_agent(agent, env, n_episodes=20000)

    #print(agent.q)
