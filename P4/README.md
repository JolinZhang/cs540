## Question 1 (3 points): Exact Inference Observation:

### Experiments:  
- `noisyDistance` returns the noisy distance readings from the sensor.  
- `emissionModel` returns the P(noisyDistance | TrueDistance)  
	**example outputs: **   

```   
	{1: 0.16492146596858642, 2: 0.16753926701570682, 3: 0.33507853403141363, 4: 0.16753926701570682, 5: 0.08376963350785341, 6: 0.041884816753926704, 7: 0.020942408376963352, 8: 0.010471204188481676, 9: 0.005235602094240838, 10: 0.002617801047120419} 
```   
- `self.beliefs` returns the probability of the ghost in the specific cell. 

*** example outputs: ***

```
{(5, 4): 0.125, (3, 4): 0.125, (1, 4): 0.125, (7, 4): 0.125, (9, 4): 0.125, (5, 2): 0.125, (2, 4): 0.125, (8, 4): 0.125}
```	

### Procedure:
1. change `allPossible[p] = 0` to `allPossible[p] = emissionModel[trueDistance] * self.beliefs[p]` this updates the beliefs(of the location of the ghosts) with the noisy sensor values.
2. put ghost into jail cell with help of `self.getJailPosition()` and `noisyDistance == None`  
   Code:
    
   ```
   if(noisyDistance == None):
        p = self.getJailPosition()
        allPossible[p] = 1.0
   ```
### Output from console:
Question q1: 3/3 


## Question 2 (4 points): Exact Inference with Time Elapse

### Experiments: 
- `newPosDist[p]` returns the newPostDist[p] = Pr( ghost is at position p at time t + 1 | ghost is at position oldPos at time t )
- we are looking for the `Prob(newPos)`
- with the help of `self.beliefs[p]` (givens the probeblity of the oldPos `Prob(oldPos)`), we can easily find `Prob(newPos)`
- `Prob(newPos) = Pr( ghost is at position p at time t + 1 | ghost is at position oldPos at time t )` * `prob(oldPos)`
### Bug!

```
for newPos, prob in newPosDist.items():
       allPossible[newPos] = prob * self.beliefs[p]
```
- previously, i used `allPossible[newPos] = prob * self.beliefs[p]` inside the forloop of update, and that was actually wrong!
- since it is updating the probability various times, therefore it should adds up all the previouse values of the probability. 
- fix: `allPossible[newPos] += prob * self.beliefs[p]`. Thanks Alfeld to help finding the bug!


## Question 3 (3 points): Exact Inference Full Test

- get ghosts' current positions from beliefs (pick the largest probability)
- find the shortest ghost index
- get all legal action for pacman in `legal`
- get all the newPos.
- get distance from pacman to all newPos after select a legal move
- select the shortest distance, and return the corresponding action. 


## Question 4 (3 points): Approximate Inference Observation


1. `initializeUniformly` - here you first create a variable that will store a list of particles and then initialize that list. create a variable that will store a list of particles.
 
2. `getBeliefDistribution` - convert a list of particles into a belief distribution and return that distribution as a Counter object. This means that you should never keep track of the belief distribution itself (simplly return `newBeliefs`), but rather keep track of the particles (only keep update on `self.particleList`) and create a distribution only when specifically asked for it.
 
3. `observe` - update the `self.particleList` (the list of the particles) by the given evidences of the probability from the sensor. 



 

  
