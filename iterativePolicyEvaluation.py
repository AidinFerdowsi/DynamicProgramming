# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 14:51:45 2019

@author: Aidin
"""

import numpy as np
import matplotlib.pyplot as plt
from Grid import standardGrid

EPSILON = 10e-4

def printValues(V,grid):
    for i in range(grid.width):
        print ("-------------------------------")
        for j in range(grid.height):
            v = V.get((i,j),0)
            if v>= 0:
                print(" %0.2f|",v)
            else:
                print("%0.2f|",v)
        print ("")
                