# coding: utf-8
#
# hw1pr2b.py
#

""" 
Title for your adventure:   The Legend of Zelda.

Notes on how to "win" or "lose" this adventure:
  To save the Princess, choose the Temple.
  To lose, choose either the Mountain or the Castle.

"""

import time

def story():
    """ this function runs one session of interactive fiction
        Well, it's "fiction," depending on the pill color chosen...
        arguments: no arguments (prompted text doesn't count as an argument)
        results: no results     (printing doesn't count as a result)
    """
    delay = 1.0          # change to 0.0 for testing or speed runs,
                         # ..larger for dramatic effect!

    name = input("What hath your mother named you, warrior? ")

    print()
    print("Welcome,", name, "to the Quest to find our beloved Princess Zelda")
    print()

    print("She has been missing for quite a while now and we are very distraught by her absence")
    ans= input("Will you help us find her? (Y/N) ")
    if ans== "Y":
        print("Thank you, oh brave warrior!")
        print("We have heard that she is either in the Mountains, the Temple or the Castle")
        search = input("Where do you want to search? (Mountains/Temple/Castle)")
        if search== "Mountains":
            print("Let us go and search for her in the mountains!")
            delay = 2.0
            print("We have searched far and wide, unfortunately we could not find her :(")
        elif search== "Temple":
            print("Let us go and find her for she might be in there!")
            print("Alas! we have found her, thank you oh mighty", name, "we shall forever cherish your legacy!")
            award = input("We must reward you for your benevolent act, would you like a pot of gold or a lifetime supply of gold-plated pop tarts? (G/P) " )
            if award == "G":
                print("Ah! a lover of shiny things I see!")
            elif award == "P":
                print("Ah! A sweet tooth for a sweet soul!")
            else:
                reward= input("Do you not want a reward for your kind act? (Y/N) ")
                if reward == "Y":
                    userchoice = input("Well then, choose between gold or pop tarts? (G/P) ")
                    if userchoice == "G":
                        print("A man of high class doth indeed have high taste!")
                    if userchoice == "P":
                        print("The sweetest candy in all the realms!")
                if reward == "N":
                    print("A true benevolent soul indeed!")
            print("We are forever in your debt for bringing back our beloved princess, your bravery will never be forgotten! ")
        elif search == "Castle":
            print("We cannot find her there! What a mess")
            print("Where is our Zelda?!")
        else:    
            print("That's not where we last saw her!")
    else: print("I understand, this quest is not worthy of your time.")