# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 14:51:45 2019

@author: Aidin
"""

import numpy as np
# import matplotlib.pyplot as plt
from gridWorld import standardGrid

EPSILON = 10e-4

def printValues(V,grid):
    for i in range(grid.width):
        print ("-------------------------------")
        for j in range(grid.height):
            v = V.get((i,j),0)
            if v>= 0:
                print(" %0.2f|" % v)
            else:
                print("%0.2f|" % v)
        print("")

def printPolicy(P,grid):
    for i in range(grid.width):
        print ("-------------------------------")
        for j in range(grid.height):
            a = P.get((i,j), ' ')
            print(" %s |" % a)
        print("")
        
        
if __name__ == '__main__':
        
    grid = standardGrid()
    states = grid.allStates()
    
    V = {}
    
    for s in states:
        V[s] = 0
    gamma = 1.0
    while True:
        biggestChange = 0
        for s in states:
            oldV = V[s]
            if s in grid.actions:
                
                newV = 0
                pAction = 1.0/len(grid.actions[s])
                for a in grid.actions[s]:
                    grid.setState(s)
                    r = grid.move(a)
                    newV +=pAction * (r + gamma * V[grid.currentState()])
                V[s] = newV
                biggestChange = max(biggestChange,np.abs(oldV-V[s]))
        if biggestChange < EPSILON:
            break
    print ("values for uniformly random actions:")
    printValues(V,grid)
    print("\n\n")
    
    ### fixed policy ###
    policy = {
            (2,0): "Up",
            (1,0): "Up",
            (0,0): "Right",
            (0,1): "Right",
            (0,2): "Right",
            (1,2): "Right",
            (2,1): "Right",
            (2,2): "Right",
            (2,3): "Up",
            }
    
    printPolicy(policy,grid)
    
    V = {}
    
    for s in states:
        V[s] = 0
    
    gamma = 0.9
    
    while True:
        for s in states:
            oldV = V[s]
            if s in policy:
                a = policy[s]
                grid.setState(s)
                r = grid.move(a)
                V[s] +=pAction * (r + gamma * V[grid.currentState()])
                biggestChange = max(biggestChange,np.abs(oldV-V[s]))
        if biggestChange < EPSILON:
            break
    print ("values for fixed actions:")
    printValues(V,grid)
    print("\n\n")