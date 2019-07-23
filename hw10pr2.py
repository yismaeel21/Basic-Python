#Yusuf Ismaeel
#Homework 10 Problem 2

"""Copying the codes from the  HW"""
def inarow_Neast(ch, r_start, c_start, A, N):
    """East equality checker for choice repeating n times"""
    NR = len(A)      # number of rows is len(A)
    NC = len(A[0])   # number of cols is len(A[0])

    if r_start >= NR:
        return False

    if c_start > NC - N:
        return False

    # are all of the data elements correct?
    for i in range(N):                  # loop index i as needed
        if A[r_start][c_start+i] != ch: # check for mismatches
            return False                # mismatch found--return False

    return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """South Equality Checker for input repeated N times"""
    NR = len(A)      # number of rows is len(A)
    NC = len(A[0])   # number of cols is len(A[0])

    if r_start > NR-N:
        return False

    if c_start > NC:
        return False

    # are all of the data elements correct?
    for i in range(N):                  # loop index i as needed
        if A[r_start+i][c_start] != ch: # check for mismatches
            return False                # mismatch found--return False

    return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """SouthEast Equality checker for the choice n times"""
    NR = len(A)      # number of rows is len(A)
    NC = len(A[0])   # number of cols is len(A[0])

    if r_start > NR-N:
        return False

    if c_start > NC - N:
        return False

    # are all of the data elements correct?
    for i in range(N):                  # loop index i as needed
        if A[r_start+i][c_start+i] != ch: # check for mismatches
            return False                # mismatch found--return False

    return True

def inarow_Nnortheast(ch,r_start, c_start, A, N):
    """Equality checker for going northeast for the choice repeating N times"""
    NR = len(A)      # number of rows is len(A)
    NC = len(A[0])   # number of cols is len(A[0])

    if r_start >NR:
        return False
    if c_start > NC:
        return False
    if NC-c_start<N:
        return False

    # are all of the data elements correct?
    for i in range(N):                  # loop index i as needed
        if A[r_start-i][c_start+i] != ch: # check for mismatches
            return False                # mismatch found--return False

    return True


class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # the string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # bottom of the board

        # and the numbers underneath here

        return s       # the board is complete, return it

    def addMove(self, col, ox): 
        """Adds a move to the given column"""
        for i in range(self.height):
            if self.data[self.height-i-1][col] == ' ':
                self.data[self.height-i-1][col] = ox
                return
    
    def clear(self):
        """removes all x's and o's from the board to return a brand new one"""
        for x in range(self.height):
            for y in range(self.width):
                self.data[x][y] = ' '
    
    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'
    
    def allowsMove(self,c):
        """A function that checks if this move is permissible in connet four or not"""
        if c<0 or c>= self.width:
            return False
        if self.data[0][c]!= ' ':
            return False
        return True

    def isFull(self):
        """A function that checks if the board is full or not"""
        for x in range(self.width):
            if self.allowsMove(x):
                return False
        return True

    def delMove(self,c):
        """Deletes a move from the board"""
        for x in range(self.height):
            if self.data[x][c] == 'X' or self.data[x][c]== 'O':
                self.data[x][c]= ' '
                return
    
    def winsFor(self,ox):
        """Checker for which option wins"""
        H = self.height
        W = self.width
        D = self.data
        for row in range(H):
            for col in range(W):
                if inarow_Neast(ox,row,col,D,4):
                    return True
                if inarow_Nnortheast(ox,row,col,D,4):
                    return True
                if inarow_Nsouth(ox,row,col,D,4):
                    return True
                if inarow_Nsoutheast(ox,row,col,D,4):
                    return True
        return False

    
    def hostGame(self):
        """This starts a game of Connect Four!"""
        print("Welcome to the intense game of Connect 4!")
        print(self)
        while True:
            users_col = -1
            while not self.allowsMove(users_col):
                users_col = int(input("X, Choose a column: "))
            self.addMove(users_col,'X')
            print(self)
            if self.winsFor("X"):
                print("X Wins!")
                break
            users_col = -1
            while not self.allowsMove(users_col):
                users_col = int(input("O, choose a column: "))
            self.addMove(users_col,'O')
            print(self)
            if self.winsFor("O"):
                print("O Wins!")
                break
            elif self.isFull:
                print("A gentleman's tie!")
                break

