# rl-blackjack

## The environment

This project are using 'Blackjack-v0' env from [OpenAI Gym](gym.openai.com).

### Actions
There are two actions in the space action of this environment, 0 (stand) or 1 (hit). 

### States
The state or observation of the env is a tuple
```python
>>> (sum_hand(self.player), self.dealer[0], usable_ace(self.player))
```
