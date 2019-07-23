#Name: Yusuf Ismaeel and Eamon Brady
#Computer Science Homework 4

#Function 1
def rot(c,n):
    """This function takes the string c and rotates it by n letters"""
    if 'a' <= c <= 'z':
        if ord(c)+n <= ord('z'):
            return chr(ord(c)+n)
        else: 
            return chr(ord(c)+n-26)
    elif 'A' <= c <= 'Z':
        if ord(c)+n <= ord('Z'):
            return chr(ord(c)+n)
        else: 
            return chr(ord(c)+n-26)
    else:
        return c
def encipher(S, n):
    """The function encipher takes in a full list of strings and enciphers every individual string by n letters,
    Instead of using recursion, I created an empty string and then I appended it by each individual letter that 
    we rotated n degrees using rot(c,n)"""
    word=''
    for i in range(len(S)):
        word += rot(S[i],n)
    return word


#Function 2:
def letter_probability(c):
    #taken from Professor Chalmers:http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0


def probScore(S):
    """This function gives you the accumulated scrabble score for the letters you use for scrabble"""
    if len(S) == 0:
        return 0
    else:
        return letter_probability(S[0])+ probScore(S[1:])
        
def decipher(S):
    L = [[rot(c,n) for c in S] for n in range(26)]
    LoL = [(probScore(x),x) for x in L]
    J= max(LoL)
    return ''.join(J[1])
#Function 3
"""I decided it would be easier to write a function that does the blsort and general sorting altogether as that made
more sense"""
def blsort(L):
    new_list = []
    for x in range(len(L)):
        new_list += [min(L)]
        L.remove(min(L))
    return new_list
#Function 4
def gensort(L):
    new_list = []
    for x in range(len(L)):
        new_list += [min(L)]
        L.remove(min(L))
    return new_list

#Function 5
def jscore(S, T):
    """I tried doing this several times using the score through just finding how many letters they had inc common
    but then I realized that the function you needed to write was to assume that it was false and then trying to prove it
    was a true case for all these function rather than assume truthfulness and prove falsehood"""
    score = 0
    letters_in_common = [False] * len(T)
    for x in S:
        for y in range(len(T)):
            if x == T[y] and letters_in_common[y] == False:
                letters_in_common[y]= True
                score += 1
                break
    return score


#Function 6:
def exact_change(target_amount, L):
    """For this function,  I had to keep on indexing each value such that I would sum up from 0:1 and then 0:2
    and still be able to remove and rekeep summing, if the sum of these elements minus one, it returns true, else it doesn't.
    I had some issues with the ability to skip one to reach the other but that's why I added the removed function"""
    J = len(L)
    if target_amount == 0:
        return True
    if target_amount<0:
        return False
    if target_amount in L:
        return True
    for i in range(0, J):
        new_list = L[0:i] + L[i+1:0]
        if exact_change(target_amount - L[i], new_list):
            return True
    return False

#Function 7
"""At first, I wrote this function but I noticed that the results I got were always reversed
so I figured out another algo towards solving this problem would be to do it in reverse and therefore
all my answeres would be in the proper order. For instance, when I did the abcdefgh example the results were dcba and not abcd
so by doing this in reverse I managed to get the same result!."""
def LCS(S,T):
    def reversed_string(a_string):
        return a_string[::-1]
    if len(S)== 0 or len(T)== 0:
        return ""
    if S[0:1]== T[0:1]:
        return LCS(S[1:],T[1:])+ S[0]
    result1 = LCS(S[1:], T)
    result2 = LCS(S, T[1:])
    if len(result1)>len(result2):
        return reversed_string(result1)
    else:
        return reversed_string(result2)


#Extra Credit
def make_change(target_amount,L):  
    if exact_change(target_amount,L)== False:
        return False

        