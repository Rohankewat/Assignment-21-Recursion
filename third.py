def printSqN(n):           # Question no :- 7
    if n>0:
        printSqN(n-1)
        print(n**2)
printSqN(10)