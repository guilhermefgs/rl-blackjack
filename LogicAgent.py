class LogicAgent:
    """Logic Agent
    It plays based on an action rule
    """

    def __init__(self, min_to_fold = 16):
        self.min_to_fold = min_to_fold

    def action(self, observation):
        """Takes an action based on rule
        Args:
            - observation: (tuple) state set given last action
        Returns:
            - 1 or 0, 1 for hit, 0 for stand
        """
        if(observation[0] >= self.min_to_fold and observation[0] < 21):
            return 0
        return 1

