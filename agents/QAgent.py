import numpy as np
from collections import defaultdict 

class QAgent:
    """Q-Learning Agent
    """
    # class attributes
    decay = 0.99

    def __init__(self):
        self.q = defaultdict(lambda: [0,0])
        self.epsilon = 0.7
        self.alpha = 0.01
        self.gamma = 0.9

    def feedback(self, state, action, reward, next_state):
        # Bellman equation
        self.q[state][action] += self.alpha * (reward + self.gamma * np.max(self.q[next_state]) - self.q[state][action])

    def choose_action(self, state):
        if np.random.random() < self.epsilon:
            action = np.random.choice([0,1])
        else:
            action = np.argmax(self.q[state])

        self.epsilon *= QAgent.decay
        return action