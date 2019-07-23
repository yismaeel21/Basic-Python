#
# hw3pr1.py
#
# Name: Yusuf Ismaeel
#
# Turtle graphics and recursion
#

import time
from turtle import *
from random import *

def tri(n):
    """Draws n 100-pixel sides of an equilateral triangle.
       Note that n doesn't have to be 3 (!)
    """
    if n == 0:
        return      # No sides to draw, so stop drawing
    else:
        forward(100)
        left(120)
        tri(n-1)    # Recur to draw the rest of the sides!

def spiral(x, y, z):
    """Spiral-drawing function.  Arguments:
       initialLength = the length of the first leg of the spiral
       angle = the angle, in degrees, turned after each spiral's leg
       multiplier = the fraction by which each leg of the spiral changes
    """
    if x <= 1:          
        return      # No more to draw, so stop this call to spiral
    else:
        forward(x)
        left(y)
        spiral(z*(x),y,z)
    
        # You will want a call to forward here...
        # You will want a turn here...
        # You will want to recur here! That is, make a new call to spiral...

def chai(size):
    """Our chai function!"""
    if (size < 5): 
        return
    else:
        forward(size)
        left(90)
        forward(size/2)
        right(90)
        chai(size/2)
        right(90)
        forward(size)
        left(90)
        chai(size/2)
        left(90)
        forward(size/2.0)
        right(90)
        backward(size)
        return
def svtree(x, y):
    """svtree: draws a side-view tree
       trunklength = the length of the first line drawn ("the trunk")
       levels = the depth of recursion to which it continues branching
    """
    if y == 0:
        return
    else:
        forward(x)
        left(30)
        svtree(x*.61,y-1)
        right(60)
        svtree(x*.61,y-1)
        left(30)
        backward(x)
        

"""three branches
        forward(x)
        left(30)
        svtree(x*.61,y-1)
        right(60)
        svtree(x*.61,y-1)
        left(30)
        right(60)
        svtree(x*.61,y-1)
        left(60)
        backward(x)
        """

def flakeside(x,y):
    if y==0:
        forward(x)
        return;
    flakeside(x/3,y-1)
    right(60)
    flakeside(x/3,y-1)
    left(120)
    flakeside(x/3,y-1)
    right(60)
    flakeside(x/3,y-1)

def snowflake (x, y):
  flakeside(x, y)
  left(120)
  flakeside(x, y)
  left(120)
  flakeside(x, y)
  left(120)      
