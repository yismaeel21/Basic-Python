#
# hw7pr5.py -  Python!
#
#  Intro to loops! (starter code below)
#
# Name:
#
def fac(n):
    """Loop-based factorial function
       Argument: a nonnegative integer, n
       Return value: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1,n+1):     # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

#
# Tests for looping factorial
#


def power(b,p):
    """This is a function that takes an integer base (b) and raises it to a power (p) using a for loop"""
    result = 1
    for x in range(p):
        result*= b
    return result

assert power(2, 5)== 32
assert power(5,2)==25
assert power(42,0)== 1
assert power(0,42)==0
assert power(0,0)==1

def summedOdds(L):
    """This is a function that sums up all the odd elemnts of a list"""
    our_list = []
    for x in range(len(L)):
        if L[x]%2 == 1:
            our_list.append(L[x])
    return sum(our_list)

assert summedOdds([4, 5, 6]) == 5
assert summedOdds(range(3, 10)) == 24    

import random

def unique(L):
  """Returns whether all elements in L are unique.
     Argument: L, a list of any elements.
     Return value: True, if all elements in L are unique,
                or False, if there is any repeated element
  """
  if len(L) == 0:
    return True
  elif L[0] in L[1:]:
    return False
  else:
    return unique(L[1:])  # recursion is OK in this function!

import random
def untilARepeat(hi):
    """this is a function that goes through a list of elements generated from the random function to find if any are repeated and how many times it took for the number to repeat!"""
    L = []
    num = 0
    while unique(L):
        x = random.choice(range(0,hi))
        L.append(x)
        num += 1
    return num