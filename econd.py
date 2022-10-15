def printRevN(n):        # Question no :- 2
    if n>0:
        print(n)
        printRevN(n-1)
printRevN(10)