#Yusuf Ismaeel

#
# Example user-interaction looping program
#  (a variant of the one done in class)
#

import math
from math import *
def menu():
    """A function that simply prints the menu"""
    print()
    print("(0) Input a new list")
    print("(1) Print the current list")
    print("(2) Find the average price")
    print("(3) Find the standard deviation")
    print("(4) Find the min and its day")
    print("(5) Find the max and its day")
    print("(6) Your TT investment plan")
    print("(9) Quit")
    print()

def predict(L):
    """Predict ignores its argument and returns
       what the next element should have been.
    """
    return 42

def find_min(L):
    """find min uses a loop to return the minimum of L.
       Argument L: a nonempty list of numbers.
       Return value: the smallest value in L.
    """
    result = L[0]
    for x in L:
        if x < result:
            result = x
    return result

def find_min_loc(L):
    """find min loc uses a loop to return the minimum of L
            and the location (index or day) of that minimum.
        Argument L: a nonempty list of numbers.
        Results:  the smallest value in L, its location (index)
    """
    minval = L[0]
    minloc = 0

    for i in list(range(len(L))):
        if L[i] < minval:  # a smaller one was found!
            minval = L[i]
            minloc = i

    return minloc

def main():
    """The main user-interaction loop"""
    secret_value = 4.2

    L = [30, 10, 20]  # an initial list

    while True:     # the user-interaction loop
        print("\n\nThe list is", L)
        menu()
        choice = input("Choose an option: ")

        #
        # "Clean and check" the user's input
        # 
        try:
            choice = int(choice)   # make into an int!
        except:
            print("I didn't understand your input! Continuing...")
            continue

        # run the appropriate menu option
        #
        if choice == 9:    # We want to quit
            break          # Leaves the while loop altogether

        elif choice == 0:  # We want to continue...
            newL= input("Enter a new list: ")    #Asks for a new list from user
            try:
                newL = eval(newL)
                if type(newL)!= type([]):
                    print("That doesn't seem like a list, not changing the list")
                else:
                    L= newL #if they're the same type, we change the list
            except:
                print("I dind't understand your input, not changing the list")
        elif choice == 1:  #print the current list
            print()
            print("Day","Price")
            print("---","-----")
            day = 0
            for price in L:
                print("  ", day, price)
                day += 1
        elif choice == 2:  #This is the average value!
            print()
            n = sum(L)/len(L)
            print("The average value is ", n)
        elif choice == 3:  #finds the standard deviation
            p = stdev(L)
            print("The standard deviation is ", p)
        elif choice == 4:  #Finds this minimum of the data set
            m = find_min(L)
            n = find_min_loc(L)
            print("The minimum value in L is", m, "at day #", n)

        elif choice == 5:  #Finds the maximum of the data set
            k = find_max(L)
            j = find_max_loc(L)
            print("The maximum value in L is", k, "at day #", j)
        elif choice == 6:
            a= max(L)
            b= find_max_loc(L)
            c= min(L)
            d= find_min_loc(L)
            print("Your TT investment strategy is to ")
            print()
            print("Buy on day ", d, "at price", c)
            print("Sell on day", b, "at price", a)
            print()
            print("For a total profit of", a-c)
        else:
            print("The choice", choice, "is not an option")
            print("Try again")
    print()
    print("See you yesterday!")

def find_max(L):
    ourMax= L[0]
    for x in L:
        if x> ourMax:
            ourMax=x
    return ourMax

def find_max_loc(L):
    ourMax = L[0]
    MaxLoc = 0
    for x in range(len(L)):
        if L[x]> ourMax:
            ourMax = L[x]
            MaxLoc = x
    return MaxLoc

def stdev(L):
    """ finds the standard deviation of a function """
    output = 0
    for num in L:
        current = (num - (sum(L)/len(L))) ** 2
        output = output + current
    output = output / len(L)
    output = sqrt(output)
    return output

#sorting list
def sortasc(L):
    ourList= []
    for x in range(len(L)):
        j = find_min(L)
        ourList.append(j)
        L.remove(j)
    return ourList

def sortdesc(L):
    J= sortasc(L)
    K = J[::-1]
    return K
    