# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState) # future reward
              mdp.isTerminal(state)
        """
        
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        # possible actions: 'exit', 'north', 'west', 'south', 'east' 
        # getT function [((0, 1), 1.0), ((0, 0), 0.0), ((0, 2), 0.0)]
        states = mdp.getStates()
        
        # Write value iteration code here
        "*** YOUR CODE HERE ***"

        # print mdp.getStates(), exit()
        # value iteration
        
        for i in range(self.iterations):
            # print "total number of iterations: ", self.iterations
            # U1 is {(0, 1): 0, (0, 0): 0, 'TERMINAL_STATE': 0, (0, 2): 0}
            # U1 = dict([(s, 0) for s in mdp.getStates()])
            U1 = self.values.copy()
            R, T, gamma = mdp.getReward, mdp.getTransitionStatesAndProbs, self.discount
            U = U1.copy()
            delta = 0
            for s in mdp.getStates():
                # when in TERMAINAL_STATE, there will be no action, 
                # in that case, the max() function will receive empty list.
                if len(mdp.getPossibleActions(s)) != 0:
                    U1[s] = R(s, None, None) + gamma * max([sum([p * U[s1] for (s1, p) in T(s, a)]) for a in mdp.getPossibleActions(s)])
                else: 
                    U1[s] = R(s, None, None)
            self.values = U1


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        discount = self.discount
        # self.mdp.getTransitionStatesAndProbs() return list of nxtState with its transitionModelProb.
        transitionModel = self.mdp.getTransitionStatesAndProbs(state, action)
        sum = 0
        for t_state_pair in transitionModel:
            nxtState = t_state_pair[0]
            tranModelProb = t_state_pair[1]
            # self.value[state] returns the utility of that state
            sum += tranModelProb * self.getValue(nxtState)
        qValue = self.mdp.getReward(state, None, None) + sum * discount
        return qValue
        
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.
            
          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        if self.mdp.isTerminal(state):
            return None
        # call computeQValueFromValues() to compute qValues, return the action with highest qValue
        actionList = self.mdp.getPossibleActions(state)
        qValList = []
        index = 0
        for action in actionList:
            qValList.append(self.computeQValueFromValues(state, action))
            #print "qValue: ",self.computeQValueFromValues(state, action), "action: ", action
            #print "qValListit: ", qValList
        maxQ = max(qValList)
        #print "maxQ is: ", maxQ
        for i in range(len(qValList)):
            if (maxQ == qValList[i]):
                index = i
        #print "actionChoose: ", actionList[index] 
        return actionList[index] 
        

        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
