#Yusuf Ismaeel
#Homework 8 Problem 2

def count_evens(nums):
    """This is a function that counts how many even numbers are in a list of integers"""
    cnt = 0
    for x in nums:
        if x%2==0:
            cnt+=1
    return cnt

def sum13(nums):
    """This function takes the sum of all values in a list less than 13"""
    oursum = 0
    for x in nums:
        if x<13:
            oursum += x
    return oursum

def big_diff(L):
    """A function that returns the range of a list, when I did this I decided it would be better to redefine the max and the min as any element of the list and then check if it is higher or less than the variable x in our list
    if so, we replace; otherwise we don't do anything"""
    ourMax=L[0]
    ourMin=L[0]
    for x in L:
        if x>ourMax:
            ourMax=x
        elif x<ourMin:
            ourMin=x
    return ourMax-ourMin

def double_char(L):
    """A function that doubles the elemnts of all characters in a string"""
    ourString = ''
    for x in range(len(L)):
        ourString += L[x]*2
    return ourString

def count_code(S):
    """This is a function that takes in a string and returns the count of how many
    times the string co*e is used in successive order"""
    count = 0
    for x in range(len(S)-3):
        if S[x:x+2]== 'co' and S[x+3]=='e':
            count+=1
    return count

def cat_dog(str):
    """A function that returns True if the strings dog and cat appear the same number of times in the string"""
    count_cat = 0
    count_dog = 0
    for x in range(len(str)-2):
        if str[x:x+3] == 'dog':
            count_dog += 1
        if str[x:x+3] == 'cat':
            count_cat += 1
    
    return count_cat == count_dog

def count_hi(str):
    count=0
    for x in range(len(str)-1):
        if str[x:x+2]== 'hi':
            count+=1
    return count

def end_other(a,b):
    a = a.lower()
    b = b.lower()
    return a[-len(b):] ==b or  b[-len(a):]==a

def xyz_there(str):
    for x in range(len(str)):
        if str[x]!= 'i' and str[x+1:x+3]=='xyz':
            return True
        if str[0:3]== 'xyz':
            return True
    return False

def sum67(nums):
    """a function that stops summing between two consecutive values of 6 and 7"""
    sum = 0
    Value_6 = False
    for i in nums:
        if i ==6:
            Value_6 = True
        if i == 7 and Value_6 == True:
            Value_6 == False
        if Value_6== False:
            sum += i
    return sum

def centered_average(nums):
    """This is a function that removes the max and minimum values of a function and then finds the average"""
    ourMax= nums[0]
    ourMin= nums[0]
    for x in nums:
        if ourMax<x:
            ourMax=x
        elif ourMin>x:
            ourMin=x
    nums.remove(ourMin)
    nums.remove(ourMax)
    return int(sum(nums)/len(nums))
    
    #another way of doing the same thing!
    #nums.remove(max(nums))
    #nums.remove(min(nums))
    #return sum(nums)/len(nums)

def has22(nums):
    """a function that checks if there are two twos back to back"""
    for x in range(len(nums)-1):
        if nums[x] == nums[x+1] == 2:
            return True
    return False
