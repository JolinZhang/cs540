# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()
        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        # bestIndices - list stores all the index of best move with best scores. ex. [0, 1, 2]
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best
        "Add more of your code here if you want to"
        print "legalMoves: ", legalMoves
        return legalMoves[chosenIndex]


    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        #print "hasWalls", help(currentGameState.hasWall), exit()
        #print "getWalls", currentGameState.getWalls()
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        """
        
        print "successorGameState= ", successorGameState
        print "newPos= ", newPos
        print "newFood= ", dir(newFood)
        print "newGhostStates= ", dir(newGhostStates[0])
        print "newScaredTimes= ", newScaredTimes    
        """
        # initializaiton
        numFood = newFood.count()
        score = 100
        twoGhosts = False
        numGhosts = len(newGhostStates)
        if numGhosts == 2:
            twoGhosts = True
        gost1Pos = newGhostStates[0].getPosition()
        """
        if twoGhosts:
            gost2Pos = newGhostStates[1].getPosition()
            g2X, g2Y = gost2Pos
        """
        foodList = newFood.asList()
        # ghosts positon
        g1X, g1Y = gost1Pos
        
        px, py = newPos
        fx, fy = 0, 0
        minDis = 100
       
        # find closest food: (dis, and cords.) 
        for food in foodList:
            fX, fY = food
            dis = abs(fX - px) + abs(fY - py)
            if dis < minDis:
                minDis = dis
                fx = fX
                fy = fY
        # avoid ghost
        # code for avoiding second ghost. 
        """
        if twoGhosts:
            if (((g2X - px)**2 + (g2Y - py)**2)**0.5) <= 1:
                score -= 5        
        """
         
        if (((g1X - px)**2 + (g1Y - py)**2)**0.5) <= 1:
            score -= 5
        # avoid ghost 
        # reasone use elif, fish and bear hand cannot get together.
        # weigh for return value
        elif minDis >= 5:
            score += 1
        elif minDis == 4:
            score += 2
        elif minDis == 3:
            score += 3
        elif minDis == 2:
            score += 4
        elif minDis == 1:
            score += 5

        # to solve wall between
        # wall in y direction
        if fx == px and fy > py:
            if currentGameState.hasWall(px, py+1):
                score -=4
        if fx == px and fy < py:
            if currentGameState.hasWall(px, py-1):
                score -=4
        # wall in x direction
        if fy == py and fx > px:
            if currentGameState.hasWall(px+1, py):
                score -=4
        if fy == py and fx < px:
            if currentGameState.hasWall(px-1, py):
                score -=4

        "*** YOUR CODE HERE ***"
        # subtract numFood*5
        # ensure pacman take the route to eat the food
        # if food was eaten, score will be subtracted smaller
        # so this move will be chose, since we choose the highest score 
        return score - numFood*5
        #return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        # print "self.depth:", self.depth, "self.evaluationFunction", self.evaluationFunction(gameState)
        # gameState.getNumAgents() # get tree depth
        # gameState.generateSuccessor(agentIndex, action)
        # legalActions = gameState.getLegalActions(0)
        # print "legalActions are: ", gameState.getLegalActions(0) 
        # print "Successors are: ", dir(gameState.generateSuccessor(0, 'East'))
        # print "gameState format:", dir(gameState)
        # print " ", help(gameState.getLegalActions)
        # gameState.generateSuccessor(0, 'East') is the state for points
        depth = self.depth
        PACMAN = 0
        print "the maximum is: ", self.minimax(gameState, 1, PACMAN)
        
        print "exit", exit()
        return ['West']
        util.raiseNotDefined()
        
        "*** YOUR CODE HERE ***"
    def minimax(self, gameState, depth, currAgent):
        currDepth = depth
        numAgents = gameState.getNumAgents()
        print "Scores: ", self.evaluationFunction(gameState),"@level:", currDepth
        print "numofAgents: ", numAgents
        if (currAgent > numAgents - 1):
            currAgent = 0
            currDepth += 1
        # terminate test: only when it reach the depth. !!! might need to concern ghost
        if (gameState.isWin() or gameState.isLose()):
            return self.evaluationFunction(gameState)
        # cutoff test:
        if (currDepth > self.depth):
            return self.evaluationFunction(gameState)
        # Max
        elif currAgent == 0: # pacman chooses the max
            print "current Agent is: ", currAgent
            legalActs = gameState.getLegalActions(currAgent)
            print "legalActs: ", legalActs
            listMaxScore = []
            successorStates = []
            for acts in legalActs:
                successorStates.append(gameState.generateSuccessor(currAgent, acts))
            print "sucessorStates are: ", successorStates
            for states in successorStates:
                listMaxScore.append(self.minimax(states, currDepth, (currAgent+1)))
            print "pacman listMaxScore are: ", listMaxScore
            print "return from agent", currAgent
            return max(listMaxScore)
        # Min
        elif currAgent != 0:
            print "*****************************"
            print "current Agent is: ", currAgent
            legalActs = gameState.getLegalActions(currAgent)
            listMinScore = []
            successorStates = []
            for acts in legalActs:
                successorStates.append(gameState.generateSuccessor(currAgent, acts))
            for states in successorStates:
                listMinScore.append(self.minimax(states, currDepth, (currAgent+1)))
            print "ghosts listMaxScore are: ", listMinScore
            print "return from agent", currAgent
            return min(listMinScore)     
        
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

