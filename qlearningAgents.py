# qlearningAgents.py
# ------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
	"""
	  Q-Learning Agent

	  Functions you should fill in:
		- computeValueFromQValues
		- computeActionFromQValues
		- getQValue
		- getAction
		- update

	  Instance variables you have access to
		- self.epsilon (exploration prob)
		- self.alpha (learning rate)
		- self.discount (discount rate)

	  Functions you should use
		- self.getLegalActions(state)
		  which returns legal actions for a state
	"""
	def __init__(self, shield=False, **args):
		"You can initialize Q-values here..."
		ReinforcementAgent.__init__(self, **args)

		"*** YOUR CODE HERE ***"
		self.q_values = util.Counter()
		self.shield = shield


	def getQValue(self, state, action):
		"""
		  Returns Q(state,action)
		  Should return 0.0 if we have never seen a state
		  or the Q node value otherwise
		"""
		"*** YOUR CODE HERE ***"
		if (state, action) in self.q_values:
			return self.q_values[(state, action)]
		else:
			return 0.0


	def computeValueFromQValues(self, state):
		"""
		  Returns max_action Q(state,action)
		  where the max is over legal actions.  Note that if
		  there are no legal actions, which is the case at the
		  terminal state, you should return a value of 0.0.
		"""
		"*** YOUR CODE HERE ***"
		max_q = 'NA'
		action_list = self.getLegalActions(state)

		if not action_list:
			return 0.0

		for action in action_list:
			q_val = self.getQValue(state, action)
			if max_q == 'NA' or q_val > max_q :
				max_q = q_val

		return max_q


	def computeActionFromQValues(self, state):
		"""
		  Compute the best action to take in a state.  Note that if there
		  are no legal actions, which is the case at the terminal state,
		  you should return None.
		"""
		"*** YOUR CODE HERE ***"
		max_q = self.computeValueFromQValues(state)
		max_action = None
		action_list = self.getLegalActions(state)

		if not action_list:
			return None

		max_action_list = []
		for action in action_list:
			if self.getQValue(state,action) == max_q:
				max_action_list.append(action)

		max_action = random.choice(max_action_list)
		return max_action


	def getAction(self, state):
		"""
		  Compute the action to take in the current state.  With
		  probability self.epsilon, we should take a random action and
		  take the best policy action otherwise.  Note that if there are
		  no legal actions, which is the case at the terminal state, you
		  should choose None as the action.

		  HINT: You might want to use util.flipCoin(prob)
		  HINT: To pick randomly from a list, use random.choice(list)
		"""
		# Pick Action
		legalActions = self.getLegalActions(state)
		action = None
		"*** YOUR CODE HERE ***"

		if not legalActions :
			action = None

		elif util.flipCoin(self.epsilon):
			action = random.choice(legalActions)

		else:
			action = self.computeActionFromQValues(state)
		# if action not in legalActions:
		# 	print("WTFFFF")
		action_copy = action

		if self.shield:
			safe = False
			legal_qval = []
			# print(legalActions)
			# legalActions.remove(action)

			for ac in legalActions:
				if ac != action:
					legal_qval.append((ac, self.getQValue(state,ac)))

			sorted(legal_qval, key=lambda x: x[1], reverse=True)
			i = 0
			# print(legal_qval)
			while not safe and len(legalActions) != 0:
				# if action not in legalActions:
				# 	print("WTFFFFF")
				px, py = state.getPacmanPosition()
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
				for j in range(num_ghosts):
					ghostpos = state.getGhostPosition(j+1)
					dist = manhattanDistance((px, py), ghostpos)
					# print(dist)
					if dist < 2.0:
						safe = False
						legalActions.remove(action)
						break
				# if action == 'Stop':
				# 	safe = False
				# print(action)
				if not safe and i < len(legal_qval):
					action = legal_qval[i][0]
				i += 1

			if len(legalActions) == 0:
				action = action_copy

		return action

	def update(self, state, action, nextState, reward):
		"""
		  The parent class calls this to observe a
		  state = action => nextState and reward transition.
		  You should do your Q-Value update here

		  NOTE: You should never call this function,
		  it will be called on your behalf
		"""
		"*** YOUR CODE HERE ***"

		max_q = self.computeValueFromQValues(nextState)

		self.q_values[(state, action)] = (1-self.alpha)*self.getQValue(state, action) + self.alpha*(reward + self.discount*max_q)


	def getPolicy(self, state):
		return self.computeActionFromQValues(state)

	def getValue(self, state):
		return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
	"Exactly the same as QLearningAgent, but with different default parameters"

	def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
		"""
		These default parameters can be changed from the pacman.py command line.
		For example, to change the exploration rate, try:
			python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

		alpha    - learning rate
		epsilon  - exploration rate
		gamma    - discount factor
		numTraining - number of training episodes, i.e. no learning after these many episodes
		"""
		args['epsilon'] = epsilon
		args['gamma'] = gamma
		args['alpha'] = alpha
		args['numTraining'] = numTraining
		self.index = 0  # This is always Pacman
		QLearningAgent.__init__(self, **args)

	def getAction(self, state):
		"""
		Simply calls the getAction method of QLearningAgent and then
		informs parent of action for Pacman.  Do not change or remove this
		method.
		"""
		action = QLearningAgent.getAction(self,state)
		self.doAction(state,action)
		return action


class ApproximateQAgent(PacmanQAgent):
	"""
	   ApproximateQLearningAgent

	   You should only have to overwrite getQValue
	   and update.  All other QLearningAgent functions
	   should work as is.
	"""
	def __init__(self, extractor='IdentityExtractor', **args):
		self.featExtractor = util.lookup(extractor, globals())()
		PacmanQAgent.__init__(self, **args)
		self.weights = util.Counter()

	def getWeights(self):
		return self.weights

	def getQValue(self, state, action):
		"""
		  Should return Q(state,action) = w * featureVector
		  where * is the dotProduct operator
		"""
		"*** YOUR CODE HERE ***"
		featureVector = self.featExtractor.getFeatures(state,action)
		weights = self.getWeights()

		Q = 0

		for key in featureVector:
			Q += featureVector[key]*weights[key]

		return Q



	def update(self, state, action, nextState, reward):
		"""
		   Should update your weights based on transition
		"""
		"*** YOUR CODE HERE ***"
		max_q = 'NA'
		action_list = self.getLegalActions(nextState)

		if not action_list:
			max_q = 0.0

		for act in action_list:
			q_val = self.getQValue(nextState, act)
			if max_q == 'NA' or q_val > max_q :
				max_q = q_val

		difference  = reward + self.discount*max_q - self.getQValue(state, action)

		weights = self.getWeights()

		featureVector = self.featExtractor.getFeatures(state,action)
		for key in featureVector:
			weights[key] = weights[key] + self.alpha*difference*featureVector[key]


	def final(self, state):
		"Called at the end of each game."
		# call the super-class final method
		PacmanQAgent.final(self, state)

		# did we finish training?
		if self.episodesSoFar == self.numTraining:
			# you might want to print your weights here for debugging
			"*** YOUR CODE HERE ***"
			pass
