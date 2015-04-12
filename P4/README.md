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

  
