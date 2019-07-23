#
# hw9pr1.py - Game of Life lab
#
# Name:
#

import random
from random import *
from copy import deepcopy
from copy import *
def createOneRow(width):
    """ returns one row of zeros of width "width"...  
         You might use this in your createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width,height):
    A = []
    for row in range(height):
        A+=[createOneRow(width)]
    return A

def printBoard(A):
    """This function prints the 2D list-of-lists A."""
    for row in A:   
        enter = ''            
        for col in row:         # col is the individual element
            enter+= str(col)
        print(enter)
    
def diagonalize(width, height):
    """Creates an empty board and then modifies it
       so that it has a diagonal strip of "on" cells.
       But do that only in the *interior* of the 2D array.
    """
    A = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return (A)

def innerCells(w,h):
    """this is a function that sets the inner cells to be equal to one disregarding the edge cells"""
    A = createBoard(w, h)
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if 0<row<h-1 and 0<col<w-1:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return (A)

def randomCells(w,h):
    A = createBoard(w,h)
    for row in range(h):
        for col in range(w):
            A[row][col] = choice([0,1])
    return (A)   

def copy(A):
    """Returns a DEEP copy of the 2D array A."""
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            newA[row][col]= A[row][col]

    return newA

def innerReverse(A):
    """A function that changes the inner values of a from 0 to 1 and vice versa"""
    for row in range(len(A)):
        for col in range(len(A[0])):
            if 0< row <len(A)-1 and 0 < col < len(A[0])-1:
                if A[row][col]==0:
                    A[row][col]=1
                else:
                    A[row][col]=0
    return A

def countNeighbors(row,col,A):
    """A function that counts the number of neighbors each row/column has"""
    count = 0
    for x in range(-1,2):
        for y in range(-1,2):
            if abs(x)+abs(y) != 0:
                count+=A[row+x][col+y]
    return count

def next_life_generation(A):
    """Makes a copy of A and then advances one
       generation of Conway's Game of Life within
       the *inner cells* of that copy.
       The outer edge always stays at 0.
    """
    h= len(A)
    w = len(A[0])
    newA= createBoard(w,h)
    for row in range(h):
        for col in range(w):
            if 0<row<h-1 and 0<col<w-1:
                count = countNeighbors(row,col,A)
                if count<2 or count > 3:
                    newA[row][col]=0
                elif count == 3:
                    newA[row][col]=1
                else:
                    newA[row][col]= A[row][col]
            else:
                newA[row][col]=0
    return newA