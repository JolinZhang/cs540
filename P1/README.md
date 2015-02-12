

2/5  
1. fixed DFS  
2. implemented BFS, change stack into FIFO for BFS  
3. fixed bug: added initial state into the explored list.  


Provisional grades
==================
Question q1: 3/3
Question q2: 3/3
Question q3: 0/3
Question q4: 0/3
Question q5: 0/3
Question q6: 0/3
Question q7: 0/4
Question q8: 0/3
------------------
Total: 6/25



2/6  
#3 UCS:  

a). data structure: priority queue  
b). priority queue pop out the lowest priority element  
c). need to set up a new variable pathCost = 0  
d). pop the lowest pathCost everytime.  


Problem: 
1. the UCS algo does not calculate the realCost of the Path:
solved: 
since I add the sucessor's path after i poped before.
However, the UCS priority queue uses the pathCost to pop the node
with the least pathCost. Therefore, I need to add the path lead to child
to the path list before pop.


#4 A-star:  

a) pathcost = pathCost of currNode
b) herustic-> state of successor -> get the manhaton distance to the goal 
c) a-star = pathcost + herustic




#Q7  

## first try:  use minimum Manhaton distance:  
expanded nodes: 13898  

## second try:  use the minimum urtinen distance:    
Path found with total cost of 60 in 15.2 seconds  
Search nodes expanded: 14191  
Pacman emerges victorious! Score: 570  

## third try: manhaton dis with max
Path found with total cost of 60 in 7.6 seconds  
Search nodes expanded: 9551  

## fourth try: euthrina dis with max  
Path found with total cost of 60 in 8.4 seconds  
Search nodes expanded: 10352  

## fifth try: manhanton dis with avg  
Path found with total cost of 60 in 10.9 seconds  
Search nodes expanded: 11632  

## sixth try: manhaton Mindis with weight of density of food.
Path found with total cost of 60 in 12.5 seconds
Search nodes expanded: 12008

## afasdf   manhanton max with foodden
     foodDen = listFoodAround.count(True)
        if foodDen != 0:
            dis = dis - foodDen 
## max manhaton distance with weight to make the large heustic even larger  
## so that pacman will not choose that path (means eat the close one first).

Provisional grades
==================
Question q1: 3/3
Question q2: 3/3
Question q3: 3/3
Question q4: 3/3
Question q5: 3/3
Question q6: 3/3
Question q7: 4/4
Question q8: 3/3
------------------
Total: 25/25

## minimum spanning tree  


