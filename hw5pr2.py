#Homework 5 Problem 2
#Yusuf Ismaeel


#Function1
def numToBaseB(N, B):
    """This function converts a  number from base ten to a number in base B"""
    if N==0:
        return ''
    if N%B==0:
        return numToBaseB(N//B,B)+'0'
    else:
        return numToBaseB(N//B,B) + str(N%B)
assert numToBaseB(0, 4) == ''
assert numToBaseB(42, 5) == '132'

#Function2
def baseBToNum(S, B):
    """This is a function that converts a number from base B to a number in base 10"""
    if S=='':
        return 0
    elif S[-1]==str(B):
        return B*(baseBToNum(S[:-1],B)) + 0
    else:
        return B*(baseBToNum(S[:-1],B)) + int(S[-1])
assert baseBToNum('1474462', 8) == 424242
assert  baseBToNum("101010", 10) == 101010

#Function3
def baseToBase(B1, B2, s_in_B1):
    """This is a function that takes a number in base B1, transforms it into a regular number and then transforms it into a number in base B2"""
    J= baseBToNum(s_in_B1,B1)
    return numToBaseB(J,B2)
assert baseToBase(2, 4, '101010') == '222'
assert baseToBase(2, 5, '1001001010') == '4321'


#Function4
"""I figured I'd be better of calling back to the functions from the lab to reduce the confusion and reduce the variables that I have to use as recalling back to baseBtoNum would have more variables"""
def binaryToNum(S):
    if S == '':
        return 0
    elif S[-1] == '1':
        return 2*binaryToNum(S[:-1])+ 1
    else:
        return 2*binaryToNum(S[:-1])+ 0
def numToBinary(N):
    if N==0:
        return ''
    elif N%2==1:
        return numToBinary(N//2) + '1'
    else:
        return numToBinary(N//2) + '0'
def add(S,T):
    J = binaryToNum(S)
    T = binaryToNum(T)
    K = J+T
    return numToBinary(K)

#Function5
def addB(S, T):
    """ This is a function that adds two binary numbers using the regular arithmetic (carry forward) technique """
    if S=='' and T=='':
        return ''
    if S=='':
        return T
    if T=='':
        return S
    if S[-1] == '0' and T[-1] == '0':
        return addB(S[:-1], T[:-1]) + '0'
    elif S[-1] == '1' and T[-1]=='0':
        return addB(S[:-1], T[:-1]) + '1'
    elif S[-1] == '0' and T[-1] == '1':
        return addB(S[:-1], T[:-1]) + '1'
    else:
        return addB(addB(S[:-1], '1'),T[:-1]) + '0'
assert addB('11', '100') == '111'
assert addB("11100", "11110") == '111010'
assert addB('110','11') == '1001'
assert addB('110101010','11111111') == '1010101001'
assert addB('1','1') == '10'

#Function6
def frontNum(S):
    if len(S)<=1:
        return len(S)
    elif S[0]==S[1]:
        return 1 + frontNum(S[1:])
    else:
        return 1
def compress(S):
    """accepts a string and compresses it into a shorter form"""
    if S=='':
        return ''
    else:
        x= frontNum(S)
        y= numToBinary(x)
        numZero= 7-len(y)
        return S[0]+numZero*'0' + y+compress(S[x:])
def uncompress(S):
    """accepts a compresssed string and uncompresses it"""
    if S=='':
        return ''
    else:
        x= baseBToNum(S[1:8],2)
        return S[0]*x + uncompress(S[8:])
