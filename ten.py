def printEvenN(n):          # Question no :- 6
    if n>2:
        print(n-2)
        printEvenN(n-2)
printEvenN(2*(10)+2)