# CS5 Gold, hw3pr2
# Filename: hw3pr2.py
# Name: Yusuf Ismaeel and Eamon Brady
# Problem description: Sleepwalking/ Drunk student


import random
from random import *
import sys
sys.setrecursionlimit(50000)

def rs():
    """rs chooses a random step and returns it.
       note that a call to rs() requires parentheses
       arguments: none at all!
    """
    return choice([-1, 1])

def rwpos(x,y):
    """x is the starting position whereas y is the number of steps"""
    print("Current location is", x)
    if y==0:
        return x
    return rwpos(x+ rs(), y-1)

def rwsteps(x,y,z):
    print("|"+"_"*(x-y)+ "S" +"_"*(z-x)+ "|")
    if x==y or x==z:
        return 0
    return 1 + rwsteps(x+rs(),y,z)

def rwposPlain(x,y):
    if y==0:
        return x
    return rwposPlain(x + rs(),y-1)

def ave_signed_displacement(x):
    totalSteps = 0
    for y in range(x):
        totalSteps+= rwposPlain(0,100)
    return float(totalSteps)/x
"""For average signed displacement, I started by assigning the value at 0 for totalSteps as that would be the displacement from
the original location, and then the increment for each step would be depend on the function I defined above (rwposPlain), this acted like my summation function
after that; I divided the total sum by the number of steps I took to find average displacement"""

def ave_squared_displacement(x):
    totalSteps= 0
    for y in range(x):
        totalSteps += rwposPlain(0,100)**2
    return float(totalSteps)/ x
"""I did the same process as I did above, but instead of just keeping the value the same, I squared the value and incremented the totalSteps function by it"""



#We also came up with this way of solving the problem:
#def ave_signed_displacement(x):
#       LC= [rwposPlain(0,100) for y in range(x)]
#       return sum(LC)/len(LC)

#def ave_squared_displacement(x):
#       LC= [rwposPlain(0,100)**2 for y in range(x)]
#        return sum(LC)/len(LC)"""