class Shield:
    def __init__(self, pacmanPos, ghostPos, legalActions, action_qval_list, action):
        self.pacmanPos = pacmanPos
        self.ghostPos = ghostPos
        self.legalActions = legalActions
        self.action_qval_list = action_qval_list
        self.apply(action)

    def apply(self, action):
        safe = False
        sorted(self.action_qval_list, key=lambda x: x[1], reverse=True)
        i = 0
        self.discarded = []
        while not safe and len(self.legalActions) != 0:
            px, py = self.pacmanPos
            if action == 'East':
                px += 1
            elif action == 'West':
                px -= 1
            elif action == 'North':
                py += 1
            elif action == 'South':
                py -= 1

            num_ghosts = len(state.data.agentStates) - 1

            safe = True
            for j in range(len(self.ghostPos)):
                ghostpos = ghostPos[j]
                dist = manhattanDistance((px, py), ghostpos)
                if dist < 2.0:
                    safe = False
                    self.discarded.append(action)
                    legalActions.remove(action)
                    break
            if not safe and i < len(action_qval_list):
                action = action_qval_list[i][0]
            i += 1

        if len(legalActions) == 0:
            action = action_copy

        return action, self.discarded