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

* **sum_hand(player)**: the agent's current sum hand
* **dealer[0]**: value of dealers first card, the second card is not shown
* **usable_ace(player)**: if agent is using ace 

