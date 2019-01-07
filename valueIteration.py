# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 11:37:45 2019

@author: user
"""

import numpy as np
from gridWorld import standardGrid, negativeGrid
from iterativePolicyEvaluation import printValues, printPolicy

EPSILON = 10e-4
GAMMA = 0.9
ACTIONS = ('U', 'D', 'L', 'R')
 


if __name__ == '__main__':
    
    grid = negativeGrid()
    
    policy = {}
    for s in grid.actions.keys():
        policy[s] = np.random.choice(ACTIONS)
        
    print ("Rewards:")
    printValues(grid.rewards,grid)
    
    print("Initial Policy:")
    printPolicy(policy,grid)
    
    V = {}
    states = grid.allStates()
    
    for s in states:
       if s in grid.actions:
           V[s] = np.random.random()
       else:
           V[s] = 0
            
    
    while True:
        biggestChange = 0
        for s in states:
            oldV = V[s]
            if s in policy:
                newV = float('-inf')
                for a in ACTIONS:
                    grid.setState(s)
                    r = grid.move(a)
                    v = r + GAMMA * V[grid.currentState()]
                    if v > newV:
                        newV = v
                V[s] = newV
                biggestChange = max(biggestChange,np.abs(oldV-V[s]))
        if biggestChange < EPSILON:
            break
        
        for s in policy.keys():
            bestA = None  
            bestValue = float('-inf')
            for a in ACTIONS:
                grid.setState(s)
                r = grid.move(a)
                v = r + GAMMA * V[grid.currentState()]
                if v > bestValue:
                      bestValue = v
                      newA = a
            policy[s] = newA
                
    print("Values:")
    printValues(V,grid)
    print("Policy:")
    printPolicy(policy,grid)