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
        PACMAN = 0
        GHOST = 1
        legalActs = gameState.getLegalActions(0)
        listOfNxtStates = [gameState.generateSuccessor(0, actions) for actions in legalActs]
        # MAX chooses maximum score from list of min scores.
        listOfMinScores = [self.minimax(nxtGameState, 1, GHOST, 1) for nxtGameState in listOfNxtStates]
        maxIndexList = []
        maxScore = max(listOfMinScores)
        for i in range(0,len(listOfMinScores)):
            if listOfMinScores[i] == maxScore:
                maxIndexList.append(i)
        chosenIndex = random.choice(maxIndexList)
        # index of corresponding actions.
        return legalActs[chosenIndex] 
        
        util.raiseNotDefined()
        
        "*** YOUR CODE HERE ***"
    def minimax(self, gameState, depth, currAgent, visitedAgent):
        currDepth = depth 
        numAgents = gameState.getNumAgents()
        if (currAgent > numAgents - 1):
            currAgent = 0
        # increment depth when visitedAgent equal num of current agents in the game. 
        if (visitedAgent != 0 and visitedAgent % numAgents == 0):
            currDepth += 1
        # terminate test: only when it reach the depth.
        if (gameState.isWin() or gameState.isLose()):
            return self.evaluationFunction(gameState)
        # cutoff test:
        if (currDepth > self.depth):
            return self.evaluationFunction(gameState)
        # Max
        elif currAgent == 0: # pacman chooses the max
            legalActs = gameState.getLegalActions(currAgent)
            listMaxScore = []
            successorStates = []
            for acts in legalActs:
                successorStates.append(gameState.generateSuccessor(currAgent, acts))
            for states in successorStates:
                listMaxScore.append(self.minimax(states, currDepth, (currAgent+1), (visitedAgent+1)))
            return max(listMaxScore)
        # Min
        elif currAgent != 0:
            legalActs = gameState.getLegalActions(currAgent)
            listMinScore = []
            successorStates = []
            for acts in legalActs:
                successorStates.append(gameState.generateSuccessor(currAgent, acts))
            for states in successorStates:
                listMinScore.append(self.minimax(states, currDepth, (currAgent+1), (visitedAgent+1)))
            return min(listMinScore)     
        
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """
    INFINITE = float('inf')
    NEG_INFINITE = float('-inf')
    
    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        PACMAN = 0
        GHOST = 1
        index = self.alphaBetaPrune(gameState, AlphaBetaAgent.NEG_INFINITE, AlphaBetaAgent.INFINITE, 1, PACMAN, 0)
        legalActs = gameState.getLegalActions(PACMAN)
        return legalActs[index]
        
        util.raiseNotDefined()
    
    def alphaBetaPrune(self, gameState, bestMin, bestMax, depth, currAgent, visitedAgent):
        currDepth = depth
        numAgents = gameState.getNumAgents()
        if (currAgent > numAgents - 1):
            currAgent = 0
        
        # increment depth when visitedAgent equal num of current agents in the game. 
        if (visitedAgent != 0 and visitedAgent % numAgents == 0):
            currDepth += 1
        
        # terminal-test:
        if (gameState.isWin() or gameState.isLose()):
            return self.evaluationFunction(gameState)
        # cut-off test:
        """
        # following code help to debug and understand the a-b minimax
        print "currDepth is: ", currDepth
        print "self.depth: ", self.depth
        print "visitedAgent: ", visitedAgent
        print "numAgents: ", numAgents
        print "currAgent: ", currAgent
        """
        if (currDepth > self.depth):
            return self.evaluationFunction(gameState)
        # Max
        elif currAgent == 0: # pacman chooses the max
            successorStates = []
            listOfVals = []
            value = AlphaBetaAgent.NEG_INFINITE
            legalActs = gameState.getLegalActions(currAgent)
            for acts in legalActs:
                state = gameState.generateSuccessor(currAgent, acts)
                listOfVals.append(self.alphaBetaPrune(state, bestMin, bestMax, currDepth, (currAgent+1), (visitedAgent+1)))
                listOfVals.append(value)
                value = max(listOfVals)
                
                if value > bestMax:
                    return value
                bestMin = max(bestMin, value)
                # final step for MAX to choose the max element
                if (len(listOfVals) > 2*len(gameState.getLegalActions(self.index)) - 1) and visitedAgent == 0:
                    for i in range(0, len(listOfVals)/2):
                        if bestMin == listOfVals[i*2]:
                            return i
            return value

        # Min
        elif currAgent != 0: 
            successorStates = []
            listOfVals = []
            value = AlphaBetaAgent.INFINITE
            legalActs = gameState.getLegalActions(currAgent)
            for acts in legalActs:
                state = gameState.generateSuccessor(currAgent, acts)
                listOfVals.append(self.alphaBetaPrune(state, bestMin, bestMax, currDepth, (currAgent+1), (visitedAgent+1)))
                listOfVals.append(value)
                value = min(listOfVals)
                #print "bestMin", bestMin
                if value < bestMin:
                    return value
                bestMax = min(bestMax, value)
            return value
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
        PACMAN = 0
        GHOST = 1
        legalActs = gameState.getLegalActions(0)
        listOfNxtStates = [gameState.generateSuccessor(0, actions) for actions in legalActs]
        # MAX chooses maximum score from list of min scores.
        listOfMinScores = [self.expectimax(nxtGameState, 1, GHOST, 1) for nxtGameState in listOfNxtStates]
        maxIndexList = []
        maxScore = max(listOfMinScores)
        for i in range(0,len(listOfMinScores)):
            if listOfMinScores[i] == maxScore:
                maxIndexList.append(i)
        chosenIndex = random.choice(maxIndexList)
        # index of corresponding actions.
        return legalActs[chosenIndex] 
        
        util.raiseNotDefined()
        
        "*** YOUR CODE HERE ***"
    def expectimax(self, gameState, depth, currAgent, visitedAgent):
        currDepth = depth 
        numAgents = gameState.getNumAgents()
        if (currAgent > numAgents - 1):
            currAgent = 0
        # increment depth when visitedAgent equal num of current agents in the game. 
        if (visitedAgent != 0 and visitedAgent % numAgents == 0):
            currDepth += 1
        # terminate test: only when it reach the depth.
        if (gameState.isWin() or gameState.isLose()):
            return self.evaluationFunction(gameState)
        # cutoff test:
        if (currDepth > self.depth):
            return self.evaluationFunction(gameState)
        # Max
        elif currAgent == 0: # pacman chooses the max
            legalActs = gameState.getLegalActions(currAgent)
            listMaxScore = []
            successorStates = []
            for acts in legalActs:
                successorStates.append(gameState.generateSuccessor(currAgent, acts))
            for states in successorStates:
                listMaxScore.append(self.expectimax(states, currDepth, (currAgent+1), (visitedAgent+1)))
            return max(listMaxScore)
        # expectival
        elif currAgent != 0:
            legalActs = gameState.getLegalActions(currAgent)
            listMinScore = []
            successorStates = []
            for acts in legalActs:
                successorStates.append(gameState.generateSuccessor(currAgent, acts))
            for states in successorStates:
                listMinScore.append(self.expectimax(states, currDepth, (currAgent+1), (visitedAgent+1)))
            return float(sum(listMinScore))/len(listMinScore)
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
	"""
	
	
    # Useful information you can extract from a GameState (pacman.py)
    #print "hasWalls", help(currentGameState.hasWall), exit()
    #print "getWalls", currentGameState.getWalls()
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    newCapsules = currentGameState.getCapsules()
    #print "scaredTimes: ", newScaredTimes[0] 

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
    # objects positons
    foodList = newFood.asList()
    g1X, g1Y = gost1Pos             # ghost1 pos
    px, py = newPos                 # pacman pos
    fx, fy = 0, 0                   # closest food pos
 
    #cap1x, cap1y = newCapsules[0]   # capsules 1 pos
    #cap2x, cap2y = newCapsules[1]   # capsules 2 pos
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
    """
    if (newScaredTimes[0] == 0 or
        newScaredTimes[0] == 39):
    """  
      #print "in eat food"
    if (((g1X - px)**2 + (g1Y - py)**2)**0.5) <= 1:
        score -= 8
    # avoid ghost 
    # reasone use elif, fish and bear hand cannot get together.
    # weigh for return value
    elif minDis >= 5:
        score += 2
    elif minDis == 4:
        score += 4
    elif minDis == 3:
        score += 6
    elif minDis == 2:
        score += 8
    elif minDis == 1:
        score += 10

    # if capsules close to you and gost, close to you also.
    # in this world, i will not to be worry about eating the capsules
    # (since the capsules are in btw foods)
    # when scaredTime != 0, hunt the ghost! (if the ghost is close to the base, dont hunt it)
    #print "newScaredTimes[0]", newScaredTimes[0], " < 37", newScaredTimes[0] < 37
    """
    if (newScaredTimes[0] < 37 and newScaredTimes[0] != 0):
        #print "inside hunt ghost"
        disToGhostX = abs(px - g1X)
        disToGhostY = abs(py - g1Y)
        # attract pacman to get closer to ghost in y-direction
        if (disToGhostY == 5):
            score += 1
        elif (disToGhostY == 4):  
            score += 3
        elif (disToGhostY == 3):  
            score += 5
        elif (disToGhostY == 2):  
            score += 7
        elif (disToGhostY == 1):  
            score += 9
        elif (disToGhostY == 0):  
            score += 14
        
        #  
        if (disToGhostY >= 8):
            score += 1
        elif (disToGhostY == 7):
            score += 3
        elif (disToGhostY == 6):
            score += 5
        elif (disToGhostX == 5):
            score += 7
        elif (disToGhostX == 4):
            score += 9
        elif (disToGhostX == 3):
            score += 13
        elif (disToGhostX == 2):
            score += 15
        elif (disToGhostX == 1):
            score += 17
        elif (disToGhostX == 0):
            score += 20
    """ 

    # to solve wall between
    # wall in y direction
    
    if fx == px and fy > py:
        if currentGameState.hasWall(px, py+1):
            score -=2
    if fx == px and fy < py:
        if currentGameState.hasWall(px, py-1):
            score -=2
    # wall in x direction
    if fy == py and fx > px:
        if currentGameState.hasWall(px+1, py):
            score -=2
    if fy == py and fx < px:
        if currentGameState.hasWall(px-1, py):
            score -=2

    "*** YOUR CODE HERE ***"
    # subtract numFood*5
    # ensure pacman take the route to eat the food
    # if food was eaten, score will be subtracted smaller
    # so this move will be chose, since we choose the highest score 
    return score - numFood*5
    #return successorGameState.getScore()
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

