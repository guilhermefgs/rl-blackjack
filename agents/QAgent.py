import numpy as np

class QAgent:
    """Q-Learning Agent
    """
    # class attributes
    decay = 0.01

    def __init__(self):
        self.q = {}
        self.epsilon = 0.7
        self.alpha = 0.1
        self.gamma = 0.9

    def feedback(self, state, action, reward, next_state):
        # handle new state
        if state not in self.q.keys():
            self.q[state] = [0,0]
        if next_state not in self.q.keys():
            self.q[next_state] = [0,0]
        
        # Bellman equation
        self.q[state][action] += self.alpha * (reward + self.gamma * np.max(self.q[next_state]) - self.q[state][action])

    def choose_action(self, state):
        if np.random.random() < self.epsilon:
            action = np.random.choice([0,1])
        else:
            action = np.argmax(self.q[state])
        self.epsilon *= QAgent.decay