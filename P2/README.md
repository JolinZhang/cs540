2/15: upload P2 files  

## q1:  
passed with 4/4
Average Score: 1073.2  
Scores:        1246.0, 912.0, 866.0, 1209.0, 1193.0, 1246.0, 702.0, 1058.0, 1227.0, 1073.0  
Win Rate:      10/10 (1.00)  
Record:        Win, Win, Win, Win, Win, Win, Win, Win, Win, Win  

reflex agent still need to fix for two ghosts.  


## q2:  
Passed with 5/5  

Question:  
1. minimax choose the best of the worst cases,  
and cannot garuntee that pacman will win the  
game, why we still want to learn about it??  
what is the advantage of using this kind of  
algorithom?>>


## q3:  

very painful debuging process!!! But we made it!!!  

previous Bugs:

1. Mistaken select the wrong start up `depth` and `visitedAgents`  
from `getAction()`. cause cutoff method malfunctioed.  

*** FAIL: test_cases/q3/2-1a-vary-depth.test  
***     Incorrect generated nodes for depth=1  
***         Student generated nodes: a b1 b2 c1 c2 cx d1 d2 d3 dx  
***         Correct generated nodes: a b1 b2 c1 c2 cx  
***     Tree:  
***                 /-----a------\  
***                /              \  
***               /                \  
***             b1                  b2  
***           /    \                 |  
***     -4 c1        c2 9           cx -4.01  
***       /  \      /  \             |  
***      d1   d2  d3   d4           dx  
***     -3    -9  10    6         -4.01  
***       
***     a - max  
***     b - min  
***     c - max  
***       
***     Note that the minimax value of b1 is -3, but the depth=1 limited value is -4.  
***     The values next to c1, c2, and cx are the values of the evaluation function, not  
***     necessarily the correct minimax backup.  

```
index = self.alphaBetaPrune(gameState, AlphaBetaAgent.NEG_INFINITE, AlphaBetaAgent.INFINITE, 0, PACMAN, 0)  

```
changed to: depth =1, visitedAgent = 0 will fixed  

```
index = self.alphaBetaPrune(gameState, AlphaBetaAgent.NEG_INFINITE, AlphaBetaAgent.INFINITE, 1, PACMAN, 0)  

```

## q4:  
### Question q4: 5/5 ###  

We just changed the MIN of the minimax to AVG, everything else should leave  
the same as minimax  

## q5:  
a follow up update on question 1 to enhance the evaluation function when reach the limiting depth.  
in q1, we set the food as the goal, but we also need to care about the ghost @ the same time.  
we also add in the condition of regarding walls.

we might also need to added the factor to eat podwer and hunting the ghost.

```
Pacman emerges victorious! Score: 363
Pacman emerges victorious! Score: 573
Pacman emerges victorious! Score: 386
Pacman emerges victorious! Score: 911
Pacman emerges victorious! Score: 933
Pacman emerges victorious! Score: 696
Pacman emerges victorious! Score: 607
Pacman emerges victorious! Score: 974
Pacman emerges victorious! Score: 964
Pacman emerges victorious! Score: 1068
Average Score: 747.5
Scores:        363.0, 573.0, 386.0, 911.0, 933.0, 696.0, 607.0, 974.0, 964.0, 1068.0
Win Rate:      10/10 (1.00)
Record:        Win, Win, Win, Win, Win, Win, Win, Win, Win, Win
*** FAIL: test_cases/q5/grade-agent.test (5 of 6 points)
***     747.5 average score (1 of 2 points)
***         Grading scheme:
***          < 500:  0 points
***         >= 500:  1 points
***         >= 1000:  2 points
***     10 games not timed out (1 of 1 points)
***         Grading scheme:
***          < 0:  fail
***         >= 0:  0 points
***         >= 10:  1 points
***     10 wins (3 of 3 points)
***         Grading scheme:
***          < 1:  fail
***         >= 1:  1 points
***         >= 5:  2 points
***         >= 10:  3 points

### Question q5: 5/6 ###

```

