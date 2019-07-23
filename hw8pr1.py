# hw8pr1.py
# Lab 8
#
# Name: Yusuf Ismaeel and Eamon Brady
#

# keep this import line...
from cs5png3 import *


#
# a test function...
#
def test_fun():
    """ algorithmic image-creation one pixel at a time...
        this is a test function: it should output
        an image named test.png in the same directory
    """
    im = PNGImage(300,200)  # creates an image of width=300, height = 200

    # Nested loops!
    for r in range(200):  # loops over the rows with runner-variable r
        for c in range(300):  # loops over the cols with c
            if  c == r:   
                im.plotPoint( c, r, (255,0,0))
            #else:
            #    im.plotPoint( c, r, (255,0,0))
                
    im.saveFile()

#
# start your Lab 8 functions here:
#

def update(l,n):
    """Update starts with z = 0 and runs z = z**2 + c
       for a total of n times. It returns the final z."""
    y=0
    for x in range(n+1):
        y = y**2 + l
    return y
    
