def isPrime(n):
    if n<2:
        return False
    for x in range(2,n):
        if n%x == 0:
            return False
    return True

def addPrimes(L):
    if len(L)==0:
        return 0
    else:
        if isPrime(L[0]):
            return L[0] + addPrimes(L[1:])
        else:
            return addPrimes(L[1:])

def uniquify(L):
    if len(L)==0:
        return L
    else:
        if L[0] in L[1:]:
            return uniquify(L[1:])
        else:
            return L[0:1] + uniquify(L[1:])

#another way

def uniquify1(L):
    NewL = []
    if len(L)==0:
        return NewL
    else:
        if L[0] not in NewL:
            NewL.append(L[0])
            return uniquify(L[1:])
        else:
            return uniquify(L[1:])
    return NewL

def median(L):
    L.sort
    J= len(L)
    if J%2==1:
        return L[J//2+1]
    else:
        return (L[J//2 + 1] + L[J//2])/2

def symmetric(M):
    if len(M)<=1:
        return True
    else:
        for x in range(len(M)):
            for y in range(len(M[x])):
                if M[x][y]!= M[y][x]:
                    return False
    return True

class Matrix:
    def __init__(self, nr, nc):
        self.NRows = nr
        self.NCols = nc
        self.data = [ [0]*self.NCols for r in range(self.NRows) ]
   
    def max(self,m2):
        minRows = min(self.NRows, m2.NRows)
        minCols = min(self.NCols, m2.NCols)
        M = Matrix(minRows, minCols)
        for x in range(minRows):
            for y in range(minCols):
                M.data[x][y] = max(self.data[x][y],m2.data[x][y])
        return M

