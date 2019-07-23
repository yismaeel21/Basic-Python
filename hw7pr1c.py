#
# hw7pr1c.py - checking uniqueness  (for the random-number generator in Hmmm)
#    The test(S) function is already here (below).
#
# Name: Yusuf Ismaeel and Eamon Brady
#
# You'll paste your 100 numbers in this triple-quoted string:
NUMBERS = """
89
76
3
70
77
24
11
38
5
12
59
46
73
40
47
94
81
8
75
82
29
16
43
10
17
64
51
78
45
52
99
86
13
80
87
34
21
48
15
22
69
56
83
50
57
4
91
18
85
92
39
26
53
20
27
74
61
88
55
62
9
96
23
90
97
44
31
58
25
32
79
66
93
60
67
14
1
28
95
2
49
36
63
30
37
84
71
98
65
72
19
6
33
0
7
54
41
68
35
42
"""

def unique( L ):

    """This is a function that I wrote to check the uniqueness of a list through checking each individual element and the one before it,
    I checked if the first element is repeated afterwards, if not continue thru recursion"""

    if len(L)== 0:
        return True
    if L[0] in L[1:]:
        return False    # check whether L[0] re-appears
    return unique(L[1:])


def test(S):
    """test accepts a triple-quoted string, S,
       containing one number per line. Then, test
       returns True if those numbers are all unique
       (or if S is empty); otherwise it returns False
    """
    S = S.strip()               # remove all spaces in front & back of S
    ListOfStrings = S.split()   # split S at each space or newline
    # print("ListOfStrings is", ListOfStrings)
    ListOfIntegers = [int(s) for s in ListOfStrings]  # convert each to an int
    # print("ListOfIntegers is", ListOfIntegers)
    return unique(ListOfIntegers)

# Try it!
result = test(NUMBERS)
print("\nUniqueness test:  The result is", result)

