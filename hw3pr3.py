# CS 5 Gold, hw3pr3
# filename: hw3pr3.py
# Name: Yusuf Ismaeel
# problem description: List comprehensions
import math
from math import *

def dbl(x):
    """Doubler!  argument: x, a number"""
    return 2*x

def sq(x):
    """Squarer!  argument: x, a number"""
    return x**2
def lc_mult(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each multiplied by 2**
    """
    return [2*x for x in range(N)]

def lc_idiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       WARNING: this is INTEGER division...!
    """
    return [x//2 for x in range(N)]

def c(x):
    """c is a semicircular function of radius two"""
    return (4 - x**2)**0.5

def lc_fdiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       NOTE: this is floating-point division...!
    """
    return [x/2 for x in range(N)]


def unitfracs(N):
    """Be sure to improve this docstring!
    """
    return[float(x/N) for x in range(N)]
assert unitfracs(2) == [0.0, 0.5]
assert unitfracs(3) == [0.0, 0.3333333333333333, 0.6666666666666666]
assert unitfracs(4) == [0.0, 0.25, 0.5, 0.75]

def scaledfracs(x,y,N):
    """this functions takes the difference between y and x and then creates N left endpoints uniformly through that given
    interval"""
    return [float(x + (y-x)*z) for z in unitfracs(N)]
assert scaledfracs(10, 30, 5) == [10.0, 14.0, 18.0, 22.0, 26.0]
assert scaledfracs(41, 43, 8) == [41.0, 41.25, 41.5, 41.75, 42.0, 42.25, 42.5, 42.75]
assert scaledfracs(0, 10, 4) == [0.0, 2.5, 5.0, 7.5]

def sqfracs(x,y,N):
    """this function returns the square of the values that we attained from the left endpoints"""
    return [float((x + (y-x)*z))**2 for z in unitfracs(N)]
assert sqfracs(4, 10, 6) == [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
assert sqfracs(0, 10, 5) == [0.0, 4.0, 16.0, 36.0, 64.0]

def f_of_fracs(f, x, y, N):
    """This is a function that takes the f function on the left hand and applies it to every element in the range of N"""
    return [f(x + (y-x)*z) for z in unitfracs(N)]
assert f_of_fracs(dbl, 10, 20, 5) == [20.0, 24.0, 28.0, 32.0, 36.0]
assert f_of_fracs(sq, 4, 10, 6) == [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]

def integrate(f, x, y, N):
    """This is the function that takes the integral (using Reimann Sum) of the function f from x and y using N number of rectangles to approximate"""
    j = float(x + (y-x)/N)
    return j*sum(f_of_fracs(f,x,y,N))

"""Question1:
    The function 2x is always increasing from -infinity to infinity, therefore the left Riemann sum approximation of this function
    will always understand the actual value unless the value of N is EXTREMELY high, if we took a function's that's always decreasing, on the other hand.
    The left Riemann sum will usually always be higher than the function itself, therefore overstating the value of the approximation of the integral.
    i.e if we look at -2x instead of 2x we'd get an overapproximation for these values"""


"""Question 2: the more boxes (N number of boxes we use) the value gets closer to pi, as the function is decreasing from 0 to 2, this is an overapproximation
for the value of pi using this method of integrating"""
    