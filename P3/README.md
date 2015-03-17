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

change `answerNoise = 0.2` to ` answerNoise = 0`  
has noise 0 means the agent will take the exact action you intend it to perform.  

### Q3: Policies

Code to test with GUI:  
`python gridworld.py -a value -i 100 -g DiscountGrid --discount 0.9 --noise 0.2 -r -2.5`

q3b - Prefer the close exit (+1), but avoiding the cliff (-10)

when I just put 'NOT POSSIBLE' without thinking, the autograder told me:   
`*** FAIL: test_cases/q3/2-question-3.2.test
***     Actually, it is possible!` LOL!!

##### Solution 3b_1:  

noise 0.2 make it possible for agents to go up. make the living award to be -0.8 force the agent to exit sooner than shooting for reward of 10.


`python gridworld.py -a value -i 100 -g DiscountGrid --discount 0.5 --noise 0.2 -r -0.8`

##### Solution 3b_2: 
path to 1.0 is closer than path to 10.0, set discount to 0.25
make the longer path to 10 less attractive. (since the longer the path is, the less we care about future reward.)  
`python gridworld.py -a value -i 100 -g DiscountGrid --discount 0.25 --noise 0.2 -r -0.08`

### Q4: Q-Learning
### Q5: Epsilon Greedy
### Q6: Bridge Crossing Revisited
### Q7: Q-Learning and Pacman
### Q8: Approximate Q-Learning



