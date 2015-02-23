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

 
index = self.alphaBetaPrune(gameState, AlphaBetaAgent.NEG_INFINITE, AlphaBetaAgent.INFINITE, 0, PACMAN, 0)  

`
changed to: depth =1, visitedAgent = 0 will fixed  

`
index = self.alphaBetaPrune(gameState, AlphaBetaAgent.NEG_INFINITE, AlphaBetaAgent.INFINITE, 1, PACMAN, 0)  

`

## q4:  
 
