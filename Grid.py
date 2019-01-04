# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 14:32:15 2019

@author: Aidin
"""

class Grid:
    def __init__(self, width, height, start):
        self.width = width
        self.height = height
        self.y = start[0]
        self.x = start[1]
        
    def set(self,rewards, actions):
        self.rewards = rewards
        self.actions = actions
    
    def setState(self,s):
        self.y = s[0]
        self.x = s[1]
    
    def currentState(self):
        return(self.x,self.y)
        
    def checkTerminal(self,s):
        return s not in self.actions
    
    def move(self,action):
        
        if action in self.actions[(self.x,self.y)]:
            if action == 'Up':
                self.y -=1
            elif action == 'Down':
                self.y +=1
            elif action == 'Right':
                self.x +=1
            elif action == 'Left':
                self.x -=1
        return self.rewards.get((self.x,self.y),0)
    
    def reverseMove(self,action):
        
        if action in self.actions[(self.x,self.y)]:
            if action == 'Up':
                self.y +=1
            elif action == 'Down':
                self.y -=1
            elif action == 'Right':
                self.x -=1
            elif action == 'Left':
                self.x +=1
        assert (self.currentState() in self.allStates())
        
    def gameOver(self):
        return (self.x,self.y) not in self.actions
    
    def allStates(self):
        return set(self.actions.keys()+self.rewards.keys())
    
def standardGrid():
    grid = Grid(3,4,(2,0))
    rewards = {(0,3):1,(1,3):-1}
    actions = {
           (0,0) : ('Down','Right'),
           (0,1) : ('Left','Right'),
           (0,2) : ('Left','Down','Right'),
           (1,0) : ('Up','Down'),
           (1,2) : ('Up', 'Down','Right'),
           (2,0) : ('Up','Right'),
           (2,1) : ('Left','Right'),
           (2,2) : ('Left','Right','Up'),
           (2,3) : ('Left','Up'),
     }
    grid.set(rewards,actions)
    return grid

def negativeGrid(stepCost = -0.1):
    grid = standardGrid()
    grid.rewards.update({
           (0,0) : stepCost,
           (0,1) : stepCost,
           (0,2) : stepCost,
           (1,0) : stepCost,
           (1,2) : stepCost,
           (2,0) : stepCost,
           (2,1) : stepCost,
           (2,2) : stepCost,
           (2,3) : stepCost,
           })
    return grid

def playGame(agent,env):
    pass
    
    