# CS5, hw2pr3
# Filename: hw2pr3.py
# Name: Yusuf Ismaeel
# Problem description: Function Frenzy!

#
# leng example from class
#

"""This is the solution to function 1"""
def mult(x,y):
    """This is a function that multiplies the x and y values by each other using recursion 
    without the usage of multiplication"""
    if y==0:
        return 0
    elif y<0:
        return - (x - mult(x, y+1))
    else:
        return x + mult(x, y-1)

"""This is the solution to function 2"""
def dot(x,y):
    """This function gives us the dot product of two vectors (in this case it will usually be a list)"""
    if len(x)!= len(y):
        return 0
    elif len(x) and len(y)==2:
        return x[0]*y[0] + x[1]*y[1]
    else:
        return x[0]*y[0] + dot(x[1:], y[1:])

"""This is the solution to function 3"""
def ind(x,y):
    """This function checks if the element is in the list, and counts how many times the element is
        used in the list"""
    if x not in y:
        return len(y)
    elif y[0]== x:
        return 0
    else:
        return 1 + ind(x,y[1:])


"""This is the solution to function 4"""
def letterScore(x):
    if x in 'qz':
        return 10
    elif x in 'aeirlnostu':
        return 1
    elif x in 'dg':
        return 2
    elif x in 'bcmp':
        return 3
    elif x in 'fhvwy':
        return 4
    elif x in 'k':
        return 5
    elif x in 'jx':
        return 8
    else:
        return 0

"""This is the solution to function 5"""
def scrabbleScore(x):
    """This function gives you the accumulated scrabble score for the letters you use for scrabble"""
    y=0
    if x == '':
        return y
    else:
        y= y + letterScore(x[0])
        y= y + scrabbleScore(x[1:])
        return y


def transcribe(s):
    if len(s)== 0:
        return ''
    else:
        s= s.replace(" ", "")
        """ the s.replace function above removes the spaces between the DNA strings (if they were to exist) and 
        treats them as if they werent there"""
        return dna_rna(s[0])+ transcribe(s[1:])
