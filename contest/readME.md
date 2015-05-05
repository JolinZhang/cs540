# Contest: Pacman Capture the Flag
link: <https://sites.google.com/site/cs540s15/assignments/ctfcompetition>


## April 25th:
1. imported CTF project file
2. set up README file
3. Read through instructions and rules

## Problem to solve
1. NA

## Requirements:

	1. each agent allows one second to return an action.
	2. There will be an initial start-up allowance of 15 seconds (use the `registerInitialState` function)
	3. observe an opponent's (position and direction) if they or their teammate is within 5 squares (Manhattan distance) - noise distance
	4. ways to end game:
		1）. eat all dots (all but two work as well)
		2）. limited 300 moves per each of the four agents
		
		
		
## Offense
1. if pacman realizes there is ghost in 5 steps to hunt him, try himself to run away from ghost. make the `distanceToFood` zero weight so that pacman will not try to eat the foods inside a deep deadend, instead he should just tries his best to run away from ghosts without the interference of foods.

2. if pacman relaizes ghost around (within 5 steps), do not try to get in to any deadend. (sucessor's state has only two actions will be the situation when in a deadend)

3. we found that when pacman's current state has four actions(WEST,STOP, NORTH, SOUTH). we said that if the number of actions of the current state's successor's successor is a dead end(namely only STOP and action back out). we said that we do not want this to happen, since we do not want to get caught by ghost inside a deadend. we set the weight to that corespoding action with negative weight so pacman will not put himself into a deadend.

4. add new feature `stayAwayFromGhost`, if we simply looking for action depends on closest food, and you do not caught by ghost as well. Give more weights to the action that returns a longer distance from ghost to pacman

5. add new function to let pacman eat specfic number of points and return base to deposite.

		if (self.foodEaten == round(self.initialFoodNum / 5)):
			# go back to base

6. if ghost around, but scared, act as there is no ghosts around. 
 
7. add feature to allow my offense agent (in ghost state) sees a oppoent pacman near by, take it down if within one distance away.

		if not successor.getAgentState(self.index).isPacman and len(invaders) != 0:
        	myPos = successor.getAgentState(self.index).getPosition()
        	disToPac = min([self.getMazeDistance(myPos, pac) for pac in invaderPos])
        	if disToPac <= 1:
            	# print "catch ghost!"
            	features['distanceToInv'] = disToPac

8. when both ghosts (my offense agent and oppoent's defense agent) are close around the boarder, my ghost (become paceman) takes an action that get father from the oppoent's ghost.


## Defense
