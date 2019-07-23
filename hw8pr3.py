#Yusuf Ismaeel

import random
from random import *
import math
from math import *
def throwDart():
    """This function makes sure if the thrown dart is inside the circle"""
    x = uniform(-1.0,1.0)
    y = uniform(-1.0,1.0)
    if x**2 + y**2 <=1:
        return True
    return False

def forPi(n):
    """This is a helper function that helps us estimate/approximate the value of pi"""
    numhits=0
    numthrows=0
    for x in range(n):
        if throwDart()==True:
            numhits+=1
        numthrows+=1
        print(numhits, " hits out of", numthrows, " throws gives us π = " ,4* numhits/numthrows)
    return 4*(numhits)/numthrows

def whilePi(n):
    """This is a function that keeps throwing darts until you get within n distance from pi"""
    numhits=0
    numthrows=0
    estimatedPi=4.0
    while abs(estimatedPi-pi)>n:
        if throwDart()==True:
            numhits+=1
        numthrows+=1
        estimatedPi= 4*(numhits)/(numthrows)
        print(numhits, "hits out of ", numthrows, "throws estimates π to be: ", estimatedPi)
    return numthrows