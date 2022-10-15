def printOddN(n):       # Question no :- 3
    if n>1:
        printOddN(n-2)
        print(n-2)
printOddN(2*(5)+1)