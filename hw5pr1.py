# CS5 Gold, hw5pr1
# Filename: hw5pr1.py
# Name: Yusuf Ismaeel
# Problem description: Binary <-> decimal conversions
import sys

#Function 1
def isOdd(N):
    if N%2==1:
        return True
    else:
        return False
assert isOdd(42) == False
assert isOdd(43) == True

#Function 2
def numToBinary(N):
    if N==0:
        return ''
    elif N%2==1:
        return numToBinary(N//2) + '1'
    else:
        return numToBinary(N//2) + '0'

assert numToBinary(0) == ''
assert numToBinary(42) == '101010'

#Function 3
def binaryToNum(S):
    """
    """
    if S == '':
        return 0
    elif S[-1] == '1':
        return 2*binaryToNum(S[:-1])+ 1
    else:
        return 2*binaryToNum(S[:-1])+ 0
#Function 4
def increment(S):
    if S== '11111111':
        return '00000000'
    else:
        n = binaryToNum(S)
        x = n+1
        y = numToBinary(x)
        numZero= 8- len(y)
        return numZero*'0'+ y
def count(S,n):
    print(S)
    if n==0:
        return
    else:
        newS = increment(S)
        return count(newS, n-1)

def numToTernary(N):
    if N==0:
        return ''
    elif N%3==1:
        return numToTernary(N//3) + '1'
    elif N%3==2:
        return numToTernary(N//3)+ '2'
    else:
        return numToTernary(N//3)+ '0'

def ternaryToNum(S):
    if S == '':
        return 0
    elif S[-1] == '1':
        return 3*ternaryToNum(S[:-1])+ 1
    elif S[-1] == '2':
        return 3*ternaryToNum(S[:-1])+ 2
    else:
        return 3*ternaryToNum(S[:-1])+ 0

def balancedTernaryToNum(S):
    if S == '':
        return 0
    elif S[-1] == '+':
        return 3*balancedTernaryToNum(S[:-1])+ 1
    elif S[-1] == '-':
        return 3*balancedTernaryToNum(S[:-1])- 1
    else:
        return 3*balancedTernaryToNum(S[:-1])+ 0

def numToBalancedTernary(N):
    if N==0:
        return ''
    elif N%3==1:
        return numToBalancedTernary((N-1)/3) + '+'
    elif N%3==2:
        return numToBalancedTernary((N+1)/3)+ '-'
    else:
        return numToBalancedTernary(N/3)+ '0'
