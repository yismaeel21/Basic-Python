#Yusuf Ismaeel
#HW10 Problem 3
# coding: utf-8
#
# the top line, above, is important --
# it ensures that Python will be able to use this file,
# even if you paste in text with Unicode characters
# (beyond ASCII)
# for an more expansive example of such a file, see
#    http://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt
#
# OK! Now we're ready for hw10pr3.py ...
#
#
# Name: Yusuf Ismaeel
#
#


# function #1
#
import random
def createDictionary(filename):
    """makes a dictionary of words and the words before it and outputs it into a txt file"""
    d ={}
    f = open(filename)
    text = f.read()
    f.close()
    word = '$'
    LoW = text.split()
    for nw in LoW:
        if word[-1] in '.?!':
            word = '$'
            d[word] += [nw]
        elif word not in d:
            d[word] = [nw]
        else:
            d[word] += [nw]
        word = nw
    
    return d

#Function 2
def generateText(d, N):
    """Combines the strings from the previous function into words using Markov"""
    word = ''
    punctuation = '.'
    for x in range(N):
        if punctuation[-1] in '.?!':
            newWord = random.choice(d["$"])
            word += newWord + ' '
            punctuation = newWord
        else:
            newWord = random.choice(d[punctuation])
            word += newWord + ' '
            punctuation =  newWord
    return word

#
# Your 500-or-so-word CS essay (paste into these triple-quoted strings below):
#
#Source: Bohemian Rhapsody by Queen
"Mama, just begun But now I've gone and thrown it all away. Mama, just begun But now he's dead Mama, life had just begun But now he's dead Mama, life had just killed a gun against his head Pulled my trigger, now I've gone and thrown it all away. Mama, just killed a man Put a gun against his head Pulled my trigger, now I've gone and thrown it all away. Mama, life had just begun But now I've gone and thrown it all away. Mama, just killed a man Put a man Put a gun against his head Pulled my trigger, now I've gone and thrown it all away. Mama, life had just begun But now I've gone and thrown it all away. Mama, just killed a man Put a man Put a gun against his head Pulled my trigger, now I've gone and thrown it all away. Mama, life had just begun But now he's dead Mama, just begun But now he's dead Mama, life had just begun But now he's dead Mama, life had just killed a gun against his head Pulled my trigger, now he's dead Mama, life had just killed a gun against his head Pulled my trigger, now he's dead Mama, life had just killed a gun against his head Pulled my trigger, now I've gone and thrown it all away. Mama, just begun But now he's dead Mama, just killed a man Put a gun against his head Pulled my trigger, now he's dead Mama, life had just begun But now I've gone and thrown it all away. Mama, life had just begun But now he's dead Mama, life had just killed a man Put a man Put a man Put a gun against his head Pulled my trigger, now he's dead Mama, just begun But now I've gone and thrown it all away. Mama, life had just killed a man Put a man Put a man Put a gun against his head Pulled my trigger, now I've gone and thrown it all away. Mama, just killed a man Put a gun against his head Pulled my trigger, now he's dead Mama, just begun But now he's dead Mama, life had just killed a gun against his head Pulled my trigger, now I've gone and thrown it all away. Mama, life had just begun But now I've gone and thrown it all away. Mama, just killed a man Put a gun against his head Pulled my trigger, now he's dead Mama, just killed a man Put a man Put a gun against his head Pulled my trigger, now he's dead Mama, life had just begun But now I've gone and thrown it all away. Mama, life had just begun But now I've gone and thrown it all away. Mama, just begun But now I've gone and thrown it all away. Mama, life had just begun But now he's dead Mama, just begun But now I've gone and thrown it all away. Mama, life "

#
#