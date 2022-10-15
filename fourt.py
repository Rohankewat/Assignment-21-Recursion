def printSqN(n):           # Question no :- 8
    if n>0:
        printSqN(n-1)
        print(n**3)
printSqN(5)