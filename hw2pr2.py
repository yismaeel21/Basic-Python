
# CS5, Lab2 part 2
# Filename: hw2pr2.py
# Name: Yusuf Ismaeel
# Problem description: First few functions!


def dbl(x):
    """Result: dbl returns twice its argument
       Argument x: a number (int or float)
       Spam is great, and dbl("spam") is better!
    """
    return 2*x
#Answer 1
def sq(x):
    """The result will be the square of the value you've entered"""
    return x**2
#Answer 2
def interp(low, hi, fraction):
    """Accepts three numbers in the argument and return the floating point value"""
    return (hi-low) * fraction + low
#Answer 3
def checkends(s):
    """Checks if the beginning of a function is the same as the end"""
    if s[0]== s[-1]:
        print(True)
    else:
        print(False)
#Answer 4
def flipside(s):
    """This is a function that takes a string and flips it halfway through"""
    x = len(s)//2
    print(s[x:] + s[:x])
#Answer 5
def convertFromSeconds(s):
    days = s // (24*60*60)  # Number of days
    s = s % (24*60*60)      # The leftover
    hours = s // (60*60)
    s = s % (60*60)
    minutes = s // 60
    s = s % 60
    seconds = s
    return [days, hours, minutes, seconds]

 #
 