# CS5, hw2pr1
# Filename: hw2pr1.py
# Name: Yusuf Ismaeel
# Problem description: Second Python lab, problem 1!

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example problem (problem 0):  [2, 7, 5, 9]
answer0 = e[0:2] + pi[-2:]  
print(answer0)
answer1 = e[1:2] + pi[1:2]
print(answer1)
answer2 = [pi[-1],e[2], e[2]]
print(answer2)
answer3 = pi[1:]
print(answer3)
answer4 = e[2:] + e[0:1] + pi[0:1] + pi[2:3] + pi[4:5]
print(answer4)

h = 'harvey'
m = 'mudd'
c = 'college'
answer5= print(h[0:1] + h[-2:])
answer6 = print(c[0:4] + m[1:3]+ c[-1])
answer7 = print(h[1:]+ m[1:])
answer8 = print(h[0:3]+ m[2:3] + c[4:5]+ 3*h[0:3])
answer9 = print(c[3:6]+ c[1:2]+ m[0:1]+ h[-1] + c[-1:-3:-1] + c[1])
answer10 = print(c[0:6:2] + h[1:3]+ c[0]+ h[1]+ 2*c[2])