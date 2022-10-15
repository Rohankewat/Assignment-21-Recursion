def printOddN(n):       # Question no :- 4
    if n>1:
        print(n-2)
        printOddN(n-2)

printOddN(2*(10)+1)