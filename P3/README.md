## CS540 Project3 due Mar.20th


### Q1: Value Iteration(6 points)

####3/9
Finished:  
1.`computeActionFromValues(state)`
2.`computeQValueFromValues(state, action)`

What need to do:  
1. figure out how to cope with the iteration value into the value iteration.

####3/14  
max() empty list bug: the list pass into the max() function is empty when the current state is TERMINAL_STATE. 

fixs:
if the action list is empty, (when it is in terminal state),
simply returns the reward of that state.

####3/16

fixs:   
1. update `self.values` with `self.values = U1` at the end of each iteration. `self.values` is the actual container that stores all the (state: utility) pairs.  
2. within the iteration for-loop, initilize `U1` with 0 utility every iteration is wrong.  
3. commented out `U1 = dict([(s, 0) for s in mdp.getStates()])`, added in `U1 = self.values.copy()` instead.  
 




### Q2: Bridge Crossing Analysis
### Q3: Policies
### Q4: Q-Learning
### Q5: Epsilon Greedy
### Q6: Bridge Crossing Revisited
### Q7: Q-Learning and Pacman
### Q8: Approximate Q-Learning



