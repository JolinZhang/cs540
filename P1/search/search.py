# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    return  [w,w,w,w,s,s,e,s,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    
    
    "*** YOUR CODE HERE ***"
    import util # to access the stack data structure
    from game import Directions
    South = Directions.SOUTH
    West = Directions.WEST
    North = Directions.NORTH
    East = Directions.EAST

    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    initialState = problem.getStartState()
    if problem.isGoalState(initialState):
        return []

    listOfSucessor = problem.getSuccessors(initialState)
    # push frontier(nodes) into Stack, set up explored list
    frontier = []
    dfs_stack = util.Stack()
    for node_temp in listOfSucessor:
        frontier.append(node_temp[0]) 
        # [node_temp[1] is the list of actions to goal] 
        node = [node_temp, []]
        dfs_stack.push(node)
    explored = []
    
    while True:
        
        currNode = dfs_stack.pop()
        print "node poped out is: ", currNode
        currNode[1].append(currNode[0][1]) # append new path to action list
        # check for goal state
        if problem.isGoalState(currNode[0][0]):
            print "find goal!: ",currNode[1]
            return currNode[1] # currNode[1] = list of actions to goal 
        # add to explored
        explored.append(currNode[0][0])
        print "&&& state of current node is: ", currNode[0][0]
        for successors in problem.getSuccessors(currNode[0][0]):
            print "current success state: ", successors[0]
            print "explored + frontier = ", explored+frontier
            if successors[0] not in explored+frontier:
                frontier.append(successors[0])
                print "new successor pushed: ", [successors, currNode[1]]
                list_goal = list(currNode[1])
                node = [successors, list_goal] 
                dfs_stack.push(node)
        # important! 
        # list_goal = currNode[1] does not copy the list, 
        # it just pass the address of old list to new list
        # use new_list = list(old_list) to copy list

        if dfs_stack.isEmpty():
            break
    return None 

    #print "the current node is: ", node 
    #print "the state of current node is: ", node[0]
    #print "action for current node is: ", node[1]
   # return [West,West,West,West,South,South,East,South,South,West]



    "***ERROR CHECK***"
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
