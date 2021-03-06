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
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        
        "*** YOUR CODE HERE ***"
        self.qVals = util.Counter()
    # 4
    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"
        return self.qVals[state, action]
        util.raiseNotDefined()

    # 4
    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"
        if not self.getLegalActions(state):
            return 0.0
        # call computeQValueFromValues() to compute qValues, return the action with highest qValue
        actionList = self.getLegalActions(state)
        qValList = []
        index = 0
        for action in actionList:
            qValList.append(self.getQValue(state, action))
        maxQ = max(qValList)
        return maxQ
        util.raiseNotDefined()
    # 4
    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"
        if not self.getLegalActions(state):
            return None
        # call computeQValueFromValues() to compute qValues, return the action with highest qValue
        actionList = self.getLegalActions(state)
        qValList = []
        index = 0
        for action in actionList:
            qValList.append(self.getQValue(state, action))
        maxQ = max(qValList)
        for i in range(len(qValList)):
            if (maxQ == qValList[i]):
                index = i
        return actionList[index] 
        util.raiseNotDefined()

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
        if util.flipCoin(self.epsilon):
            return random.choice(legalActions)
        else:
            return self.computeActionFromQValues(state)

        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    # q4
    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"
        # - self.epsilon (exploration prob)
        # - self.alpha (learning rate)
        # - self.discount (discount rate)        
        # self.getLegalActions(state)
        # self.getQValue
        
        Q1 = self.qVals.copy()
        alpha = self.alpha
        discount = self.discount
        Q = Q1.copy()
        
        listQvals = []
        for a in self.getLegalActions(nextState):
            listQvals.append(self.getQValue(nextState, a))
        if (nextState == 'TERMINAL_STATE' or not listQvals):
            maxQ = 0
        else: 
            maxQ = max(listQvals)
        Q1[state, action] = Q[state, action] + alpha * (reward + discount * maxQ - Q[state, action])
        self.qVals = Q1
        return self.qVals

        util.raiseNotDefined()

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
        weight = self.getWeights()
        feature = self.featExtractor.getFeatures(state, action)
        qValue = 0
        #print "weight: ", weight
        #print "feature: ", feature
        for f in feature:
            qValue += feature[f] * weight[f]
        return qValue
        
        util.raiseNotDefined()

    def update(self, state, action, nextState, reward):
        """
           Should update your weights based on transition
        """
        "*** YOUR CODE HERE ***"
        

        w1 = self.weights.copy()
        alpha = self.alpha
        discount = self.discount
        feature = self.featExtractor.getFeatures(state, action)
        w = w1.copy()

        listQvals = []
        for a in self.getLegalActions(nextState):
            listQvals.append(self.getQValue(nextState, a))
        if (nextState == 'TERMINAL_STATE' or not listQvals):
            maxQ = 0
        else:
            maxQ = max(listQvals)
        
        # update for EACH wi.
        
        for f in feature:
            w1[f] = w[f] + alpha * (reward + discount * maxQ - self.getQValue(state, action)) * feature[f] 
        self.weights = w1
        print "w1", w1
        return self.weights
        
        util.raiseNotDefined()

    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            pass
